---
title: 安装 SOD
date: 2015-11-05
author: SeisMan
category: 地震学软件
tags: [安装, 数据申请, 软件, Java]
---

主页： <http://www.seis.sc.edu/sod/index.html>

SOD 是一个 Java 写的命令行程序，用于下载地震相关数据。

<!--more-->

``` bash
$ wget http://www.seis.sc.edu/downloads/sod/3.2.6/sod-3.2.6.tgz
$ tar -xvf sod-3.2.6.tgz
$ sudo mv sod-3.2.6 /usr/local
$ echo 'export PATH=${PATH}:/usr/local/sod-3.2.6/bin'>> ~/.bashrc
$ exec $SHELL -l
```
