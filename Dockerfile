FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
      wget \
      xz-utils \
      python3 \
      pip

WORKDIR /tmp

RUN wget https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-amd64-static.tar.xz \
      && tar xvf ./ffmpeg-git-amd64-static.tar.xz \
      && cp ./ffmpeg*amd64-static/ffmpeg /usr/local/bin/

RUN pip install mutagen

CMD /bin/bash

