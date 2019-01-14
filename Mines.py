#coding:UTF-8
#Author: Hegc Huang
import time, random
import sys
import Tkinter, tkMessageBox, tkFont
from types import *
__AUTHOR__  = "Hegc Huang"
__NAME__    = "Mine Game"
__VERSION__ = "1.0"
__LOSE__    = 'lose.gif'
__WIN__     = 'win.gif'
__LBEVENT__ = '<ButtonRelease-1>'
__RBEVENT__ = '<ButtonRelease-3>'
__TITLE__   = 'Mine Game v1.0 - Hegc Huang for Jessica'
#class for Mines
class Mines:
    """Class for the Mine Game's data structure.
    
    when initializing the game, note that:
    Mine(minecount=16, width=9, height=None)
    width: Chessboard's width.
    minecount: Count of mines.
    height: Chessboard's height.
    minecount must less than width*height, and if height isn't set, it equals width as default.
    so, Mines() means a 9*9 chessboard, and 16 mines;
    Mines(17, 10) means 10*10 chessboard, and 17 mines;
    Mines(17, 10, 11) means 10*11 chessboard, and 17 mines.
    as a result of random generator, minecount may change to a realistic number.
    """
    
    def __init__ (self, minecount=16, width=9, height=None):
        if height == None:
            height = width
        self._width        = width       #for private use
        self._minecount    = minecount     #for private use
        self._height       = height       #
        #print "width= %d, height= %d" % (width, height)
        if self._minecount>=self._width * self._height:
            print 'too small a chessboard. to exit.'
            sys.exit()
        self.mines = None
        self.chessboard = None
        self.reset(minecount, width, height)
        #self.mines          = [0 for x in range(minecount)] #each 0, total minecount
        #self.chessboard     = [[0 for x in range(width)] for y in range(height)]#size: width*height
        #print self.chessboard
        #self.__initialize()
    def __initialize (self):
        random.seed(time.time())    #set seed for random
        count   = 0
        size    = self._width * self._height - 1
        while count<self._minecount:
            randresult = int(random.random()*size + 1)    #random for chess
            if not self.check(count, randresult):
                randresult = int(random.random()*size + 1)    #random for chess
            self.mines[count] = randresult
            count += 1
            del randresult
            #end initialize mines[]
        #self.mines.sort()  #unuseful
        #chessboard init
        for r in self.mines:
            x = r//self._width
            y = r%self._width
            #print 'x = %d, y = %d' % (x, y)
            if self.chessboard[x][y] == -1:
                self.mines.remove(r)
                continue
            self.chessboard[x][y] = -1
        #
        self._minecount = len(self.mines)
        allmines = 0    #all indeed mines
        cx = 0
        while cx<self._height:
            cy = 0
            while cy<self._width:
                c = self.getcount(cx, cy)
                #print 'c =  ', c
                if c==-1:
                    allmines += 1
                self.chessboard[cx][cy] = c
                cy += 1
            #print self.chessboard[cx][:self._height]
            cx += 1
        #self.minecount = allmines
        #end initialize chessboard[][]
        #print "Mines : ", self.mines, ' ;XX; ', allmines
        #print 'All mines = ', self._minecount
    def check (self, count, rr):
        if self.mines[:count].__contains__(rr):
            return False
        return True
    #for external call
    def ismine (self, x, y):
        if self.chessboard[x][y] == -1:
            return True;
        return False
    def getcount (self, x, y):
        #print 'x=%d, y=%d' % (x, y)
        ret = 0;
        if self.chessboard[x][y]==-1:
            ret =-1
        elif x==0 and y==0 and self.chessboard[x][y]!=-1:
            if self.chessboard[x+1][y] == -1:
                ret += 1
            if self.chessboard[x+1][y+1] == -1:
                ret +=1
            if self.chessboard[x][y+1] == -1:
                ret +=1
        elif x==self._height-1 and y==self._width-1 and self.chessboard[x][y]!=-1:
            if self.chessboard[x-1][y] == -1:
                ret += 1
            if self.chessboard[x-1][y-1] == -1:
                ret +=1
            if self.chessboard[x][y-1] == -1:
                ret +=1
        elif y==0 and self.chessboard[x][y]!=-1:
            if self.chessboard[x-1][y] == -1:
                ret += 1
            if self.chessboard[x-1][y+1] == -1:
                ret +=1
            if self.chessboard[x][y+1] == -1:
                ret +=1
            if x < self._height-1:
                if self.chessboard[x+1][y] == -1:
                    ret += 1
                if self.chessboard[x+1][y+1] == -1:
                    ret += 1
        elif x==0 and self.chessboard[x][y]!=-1:
            if self.chessboard[x+1][y] == -1:
                ret += 1
            if self.chessboard[x+1][y-1] == -1:
                ret +=1
            if self.chessboard[x][y-1] == -1:
                ret +=1
            if y < self._width-1:
                if self.chessboard[x+1][y+1] == -1:
                    ret += 1
                if self.chessboard[x][y+1] == -1:
                    ret += 1
        elif x==self._height-1 and self.chessboard[x][y]!=-1:
            if self.chessboard[x-1][y] == -1:
                ret += 1
            if self.chessboard[x-1][y-1] == -1:
                ret +=1
            if self.chessboard[x][y-1] == -1:
                ret +=1
            if self.chessboard[x-1][y+1] == -1:
                ret += 1
            if self.chessboard[x][y+1] == -1:
                ret += 1
        elif y==self._width-1 and self.chessboard[x][y]!=-1:
            if self.chessboard[x-1][y] == -1:
                ret += 1
            if self.chessboard[x+1][y] == -1:
                ret +=1
            if self.chessboard[x][y-1] == -1:
                ret +=1
            if self.chessboard[x+1][y-1] == -1:
                ret += 1
            if self.chessboard[x-1][y-1] == -1:
                ret += 1
        elif self.chessboard[x][y]!=-1:
            if self.chessboard[x-1][y-1] == -1:
                ret += 1
            if self.chessboard[x-1][y] == -1:
                ret +=1
            if self.chessboard[x-1][y+1] == -1:
                ret +=1
            if self.chessboard[x][y+1] == -1:
                ret += 1
            if self.chessboard[x+1][y+1] == -1:
                ret += 1
            if self.chessboard[x+1][y] == -1:
                ret +=1
            if self.chessboard[x+1][y-1] == -1:
                ret += 1
            if self.chessboard[x][y-1] == -1:
                ret += 1
        
       
        return ret
        #end getcount
    def reset (self, minecount = 16, width = 9, height = 9):
        if self.mines:
            del self.mines
        if self.chessboard:
            del self.chessboard
        self._width         = width
        self._height        = height
        self._minecount     = minecount
        self.mines          = [0 for x in range(minecount)] #each 0, total minecount
        self.chessboard     = [[0 for x in range(width)] for y in range(height)]#size: width*height
        self.__initialize()
        #print self.chessboard
