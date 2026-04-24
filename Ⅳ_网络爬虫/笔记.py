def main():
    #       ↓在此控制运行哪些章节的示例代码↓
    #        "ctrl + /" 快捷注释 / 取消注释
    #********************控制台********************
    # basic_theory()                 # 一、基础理论
    # http_and_https()               # 二、HTTP和HTTPS协议
    requests()                     # 三、requests入门
    #********************控制台********************

#--------------------------------------------------------------------------------
# 一、基础理论
def basic_theory():
    print("一、基础理论========================================")
    # 1.数据来源渠道：
    #   🞉 去第三方的公司购买(如企查查)
    #   🞉 去免费的数据网站下载(如国家统计局)
    #   🞉 通过爬虫爬取
    #   🞉 人工收集(如问卷调查)

    # 2.什么是爬虫？
    #   🞉 定义：爬虫(WebCrawler)是一种自动获取网页信息的程序或脚本，
    #           也称为网络蜘蛛(Spider)或网络机器人(Bot)
    #   🞉 举例：想象一只蜘蛛在网上不断地爬行，查找并收集各种信息
    #           搜索引擎如Google、百度等使用爬虫来自动抓取网页内容，以建立搜索引擎索引
    # 3.学习爬虫的好处：快速、自动地获取互联网上的各种数据，利于研究、分析和决策

    # 4.爬虫的主要用途：
    #   🞉 搜索引擎：
    #     · 搜索引擎利用爬虫收集网页信息，建立索引，用户通过搜索引擎可以快速找到所需信息
    #   🞉 数据分析：
    #     · 爬虫可以采集大量数据，用于分析和展示。用于数据分析、挖掘和建模，帮助企业了解市场趋势、用户行为等
    #   🞉 舆情分析：
    #     · 爬虫可以收集网络上的舆情信息，分析舆情走向，为企业决策提供参考
    #   🞉 信息监控：
    #     · 爬虫可以定时监控网页内容的变化，如监控竞争对手的价格变化、全网的热门话题信息数据
    #   🞉 信息聚合
    #     · 爬虫可以将不同来源的信息聚合到一起，为用户提供更便捷的信息获取方式
    #   🞉 应用开发：
    #     · 爬虫可以为应用开发提供数据支持，如天气预报、股票信息等

    # 5.爬虫的分类：
    #   🞉 通用爬虫(一般用于搜索引擎)，具有以下特点：
    #     · 广泛性：通用爬虫可以访问和抓取互联网上的绝大多数网站，具有很强的覆盖能力
    #     · 自动化：通用爬虫能够自动发现和抓取网页，无需人工干预，提高了效率
    #     · 智能化：通用爬虫通常会根据网页链接关系进行智能化的抓取，以尽可能全面地收集网页信息
    #     · 持续性：通用爬虫可以持续地抓取网页信息，保持数据的更新和完整性
    #     · 去重处理：通用爬虫会对抓取到的网页进行去重处理，避免重复抓取相同内容
    #     · 性能优化：通用爬虫会针对不同类型的网站和网络环境进行性能优化，提高抓取效率
    #   🞉 聚焦爬虫(用于特定领域/需求等)，具有以下特点：
    #     · 定制性强：聚焦爬虫根据特定需求定制开发，可以针对性地抓取目标网站的特定信息
    #     · 精准度高：由于定位明确，聚焦爬虫可以精准地抓取目标网站的所需信息，减少无效数据的抓取
    #     · 效率高：相比通用爬虫，聚焦爬虫只需抓取目标网站的特定内容，因此效率更高，消耗的资源更少
    #     · 隐蔽性强：聚焦爬虫一般不会频繁访问大量网站，降低了被目标网站封禁的风险
    #     · 数据处理：聚焦爬虫通常会对抓取到的数据进行处理和分析，以便更好地满足特定需求
    #     · 定时更新：聚焦爬虫可以定时更新目标网站的数据，保持数据的新鲜性和有效性
    #   🞉 增量式爬虫：在上一次抓取的基础上，只抓取新增加或有更新的数据，在提高效率的同时保持数据的及时性、准确性。
    #                 常用于新闻网站、论坛等需要频繁更新数据的场景
    #   🞉 深层网络爬虫：深层网络爬虫专门用来抓取存在于互联网深层的页面，这些页面通常是非结构化的，
    #                   需要通过特定的查询参数或请求才能访问。深层网络爬虫可能需要更多的技术和资源来实现高效的网页抓取

    # 6.爬虫的工作流程：
    #   🞉 发送请求：爬虫首先发送 HTTP请求 到目标网站
    #   🞉 获取响应：获取请求返回的响应内容
    #   🞉 解析响应，提取数据：爬虫解析响应内容，提取需要的信息，比如 URL链接、文本数据等
    #   🞉 存储数据：爬虫将提取的信息存储到本地文件或数据库中

    # 7.robots协议：
    #   Robots协议(也称为robots.txt)是一个位于网站根目录下的文本文件，用于指示搜索引擎爬虫哪些页面可以访问，
    #   哪些页面不应该被访问。该文件包含一系列规则，定义了爬虫对网站的访问权限。
    #   🞉 Robots协议的基本语法包括两个关键字：User-agent 和 Disallow
    #      · User-agent：指定了爬虫的名称或标识符
    #      · Disallow：指定了不允许被访问的URL路径
    #     示例：https://www.baidu.com/robots.txt
    #   注：实际使用时为了获取想要的数据往往需要违反robots协议，这注定了使用爬虫是灰色地带
    #       因此，不要将爬虫用于商业用途！不要采集隐私数据！！更不要采集非法数据！！！
    print("× 本章无控制台输出案例")

    print()
