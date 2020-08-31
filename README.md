# 制作动机

在学校要使用PPPOE，宽带拨号，每次开机都需要自己拨号，很麻烦，于是写此脚本实现自动拨号。

# 使用说明

## 配置信息

在u_a_p.txt文本文件中写入自己的宽带连接名称（宽带连接）、号码（usename）和密码（password），如：

```
宽带连接
1560000211
1200321
```

三行信息一定要分行写，不能写成一行。

这些信息是运营商提供给您的，您也可以进入设置-拨号页面查看您已经建立的宽带连接。

## 自动运行

完成上述配置之后，利用Windows任务计划程序实现开机自动运行。

如果您没有Python解释器，您也可以使用exe文件。