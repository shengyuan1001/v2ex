# v2ex

##	1.爬取v2ex网站<br>

cd v2ex/v2ex_spider/v2ex_spider<br> 

scrapy crawl v2ex -o v2ex.csv<br>

##	2.构建自定义镜像<br>

docker build -t baobingbo/v2ex:v0.1 . -f Dockerfile<br>

##	3.启动并后台运行容器<br>

docker run -dit --name v2ex_spider baobingbo/v2ex:v0.1<br>
