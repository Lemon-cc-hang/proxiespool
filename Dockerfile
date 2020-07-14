FROM python:3.7

MAINTAINER lemoncc <4831703@qq.com>

ENV MYPATH /app

ADD . /app

WORKDIR $MYPATH

#COPY ./requirements.txt .

#RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
# apk add gcc musl-dev libffi-dev python3-dev libressl-dev openssl-dev && \

RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple/ && \
    pip install requests bs4 pymongo -i https://pypi.tuna.tsinghua.edu.cn/simple/
    # pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/ # && \
#    apk del gcc musl-dev

EXPOSE 5010

CMD [ "sh", "start.sh", "&&", "tail", "-F", "./logs/scraping.log"]