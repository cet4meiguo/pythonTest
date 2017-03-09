# -*- coding: utf-8 -*-

import requests 
from bs4 import BeautifulSoup 
import os

class downloadImgUrl():
    def request(self, url):
        headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        content = requests.get(url,  headers=headers)
        return content
        pass

    def saveImg(self, url):
        name = url[-9:-4]
        img = self.request(url)
        f = open(name+'.jpg', 'ab')
        f.write(img.content) 
        f.close()
        print(name)
        pass

    def mkdir(self,path):
        path = path.strip()
        isExists = os.path.exists(os.path.join("D:\mzitu", path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join("D:\mzitu", path))
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False
        pass

    def img(self,pageEnd,url):
        for page in range(1, int(pageEnd)+1):
            downSrc = url+str(page)
            img_html = self.request(downSrc)
            img_Soup = BeautifulSoup(img_html.text, 'lxml')
            img_url = img_Soup.find('div', class_='main-image').find('img')['src']
            self.saveImg(img_url)
        pass

    def all_url(self,url):
        html = self.request(url)
        Soup = BeautifulSoup(html.text, 'lxml')
        pageEnd = Soup.find('div',class_='pagenavi').find_all('span')[-2].get_text()
        title = Soup.find('h2',class_='main-title').get_text() 
        self.mkdir(title)
        os.chdir("D:\mzitu\\"+title) ##切换到上面创建的文件夹
        self.img(pageEnd,url)
        pass

Mzitu = downloadImgUrl() ##实例化
Mzitu.all_url('http://www.mzitu.com/82178/')






    


