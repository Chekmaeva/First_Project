import sys, re, urllib, html2text # re нужен для того, чтобы получить доступ к информации с определённого сайта
from urllib import request
from professions import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.newsurl = []
        self.Parse()                 
        self.ui.pushButton.clicked.connect(self.AllNews)
    
    def Parse(self):
        s = 'https://russian.rt.com/news'
        doc = urllib.request.urlopen(s).read().decode('utf-8', errors='ignore')
        doc = doc.replace('\n', '')
        headlines = re.findall('<a class="link link_color" href="(.+?)</a>', doc)
        for i in headlines:
            self.newsurl.append(i.split('">')[0])
            self.ui.listWidget.addItem(i.split('">')[1].strip())
            
              
    def AllNews(self):
        row = self.ui.listWidget.currentRow() # номер строчки из списка с заголовками
        link = 'https://russian.rt.com/news' + self.newsurl[row] # ссылка на страницу с содержанием заголовка
        doc=urllib.request.urlopen(link).read().decode('utf-8', errors='ignore') #  получение HTML-кода, соответствующего ссылке
        t = html2text.HTML2Text() # текст ссылок
        t.ignore_links=True # чтобы в тексте не просматривались ссылки
        t.body_width=False
        t.ignore_images=True # чтобы в тексте не просматривались картинки
        doc = t.handle(doc) # получаем сам текст
        m = doc.split('\n') # разделим текст на строки, это нужно для того, чтобы убрать всю ненужную информацию и оставить только то, что нам необходимо, мы просто удалим короткие строки, которыми обычно являются ссылки и другая лишняя информация
        strr = ''
        for i in m:
            if len(i) > 120:
                strr += i + '\n\n' # двойное \n\n специально, чтобы разделить по абзацам
        self.ui.textEdit.setText(strr)
                
        
if __name__== '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())