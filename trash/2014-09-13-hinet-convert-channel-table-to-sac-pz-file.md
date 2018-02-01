---
title: Hi-net 生成仪器响应 SAC PZ 文件
author: SeisMan
date: 2014-09-13
categories:
  - 地震学基础
tags:
  - Hinet
  - 仪器响应
  - Python
slug: hinet-convert-channel-table-to-sac-pz-file
---

前文 [Hinet 仪器响应](/hinet-instrumental-response.html) 中介绍了 Hi-net 的
仪器响应的详细信息。据此，用 Python 写了一个脚本，将 Hi-net 的 Channel Table
文件转换为常用的 SAC PZ 文件。

脚本位于：[ch2pz.py](https://github.com/seisman/HinetScripts/blob/master/ch2pz.py)。

<!--more-->

需要特别说明的是：该脚本适用于 Hinet，不适用于 Fnet，不确定是否适用于其他台网。

## 用法

    Convert Hi-net Channel Table file to SAC PZ files

    Usage:
        ch2pz.py DIRNAME [-C <comps>] [-D <outdir>] [-S <suffix>]

    Options:
        -C <comps>      Channel Components to convert. Choose from U,N,E,X,Y.
                        Default to convert all components.
        -D <outdir>     Output directory of SAC PZ files. Use the directory of
                        Channel Table file as default.
        -S <suffix>     Suffix for SAC PZ files. [default: SAC_PZ]

其中， `DIRNAME` 是目录名，其中包含了一个 Channel Table 文件。Channel Table 文件的文件名格式为 `XX_YYYYMMDD.ch`。

## 说明

参考 [Hi-net WIN32 转 SAC](/hinet-convert-win32-files-to-sac.html) 一文中对选项的解释。
