import requests
import json

url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_551816010?csrf_token=568cec564ccadb5f1b29311ece2288f1'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
    'Referer':'http://music.163.com/song?id=551816010',
    'Origin':'http://music.163.com',
    'Host':'music.163.com'
}
#
user_data = {
    'params': 'vRlMDmFsdQgApSPW3Fuh93jGTi/ZN2hZ2MhdqMB503TZaIWYWujKWM4hAJnKoPdV7vMXi5GZX6iOa1aljfQwxnKsNT+5/uJKuxosmdhdBQxvX/uwXSOVdT+0RFcnSPtv',
    'encSecKey': '46fddcef9ca665289ff5a8888aa2d3b0490e94ccffe48332eca2d2a775ee932624afea7e95f321d8565fd9101a8fbc5a9cadbe07daa61a27d18e4eb214ff83ad301255722b154f3c1dd1364570c60e3f003e15515de7c6ede0ca6ca255e8e39788c2f72877f64bc68d29fac51d33103c181cad6b0a297fe13cd55aa67333e3e5'
}

response = requests.post(url,headers=headers,data=user_data)

data = json.loads(response.text)
#print(response.text)
hotcomments = []
for hotcommment in data['hotComments']:
    item = {
        'nickname':hotcommment['user']['nickname'],
        'content':hotcommment['content'],
        'likedCount':hotcommment['likedCount']     
    }
    hotcomments.append(item)

#获取评论用户名，内容，以及对应的获赞数   
content_list = [content['content'] for content in hotcomments]
nickname = [content['nickname'] for content in hotcomments]
liked_count = [content['likedCount'] for content in hotcomments]

#print(content_list)
#print("--------------------")
#print(nickname)
print("--------------------")
#print(liked_count)

from pyecharts import Bar

bar = Bar("热评中点赞数示例图")
bar.add( "点赞数",nickname, liked_count, is_stack=True,mark_line=["min", "max"],mark_point=["average"])
bar.render()
#
#sample:::::::
#from pyecharts import Bar
#
#attr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
#v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
#v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
#bar = Bar("Bar chart", "precipitation and evaporation one year")
#bar.add("precipitation", attr, v1, mark_line=["average"], mark_point=["max", "min"])
#bar.add("evaporation", attr, v2, mark_line=["average"], mark_point=["max", "min"])
#bar.render()

