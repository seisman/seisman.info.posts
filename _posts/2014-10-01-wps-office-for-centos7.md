---
title: CentOS 7 下安装 WPS Office
date: 2014-10-01
updated: 2014-11-03
author: SeisMan
categories: Linux
tags: CentOS
---

在 Microsoft Office 盛行的今日，Linux 下一直没有一个能与之完美兼容的 Office 套件。
大多数发行版默认安装的 OpenOffice 或 LibreOffice，也只是刚刚达到能用的地步，
界面以及功能的差异还是很明显的。

或许 WPS Office for Linux 是个不错的选择。

-   中文官网： <http://linux.wps.cn/>
-   英文官网： <http://www.wps.com/linux/>

<!--more-->

目前 WPS Office for Linux 尚处在测试阶段。根据惯例，alpha 版为内测版本，beta
版为公测版本。这里选择 Alpha 16。

-   安装包：[wps-office-9.1.0.4909-1.a16p1.i686.rpm](http://kdl.cc.ksosoft.com/wps-community/download/a16/wps-office-9.1.0.4909-1.a16p1.i686.rpm)
-   字体包：[wps-office-fonts-1.0-1.noarch.rpm](http://kdl.cc.ksosoft.com/wps-community/download/a15/wps-office-fonts-1.0-1.noarch.rpm)

WPS Office 提供的 rpm 包为 32 位版本，对于 64 位系统需要安装相应的 32 位依赖包方可使用，幸好
`yum` 可以自动判断并解决包的依赖关系，所以安装很简单。

首先 `cd` 到下载的 RPM 包所在的文件夹下，然后执行如下 `yum` 命令。注意，这里用的
是 `yum` 而不是 `rpm -i` ，因为 `rpm` 似乎无法自动解决 32 位库的依赖问题。

``` bash
$ sudo yum install wps-office-9.1.0.4909-1.a16p1.i686.rpm
$ sudo yum install wps-office-fonts-1.0-1.noarch.rpm
```

安装完成后，即可在 “Application” 中找到相关项。

## 参考

1.  [WPS 下载地址](http://community.wps.cn/download/)
2.  [WPS 社区 Wiki](http://community.wps.cn/wiki/%E9%A6%96%E9%A1%B5)
3.  [原生对话框问题](http://bbs.wps.cn/thread-22371203-1-1.html)
4.  [部分数学公式显示支持](http://community.wps.cn/wiki/%E9%83%A8%E5%88%86%E6%95%B0%E5%AD%A6%E5%85%AC%E5%BC%8F%E6%98%BE%E7%A4%BA%E6%94%AF%E6%8C%81)

## 修订历史

-   2014-10-01：初稿；
-   2014-10-23：更新至 Alpha16；此版本中不再有 `mui` 语言包；
-   2014-11-03：更新至 Alpha16 Patch1；

