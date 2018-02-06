# -*- coding: utf-8 -*-
"""
Create on: 2018-2-6
@Author  : sunhailin-Leo
@File    : wx_controller.py
"""
# Python内置库
import time
import xml.etree.ElementTree as Element

# Sanic
from sanic.response import text
from sanic import Blueprint

# 项目内部库
from utils.validate_wx_get import validate
from utils.reply_center import *

# 初始化一个Blueprint
wx_bp = Blueprint("wx_bp")


@wx_bp.route("/", methods=["GET", "POST"])
async def root_path(request):
    # 获取请求方式
    method = request.method
    print("Request method: %s " % method)
    if method == "GET":
        return text(validate(request=request))
    else:
        """
        收到POST请求就是有信息在公众号里面
        需要解析很多东西
        目前只解析: 文字信息
        """
        # 这里用的request.body
        # xml数据都在body里面
        xml_res = Element.fromstring(request.body.decode("UTF-8"))

        # 解析xml里面的数据. 具体有哪些数据还是要看微信公众号里面的开发文档
        to_user = xml_res.find('ToUserName').text
        from_user = xml_res.find('FromUserName').text
        msg_type = xml_res.find("MsgType").text
        create_time = xml_res.find("CreateTime")

        # 文字信息
        if msg_type == "text":
            content = xml_res.find('Content').text
            return text(reply_text(from_user, to_user, reply(from_user, content)))
