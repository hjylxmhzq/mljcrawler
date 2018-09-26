# -*- coding: utf-8 -*-
import os
import csv
import codecs
import re
import requests
from bs4 import BeautifulSoup
import random
import time
import csv
import sys
import multiprocessing
import sys,codecs,locale

print('''********************************
*      获取缺失企业信息条目        *
*   将文件放在企业信息.csv文件目录  *
********************************''')


#main part



def getheader(area):
    User_Agent= [
        "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
        "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
        "Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
    ]
    ua=random.choice(User_Agent)
    ref = 'https://gongshang.mingluji.com/'+area+'/node/' + str(random.randint(1,200000))
    headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Accept-Language':'zh-CN,zh;q=0.9','Cache-Control':'max-age=0','Connection':'keep-alive','Referer': ref,'Host':'gongshang.mingluji.com','Upgrade-Insecure-Requests':'1','User-Agent':ua}
    return headers

def getallip():
    url="http://www.httpipqq.com/api.asp?sl=10&noinfo=true&ddbh=174517085071730342"
    data = []
    while(not data):
        try:
            data = requests.get(url,timeout=10)
        except:
            print("request ip time out")
            data = []
            time.sleep(1)
    html = data.text.split("\r\n")
    return html

def getmaxnode(area):
    files = os.listdir()
    files = list(files)
    if 'node.txt' in files:
        with open('node.txt','r',encoding='utf8') as f:
            maxnodenum = int(f.readline())
        print("node number exist")
        return maxnodenum
    url = 'https://gongshang.mingluji.com/' + area + '/'
    allip = []
    trytime = 0
    iptrytime = 0
    latesttime = ''
    timeorderurl = ''
    proxy = {"https":""}
    infopage = []
    while trytime < 10 and (not infopage):
        latesttime = ''
        trytime += 1
        iptrytime = 0
        if trytime%3 == 0:
            oldallip = allip
            allip = []
        while (not allip) and iptrytime < 3:
            iptrytime += 1
            try:
                allip = getallip()
            except:
                allip = oldallip
                print("request ip timeout")
        
        proxy["https"] = random.choice(allip)
        headers = getheader(area)
        try:
            html = requests.get(url,proxies=proxy,headers=headers,timeout=5)
        except:
            print('request time out')
            continue
        soup = BeautifulSoup(html.text,'html.parser')
        latesttime = soup.find_all('td')
        try:
            latesttime = latesttime[0].string
        except:
            continue
        if latesttime:
            timeorderurl = 'https://gongshang.mingluji.com/' + area + '/zhuceriqi/' + latesttime
            proxy["https"] = random.choice(allip)
            headers = getheader(area)
            try:
                infopage = requests.get(timeorderurl,proxies=proxy,headers=headers,timeout=5)
            except:
                print('request time out')
                continue
            soup = BeautifulSoup(infopage.text,'html.parser')
            try:
                for i in soup.find('td').children:
                    try:
                        with open('node.txt','w',encoding='utf8') as nodef:
                            print(int(i.attrs['href'].split('/')[-1]),file = nodef)
                        return int(i.attrs['href'].split('/')[-1])
                    except:
                        continue
            except:
                continue
    return 0
        
def mixfile():
    filedict = dict()
    files = os.listdir()
    files = list(files)
    read_file = 0
    for file in files:
        if file[:9] == "miss_data":
            read_file += 1
            if read_file % 20 == 0:
                for (filename,itemlist) in filedict.items():
                    try:
                        with open(filename,'r',encoding='utf8') as f1:
                            reader1 = list(csv.reader(f1))
                            filedict[filename].extend(reader1)

                    except:
                        print('创建文件{}'.format(filename))
                    itemlist.sort(key=lambda x:int(x[-1]))
                    with open(filename[3:],'w',encoding='utf8',newline='') as f1:
                        writer = csv.writer(f1)
                        for i in itemlist:
                            writer.writerow(i)
                    with open(filename,'w',encoding='utf8',newline='') as f1:
                        writer = csv.writer(f1)
                        for i in itemlist:
                            writer.writerow(i)
                filedict = {}
            with open(file,encoding="utf8") as f:
                reader = list(csv.reader(f))
                for row in reader:
                    num = row[-1]
                    filename = 'utf' + str(int(num) + 1000 -1 - ((int(num) + 1000 -1)%1000)) + '.csv'
                    filedict.setdefault(filename,[])
                    filedict[filename].append(row)

                        
                        




