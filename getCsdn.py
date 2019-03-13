# -*-coding:UTF-8-*-
import re
import urllib2
import sys


# 目的：读取博客文章，记录标题，用Htnl格式保存存文章内容
# 版本：python2.7.13
# 功能：读取网页内容
class GetHtmlPage():
    # 注意大小写
    def __init__(self, strPage):
        self.strPapge = strPage

    # 获取网页
    def GetPage(self):
        req = urllib2.Request(self.strPapge)  # 建立页面请求
        rep = req.add_header("User-Agent",
                             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
        try:
            cn = urllib2.urlopen(req)  # 网页请求
            page = cn.read()  # 读网页
            uPage = page.decode("utf-8")  # 网页编码
            cn.close()
            return uPage
        except urllib2.URLError, e:  # 捕获异常
            print 'URLError:', e.code
            return
        except urllib2.HTTPError, e:  # 捕获异常
            print 'HTTP Error:' + e.reason
            return
        return rePage


# 正则表达式，获取想要的内容
class RePage():
    # 正则表达式提取内容，返回链表
    def __init__(self):
        pass

    def GetReText(self, page, recode):
        rePage = re.findall(recode, page, re.S)
        return rePage


# 保存文本
class SaveText():
    def __init__(self):
        pass

    def Save(self, text, tilte):
        try:
            t = "blog\\" + tilte + ".html"
            f = file(t, "a")
            f.write(text)
            f.close()
        except IOError, e:
            print e.message


if __name__ == "__main__":
    s = SaveText()
    # 文件编码
    # 字符正确解码
    reload(sys)
    sys.setdefaultencoding("utf-8")  # 获得系统的默认编码
    # 获取网页　https://blog.csdn.net/u013088062/article/list/1
    page = GetHtmlPage("http://blog.csdn.net/u013088062/article/list/1")
    htmlPage = page.GetPage()
    # 提取内容
    reServer = RePage()
    reBlog = reServer.GetReText(htmlPage,
                                r'<span class="link_title"><a href="(.+?)">.*?(\s.+?)</a></span>')  # 获取网址链接和标题
    # 再向下获取正文
    for ref in reBlog:
        pageHeard = "http://blog.csdn.net/"  # 加链接头
        strPage = pageHeard + ref[0]
        tilte = ref[1].replace('<font color="red">[置顶]</font>', "")  # 用替换的功能去除杂的英文
        tilte = tilte.replace("\r\n", "").lstrip().rstrip()
        # 获取正文
        htmlPage = GetHtmlPage(strPage)
        htmlPageData = htmlPage.GetPage()
        reBlogText = reServer.GetReText(htmlPageData, '<div id="article_content" class="article_content">(.+?)</div>')
        # 保存文件
        for s1 in reBlogText:
            s1 = '<meta charset="UTF-8">\n' + s1
            s.Save(s1, tilte)
