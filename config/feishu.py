# -*- encoding: utf-8 -*-
"""
@Author  : Shirley
@File    :feishu.py
@Time    :2023/9/20 13:41
@Remark :飞书通知
"""
import sys
import requests
 
#定义python系统变量
# JOB_URL = sys.argv[1]
# JOB_NAME = sys.argv[2]
JOB_URL = "http://localhost:8080/job/LocalWorkspace/job/LocalShirleyPytest/"
JOB_NAME = "H37项目功能自动化测试"
# 飞书机器人的webhook地址
url = 'https://open.feishu.cn/open-apis/bot/v2/hook/5b341c51-959d-4107-bb68-b2713787a8bb'
method = 'post'
headers = {'Content-Type':'application/json'}
 
data = {
    "msg_type": "interactive",
    "card": {
        "config": {
                "wide_screen_mode": True,
                "enable_forward": True
        },
        "elements": [{
                "tag": "div",
                "text": {
                        "content": "用例已执行完成", # 这是卡片的内容，也可以添加其他的内容：比如构建分支，构建编号等
                        "tag": "lark_md"
                }
        }, {
                "actions": [{
                        "tag": "button",
                        "text": {
                                "content": "查看测试报告", # 这是卡片的按钮，点击可以跳转到url指向的allure路径
                                "tag": "lark_md"
                        },
                        "url": f"{JOB_URL}/allure/", # JOB_URL 调用python定义的变量，该url是服务器下的allure路径
                        "type": "default",
                        "value": {}
                }],
                "tag": "action"
        }],
        "header": {
                "title": {
                        "content": f"{JOB_NAME}" + "构建报告", # JOB_NAME 调用python定义的变量，这是卡片的标题
                        "tag": "plain_text"
                }
        }
    }
}
print("JOB_NAME:",JOB_NAME)
print("JOB_URL:",JOB_URL)
res= requests.request(method=method,url=url,headers=headers,json=data)
print(res)
print(res.json())