# --------------------------------------------------------------------------------
# 二、HTTP和HTTPS协议
def http_and_https():
    print("二、HTTP和HTTPS协议========================================")
    # 1.基础知识：
    #   HTTP协议(HyperText Transfer Protocol，超文本传输协议)：是一种发布和接收HTML页面的方法
    #   HTTPS(Hypertext Transfer Protocol over Secure Socket Layer)简单讲是HTTP的安全版，在HTTP下加入SSL层
    #   SSL(Secure Sockets Layer 安全套接层)主要用于Web的安全传输协议，在传输层对网络连接进行加密，保障在Internet上数据传输的安全
    #   🞉 HTTP 的端口号为 80
    #   🞉 HTTPS 的端口号为 443

    # 2.HTTP请求过程：
    #   HTTP通信由两部分组成：客户端请求消息 与 服务器响应消息
    #   浏览器发送HTTP请求的过程：
    #   (1).浏览器先向地址栏中的URL发起请求，并获取响应
    #   (2).在返回的响应内容(html)中，会带有css、js、图片等URL地址，以及ajax代码，
    #       浏览器按照响应内容中的顺序依次发送其他的请求，并获取相应的响应
    #   (3).浏览器每获取一个响应就对展示出的结果进行添加(加载)，js，css等内容会修改页面的内容，
    #       js也可以重新发送请求，获取响应
    #   (4).从获取第一个响应并在浏览器中展示，直到最终获取全部响应，并在展示的结果中添加内容或修改 ——
    #       这个过程叫做浏览器的渲染
    #   🞉 URL介绍：
    #      URL(Uniform/UniversalResourceLocator的缩写)：统一资源定位符，
    #      是用于完整地描述Internet上网页和其他资源的地址的一种标识方法(通俗的叫法就是网址)

    # 3.HTTP请求信息：
    #   3.1.HTTP请求报文：
    #       URL只是标识资源的位置，而HTTP是用来提交和获取资源
    #       客户端发送一个HTTP请求到服务器的请求消息，包括以下格式：
    #           请求首行
    #           请求头部
    #           空行
    #           请求数据
    #       四部分组成，以下是请求报文的一般格式：
    #           请求行：  | 请求方法 | 空格 | URL | 空格 | 协议版本 | 回车换行符 |
    #           请求头部{ | 头部字段名 | : | 值 | 回车换行符 |
    #                   { |               ...               |
    #                   { | 头部字段名 | : | 值 | 回车换行符 |
    #           请求数据：|               ...               |
    #   3.2.HTTP请求方法：
    #       根据HTTP标准，HTTP请求可以使用多种请求方法
    #       🞉 HTTP 0.9：只有基本的文本GET功能
    #       🞉 HTTP 1.O：完善的请求/响应模型，并将协议补充完整，定义了三种请求方法：GET，POST和HEAD方法
    #       🞉 HTTP 1.1：在1.0基础上进行更新，新增了五种请求方法：OPTIONS，PUT，DELETE.TRACE和CONNECT方法
    #        方法        描述
    #       GET        请求指定的页面信息，并返回实体主体
    #       HEAD       类似于get请求，只不过返回的响应中没有具体的内容，用于获取报头
    #       POST       向指定资源提交数据进行处理请求(例如提交表单或者上传文件)，数据被包含在请求体中。
    #                  POST请求可能会导致新的资源的建立和/或已有资源的修改
    #       PUT        从客户端向服务器传送的数据取代指定的文档的内容
    #       DELETE     请求服务器删除指定的页面
    #       CONNECT    HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器
    #       OPTIONS    允许客户端查看服务器的性能
    #       TRACE      回显服务器收到的请求，主要用于测试或诊断
    #
    #       爬虫发送HTTP请求，主要分为 GET 和 POST 两种方法：
    #       🞉 GET是从服务器上获取数据，GET请求参数显示，都显示在浏览器网址上，
    #          HTTP服务器根据该请求所包含URL中的参数来产生响应内容，即“Get”请求的参数是URL的一部分
    #          例如：http://www.baidu.com/s?wd=Chinese
    #       🞉 POST是向服务器提交数据，POST请求参数在请求体当中，消息长度没有限制而且以隐式的方式进行发送
    #   3.3.常用的请求头：
    #       🞉 Host (主机和端口号)
    #       🞉 Connection (链接类型)
    #       🞉 Upgrade-Insecure-Requests (升级为HTTPs请求)
    #       🞉 User-Agent (浏览器名称)
    #       🞉 Accept (传输文件类型)
    #       🞉 Referer (页面跳转处)
    #       🞉 Accept-Encoding (文件编解码格式)
    #       🞉 Accept-Language (语言种类)
    #       🞉 Content-Type (POST数据类型)
    #       🞉 Cookie (Cookie)
    #       🞉 x-requested-with:XMLHttpRequest (表示该请求是Ajax异步请求)

    # 4.HTTP响应信息：
    #   4.1.响应报文：
    #       响应报文也由四个部分组成，分别是：状态行、消息报头、空行、响应正文
    #           状态行：  | 版本 | 空格 | 状态码 | 空格 | 短语 | 回车换行符 |
    #           首部行  { | 首部字段名 | : | 值 | 回车换行符 |
    #                   { |               ...               |
    #                   { | 首部字段名 | : | 值 | 回车换行符 |
    #           实体主体：|      ... (有些响应报文不用)      |
    #   4.2.状态码范围：
    #       🞉 100~199：表示服务器成功接收部分请求，要求客户端继续提交其余请求才能完成整个处理过程
    #       🞉 200~299：表示服务器成功接收请求并已完成整个处理过程。常用200(OK请求成功)
    #       🞉 300~399：为完成请求，客户需进一步细化请求。例如：请求的资源已经移动一个新地址、
    #                   常用302(所请求的页面已经临时转移至新的URL)、307和304(使用缓存资源)
    #       🞉 400~499：客户端的请求有错误，常用404(服务器无法找到被请求的页面)、403(服务器拒绝访问，权限不够)
    #       🞉 500~599：服务器端出现错误，常用500(请求未完成。服务器遇到不可预知的情况)
    #   4.3.HTTP响应状态码参考：
    #       🞉 200：成功
    #       🞉 302：临时转移至新的URL
    #       🞉 307：临时转移至新的URL
    #       🞉 404：找不到该页面
    #       🞉 500：服务器内部错误
    #       🞉 503：服务不可用，一般是被反爬
    #   4.4.Cookie信息：
    #       🞉 Set-Cookie (对方服务器设置cookie到用户浏览器的缓存)
    #       服务器和客户端的交互仅限于请求/响应过程，结束之后便断开，在下一次请求时，服务器会认为新的客户端。
    #       为了维护他们之间的链接，让服务器知道这是前一个用户发送的请求，必须在一个地方保存客户端的信息
    #       Cookie：通过在客户端记录的信息确定用户的身份。
    #       Session：通过在服务器端记录的信息确定用户的身份。
    print("× 本章无控制台输出案例")

    print()
