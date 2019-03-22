# coding:utf-8
# gevent pool对象使用

from gevent import monkey

monkey.patch_all()
import urllib2
from gevent.pool import Pool


def run_task(url):
    print 'Visit --> %s' % url
    try:
        response = urllib2.urlopen(url)
        data = response.read()
        print '%d bytes received from %s.' % (len(data), url)
    except Exception, e:
        print e
    return 'url:%s --->finish' % url


if __name__ == '__main__':
    pool = Pool(2)
    urls = ['https://github.com/', 'https://www.python.org/', 'http://www.cnblogs.com/']
    results = pool.map(run_task, urls)
    print results

'''
Visit --> https://github.com/
Visit --> https://www.python.org/
<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:726)>
Visit --> http://www.cnblogs.com/
<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:726)>
<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:726)>
['url:https://github.com/ --->finish', 'url:https://www.python.org/ --->finish', 'url:http://www.cnblogs.com/ --->finish']

Process finished with exit code 0

'''
