---
title: TauP 的安装
date: 2014-10-08
author: SeisMan
categories:
  - 地震学软件
tags:
  - Java
  - 走时
slug: taup-install
---

TauP 是用 Java 写的一个用来计算震相走时的软件。

官方主页: <http://www.seis.sc.edu/taup/index.html>

<!--more-->

1.  确认 Java 运行环境已安装

    在终端中键入 `java -version`，若显示版本信息，则表示 Java 运行环境已安装:

        $ java -version
        openjdk version "1.8.0_161"
        OpenJDK Runtime Environment (build 1.8.0_161-b14)
        OpenJDK 64-Bit Server VM (build 25.161-b14, mixed mode)

    否则则需要先安装 Java 运行环境，在 CentOS 7 下用如下命令:

        $ sudo yum install java

    在 Ubuntu 上:

        $ sudo apt update
        $ sudo apt install default-jre
        $ sudo apt install default-jdk
        $ sudo apt upgrade

    在 macOS 下使用如下命令:

        $ brew cask install java

    TauP最新版本为2.4.5，该版本要求Java版本大于1.8。若你的机器的Java版本小于1.8，
    可以考虑下载使用旧版本的TauP。但要注意，旧版本TauP可能存在已知的BUG。

2.  下载 TauP:

        wget http://www.seis.sc.edu/downloads/TauP/TauP-2.4.5.tgz

3.  解压:

        tar -xvf TauP-2.4.5.tgz

4.  安装:

        sudo mv TauP-2.4.5 /opt

5.  修改环境变量:

        echo 'export TAUPHOME=/opt/TauP-2.4.5' >> ~/.bashrc
        echo 'export PATH=${TAUPHOME}/bin:${PATH}' >> ~/.bashrc
        source ~/.bashrc

6.  执行测试

    终端键入 `taup` 若出现 TauP 图形界面则表示安装成功。
