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
- 当分数 < 10 的时候
    - 如果验证成功, 分数 == 10
- 当分数 >= 100 的时候
    - 分数不再增加
- 爬取完毕之后, 取出所有的代理, 再次进行验证



请求头随机换 来 频繁请求网站, 当数据库中的代理 有100个以上的时候, 取出分数最高的10个, 随机返回一个代理 进行请求, 防止封自己的IP地址



**目的:**

1. 保证后面的高分代理都是高可用的
2. 防止一次的 代理连接失效 而删除代理



> 项目详解

1. db.dbClient:

    用于集成数据库, 以方便, 日后增加数据库, 所有数据库通用方法

2. db.mongoClient:

    mongodb配置

3. db.redisClient:

    待更新

4. finish\_.finish\_:

    结束时验证数据库的代理

5. helper.common:

    集成logs和dbClient, 生成对象, 建立一个对象即可

6. helper.logs:

    日志封装

7. helper.scheduler:

    调度getHtml和parseHtml方法

8. helper.verify:

    验证数据方法封装

9. logs.scraping.log:

    日志记录,  需要的话可以在logs模块自行添加

10. spider.getHtml:

    获取网页源代码

11. spider.getPages:

    获取网页的页面数量

12. spider.parseHtml:

    解析页面

13. spider.spider:

    爬虫模块封装

14. config.py:

    配置_ 还没完善

15. Dockerfile:

    由于本人学艺不精, 生成docker镜像时候频频出错, 有大佬可以指点一下

16. main.py  start.sh:

    启动



> 个人博客

http://www.hangblog.com.cn/