#!/usr/bin/python
#coding=utf8
import smtplib 
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate 

MAIL_LIST = ["qc.zhao@raiyun.com"]
MAIL_HOST = "smtp.raiyun.com"
MAIL_USER = "qc.zhao"
MAIL_PASS = "zqc209213"
MAIL_SENDER = "qc.zhao@raiyun.com"


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
        print "send mail failed"
        print e
        return False