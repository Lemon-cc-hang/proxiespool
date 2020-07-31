FROM python:3.7

MAINTAINER lemoncc <4831703@qq.com>

ENV MYPATH /app

ADD . /app

WORKDIR $MYPATH

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

EXPOSE 5010

CMD [ "sh", "startApi.sh"]