import requests

# name=[]
proxies = {
    "http":'116.211.118.3:808',
    "https":'116.211.118.3:808',
}

r = requests.get("https://www.baidu.com", proxies=proxies)
print r.url,
