[![Python3](https://www.python.org/)]

[西游代理](https://xiyou360.net/)是一个价格适当、不限流量、简单易用的代理。

有时候需要在 windows 下使用，但不希望它接管系统代理  
实际上西游 windows 客户端启动后，会在 127.0.0.1:9999 启动 http proxy，可以方便的在命令行中使用  
只需要再把对应的系统代理配置关掉就好了  
可气的是西游客户端会定时检查代理的配置情况并修正，真是勤劳的家伙  
除了深入修改源码外，就开发了这个服务，运行 run.py 就可以在托盘中添加一个图标，程序功能是定时关闭系统代理。

如果要深入源码去研究西游的代理，最好看一下 chrome 插件，尤其是看下 Network，基本能把流程理清。

使用
----
```bash
git clone https://github.com/shapled/xiyou-helper
cd xiyou-helper
pip install -r requirements.txt
python run.py
```

可以把 .py 后缀的文件关联上 python 程序，然后做到软链接到桌面  
