<center><h2>个人简历</h2></center>  

### 个人信息  
* 贾冬青/男/1996/全日制本科/济南大学化学系  
* 期望职位: python后端  
* 期望城市: 上海/南京  

### 联系方式  
* 手机: 15318808480  
* 微信/QQ: 957360688  
* 邮箱: jeedq@qq.com  

### 技能  
- 开发框架: Django/Flask

- 数据库: Mysql/Redis  

- 熟悉Linux操作系统  

- 了解html/css/js、jQuery 、Ajax、bootstrap

- Git//Vim/Celery

### 学习经历  

- 大二时, 参照github上的shadowsocks源码完成科学上网, 在此期间,学会了vim的使用和Linux操作系统的部分使用
- 《笨办法学python》入门python语言学习
- 数据结构与算法
- 使用python建立tcp/udp的连接
- 基于tcp/ip协议搭建微型服务器
- 学习和应用MySQL、Redis数据库
- 基于微服务器，wsgi协议，编写微型框架（网页简单渲染，提供前端api接口，与mySQL交互等）并实现与服务器的解耦
- 学习html/css/js、jQuery 、Ajax、bootstrap等并做一些简单的前端小页面和动画效果
- django框架 - [天天生鲜项目](#天天生鲜) / [个人博客](#个人博客)
- flask框架 - [爱家租房项目](#爱家租房)  

### 项目实践  

> 本人学习过程通过自学和B站/YouTube等视频网站, 除项目网页模板之外的各种操作, 包括MySQL, Redis, FastDFS, 环境的搭建, python后端代码, 前端部分js, 前后端不分离时的模板渲染, 前后端分离时的ajax, 均为本人通过各种查询方式(csdn, 博客园, 知乎, 简书, github, 官方文档等)独立完成

##### 爱家租房

- 项目描述:
  1. 主页: 动态显示幻灯片 / 提供注册登陆 / 动态加载城区信息
  2. 用户: 注册 / 登陆 / 验证码60秒发送一次 / 错误过多记录ip5分钟再试
  3. 列表: 按时间,区域排序 / 分页加载信息 / 筛选条件更新后页面立即刷新
  4. 其他: 房屋详情 / 预定 / 个人主页修改个人信息, 上传房屋, 接订单等 

- 部 &nbsp; 署: 两个Ubuntu云服务器, 一个腾讯云, 一个阿里云
  - 腾讯云: redis缓存/储存session信息/异步broker, celery异步worker, MySQL数据库, Nginx与FastDFS配合提供分布式图片存储
  - 阿里云: Nginx提供静态文件/转发动态请求, gunicorn服务器+Flask框架

- 数据库: **MySQL** + **Redis**  
- 作品链接: [jeedq.cn](http://jeedq.cn)  
- 源码: https://github.com/PhoeniXWhite/ihome
- 测试账号: (密码均为: a12123)
    - 房客: 
    957360688@qq.com
    - 房东:
    jeedq@qq.com
    - 自行通过邮箱注册也可
- 前后端分离



##### 天天生鲜

- 项目描述: 
  1. 用户模块: 注册 / 登陆 / 用户订单 / 基本信息 / 用户地址等
  2. 商品模块: 负责展示首页, 详情页, 排序
  3. 购物车模块: 添加 / 展示 / 更新已选购的SKU
  4. 订单模块: 提交订单和支付(使用支付宝api)

- 部 &nbsp; 署: 
  - 利用了[爱家租房项目](#爱家租房) 部分环境: FDFS文件存储, redis和MySQL数据库
  - 腾讯云: Nginx: 提供静态文件/转发动态请求
  - 阿里云: Uwsgi服务器+ django框架

- 数据库: **MySQL** + **Redis**  
- 前后端不分离



##### 个人博客

- 部 &nbsp; 署: 
  - 腾讯云: Nginx: 提供静态文件/转发动态请求
  - 阿里云: gunicorn服务器+ django框架
- 支持 Markdown 语法和代码高亮  
- 自定义模板标签  
- 数据库: sqlite3
- 作品链接: http://49.234.29.32 (国内服务器未备案)
- 前后端不分离

