#!/usr/bin/python
#coding=utf8
import smtplib 
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate 

MAIL_LIST = ["user@yourhost.com"]
MAIL_HOST = "smtp.yourhost.com"
MAIL_USER = "yourhost"
MAIL_PASS = "user"
MAIL_SENDER = "youremailaddress"


def send_mail(text): 
    try:
        print text
        msg = MIMEMultipart() 
        msg['From'] = MAIL_USER
        msg['Subject'] = u"不好了网站挂了" 
        msg['To'] = ";".join(MAIL_LIST)
        msg['Date'] = formatdate(localtime=True) 
        msg.attach(MIMEText(text,'html','GBK')) 
        smtp = smtplib.SMTP(MAIL_HOST) 
        #smtp.set_debuglevel(1)
        smtp.login(MAIL_USER, MAIL_PASS) 
        smtp.sendmail(MAIL_SENDER, MAIL_LIST, msg.as_string()) 
        smtp.close()
        print "sendmail success"
        return True
    except Exception, e:
        print "send mail failed hi"
        print e
        return False
