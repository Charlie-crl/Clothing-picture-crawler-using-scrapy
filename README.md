# Clothing-picture-crawler-using-scrapy
### 研一导师小任务

爬取穿针引线官网服装设计图片做CV研究。现已实现爬取作品下设计稿，其他栏目类似。

### 用到的技术

主要是scrapy框架，用动态请求间隔与随机UA来实现反爬，分布式与IP代理暂未实现。数据大概几万张图片。

### 快速开始

安装scrapy相关类库，再下载一个配置json文件放入相应位置，具体参阅

https://www.freesion.com/article/37461287842/

最后运行 quick_start.py 文件即可
### debug
在运行过程中若看到日志里出现421状态码而不是200，手动打开浏览器通过验证码即可

