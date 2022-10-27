'''import  requests
url="https://movie.douban.com/j/chart/top_list"
a={ "type": "24",
"interval_id": "100:90",
"action":"",
"start": 60,
"limit": 20,}
headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
b=requests.get(url=url,params=a,headers=headers)
print(b.json())
b.close()'''''
'''import  re
import requests
url="https://movie.douban.com/typerank"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
page=requests.get(url,headers=headers)
page.close()'''''
'''import re
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
domain="https://m.dytt8.net/index2.htm"
reps=requests.get(url=domain,verify=False)
reps.encoding="gb2312"
obj=re.compile(r"最新电影更新.*?<ul>(?P<nan>.*?)</ul>",re.S)
obj2=re.compile(r"<a herf='(?P<LIANJIE>.*?)'",re.S)
result1=obj.finditer(reps.text)
for i in result1:
  ul=i.group('nan')

  result2=obj2.finditer(ul)
  for j in result2:
     print(j.group('LIANJIE'))'''''
'''''import  requests
from bs4 import BeautifulSoup
url="http://www.xinfadi.com.cn/priceDetail.html"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
reps=requests.get(url=url,headers=headers)
A=BeautifulSoup(reps.text,"html.parser")
b=A.find("div",class_="tbl-body")
print(b)
reps.close()'''
''''import  re
import  bs4
import time
import requests
from bs4 import BeautifulSoup
url ="https://m.woyaogexing.com/tupian/"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
reps=requests.get(url,headers=headers)
reps.encoding="utf-8"

FIRST=BeautifulSoup(reps.text,"html.parser")
SECOND=FIRST.find("div",class_="g-piclist-container").find_all("a")
for a in SECOND:
    c="https://m.woyaogexing.com"+a.get("href")
    child=requests.get(c)
    child.encoding="utf-8"
    child_text=child.text
    child.encoding="utf-8"
    child_page=BeautifulSoup(child_text,"html.parser")
    third =child_page.find("li",class_="tx-box size big").find_all("a")

    for d in third:
        e="https:"+d.get("href")
        print(e)
        img_resp=requests.get(e)
        img_name=e.split("/")[-1]
        with open(img_name,mode="wb")as f:
            f.write(img_resp.content)
        print("over")
        time.sleep(2)
print("all over")'''''
'''import requests
from lxml import etree
url="https://www.zbj.com/ydyykf/f.html?fr=newpdy.it.20.8.04&r=1"
reps=requests.get(url)
html =etree.HTML(reps.text)

divs=html.xpath("/html/body/div[2]/div/div/div[2]/div/div[2]/div[4]/div[1]/div[1]")
print(divs)
reps.close()'''

'''import requests
session=requests.session()
data={
"loginName": "19830905193",
"password": "grb200104"
}
url="https://passport.17k.com/ck/user/login"
requests.post(url,data=data)
''''''
reps=requests.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919',headers={
"Cookie": "GUID=accb2ae6-9e8f-417b-a9c5-389f3b2a02fc; __bid_n=18405162803686bfba4207; c_channel=0; c_csc=web; Hm_lvt_9793f42b498361373512340937deb2a0=1666532643,1666578877,1666580779,1666599605; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F15%252F35%252F61%252F99196135.jpg-88x88%253Fv%253D1666532904000%26id%3D99196135%26nickname%3Dgrb20%26e%3D1682152208%26s%3Ddcd97135f9dc4ff8; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2299196135%22%2C%22%24device_id%22%3A%22184051610bc1116-08a97ab9a4f92b-26021c51-1327104-184051610bd576%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22accb2ae6-9e8f-417b-a9c5-389f3b2a02fc%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1666615460"
})
print(reps.json())
reps.close()'''
'''import requests
url="https://www.pearvideo.com/video_1481261"
cont_ID=url.split("_")[1]
videostaus=f"https://www.pearvideo.com/videoStatus.jsp?contId={cont_ID}&mrd=0.9060101879510951"
reps=requests.get(videostaus,headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
"Referer": "https://www.pearvideo.com/video_1481261"
})
dic=reps.json()
srcurl=dic["videoInfo"]["videos"]["srcUrl"]
systemTime=dic["systemTime"]
srcurl=srcurl.replace(systemTime,f"cont-{cont_ID}")
with open("a.mp4",mode="wb")as  f:
    f.write(requests.get(srcurl).content)
reps.close()'''
import  requests
from Crypto.Cipher import AES
from base64 import  b64encode
import json
url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
data={
"csrf_token": "",
"cursor": "-1",
"offset": "0",
"orderType": "1",
"pageNo":"1",
"pageSize": "20",
"rid": "R_SO_4_1891431677",
"threadId": "R_SO_4_1891431677",
    }
"""   function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {d；data e:010001
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }"""
f="00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g='0CoJUm6Qyw8W8jud'
i="Y29V9D9Bg8UutxTM"
e = "010001"
def get_encseckey():
    return "bb2595377508b61e1ac52299f9463c2d17e998e91188b8bd70d57167fdaef677573aedb2a6a09cf273ee176b72335d2b46a4607bcb84eaa3e6dbb1d52135ca288119a84a2ed633412c12422846f2d59b487c41b9904c6f827d795cfee566bc4df00e8d2455ec6e06085523308987d9fe096416166114b0be08af06674a48f1ea"
def get_params():
    first=enc_params(data,g)
    second=enc_params(first,i)
    return second
def enc_params(data,key):
    iv="0102030405060708"
    data=to16(data)
    aes=AES.new(key=key.encode("utf-8"),IV=iv.encode("utf-8"),mode=AES.MODE_CBC)
    bs= aes.encrypt(data.encode("utf-8"))
    b64encode(bs)
    return str(b64encode(bs),"utf-8")
def to16(data):
    pdd=16-len(data)%16
    data+=chr(pdd)*pdd
    return data
reps=requests.post(url,data={
    "params":get_params(json.dumps(data)),
    "encSeckey":get_encseckey()
})
print(reps.text)