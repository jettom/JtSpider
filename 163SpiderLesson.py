#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


newsurl="https://news.sina.com.cn/china/"
res=requests.get(newsurl)


# In[3]:


res.encoding='UTF-8'
print(res)
#print(res.text)
print(type(res))


# In[4]:


from bs4 import BeautifulSoup


# In[5]:


html_sample=' <html> <body> <h1 id="title">HELLO</h1><a class="link" href="#">this is link</a> </body> </html>'


# In[6]:


soup=BeautifulSoup(html_sample,"html.parser")


# In[7]:


print(type(soup))


# In[8]:


#return without html element 
print(soup.text)


# In[9]:


#select by html element h1
header=soup.select("h1")


# In[10]:


print(header)
#return header array
#print(header[0]) is array 0


# print(header[0])

# print(header[0].text)

# In[11]:


print(header[0])
print(header[0].text)


# In[12]:


#select id user #
atitile=soup.select("#title")
print(atitile)


# In[15]:


#select class link #
atitile=soup.select(".link")
#link array
print(atitile)
# print link href
print(atitile[0]['href'])


# In[16]:


#select all a element (link)
alinks=soup.select('a')
for link in alinks:
    print(link)
    #print(link['href'])


# In[18]:


#sample for get attribute
a='<a href="#" abc=1 bcd=2> simple link</a>'
soup2=BeautifulSoup(a)
print(soup2.select('a')[0])
print(soup2.select('a')[0]['abc'])


# In[19]:


# print sina news title and it's href 
soup=BeautifulSoup(res.text)
for news in soup.select('.news-2'):
    for news1 in news.select('li'):
        print(news1.text)
        print(news1.select('a')[0]['href'])
#    if(len(news.select('li'))>0):
#        h2=news.select('li')[0].text
#        #time=news.select('.time')[0].text
#        a=news.select('a')[0]['href']
#        print(h2,a)


# In[20]:


'''
another sample for youku 
'''
# new sample for youku wangyubing 
import requests
from bs4 import BeautifulSoup


# In[21]:


newsurl="http://i.youku.com/i/UNDA0NDIzMDgw/videos?spm=a2hzp.8244740.0.0"
res=requests.get(newsurl)


# In[22]:


res.encoding='UTF-8'
print(res)
#print(res.text)
print(type(res))


# In[23]:


soup=BeautifulSoup(res.text)
#print(soup)


# In[24]:


#select by class videos-list
news = soup.select('.items')


# In[25]:


print(news[0].select('.va')[0].select('.v-meta-title')[0].select('a')[0].text)
print(news[0].select('.va')[0].select('.v-meta-title')[0].select('a')[0]['href'])


# In[26]:


for news in soup.select('.items'):
    for news1 in news.select('.va'):
        #print(news1.select('.v-meta-title')[0].select('a')[0].text)
        print(news1.select('.v-meta-title')[0].select('a')[0]['href'])
        #print(news1.select('a')[0]['href'])


# In[ ]:




