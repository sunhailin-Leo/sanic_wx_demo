# -*- coding: utf-8 -*-
"""
Create on: 2018-2-6
@Author  : sunhailin-Leo
@File    : reply_center.py
"""
# Python内置库
import time
import datetime


def reply_text(to_user, from_user, content):
    """
    以文本类型的方式回复请求
    :param to_user:
    :param from_user:
    :param content:
    :return:
    """
    return """
    <xml>
        <ToUserName><![CDATA[{}]]></ToUserName>
        <FromUserName><![CDATA[{}]]></FromUserName>
        <CreateTime>{}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{}]]></Content>
    </xml>
    """.format(to_user, from_user,
               int(time.time() * 1000), content)


def reply(openid, msg):
    """
    回复逻辑
    :param openid:
    :param msg:
    :return:
    """
    if "日期" == msg:
        return "今天是%s" % datetime.datetime.now().strftime('%Y年%m月%d日 %H时%M分%S秒')
    else:
        return "其他的...\n等等吧...我的功能还很一般."
