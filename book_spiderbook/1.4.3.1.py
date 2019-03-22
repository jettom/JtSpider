#coding:utf-8
#gevent的使用流程

from gevent import monkey; monkey.patch_all()
import gevent
import urllib2

def run_task(urlP):
    print 'Visit --> %s' % urlP
    try:
        response = urllib2.urlopen(urlP)
        data = response.read()
        print '%d bytes received from %s.' % (len(data), urlP)
    except Exception, e:
        print e


if __name__ == '__main__':
    urls = ['https://github.com/', 'https://www.python.org/', 'http://www.cnblogs.com/']
    greenlets = [gevent.spawn(run_task, url) for url in urls]
    gevent.joinall(greenlets)

#TODO RUN ERROR
'''
Visit --> https://github.com/
Visit --> https://www.python.org/
Visit --> http://www.cnblogs.com/
<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:726)>
<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:726)>
<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:726)>

Process finished with exit code 0
'''