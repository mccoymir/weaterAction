#!/usr/bin/python3
#coding=utf-8

import requests, json
import os

SCKEY= os.environ.get('SCKEY') ##Server酱推送KEY


def ServerPush(info): #Server酱推送
    api = "https://sc.ftqq.com/{}.send".format(SCKEY)
    title = u"青医推送"
    content = info.replace('\n','\n\n')
    data = {
        "text": title,
        "desp": content
    }
    print(content)
    requests.post(api, data=data)
# def CoolPush(info): #CoolPush酷推
#     # cpurl = 'https://push.xuthus.cc/group/'+spkey   #推送到QQ群
#     # cpurl = 'https://push.xuthus.cc/send/' + SKey  # 推送到个人QQ
#     api='https://push.xuthus.cc/send/{}'.format(SKey)
#     print(api)
#     print(info)
#     requests.post(api, info.encode('utf-8'))
def main():
    try:

            url = "https://wxzfb.qduhospital.cn/wehospital/opregister/getschedoclist?departmentCode=cSt3dw&schDate=2021-12-29"

            payload='departmentCode=%20cSt3dw&schDate=%202021-12-22'
            headers = {
                        'Referer': 'https://wxzfb.qduhospital.cn/wehospital/opregister/choosedoctor/cSt3dw?chInfo=ch_share__chsub_Copyli%3Cx%3Enk&code=021kUm000vTV5M1y5e400XOPzP1kUm0A&state=7b553326e44ecb8e1c1434b113cbb873',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Cookie': 'PHPSESSID=2f1fc8286fb40fb4742664c5e7c22f83',
                        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
                        'sec-ch-ua-mobile': '?0',
                        'X-Requested-With': 'XMLHttpRequest'
                        }

            response = requests.request("POST", url, headers=headers, data=payload)
            t = response.json()  #返回的数据
            msg =  t['msg']
            htxt = t['html']
            print(htxt)
            if not htxt.__contains__("暂无数据"):
                ServerPush(msg+htxt)
            # CoolPush(tdwt)
    except Exception:
        error = '【出现错误】\n　青医推送错误，请检查服务或网络状态！'
        print(error)
        print(Exception)
        ServerPush(error)

if __name__ == '__main__':
    main()
    
