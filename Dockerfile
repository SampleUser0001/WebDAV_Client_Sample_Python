# 任意のイメージを取得
FROM python:3.9

RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN python -m pip install --upgrade pip
RUN pip install python-dotenv webdavclient3

WORKDIR /opt/app

COPY app /opt/app

RUN chmod 755 /opt/app/start.sh

RUN mkdir /tmp/webdav_home

RUN python --version

# ENTRYPOINT [ "/opt/app/start.sh" ]
