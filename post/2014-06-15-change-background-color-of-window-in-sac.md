---
title: SAC 修改绘图窗口的背景色
author: SeisMan
date: 2014-06-15
categories:
  - SAC
tags:
  - SAC技巧
  - 图像
slug: change-background-color-of-window-in-sac
---

SAC 在绘图时默认使用白色作为背景色、用黑色绘制波形数据。这样的配色对比很明显，看起来也很清晰。

但是在需要长期查看波形、拾取震相时，黑底白线这种强烈的颜色对比，对眼睛很不友好，经常看着看着就花了。

SAC 的 color 命令可以修改绘图窗口的背景色。SAC 目前只支持几种简单的颜色：red、green、blue、yellow、cyan、magenta、black、white。其中 cyan 作为背景色是不错的选择。

因而，在绘图之前，使用 color 命令将窗口背景色修改为 cyan:

    color black background cyan

每次绘图之前都执行这个命令显然比较麻烦，可以设置让 SAC 在启动时自带执行该命令。

在 `~/.bashrc` 中加入如下 `alias` 语句:

    alias sac="${SACHOME}/bin/sac ${SACAUX}/init.m"

并在 `${SACAUX}` 目录下（一般是 `/usr/local/sac/aux` ）新建文件 `init.m`，其内容为:

    color black background cyan

即可。
