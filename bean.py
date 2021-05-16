#原作者：happy knva
#精简：@yyfyy123
#增加推送：@vesugier

from datetime import datetime, timezone, timedelta
from telethon import TelegramClient, events
import requests, re, time, os, urllib.parse

api_id = ''
api_hash = ''
tg_user_id = ''
tg_bot_token = ''
output_msg = True # 是否打印消息
channel_white_list = [1479368440,1197524983] # 过滤频道消息 1427039780 1212172599,
cookies = [
         ''
  
        ]
        
        #'pt_pin=as2012_m;pt_key=AAJgSdj0ADDfOtWVexcRjwaQ_j9PeY4RvuUj8Mk5mgynO6oj51-wUl1GGAMdXq1-N-beWMKJJdA;'

proxies={ #tg推送用代理，不需要的请删除51行proxies参数或者取消52行注释 注释51行
        'http':'http://127.0.0.1:7890',
        'https':'http://127.0.0.1:7890'
        }

regex = re.compile(r"(https://api.m.jd.com.*)\)", re.M)

client = TelegramClient(
        'test',
        api_id,
        api_hash
        )

#Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Mobile/15E148 Safari/604.1
headers = {
        "User-Agent": "jdapp;iPhone;9.2.2;14.2;%E4%BA%AC%E4%B8%9C/9.2.2 CFNetwork/1206 Darwin/20.1.0",
        "Cookie": "",
        "Referer": "https://servicewechat.com/wx4830b51270836408/13/page-frame.html"
        }

# utc_datetime = datetime.utcnow().replace(tzinfo=timezone.utc)
# beijing_datetime = utc_datetime.astimezone(timezone(timedelta(hours=8)))

# if beijing_datetime.minute % 10 == 0:
    # f = open("push.txt","r")
    # text = f.read()
    # f.close()
    # msg ={
        # 'chat_id': {tg_user_id},
        # 'text': f'直播间京豆\n\n{text}',
        # 'disable_web_page_preview': 'true'
        # }
    # #requests.post(url=f'https://api.telegram.org/bot{tg_bot_token}/sendMessage', data=msg, timeout=15, proxies=proxies).json()
    # requests.post(url=f'https://api.telegram.org/bot{tg_bot_token}/sendMessage', data=msg, timeout=15).json()
    # f = open("push.txt","w")
    # f.write(" ")
    # f.close()

def get_bean(url):
    for cookie in cookies:
        pt_pin = urllib.parse.unquote(cookie.split(';')[0].split('=')[1]);
        headers["Cookie"] = cookie
        res = requests.get(url, headers=headers).json()
        if int(res['code']) != 0:
            print(pt_pin, "cookie无效")
        else:
            print(pt_pin, res['result']['giftDesc'])
        desp = ''
        desp += '{}\n'.format(res['result']['giftDesc'])
        # if "None" in desp:
            # continue
            # #break
        # else:
            # f=open(push.txt,"a")
            # f.write(desp)
            # f.close


@client.on(events.NewMessage)
async def my_event_handler(event):
    if event.peer_id.channel_id not in channel_white_list :
        return
    jdUrl = re.findall(regex, event.message.text)
    if output_msg:
        print(event.message.text)
    if len(jdUrl) == 1:
        get_bean(jdUrl[0])

with client:
    client.loop.run_forever()