#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python3 抓取 bing 主页背景图片
import urllib.request,re,sys,os
def get_bing_backphoto():
    directory = 'photos';
    if (os.path.exists(directory) == False):
        os.mkdir(directory)
    else:
        for filename in os.listdir(directory):
            os.remove(directory+'/'+filename)
            print('remove ' + filename + 'success')

    for i in range(0,3):
        url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx='+str(i)+'&n=1&nc=1361089515117&FORM=HYLH1'
        html = urllib.request.urlopen(url).read()
        if html == 'null':
            print( 'open & read bing error!')
            sys.exit(-1)
        html = html.decode('utf-8')
        reg = re.compile('"url":"(.*?)","urlbase"',re.S)
        text = re.findall(reg,html)
        for imgurl in text :
            bingimgurl = 'http://cn.bing.com'+imgurl
            right = imgurl.index('&')
            name = imgurl.replace(imgurl[right:],'')
            left = name.index('.')
            imgname = name.replace(name[:left+1],'')
            savepath = directory + '/'+ imgname
            urllib.request.urlretrieve(bingimgurl, savepath)
            print (imgname + ' save success!')
get_bing_backphoto()