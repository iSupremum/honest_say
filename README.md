## 功能描述

* 显示QQ“坦白说”发送方的QQ号。

## 开发环境

* 操作系统： Windows
* 编程语言： python3.6（安装好pip模块）


## 依赖项

* `selenium` 模块。安装方式：
```Bash
  pip install selenium
```
* `PhantomJS`。下载方式：
    	[PhantomJS下载地址](http://phantomjs.org/download.html)  
	**注意**：解压后将解压的bin目录的路径配置到环境变量中。  
	测试是否安装成功,在控制台输入：
```Bash
  phantomjs -v
```
	  成功返回版本号即表示安装成功。

## 执行方法
* Step1：打开“QQ_information.txt”文件，修改第一行为你的QQ号，第二行为你的QQ密码。（不要有多余的字符）
* Step2：执行`“main.py”`文件即可。

## 结果说明
* 结果显示在result分割线下。
* 每一个topic_name指的是坦白说里对方发起的第一句话（给出的标签）
* nick_name是对方在坦白说下的昵称
* qq_number是对方的QQ号
* 2018.5.4 测试可行。
 <div align=center>![](https://github.com/iSupremum/honest_say/raw/master/result_image/result.png)</div>
