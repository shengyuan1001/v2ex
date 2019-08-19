import random

all_ua = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36     (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/75.0.3770.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36     (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/73.0.3683.86 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/75.0.3770.80 Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko)     Version/11.0 Mobile/15A5341f Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36     (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/75.0.3770.80 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X)     AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/75.0.3770.80 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/74.0.3729.131 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/74.0.3729.169 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/73.0.3683.103 Safari/537.36",

]

all_ip = [
    "http://112.85.130.157:9999",
    "http://163.204.242.225:8888",
    "http://123.163.97.144:9999",
    "http://117.95.198.88:9999",
    "http://123.163.97.10:9999",
    "http://120.83.104.97:9999",
    "http://60.166.87.171:808",
    "http://60.13.42.168:9999",
    "http://58.253.156.36:9999",
    "http://163.204.246.34:9999",
    "http://183.129.207.86:11206",
    "http://210.26.64.44:3128",
    "http://183.129.207.92:11056",
    "http://120.78.225.5:3128",
    "http://113.140.1.82:53281",
    "http://111.231.92.21:8888",
    "http://180.109.167.184:8118",
    "http://125.120.176.18:9999",
    "http://117.67.216.240:8118",
    "http://106.14.155.117:3128",
    "http://112.85.130.157:9999",
    "http://117.95.198.88:9999",
    "http://123.163.97.10:9999",
    "http://210.26.64.44:3128",
    "http://120.83.104.97:9999",
    "http://163.204.243.32:9999",
    "http://60.13.42.41:9999",
    "http://114.239.255.78:9999",
    "http://60.13.42.139:9999",
    "http://117.95.232.42:9999",
    "http://163.204.242.225:8888",
    "http://123.163.97.144:9999",
    "http://183.129.207.86:11206",
    "http://163.204.242.143:9999",
    "http://163.204.95.106:9999",
    "http://163.204.247.52:9999",
    "http://182.35.84.77:9999",
    "http://163.204.247.134:9999",
    "http://112.85.131.5:9999",
    "http://60.13.42.24:9999",
    "http://120.83.104.222:6675",
    "http://120.83.111.155:6666",
    "http://121.63.198.84:6668",
    "http://121.31.193.132:6675",
    "http://117.69.98.216:6666",
    "http://113.121.245.231:6675",
    "http://218.73.130.59:6675",
    "http://110.73.30.246:6666",
    "http://171.38.64.67:6675",
    "http://222.172.239.69:6666",

]


def get_ip():
    return random.choice(all_ip)


def get_ua():
    return random.choice(all_ua)