# -*- coding: utf-8 -*-
"""
Create on: 2018-2-6
@Author  : sunhailin-Leo
@File    : wx_backend.py
"""

# Sanic包
from sanic import Sanic

from controller.wx_controller import wx_bp


app = Sanic(__name__)

# 蓝图模式
app.blueprint(wx_bp, url_prefix='/weixin')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)

