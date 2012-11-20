#!/usr/bin/env python
#coding:utf-8

import json
import urllib
import threading
import time

import MySQLdb

start_id = 1100000
end_id = 1200000
grabbing = True
lock = threading.Lock()
conn = MySQLdb.connect(host='localhost', port=3306, user='root',
                       passwd='111', charset='utf8')
cur = conn.cursor()

cur.execute('create database if not exists douban_book')
cur.execute('use douban_book')
tb = 'book_%s_%s' % (start_id, end_id)
cur.execute('''CREATE TABLE IF NOT EXISTS `%s` (
`id`  int NOT NULL ,
`json`  text NOT NULL ,
PRIMARY KEY (`id`)
);
''' % tb
)

cur.execute('select id from `%s` order by id desc limit 1' % tb)
top = cur.fetchone()
if top is not None and top > start_id:
    top = top[0]
    top = top - 20
    if top < start_id:
        top = start_id
    start_id = top

ranges = iter(xrange(start_id,  end_id))
print top
print start_id

class Book(dict):
    def __init__(self, info):
        self.update(info)

    def __getattr__(self, item):
        return self[item]


#max = 19973896
class Douban(threading.Thread):
    def __init__(self, id):
        super(Douban, self).__init__()

        self.id = id

    def getImg(self, url):
        return urllib.urlopen(url).read()

    def run(self):
        url = 'https://api.douban.com/v2/book/%s' % self.id
        try:
            jsn = urllib.urlopen(url).read()
            meta = json.loads(jsn)
            book = Book(meta)
            if not 'code' in book:
                jsn = jsn.replace("'", "\\'")
                lock.acquire()
                sql = "insert into `%s` values('%s','%s')" % (tb, self.id, jsn)
                try:
                    cur.execute(sql)
                    conn.commit()
                    print self.id, 'ok'
                except:
                    print self.id, 'already grabbed'
                lock.release()
            else:
                print self.id, book.msg
        except Exception as e:
            print self.id, e
        try:
            grab(ranges.next())
        except StopIteration:
            global grabbing
            grabbing = False
            print 'over'


def grab(id):
    task = Douban(id)
    task.setDaemon(True)
    task.start()


def main():
    # 6???
    blocks = 10
    for i in range(blocks):
        grab(ranges.next())
    while grabbing:
        time.sleep(0.001)


if __name__ == '__main__':
    main()
