# v2ex
爬取v2ex网站
cd v2ex/v2ex_spider/v2ex_spider 
scrapy crawl v2ex -o v2ex.csv
构建自定义镜像
docker build -t baobingbo/v2ex:v0.1 . -f Dockerfile
启动并后台运行容器
docker run -dit --name v2ex_spider baobingbo/v2ex:v0.1