# --------------------------------------------------------------------------------
# 三、requests入门
def requests():
    print("三、requests入门========================================")
    # 0.requests模块介绍：
    #   作用：发送HTTP网络请求，返回响应数据
    #   中文文档：https://requests.readthedocs.io/projects/cn/zh-cn/latest/
    #   通过观察文档来学习：如何使用requests来发送网络请求

    # 1.发送get请求：requests.get()
    # 2.响应数据的获取：
    #   🞉 response.text
    #     · 类型：str
    #     · 解码类型：requests模块自动根据HTTP头部对响应的编码作出有根据的推测，推测的文本编码
    #     · 如何修改编码方式：response.encoding="gbk"
    #   🞉 response.content
    #     · 类型：bytes
    #     · 解码类型：无指定
    #     · 如何修改编码方式：response.content.decode("utf8")
    #   🞉 获取网页源码的通用方式：
    #     · response.content.decode()
    #     · response.content.decode("GBK")
    #     · response.text
    #    以上三种方法从前往后尝试，能够100%的解决所有网页解码的问题
    #    所以，更推荐使用response.content.decode()的方式获取响应的html页面

    # 3.字符集编码：
    #   3.1.字符、字符集：
    #       字符(Character)是各种文字和符号的总称，包括各国家文字、标点符号、图形符号、数字等
    #       字符集(Characterset)是多个字符的集合
    #       字符集包括：ASCII字符集、GB2312字符集、GB18030字符集、Unicode字符集等
    #       ASCll编码是1个字节，而Unicode编码通常是2个字节。
    #       UTF-8是Unicode的实现方式之一，UTF-8是它是一种变长的编码方式，可以是1，2，3个字节
    #   3.2.Pyhton3 中的字符串：
    #       Pyhton3 中两种字符串类型：
    #       🞉 str：unicode的呈现形式
    #       🞉 bytes：字节类型，互联网上数据的都是以二进制的方式(字节类型)传输的
    #   3.3.str和bytes类型的互相转换：
    #       🞉 str.encode() 🡪 bytes
    #       🞉 bytes.decode(字符集[默认utf8]) 🡪 str
    #      注意：编码方式解码方式必须一样，否则就会出现乱码

    # 4.response的其他属性
    #   🞉 response.status_code        响应状态码
    #   🞉 response.request.headers    响应对应的请求头
    #   🞉 response.headers            响应头
    #   🞉 response.request.cookies    响应对应请求的cookie
    #   🞉 response.cookies            响应的cookie(经过了set-cookie动作)

    # 5.基础反爬虫手段应对措施：
    #   🞉 检测请求头中的 User-Agent 是否是一个正常浏览器的 User-Agent
    #       解决方案：在请求时自己设置请求头中的 User-Agent

    # 6.Xpath：
    #   🞉 介绍：即XML路径语言，是一种用来确定XML文档中某部分位置的语言
    #   🞉 常用表达式：XPath使用路径表达式来选取XML文档中的节点或者节点集，
    #                 这些路径表达式和我们在常规的电脑文件系统中看到的表达式非常相似。以下是常用的路径表达式
    #       ----------------------------------------
    #        表达式       描述
    #       nodename    选取此节点的所有子节点
    #       /           从根节点选取
    #       //          从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置
    #       .           选取当前节点
    #       ..          选取当前节点的父节点
    #       @           选取属性
    #       ----------------------------------------
    #        示例        意义
    #       div        选取div元素的所有子节点
    #       /div       选取根元素div  ※注意：假如路径起始于正斜杠(/)，则此路径始终代表到某元素的绝对路径！
    #       div/a      选取属于div的子元素的所有a元素
    #       //div      选取所有div子元素
    #       div//p     选择属于div元素的后代的所有div元素，而不管它们位于p之下的什么位置
    #       //@lang    选取名为lang的所有属性
    #   🞉 谓语(条件过滤)
    #        示例
    #       /ul/li[1]               选取属于 ul 子元素的第一个 li 元素
    #       /ul/li[last()]          选取属于 ul 子元素的最后一个 li 元素
    #       /ul/li[last()-1]        选取属于 ul 子元素的倒数第二个 li 元素
    #       /ul/li[position()<3]    选取最前面的两个属于 ul 元素的子元素的 li 元素
    #       //div[@attr]            选取所有拥有名为 attr 的属性的 div 元素
    #       //div[@attr='leng]      选取所有 div 元素，且这些元素拥有值为 leng 的 attr 属性

    # 例：
    # get_baidu_page()      # 例1：获取百度首页数据
    # get_baidu_picture()   # 例2：获取百度图片数据
    get_music()           # 例3：获取音频
    get_douban_ranking()  # 例4：获取豆瓣电影排行榜数据(详见"知识点6")
