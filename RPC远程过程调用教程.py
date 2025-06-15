"""
RPC重点: 找到加密函数的地方
"""

"""

1. 安装油猴
    油猴的基础使用
2. 得安装java
3. 安装sekiro, 并且运行起来
    https://oss.iinti.cn/sekiro/sekiro-demo
4. 将js代码注入到油猴中去, 先就放默认的js代码, 后面找到通过断点的代码来调整

注意:
1. 传递数据的时候最好使用post, 一旦数据非常长使用get就会失败
2. 油猴中写的变量得用var
3. 测试的时候, resolve里面的内容不能是数字
4. sekiro得一直开着
5. 所访问的网站也得通过浏览器一直打开
6. 编写完油猴的代码, 一定得保存, 同时一定得刷新访问的网站, 注意油猴是否注入到该网站中
"""

import requests

url = "http://127.0.0.1:5612/business/invoke"
params = {
    "group": "dy_live",
    "action": "test",
    "s":"xx"
}
data = {
    't': 'xx'
}
r = requests.get(url, params=params).text
print(r)
