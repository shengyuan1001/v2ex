#
import csv
import datetime

__author__ = 'bob'
__date__ = '2019/8/20 9:38'

import smtplib
from email.mime.text import MIMEText


#   创建邮件类
class SendEmail(object):
    def sendemail(self):
        """
        发送邮件
        user: 用户名
        pwd: 密码【授权码】
        sender: 发送方-----》字符串
        recevier: 接收方(多方)-----》列表
        title: 邮件标题
        text: 邮件正文
        tiem: 时间
        """
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user = '17602915538@163.com'
        pwd = 'bbb17602915538'
        sender = '17602915538@163.com'
        recevier = ['879163988@qq.com']
        title = '今日信息   ' + time + '    v2ex tops'
        text = []
        with open('v2ex.csv', encoding='utf-8')as f:
            # 映射字典
            contents = csv.DictReader(f, ['title', 'text'])

            for content in contents:
                if content['title'] != 'title' and content['text'] != 'text':
                    text.append(content['title'])
                    text.append((content['text']))
            #  添加html样式
            text = "<html><body>{}</body></html>".format(''.join(text))

        # 163的smtp服务器
        mail_host = "smtp.163.com"
        # 一、准备工作
        # 1.将邮件信息打包成一个对象,参数：内容，格式，编码
        #  _subtype是MIME子内容类型，默认为“plain”改为“html”
        message = MIMEText(text, _subtype="html", _charset="utf-8")
        # 2.设置邮件的发送方
        message["From"] = sender
        # 3.设置邮件的接收方(群发)
        message["To"] = ",".join(recevier)
        # 4.设置邮件标题
        message["Subject"] = title
        # 二、发送邮件
        try:
            # 1.启用SSL
            # 参数：smtp服务器，端口号【465】
            obj = smtplib.SMTP_SSL(mail_host, 465)
            # 2.登录邮箱进行验证
            # 参数：用户名 密码【授权码】
            obj.login(user, pwd)
            # 3.开始发送
            # 参数：发送者，接收者，打包好的邮件信息
            obj.sendmail(sender, recevier, message.as_string())
            print("发送成功")
        except smtplib.SMTPException as e:
            print(e)

