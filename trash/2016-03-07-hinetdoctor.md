---
title: Hinet 配置检查脚本
date: 2016-03-07
author: SeisMan
categories:
  - 地震学基础
tags:
  - Hinet
  - Python
slug: hinetdoctor
---

`HinetDoctor.py` 是 [HinetScripts](https://github.com/seisman/HinetScripts)
项目中的一个 Python 脚本。

该脚本主要有如下功能：

1.  检查 Python 版本是否大于 3.3
2.  检查是否已安装所有依赖
3.  检查配置文件是否可正常读取
4.  检查账号密码是否正确，或是否可以正常登陆
5.  检查 Hinet 网站是否有更新，若网站有更新，而脚本未更新，则脚本可能失效
6.  检查 win32tools 中的 `catwin32` 和 `win2sac_32` 是否可以被正常调用
7.  检查已选中的 Hinet 和 Fnet 的台站数目
8.  检查配置文件中 `MaxSpan` 是否符合要求

