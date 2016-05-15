---
title: TauP 的安装
date: 2014-10-08
author: SeisMan
categories: 地震学软件
tags: [Java, 走时]
---

TauP 是用 Java 写的一个用来计算震相走时的软件。

官方主页: <http://www.seis.sc.edu/taup/index.html>

1.  确认 Java 运行环境已安装

    在终端中键入 `java -version`，若显示版本信息，则表示 Java 运行环境已安装:

        $ java -version
        java version "1.7.0_65"
        OpenJDK Runtime Environment (rhel-2.5.1.2.el7_0-x86_64 u65-b17)
        OpenJDK 64-Bit Server VM (build 24.65-b04, mixed mode)

    否则则需要先安装 Java 运行环境，在 CentOS 7 下用如下命令:

        $ sudo yum install java

2.  下载 TauP:

        wget http://www.seis.sc.edu/downloads/TauP/TauP-2.1.2.tgz

3.  解压:

        tar -xvf TauP-2.1.2.tgz

4.  安装:

        sudo mv TauP-2.1.2 /opt

5.  修改环境变量:

        echo 'export TAUPHOME=/opt/TauP-2.1.2' >> ~/.bashrc
        echo 'export PATH=${TAUPHOME}/bin:${PATH}' >> ~/.bashrc
        source ~/.bashrc

6.  执行测试

    终端键入 `taup` 若出现 TauP 图形界面则表示安装成功。


