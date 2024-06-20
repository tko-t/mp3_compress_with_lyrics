from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, TIT2, USLT

mp3_file_path = "./output/sample.mp3"
mp3_file_path = "./output/01_Unit 1.1.mp3"


tags = EasyID3(mp3_file_path)

# 辞書型で格納されたメタデータ表示
for key, value in tags.items():
    print(key,":", value[0])


audio = ID3(mp3_file_path)
for key, value in audio.items():
    print(key,":", value)
    audio.pop(key)

audio.save()

#audio.add(USLT(encoding=3, text="otatatata"))
#audio.save()

