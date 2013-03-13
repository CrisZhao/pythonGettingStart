#!/usr/bin/python
#coding=utf8

import httplib
import threading
import time,datetime
from sendMail import send_mail

urls = ["www.raiyun.com:8888/DashBoard"]
testTomcatRes = "/RaiyunService/json/template"

def http_open(host, port, resource):
    print host,port,resource
    # if not resource.startwith("/")
    #     resource = "/" +resource
    try:
        conn = httplib.HTTPConnection(host, port, timeout = 5*60)
        print "http connection created successfully"
        # conn.request("GET", resource)
        conn.request("GET", testTomcatRes)
        r=conn.getresponse()
        return r.status  
    except Exception,e:
        return e

def http_openurl(inputurl):
    host_port, res1 = inputurl.split("/")
    host, port = host_port.split(":")
    return http_open(host, port, resource = "/"+res1)



class check(threading.Thread): 
    def __init__(self, url ,interval):
        threading.Thread.__init__(self)
        self.interval = interval
        self.url=url
 
    def run(self):
        status = http_openurl(self.url)
        print status
        if status==200:
            print u"链接[%s]响应正常1，状态为：%s"%(self.url,status)
        elif status==302:
            print u"链接[%s]响应正常2，状态为：%s"%(self.url,status)
        else:
            print u"链接[%s]响应异常3，状态为：%s"%(self.url,status)
            print "strat send mail"
            send_mail(u"链接[%s]响应异常，状态为：%s"%(self.url,status))
            print "end send mail"
        time.sleep(self.interval)

def main():
    thread_list =[]

    print u"webmonitor start"
    print u"共有%s个网站需要检测"%len(urls)
    
    while(True):
        print u"执行时间:%s"%(datetime.datetime.now())
        for url in urls:
            thread = check(url,1*60)
            thread.start()
            thread_list.append(thread)
        time.sleep(30*60)
        print "------\n\n"
        
if __name__ == "__main__":
    main()
    # http_openurl("www.raiyun.com:8888/DashBoard")
    # send_mail("ssss")