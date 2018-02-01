---
title: Linux 下安装 TeXLive 2017
date: 2013-07-11
lastmod: 2017-06-14
author: SeisMan
categories:
  - 编程
tags:
  - 安装
  - LaTeX
slug: install-texlive-under-linux
---

本文将介绍如何在 Linux 下安装 TeXLive 2017。

<!--more-->

## 依赖包

- 安装过程中需要调用 Perl 的模块 `Digest::MD5` 来检测 ISO 文件的完整性；
- 升级过程中界面需要调用 Perl 的模块 `Tk` ；

CentOS:

    $ sudo yum install perl-Digest-MD5 perl-Tk

Ubuntu:

    $ sudo apt-get install libdigest-perl-md5-perl perl-tk

## 安装

### 下载

下载地址：

- 官方镜像: [texlive2017.iso](http://mirrors.ctan.org/systems/texlive/Images/texlive2017.iso)
- USTC 镜像: [texlive2017.iso](http://mirrors.ustc.edu.cn/CTAN/systems/texlive/Images/texlive2017.iso)

Linux 下可以用 wget、axel，windows 下可以用迅雷，怎么快怎么来。

### 挂载 ISO 镜像

``` bash
$ su
# mount -o loop texlive2017.iso  /mnt/
# cd /mnt
# ./install-tl
```

出现选项后，输入 `I` 直接安装（也可以更改选项）。不出意外的话，5 分钟应该就 OK 了，
然后退出 root 用户。

### 环境变量

在当前用户的 `~/.bashrc` 中加入如下语句：

``` bash
# TeX Live 2017
export MANPATH=${MANPATH}:/usr/local/texlive/2017/texmf-dist/doc/man
export INFOPATH=${INFOPATH}:/usr/local/texlive/2017/texmf-dist/doc/info
export PATH=${PATH}:/usr/local/texlive/2017/bin/x86_64-linux
```

### 卸载 ISO 镜像

``` bash
$ cd
$ sudo umount /mnt/
```

## 更新 TeXLive

可以使用如下命令更新 TeXLive 宏包：

``` bash
$ su
# 更新 TeXLive 包管理器 tlmgr
# tlmgr update --self
# 更新 TeXLive 的全部包
# tlmgr update --all
```

默认情况下，会自动搜索合适的镜像来更新，也可以使用 `--repository` 选项指定了要使用
哪一个 CTAN 镜像。

比如 USTC 镜像:

    # tlmgr update --self --repository http://mirrors.ustc.edu.cn/CTAN/systems/texlive/tlnet/
    # tlmgr update --all --repository http://mirrors.ustc.edu.cn/CTAN/systems/texlive/tlnet/

比如阿里云镜像:

    # tlmgr update --self --repository http://mirrors.aliyun.com/CTAN/systems/texlive/tlnet/
    # tlmgr update --all --repository http://mirrors.aliyun.com/CTAN/systems/texlive/tlnet/

如果希望在图形界面下升级，可以使用如下命令调出 tlmgr 的中文图形界面：

``` bash
$ su
# tlmgr --gui --gui-lang zh_CN
```

## 安装额外的字体

TeXLive 2017 在使用 xeLaTeX 处理中文时，有自己的默认字体。大多数 Linux 发行版下，
都使用自带的 Fandol 字体。

如果想要使用 Windows 字体，可以将字体文件复制到 `~/.fonts` 目录下，并在 tex 源码中
指定字体选项即可。

## 修订历史

- 2013-07-11：初稿；
- 2014-07-06：修改为 TeXLive2014，并删除中文字体部分；
- 2015-03-08：新增 “安装依赖”；
- 2015-03-15：使用命令行更新包；
- 2015-03-20：指定更新源以及 GUI 更新；
- 2015-06-13：更新至 TeXLive 2015；
- 2016-06-07：更新至 TeXLive 2016；
- 2017-06-14：更新至 TeXLive 2017；
