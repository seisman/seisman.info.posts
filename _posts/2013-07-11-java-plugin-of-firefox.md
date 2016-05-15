---
title: Firefox 安装 Java 插件
date: 2013-07-11
author: SeisMan
categories: Linux
tags: [Firefox, Java]
---

由于某个变态网站，需要 Java 插件才能使用，所以需要在 Firefox 上安装 Java 插件。在
Oracle 的网站上搜到解决办法，原文在 [这里](http://www.oracle.com/technetwork/java/javase/manual-plugin-install-linux-136395.html)，
排版难看的要死，故而重新排版。

我的计算机环境如下：

-   操作系统：CentOS 6.4 Final
-   Firefox 版本：17.0.7
-   Java 版本：OpenJDK 1.7.0

安装步骤如下：

1.  退出 Firefox；
2.  卸载原来安装的 Java 插件（没装过就不卸了）；
3.  找到 Java 自带的浏览器插件的位置；

        $ locate libnpjp2
        /usr/java/jre1.7.0_21/lib/amd64/libnpjp2.so
        /usr/local/cuda-5.0/jre/lib/amd64/libnpjp2.so

4.  在 firefox 插件目录中建立到 Java 插件文件的软链接；

        $ cd ~/.mozilla/plugins/
        $ ln -s /usr/java/jre1.7.0_21/lib/amd64/libnpjp2.so libnpjp2.so

5.  启动 firefox，在地址栏输入 `about:plugins`，查看插件是否正常加载；
6.  搞定收工。
