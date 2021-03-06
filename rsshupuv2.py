import json
import random
import re
import requests
from bs4 import BeautifulSoup
import AddXML

class hot_topic(object):
    def __init__(self,spot_topic:str):
        self.spot_topic=spot_topic

    def getRandomAgent(self):
        USER_AGENTS = [
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        ]
        return USER_AGENTS[random.randint(0, 9)]


    def crawl_his_tops(self):
        headers={
            "user-agent":self.getRandomAgent(),
        }
        rp=requests.get(self.spot_topic,headers=headers)
        soup = BeautifulSoup(rp.content,'lxml')
        his_feeds=soup.find_all(attrs={'class':'jc-c'})[1]
        spot_topic_set=[]
        for his_news in his_feeds.find_all('tr'):
            entry=his_news.find_all('td')
            s=entry[1].get_text()
            s=s.replace(" ", "")
            s = s.replace(".", "")
            cop = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9]")  # ??????????????????????????????????????????????????????
            # string1 = '@ad&*jfad???132???www????????????'
            string1 = cop.sub('', s)  # ???string1???????????????????????????????????????

            # entry_content={
            #     "??????":entry[1].get_text(),
            #     "??????":entry[2].get_text(),
            #     "??????":domain + entry[1].a.attrs['href']
            # }{"a":1,"b":2,"c":3,"d":4,"e":5}
            entry_content="{\"title\":"+"\""+string1 +"\""+ ","+"\"link\":"+"\""+domain + entry[1].a.attrs['href']+"\""+"}"
            spot_topic_set.append(entry_content)
        return spot_topic_set



if __name__ == '__main__':
    websites={
        # '????????????': "https://tophub.today/n/KqndgxeLl9",  # ????????????
        # '????????????': "https://tophub.today/n/mproPpoq6O",  # ????????????
        # '????????????': "https://tophub.today/n/Jb0vmloB1G",  # ????????????
        # '36???': "https://tophub.today/n/Q1Vd5Ko85R",  # 36???
        # '?????????': "https://tophub.today/n/Y2KeDGQdNP",  # ?????????
        # '?????????': "https://tophub.today/n/5VaobgvAj1",  # ?????????ENeYLEZdY4\1VdJzbpdLQ\G47o8weMmN\MZd7wnDdrO??????\???????????? ????????????NKGoRAzel6
    }

    domain="https://tophub.today"

    # my_sender = '395407702@qq.com'  # ?????????????????????
    # my_sender_alias = '???????????????'  # ?????????????????????
    # my_pass = 'frrxawwuwmzybghg'  # ?????????????????????
    # my_user = '395407702@qq.com'  # ????????????????????????????????????????????????
    # my_user_alias = '??????????????????'  # ???????????????????????????
    websites_brief=""
    spot_topic_set = hot_topic("https://tophub.today/n/G47o8weMmN").crawl_his_tops()
    # print(spot_topic_set)
    for i in spot_topic_set:
        data_dict = json.loads(i)
        print(data_dict)
        Title=data_dict['title']
        # Title = data_dict['title']
        Url = data_dict['link']
        # print(fg)
        AddXML.add_newxml(Title, Title, Url)



    # for key,value in websites.items():
    #     website_ttile = key
    #     spot_topic_set=hot_topic(websites[website_ttile]).crawl_his_tops()
    #     print(type(spot_topic_set))
    #     print(spot_topic_set)

    #     website_context="\n".join(["<tr><td>"+spot["??????"] + "<a href=" + spot["??????"] +">" + spot["??????"] + "</a></td></tr>" for spot in spot_topic_set ])
    #     website_section="<table><tr>{}</tr>{}</table>".format(website_ttile,website_context)
    #     websites_brief +=website_section
    # context_ttile="??????????????????(??????|??????|??????|36???|?????????|?????????)"
    # sd = sendEmail.send_mail(my_sender, my_pass, my_user, context=websites_brief, my_sender_alias=my_sender_alias, my_user_alias=my_user_alias,context_ttile=context_ttile)
    # sd.make_message()
    # sd.send_mail()
    # print("??????{}????????????".format(context_ttile))
