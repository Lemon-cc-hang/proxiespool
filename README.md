# proxiespool
代理池 存储进入mongodb里



安装依赖 `pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/`



运行:

进入目录下

```shell
python main.py
```

或

```shell
bash start.sh
```



构建代理池 , 还没有设计接口

>  取出代理

需要自己从数据库中取出



>  设计原理

**分数制:**  ***由于 免费的代理的时效性***

- 获取代理并验证, 如果验证成功, 
    - 如果数据库没有, 存入数据库, 并初始化分数10分
    - 如果数据库有, 分数+1
- 如果验证失败
    - 如果数据库有, 分数-1
- 爬取完毕之后, 取出所有的代理, 再次进行验证



请求头随机换 来 频繁请求网站, 当数据库中的代理 有100个以上的时候, 取出分数最高的10个, 随机返回一个代理 进行请求, 防止封自己的IP地址



> 个人博客

http://www.hangblog.com.cn/