#the following two methods is from Tkinter.py
def _flatten(tuple):
    """Internal function."""
    res = ()
    for item in tuple:
        if type(item) in (TupleType, ListType):
            res = res + _flatten(item)
        elif item is not None:
            res = res + (item,)
    return res
def _cnfmerge(cnfs):
    """Internal function."""
    if type(cnfs) is DictionaryType:
        return cnfs
    elif type(cnfs) in (NoneType, StringType):
        return cnfs
    else:
        cnf = {}
        for c in _flatten(cnfs):
            try:
                cnf.update(c)
            except (AttributeError, TypeError), msg:
                print "_cnfmerge: fallback due to:", msg
                for k, v in c.items():
                    cnf[k] = v
        return cnf
#class for Game
class Game:
    def __init__ (self, master, mines):
        self._mines = mines
        self._errormines = []
        self._master = master
        self._font = tkFont.Font(weight=tkFont.BOLD, size=12)
        self._allcount = mines._minecount
        self.createimage()
        self.initframe()
    def createimage (self):
        self.__LOSE__ = Tkinter.PhotoImage(file=__LOSE__)
        self.__WIN__  = Tkinter.PhotoImage(file=__WIN__)
    def power (self, event):
        w = event.widget
        t = w.cget('text')
        if t == 'l':
            w.config(text='w', image=self.__WIN__)
        _m = self._mines
        self.restart(_m._minecount, _m._width, _m._height)
    def restart (self, ms, row, column, rs = True): #rs = True for real restart
        #print 'ms = %d; r = %d, c = %d' % (ms, row, column)
        if self.mainframe:
            self.mainframe.destroy()
        if rs:
            self._mines.reset(ms, row, column)
        self._allcount = self._mines._minecount
        self._errormines = []
        self.countlabel.config(text=self._allcount, font=self._font, fg='#FA3CAD')
        self.mainframe = Tkinter.Frame(self._master)
        self.buildmain(self.mainframe)
        self.mainframe.pack(side=Tkinter.BOTTOM, fill=Tkinter.BOTH)
    def initframe (self):
        self.funcframe = Tkinter.Frame(self._master)
        #
        self.countlabel = Tkinter.Label(self.funcframe)   #display the number of mines
        self.countlabel.pack(side = Tkinter.LEFT, expand=3, fill=Tkinter.BOTH)
        #
        #self.canvas = Tkinter.Canvas(self.funcframe)
        #self.canvas.pack(side = Tkinter.LEFT, fill=Tkinter.X)
        #self.canvas.create_text(10, 10, text=self._mines.minecount, fill='#FF3333')
        #
        self.powerbutton = Tkinter.Button(self.funcframe, image=self.__WIN__, text='w')
        self.powerbutton.bind(__LBEVENT__, self.power)
        self.powerbutton.pack(side=Tkinter.RIGHT)
        #
        self.funcframe.pack(side=Tkinter.TOP)
        #
        self.mainframe = None
        _m = self._mines
        self.restart(_m._minecount, _m._width, _m._height, False)#use restart to init
    def buildmain (self, mf):
        width  = self._mines._width
        height = self._mines._height
        #mf     = self.mainframe
        r = 0
        #print "R=%d, C=%d" % (height, width)
        while r < height:
            c = 0
            while c < width:
                button = Tkinter.Button(mf,  text='', width=2, height=1)#width=2, height=1
                button.grid(row=r,column=c,rowspan=1, columnspan=1)
                button.bind(__LBEVENT__, self.lbclick)
                button.bind(__RBEVENT__, self.lbclick)
                #print "c = %d" % c
                c += 1
            r += 1
            #print "r = %d" % r
    def lbclick (self, event):#handle click the chessboard
        w = event.widget
        g = w.grid_info()
        r = int(g['row'])   #for row
        c = int(g['column'])#for column
        mnum = event.num    #mouse button
        #print u"鼠标num = ", mnum
        if mnum == 1:       #left button
            self.clickleft(w, r, c)
        elif mnum == 3:     #right button
            self.clickright(w, r, c)
        #if self._mines.ismine(r, c):
    def clickright (self, w, r, c):
        t = w.cget('text')
        if t=='?':
            w.config(text='')
            w.bind(__LBEVENT__, self.lbclick)
        elif t=='$':
            w.config(text='?')
            w.unbind(__LBEVENT__)
            _m = self._mines
            ml = r*_m._width + c    #mine location
            if not _m.ismine(r,c):
                self._errormines.remove(ml)
                self._allcount += 1 #allcount + 1
                self.countlabel.config(text=self._allcount, font=self._font, fg='#FA3CAD')
            else:
                _m.mines.append(ml)
        else:
            w.config(text='$')
            w.unbind(__LBEVENT__)
            _m = self._mines
            ml = r*_m._width + c    #mine location
            if not _m.ismine(r,c):
                self._errormines.append(ml)
                self._allcount -= 1 #allcount - 1
                self.countlabel.config(text=self._allcount, font=self._font, fg='#FA3CAD')
            else:
                _m.mines.remove(ml)
                self._allcount -= 1 #allcount - 1
                self.countlabel.config(text=self._allcount, font=self._font, fg='#FA3CAD')
            if self._allcount==0:   #all found
                if len(self._errormines)>0: #some error
                    self._showresult(r, c)
                else:
                    self._showresult(r, c, 'WIN')
    def _showresult (self, r, c, result = 'LOSE'):
        if result == 'WIN':
            tkMessageBox.showinfo(message=u'Congratulations!!/nYou Winned.', title=u'Win')
            return;
        self.powerbutton.config(text='l', image=self.__LOSE__)
        for m in self._errormines:
            x = m//self._mines._width
            y = m%self._mines._width
            self._forbutton(x, y, True, text='X', state=Tkinter.DISABLED, disabledforeground='#FFAA00', relief=Tkinter.FLAT)   #show all error mines
        for m in self._mines.mines:      
            x = m//self._mines._width
            y = m%self._mines._width
            self._forbutton(x, y, True, text='#', state=Tkinter.DISABLED, disabledforeground='#FFAFCD', relief=Tkinter.FLAT)   #show all mines, and unbind all action
        tkMessageBox.showinfo(message=u'Sorry!!/nBut you Failed.', title=u'Fail')    #third, tell the result 'LOSE'
    def clickleft (self, w, r, c):
        if self._mines.ismine(r, c):    #click a mine, game over
            ml = r*self._mines._width + c
            self._mines.mines.remove(ml)
            self._forbutton(r, c, True, text='#', state=Tkinter.DISABLED, disabledforeground='#FF0000', relief=Tkinter.FLAT)
            #for m in self._mines.mines:      
            #    x = m//self._mines._width
            #    y = m%self._mines._width
            #    self._forbutton(x, y, True, text='#', state=Tkinter.DISABLED, disabledforeground='#FF0000', relief=Tkinter.FLAT)   #show all mines, and unbind all action
            #self.powerbutton.config(text='l', image=self.__LOSE__)   
            #tkMessageBox.showinfo(message=u'踩到雷了！！', title=u'失败')    #third, tell the result 'LOSE'
            self._showresult(r, c)
        else:
            m = self._mines
            t = ''
            n = m.chessboard[r][c]
            if n>0:
                t = '%s' % n
            w.config(relief = Tkinter.FLAT, state = Tkinter.DISABLED, text = t)
            self.unbind(w)      #disable, and unbind
            if n==0:    #none around
                self._showaround(r, c)
    def _forbutton (self, r, c, ub, cnf={}, **kw): #imitate the Button.__init__(), in fact, 'n=v's impose on kw(tuple). ub true for unbind
        bt = self.mainframe.grid_slaves(row=r, column=c)[0]
        state = bt.cget('state')
        if state == Tkinter.DISABLED:
            return 'done'
        #bt.config(relief = Tkinter.FLAT, state = st, text = t, disabledforeground = dfg)
        if kw:
            #print 'cnf = ', cnf, ' ; kw = ', kw    #cnf is alwayes {}
            cnf = _cnfmerge((cnf, kw))
            #print 'CNF = ', cnf
        bt.config(cnf)
        if ub:
            self.unbind (bt)
        return None
    def _decide (self, r, c):
        n = self._mines.chessboard[r][c]
        if n==0:
            st = self._forbutton(r, c, True, state=Tkinter.DISABLED, relief=Tkinter.FLAT)
            #print 'st = ', st
            if st == None: #hasn't handled
                self._showaround(r, c)
        else:
            self._forbutton(r, c, True, text = '%s' % n, state=Tkinter.DISABLED, relief=Tkinter.FLAT)
    def _showaround (self, r, c):
        cb = self._mines.chessboard
        if r>0:     
            _r = r-1    #north
            _c = c
            #self._forbutton(_r, _c, '')
            self._decide(_r, _c)
            if c>0:     #northwest
                _r = r-1
                _c = c-1
                #self._forbutton(_r, _c, '')
                self._decide(_r, _c)
            if c<self._mines._width-1: #northeast
                _r = r-1
                _c = c+1
                #self._forbutton(_r, _c, '')
                self._decide(_r, _c)
        if r<self._mines._height-1:
            _r = r+1    #south
            _c = c
            #self._forbutton(_r, _c, '')
            self._decide(_r, _c)
            if c>0:     #southwest
                _r = r+1
                _c = c-1
                #self._forbutton(_r, _c, '')
                self._decide(_r, _c)
            if c<self._mines._width-1: #southeast
                _r = r+1
                _c = c+1
                #self._forbutton(_r, _c, '')
                self._decide(_r, _c)
        if c>0:     #west
            _r = r
            _c = c-1
            #self._forbutton(_r, _c, '')
            self._decide(_r, _c)
        if c<self._mines._width-1:  #east
            _r = r
            _c = c+1
            #self._forbutton(_r, _c, '')
            self._decide(_r, _c)
    def unbind (self, w):
        w.unbind(__LBEVENT__)
        w.unbind(__RBEVENT__)
