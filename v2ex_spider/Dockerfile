FROM ubuntu:latest
MAINTAINER baobingbo 879163988@qq.com
RUN mkdir /usr/src/Projects
ENV MYMATH /usr/src/Projects
WORKDIR $MYMATH
RUN apt-get update
RUN apt-get install cron
RUN apt-get install python3
RUN apt-get install python3-pip
RUN pip install scrapy
RUN service cron start
RUN git clone https://github.com/shengyuan1001/v2ex
WORKDIR /usr/src/Projects/v2ex/v2ex_spider/
RUN  chmod +x v2ex_start.sh
RUN  crontab v2ex_crontab.cron
CMD pyhton3