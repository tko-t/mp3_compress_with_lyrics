import glob
import os
import subprocess
import time
import re
from datetime import datetime
from mutagen.id3 import ID3, USLT

# 階層ごとに書き換えてた。引数でよかったな
LEVEL = 'M'

# 検索フォルダ(と拡張子).
#TARGET_DIR = "./origin/"
TARGET_DIR = f"./origin/hanon_audios/{LEVEL}/"

# 出力フォルダ.
#OUTPUT_DIR = f"./output/"
OUTPUT_DIR = f"./compress/hanon_audios/{LEVEL}/"
# ビットレート.
BIT_RATE = "24k"

# 指定フォルダのmp3ファイルをリストアップ.
files = glob.glob(os.path.join(TARGET_DIR, '*.mp3'))

for file in files:
    # 入力ファイル名 s/[ .]/_/ したのが出力ファイル名
    filename = re.sub('(\d+)\.(\d+)', '\\1_\\2', os.path.basename(file))
    filename = re.sub(' ', '_', filename)
    out = os.path.join(OUTPUT_DIR, filename)

    # 歌詞をffmpegで取り出してたけど歌詞以外のメタデータいらないのでやめた
    #met = f'{os.path.join(OUTPUT_DIR, os.path.basename(file))}.txt'
    #cmd = [
    #    "ffmpeg",
    #    "-i",
    #    file,
    #    "-map_metadata",
    #    "0",
    #    "-f",
    #    "ffmetadata",
    #    met,
    #]
    #print(f'---------------------------{cmd}')
    #subprocess.run(cmd) # メタデータをテキスト出力
    #--------------------------- ffmpeg -i ./origin/sample.mp3 -map_metadata 0 -f ffmetadata ./compress/sample.mp3.txt

    cmd = [
        'ffmpeg',
        '-i',
        file,
        '-map_metadata',
        '-1',
        '-b:a',
        BIT_RATE,
        out,
    ]
    print(f'--------------------------- {cmd}')
    subprocess.run(cmd) # メタデータ全部消して mp3を再圧縮
    #--------------------------- ffmpeg -i ./origin/sample.mp3 -map_metadata -1 -b:a 24k ./output/sample.mp3

    # オリジナルファイルから歌詞抽出
    audio = ID3(file)
    lyrics = re.sub("\r", '', audio.getall("USLT")[0].text.lstrip().rstrip()) # 歌詞

    # 圧縮ファイルからタグ削除(-map_metadata -1 だけだと消しきれない
    audio = ID3(out)
    for key, value in audio.items():
      audio.pop(key)

    audio.add(USLT(encoding=3, text=lyrics)) # 歌詞埋め込み
    audio.save() # 更新

    #cmd = [
    #    'rm',
    #    met,
    #]
    #print(f'--------------------------- {cmd}')
    #subprocess.run(cmd) # メタデータファイル削除

    cmd = [
        'chown',
        '1000:1000',
        out,
    ]
    print(f'--------------------------- {cmd}')
    subprocess.run(cmd) # オーナー変更

