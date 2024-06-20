## なにこれ

歌詞データのあるmp3ファイルで、歌詞情報を保持しつつ再圧縮をしたかった

## USAGE

```
$ docker build -t ffmpeg:latest .
$ docker run --rm -ti -v .:/tmp ffmpeg:latest /bin/bash

... in the container
# mkdir ....
# edit mp3.py ...

# python3 mp3.py
```