#main class
class MineGame:
    def __init__ (self):
        self.mine = Mines(40, 16, 16)   #默认：中级
        self.root = Tkinter.Tk()
        self.root.title(__TITLE__)
        self.game = Game(self.root, self.mine)
        self._addmenu(self.root)
        self.root.wm_resizable(False, False)    #can not resize
        self.root.mainloop()
    def _addmenu (self, _master):
        bar = Tkinter.Menu()
        fil = Tkinter.Menu()
        for x in u'初级', u'中级', u'高级', u'自定义', '-', u'退出':
            if x=='-':
                fil.add_separator()
            else:
                fil.add_command(label=x, command = lambda x=x: self.newgame(x))
        bar.add_cascade(label=u'游戏', menu=fil)
        _master.config(menu = bar)
    def newgame (self, x):
        if x==u'初级':
            self.game.restart(10, 9, 9)
        elif x==u'中级':
            self.game.restart(40, 16, 16)
        elif x==u'高级':
            self.game.restart(99, 30, 16)
        elif x==u'自定义':
            def _okb ():
                try:
                    wd = int(wfunc.get())
                    hg = int(hfunc.get())
                    mc = int(cfunc.get())
                except TypeError:
                    tkMessageBox.showwarning(message=u'请输入正确的数字', title='警告')
                    return
                
                m = wd * hg
                if m//mc>10:
                    tkMessageBox.showwarning(message=u'棋盘太大了，而雷太少了。/n请确保地雷数目不少于棋盘大小的1/10。', title='警告')
                    return
                elif m//mc<3:
                    tkMessageBox.showwarning(message=u'棋盘太小了，而雷太多了。/n请确保地雷数目不超过棋盘大小的1/4。', title='警告')
                    return
                root.destroy()
                self.root.wm_resizable(True, True)
                self.game.restart(mc, wd, hg)
                self.root.wm_resizable(False, False)
            def _ccb ():
                root.destroy()
            root = Tkinter.Tk()
            fram = Tkinter.Frame(root)
            Tkinter.Label(fram, text=u'宽度(6~30  ): ').pack(side=Tkinter.LEFT)
            wfunc = Tkinter.Entry(fram)
            wfunc.pack(side=Tkinter.RIGHT, fill=Tkinter.BOTH, expand=1)
            fram.pack()
            fram = Tkinter.Frame(root)
            Tkinter.Label(fram, text=u'高度(6~24  ): ').pack(side=Tkinter.LEFT)
            hfunc = Tkinter.Entry(fram)
            hfunc.pack(side=Tkinter.RIGHT, fill=Tkinter.BOTH, expand=1)
            fram.pack()
            fram = Tkinter.Frame(root)
            Tkinter.Label(fram, text=u'雷数(6~180): ').pack(side=Tkinter.LEFT)
            cfunc = Tkinter.Entry(fram)
            cfunc.pack(side=Tkinter.RIGHT, fill=Tkinter.BOTH, expand=1)
            fram.pack()
            fram = Tkinter.Frame(root)
            Tkinter.Button(fram,text=u'确定', command=_okb).pack(side= Tkinter.LEFT)
            Tkinter.Button(fram,text=u'取消', command=_ccb).pack(side= Tkinter.RIGHT)
            fram.pack()
            root.mainloop()
        elif x==u'退出':
            sys.exit()
#main start function
def start (arg):
    if arg=='c':
        mines = Mines(16, 9)
        print Mines.__doc__
        _l = len(mines.chessboard)
        l = 0
        while l<_l:
            for i in mines.chessboard[:][l]:
                if i==-1:
                    i = '/x0F'
                print i, ' ',/
            
            print ''
            l += 1
    else:
        MineGame()
        
argc = len(sys.argv)
if argc>1:
    arg = sys.argv[1]
    start(arg)
else:
    start('g')

#---------------------
#作者：hegch
#来源：CSDN
#原文：https://blog.csdn.net/HegcH/article/details/2892209?utm_source=copy
#版权声明：本文为博主原创文章，转载请附上博文链接！
