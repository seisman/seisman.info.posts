---
title: GMT 5.1.2 在 Windows 下的安装
date: 2015-04-18
updated: 2015-06-02
author: SeisMan
categories: GMT
tags: [GMT, Windows, 安装]
---

本文介绍如何在 Windows 7 下安装 GMT5.1.2。

<!--more-->

## 下载

Windows 下安装 GMT5.1.2 需要下载三个文件：

1.  [GMT 64 位安装包](http://mirrors.ustc.edu.cn/gmt/bin/gmt-5.1.2-win64.exe)
    或 [GMT 32 位安装包](http://mirrors.ustc.edu.cn/gmt/bin/gmt-5.1.2-win32.exe)
2.  [ghostscript 64 位安装包](https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs919/gs919w64.exe) 或
    [ghostscript 32 位安装包](https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs919/gs919w32.exe)
3.  [GSView 64 位安装包](http://pages.cs.wisc.edu/~ghost/gsview/download/gsv50w64.exe)
    或 [GSView 32 位安装包](http://pages.cs.wisc.edu/~ghost/gsview/download/gsv50w32.exe)

## 安装

### 安装 GMT

跟大多数 Windows 的程序一样，双击 exe 就好。几个需要注意的地方如下图：

GMT5 安装文件会自动添加环境变量，如下图所示，三个可选项中选第一个或第二个就好。不要选第三个，除非你知道自己在做什么。

![](/images/2015041801.png)

GMT5 默认的安装目录是 `c:\programs\gmt5`，使用此默认值就好，不建议修改此安装目录。

尝试安装在 `c:\Program Files\gmt5` 下，执行命令好像也没问题，但不确定目录名中的空格是否会在什么地方挖个坑。

![](/images/2015041802.png)

选择组件那里，Runtimefiles 是必须的，DCW 是国界、省界数据，Documentation 是官方文件以及官方示例，GSHHG 是海岸线数据。所以四个都安装就好。

![](/images/2015041803.png)

安装完成之后，启动 cmd：“开始”-\>“所有程序”-\>“附件”-\>“命令提示符”，也可以直接在开始那里搜索 “cmd”。在 cmd 窗口中键入 `gmt`，效果如下则表明 GMT 安装成功。

![](/images/2015041804.png)

### 安装 ghostscript

ghostscrip 的安装没什么好说的，在安装的最后，第一个复选框一定要选上，这关系到 GMT 能否支持中文的问题。

![](/images/2015041805.png)

### 安装 GSView

GSView 的安装没什么好说的，一直点下去用默认的选项就好。

## 测试

GMT 自带了一些例子，可以把 `C:\programs\gmt5\share\doc\examples` 目录下的例子复制一份到自己的目录下。每个例子里包含了 bat 脚本，以及执行脚本所需的数据文件。

双击即可直接执行 bat 脚本，右键编辑即可查看 bat 脚本的内容。

双击生成的 PS 文件即可用 GSView 打开。

## 其他

安装完成后，你可以对如下几篇博文感兴趣：

1.  [GMT4 脚本风格指南](/gmt4-style-guide.html)：虽然是针对 GMT4 的，但是对 GMT5 也有一定的指导意义
2.  [Windows 下使用 GMT 的正确姿势](how-to-use-gmt-under-windows.html)：教你如何在 Windows 下更愉快地使用 GMT
3.  [GMT 在 Windows 下的中文支持](/gmt-chinese-support-under-windows.html)：如何在 GMT 中添加中文

## 修订历史

-   2015-04-18：初稿；
-   2015-06-02：更新至 5.1.2；