def geturl(process,misslist,counterstart,counter,area):
    count = counterstart
    n = 0
    success = 0
    fail = 0
    trytime = 0
    url_page = ['https://gongshang.mingluji.com/'+area+'/node/{}'.format(num) for num in misslist]
    datalists = []
    allip = []
    while not allip:
        try:
            allip = getallip()
        except:
            print("request ip timeout")
    proxy = {"https":""}
    proxy["https"] = random.choice(allip)
    headers = getheader(area)
    print('代理ip: {}'.format(proxy['https']))
    starttime = time.time()
    datalists = []
    for page in url_page:
        if trytime == 10:
            fail += 1
        if n % 50 == 0:
            print('process {}: success: {}    fail: {}'.format(process, success, fail))
        n+=1
        pagenum = page.split('/')[-1]
        trytime = 0
        while trytime < 10:
            endtime = time.time()
            if endtime - starttime > 60:
                try:
                    allip = getallip()
                    starttime = endtime
                except:
                    print("request ip timeout")
            try:
                trytime+=1
                headers = getheader(area)
                try:
                    html = requests.get(url=page,proxies=proxy,headers=headers,timeout=5)
                except:
                    proxy["https"] = random.choice(allip)
                    headers = getheader(area)
                    continue
                if(html.status_code==200 and html.text):
                    trytime=0
                    datalist = ['','','','','','','',str(pagenum)]
                    success += 1
                    soup = BeautifulSoup(html.text,'html.parser')
                    datalist[0] = soup.find_all(attrs={"itemprop":"name"})
                    datalist[1] = soup.find_all(attrs={"itemprop":"address"})
                    datalist[2] = soup.find_all(attrs={"itemprop":"location"})
                    datalist[3] = soup.find_all(attrs={"itemprop":"founder"})
                    datalist[5] = soup.find_all(attrs={"itemprop":"foundingDate"})
                    temp = soup.find_all("span")
                    for i in range(len(temp)):
                        if temp[i].string == "注册资金":
                            datalist[4] = temp[i+1].string
                            break
                    datalist[6] = soup.find_all(attrs={"itemprop":"makesOffer"})
                    for i in range(7):
                        if datalist[0]:
                            try:
                                datalist[i] = datalist[i][0].string
                            except:
                                continue
                        else:
                            datalist[i] = ''
                    datalists.append(datalist)
                    break
                else:
                    proxy["https"] = random.choice(allip)
                    headers = getheader(area)
            except:
                fail += 1
                continue
        time.sleep(random.random()*2)
        #每counter个保存一次
        if datalists:
            if datalists[-1][-1] != str(pagenum):
                datalists.append(['','','','','','','',str(pagenum)])
        if(n%counter==0):
            with open("miss_data"+str(count)+".csv","w",encoding='utf8',newline='') as f:
                count+=1
                writer = csv.writer(f)
                for i in datalists:
                    try:
                        writer.writerow(i)
                    except:
                        print('write file error')
                        continue
                datalists = []

def ReadFile(filePath,encoding):
    with codecs.open(filePath,"r",encoding) as f:
        return f.read()
def WriteFile(filePath,u,encoding):
    with codecs.open(filePath,"w",encoding) as f:
        f.write(u)
'''
定义GBK_2_UTF8方法，用于转换文件存储编码
'''
def GBK_2_UTF8(src,dst):
    content = ReadFile(src,encoding='gbk')
    WriteFile(dst,content,encoding='utf_8')
    
def UTF8_2_UTF8(src,dst):
    content = ReadFile(src,encoding='utf_8')
    WriteFile(dst,content,encoding='utf_8')
 
'''
qyx.csv文件使用GBK编码存储，现在将其转为UTF_8存储
'''
#11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

if __name__ == '__main__':
    print('拼接已有文件')
    mixfile()
    area = 'shanghai'
    counter = 1000
    area = input("输入检索的地区(e.g. shanghai): ")
    maxnodenum = 0
    print('正在查询最大的node值...')
    maxnodenum = getmaxnode(area)
    if maxnodenum == 0:
        maxnodenum = input('获取最大node值错误，手动输入: ')
    else:
        print('最大node值 {}'.format(maxnodenum))
#change file format to utf-8

    print('转换文件为utf-8编码...')
    files = os.listdir()
    for file in files:
        if file[-3:] == "csv":
            src = file
            dst = 'utf'+file
            if src[:4] == 'qiye':
                dst = 'utf' + file[4:]
            if src[:3] == 'utf':
                continue
            if src[:4] == 'miss':
                continue
            try:
                GBK_2_UTF8(src,dst)
            except:
                UTF8_2_UTF8(src,dst)
        
        
#create misslist

    misslist = []
    files = os.listdir()
    files = list(files)
    print('检测csv文件正确性...')
    for file in files:
        if file[-3:] == "csv" and file[:3] == "utf" and file[3:6] != "utf":
            with open(file,encoding="utf8") as f:
                reader = list(csv.reader(f))
                if len(reader) > 1000:
                    print("文件{}中条目数量超过1000".format(file))
                if int(re.sub("\D","",file)) <1000:
                    print("文件{}命名错误".format(file))

    print('提取缺失条目...')
    for file in files:
        if file[-3:] == "csv" and file[:3] == "utf" and file[3:6] != "utf":
            with open(file,encoding="utf8") as f:
                reader = list(csv.reader(f))
                filenum = file
                filenum = re.sub("\D","",filenum)
                for i in range(len(reader)):
                    if not reader[i][0]:
                        if (int(filenum)-1000+i) >= 0:
                            misslist.append(int(filenum)-1000+i)
                if len(reader) != 1000:
                    for i in range(len(reader),1000):
                        if (int(filenum)-1000+i) >= 0:
                            misslist.append(int(filenum)-1000+i)
    newfilelist = [int(re.sub("\D","",file)) for file in files if file[-3:] == "csv"]
    newfilelist = [int(i/1000) for i in newfilelist if i > 1000]
    newfilelist = list(set(newfilelist))
    for i in range(1,int(maxnodenum/1000)):
        if i not in newfilelist:
            for n in range(1,1001):
                if ((i-1)*1000+n) >= 0:
                    misslist.append((i-1)*1000+n)
    with open("misslist.txt","w") as f:
        for i in misslist:
            print(i,file=f)
    misslist.sort()
    print("misslist.txt文件在 {} 创建,共缺少 {} 条记录".format(sys.path[0],len(misslist)))
    print("开始获取缺少的记录...")

    treadnum = input("输入需要的进程数")
    treadnum = int(treadnum)
    for i in range(treadnum):
        time.sleep(2)
        print('process {} started'.format(i))
        single = int(maxnodenum/treadnum)
        countstart = int(single/counter)
        p = multiprocessing.Process(target=geturl, args=(i,misslist[i*single:(i+1)*single],countstart*i+1,counter,area))
        p.start()
