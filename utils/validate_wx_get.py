# -*- coding: utf-8 -*-
"""
Create on: 2018-2-6
@Author  : sunhailin-Leo
@File    : validate_wx_get.py
"""
# Python内置库
import hashlib


def validate(request):
    """
    校验token
    :param request: 请求
    :return: str
    """
    # 这里改写你在微信公众平台里输入的token
    token = 'sunhailin'

    # 获取输入参数
    data = request.args
    signature = data.get('signature', '')
    timestamp = data.get('timestamp', '')
    nonce = data.get('nonce', '')
    echostr = data.get('echostr', '')

    # 字典排序
    list_1 = [token, timestamp, nonce]
    list_1.sort()

    s = list_1[0] + list_1[1] + list_1[2]

    # sha1加密算法
    code = hashlib.sha1(s.encode('utf-8')).hexdigest()

    # 如果是来自微信的请求，则回复echostr
    if code == signature:
        return echostr
    else:
        return ""
