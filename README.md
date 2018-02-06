# Sanic 微信公众号开发 --- 初探

---

<h3 id="Prepare">准备工作</h3>

* 一个linux系统或者一个mac电脑(因为Sanic不兼容Windows)
* 一个服务器(云服务器就可以了,如果是在内网的很麻烦,而且不推荐那么折腾)
* Python3.5以上(之前版本都不支持)
* 一个公众号(个人或者企业都可以)

---

<h3 id="ProEnv">项目环境</h3>

* Ubuntu 17.10 (建议用16.01或者14.04的,因为太新了gcc和g++安装部分要往下降级比较麻烦)
* Python 3.5.5 (用了3.5最新的版本)
* 编译器Pycharm最新版本

---

<h3 id="ProStructure">项目结构</h3>

```html
sanic_wx_project/
|-- controller/
|   |-- __init__.py
|   |-- wx_controller.py
|
|-- utils/
|   |-- __init__.py
|   |-- reply_center.py
|   |-- validate_wx_get.py
|
|-- README
|-- requirements.txt
|-- wx_backend.py
```

* controller -- 蓝图的实现方法
* utils      -- reply_center是回复中心, validate_wx_get是返回微信那边的GET请求,在初次校验token的时候需要使用
* wx_backend -- 启动Sanic的方法

---

<h3 id="WxDev">微信公众号开发的答疑区</h3>

大致申请公众号流程以及开发前的准备:

1. 申请一个公众号(初学者用个人帐号)
2. Sanic如果没有用gunicorn或者nginx做代理,那么请在启动时使用80端口(原因很简单,微信那边只认80端口)
3. 准备好一个公网的服务器或者云服务器(我用阿里云的,开放80端口)
4. 先写好一个get方法去返回验证token结果(代码如下)

```python
import hashlib

def validate(request):
    """
    校验token
    :param request: 请求
    :return: str
    """
    # 这里改写你在微信公众平台里输入的token
    token = 'token'
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
```

5. 公众号管理界面验证成功后点启用就ok了.接下来就是开发的过程了.
6. 具体开发有什么权限的请研读接口权限(需要在登录平台后才能看)、[微信公众平台技术文档](https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1445241432)
7. 以上弄完就可以认真开发调试了.

---

<h3 id="Chat">小谈</h3>

* 我一直关注Sanic很久了,最近才有时间静下来认真看Sanic(如果之前有学习过Flask或者Flask-restful就很容易上手).
* Django的同学就可以要花点时间去适应下Sanic的写法
* Sanic大概花了一天的时间去看文档，然后开发这个demo只用了一个下午(demo代码就不多, so easy)
* 之后自己会在demo的基础上开发更多的功能,玩玩微信公众号的二次开发.