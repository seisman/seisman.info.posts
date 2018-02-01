---
title: GMT 4 在 Mac 下的安装
date: 2015-09-05
author: SeisMan
categories:
  - GMT
tags:
  - 安装
slug: install-gmt4-under-mac
---

GMT 官方没有为 Mac 提供 GMT4 的安装包，因而只能通过其他方式安装。Mac 下有很多第三方软件管理工具，比如 MacPorts 和 Homebrew。MacPorts 和 Homebrew 中自带最新版本的 GMT，可以直接安装，是比较推荐的使用方式。某些情况下可能会希望自己手动编译，比如自己修改了 GMT 源码。

因而，本文会介绍四种安装 GMT4 的方法，列举如下

1.  用 Homebrew 安装 GMT4
2.  用 MacPorts 安装 GMT4
3.  基于 Homebrew 安装 GMT4
4.  基于 MacPorts 安装 GMT4

<!--more-->

## 安装命令行开发工具

在开始之前，先要安装 Mac 下的命令行开发工具。因为全新的 Mac 默认是没有自带的:

    $ xcode-select --install

## 使用 Homebrew 安装

1.  到 [Homebrew](http://brew.sh/) 首页，复制首页上的安装代码到终端，执行即可安装 Homebrew。
2.  使用 Homebrew 安装 GMT4:

        $ brew install homebrew/science/gmt4

## 使用 MacPorts 安装

1.  到 [MacPorts](https://www.macports.org/install.php) 网站，下载当前系统对应的 pkg 文件并安装
2.  使用 MacPorts 安装 GMT4:

        $ sudo port install gmt4

## 手动编译 GMT

手动编译 GMT 需要如下几步：

1.  下载
2.  解决依赖关系
3.  编译 GMT 源码
4.  安装海岸线数据
5.  修改环境变量

具体操作参考 [Linux 下安装 GMT4](/install-gmt4-under-linux/) 一文，Linux 与 Mac 唯一的不同仅仅是 “解决依赖关系” 这一步。

### 解决依赖关系

GMT4 依赖于 netCDF，必须安装；不依赖于 gdal，但 gdal 在转换数据格式时经常用到，推荐安装。

可以用 Homebrew 安装依赖包:

    $ brew install gdal
    $ brew install homebrew/science/netcdf

也可以用 MacPorts 安装依赖包:

    $ sudo port install netcdf +gdal +curl +geos +hdf5
