# -*-coding:UTF-8-*-
import re
# import urllib2
import urllib.request, urllib.error, urllib.parse
import sys
import imp


class GetHtmlPage():
    def __init__(self, strPage):
        self.strPapge = strPage

    def GetPage(self):
        #                req = urllib2.Request(self.strPapge)
        req = urllib.request.Request(self.strPapge)
        rep = req.add_header("User-Agent",
                             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
        try:
            #                   cn = urllib2.urlopen(req)
            cn = urllib.request.urlopen(req)
            page = cn.read()
            uPage = page.decode("utf-8")
            cn.close()
            return uPage
        except urllib.error.URLError as e:
            print('URLError:', e.code)
            return
        except urllib.error.HTTPError as e:
            print('HTTP Error:' + e.reason)
            return
        return rep


class RePage():

    def GetReText(self, page, recode):
        # print(page,recode)

        rePage = re.findall(recode, page, re.S)
        for m in rePage:
            print(m)
        return rePage


class SaveText():
    def Save(self, text, tilte):
        try:
            t = "blog\\" + tilte + ".html"
            f = file(t, "a")
            f.write(text)
            f.close()
        except IOError as e:
            print(e.message)


if __name__ == "__main__":
    s = SaveText()
    print(1111111)

    imp.reload(sys)
    #    sys.setdefaultencoding( "utf-8" )

    page = GetHtmlPage("http://blog.csdn.net/u013088062/article/list/1")
    htmlPage = page.GetPage()

    reServer = RePage()
    reBlog = reServer.GetReText(htmlPage, r'<a href="(.+?)">.*?(\s.+?)</a>')
    print(reBlog)
    for ref in reBlog:
        print(ref)
        pageHeard = "http://blog.csdn.net/"
        strPage = pageHeard + ref[0]
        tilte = ref[1].replace('<font color="red">[TOP]</font>', "")
        tilte = tilte.replace("\r\n", "").lstrip().rstrip()
        #
        htmlPage = GetHtmlPage(strPage)
        htmlPageData = htmlPage.GetPage()
        reBlogText = reServer.GetReText(htmlPageData, '<div id="article_content" class="article_content">(.+?)</div>')
        #
        for s1 in reBlogText:
            s1 = '<meta charset="UTF-8">\n' + s1
            s.Save(s1, tilte)