# ----------------------------------------
def get_baidu_page():
    import requests
    url_1 = "https://www.baidu.com"
    # 向目标URL发送get请求
    response = requests.get(url=url_1)
    # 打印响应内容
    print(response.text)  # 获取字符串(可能出现乱码，因为有二进制数据)
    print("--------------------")
    print(response.content)  # 【推荐】获取原始的二进制数据(byte类型的数据)
    print("--------------------")
    print(response.request.headers) # 请求头中的 User-Agent 显然是一个爬虫的 User-Agent
    print("====================")
    # 请求头是字典格式
    headers_1 = {
        "user-agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0"
    }
    response = requests.get(url = url_1, headers = headers_1)
    print(response.content.decode())
    print("--------------------")
    print(response.request.headers)
    with open("百度首页.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    print()
# ----------------------------------------
def get_baidu_picture():
    import requests
    url_2 = "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"
    headers_2 = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0"
    }
    response = requests.get(url=url_2, headers=headers_2)
    with open ("百度logo.png", "wb") as f:
        f.write(response.content)
    print("图片已成功获取")

    print()
# ----------------------------------------
def get_music():
    import requests
    url_3 = "https://m804.music.126.net/20260424230147/58adf40ce54e5a3e13bb3b8dfe6b113a/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/79292552159/7e21/9ffe/5cd1/7852d5fe01bea22f6fb170be2c1b4108.m4a?vuutv=voZ5wKyHBRAUxwl2WNC+y8eJVS9ruF8vg8/InlvF81jZfCi8VOOdEOvaXWLjeeDJiv59RPmWI6L6f8GaHsoTmWuham2VSsG7MSMstIYixeM=&authSecret=0000019dbfebfd5a08810a32b0a90006&cdntag=bWFyaz1vc193ZWIscXVhbGl0eV9leGhpZ2g"
    headers_3 = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0"
    }
    response = requests.get(url=url_3, headers=headers_3)
    with open ("灰烬之国音乐.m4a", "wb") as f:
        f.write(response.content)
    print("音乐已成功获取")

    print()
# ----------------------------------------
def get_douban_ranking():
    import requests
    url_4 = "https://movie.douban.com/top250"
    headers_4 = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0"
    }
    response = requests.get(url=url_4, headers=headers_4)


# --------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
