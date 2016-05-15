---
title: Hinet/Fnet 台站选择工具
date: 2016-03-08
author: SeisMan
categories: 地震学基础
tags: [Hinet, Python]
---

Hinet 大概有不到 800 个台站，Fnet 大概有 150 个左右的台站。在从 Hinet 网站上下载
数据时，默认是会下载所有台站的波形数据的。若只需要申请其中部分台站的数据，
则需要使用 Hinet 网站自带的台站选择工具。

Hinet 网站自带的台站工具有如下优缺点：

1.  图形界面，直观得显示了每个台站的位置
2.  无法通过某些条件进行筛选，一次只能选中或删除一个台站
3.  似乎需要一个 Java 的浏览器工具才能使用

因此，写了一个可以用于选择台站的 Python 工具，即 `StationSelector.py`，其是
[HinetScripts](https://github.com/seisman/HinetScripts) 项目下中的一个脚本。

其用法如下:

    $ python StationSelector.py -h
    Select Hi-net/F-net stations to request waveform data from NIED

    Usage:
        StationSelector.py -c CODE [-l LIST]
        StationSelector.py -h

    Options:
        -h, --help              Show this help.
        -c CODE, --code=CODE    Network code. Hi-net: 0101, F-net: 0103.
        -l LIST, --list=LIST    Station list file.

说明：

1.  `-c CODE` 选项用于指定是选择 Hinet 台网下的台站还是 Fnet 台网下的台站
2.  若不使用 `-l` 选项，则会选择全部台站
3.  `-l LIST` 指定了一个列表文件，文件中包含了台站列表，每行一个台站名，以 `#`
    开头的行会被忽略
4.  台站名的格式为 `X.XXXX` 而不是 `X.XXXX.X`，即只能指定台站名，无法精确到分量名
5.  该脚本并不检查台站名是否属于该台网

示例如下，假如台站列表文件 `sta.list` 中包含如下几行:

    N.FJ2H
    N.OTWH
    # N.IICH
    N.SMGH

则:

    python StationSelector.py -c 0101 -l sta.list

会选中 Hinet 的三个台站， `N.IICH` 不会被选中。

该脚本功能并不强大，因而建议的用法是：

1.  用 `HinetContRequest.py` 申请全部台站的几分钟的数据
2.  用 `rdhinet.py` 解压所有台站的数据，得到 SAC 格式的数据
3.  用 `saclst stlo stla f *.U` 获取台站的经纬度信息
4.  用 `awk` 或写脚本筛选出自己需要的台站列表
5.  调用 `StationSelector.py` 选择台站
