---
title: Hinet 连续波形数据申请及下载的脚本实现
date: 2014-08-30
updated: 2015-01-17
author: SeisMan
categories: 地震学基础
tags: [Hinet, 数据, 申请, Python]
---

前文已经说到，Hi-net 连续波形数据申请的本质可以简化为如下几步：

1.  指定参数，构建 query string
2.  向 Hi-net 发送数据请求
3.  等待数据准备
4.  下载数据

## HinetContRequest.py

`HinetContRequest.py` 是 [HinetScripts](https://github.com/seisman/HinetScripts/)
中的一个 Python 脚本，其可以用于申请与下载 Hi-net 连续波形数据。

## 设计思路

整个脚本的设计思路如下：

1.  从配置文件中读取配置信息，比如用户名和密码
2.  从命令行参数中读入要申请的连续波形数据的起始时间和时间跨度等信息
3.  确定要申请的台网的代码，并检测台网在该时间段内是否有可用数据
4.  若要申请的数据的时间跨度超过了 Hi-net 网站单次申请的限制，则将整个时间跨度分成多个符合要求的子申请。比如要申请 Hi-net 全部台站的 60 分钟的数据，根据 Hi-net 网站对数据申请的限制可知，这种情况下单次申请的数据时间跨度不能超过 5 分钟，因而需要将 60 分钟的数据申请拆分成 12 个 5 分钟的子申请。
5.  通过循环依次执行每一个子申请。每个子申请中的步骤如下：
    1.  构建 query string
    2.  发送申请
    3.  每隔一定时间检查此次申请的状态。
        -   若还在准备数据，则等待然后再检查
        -   若数据已准备好，则进行下一次申请
        -   若出现错误，则退出
        -   偶尔会出现很长时间都没有动静的情况，原因不明，怀疑是 Hi-net 服务器的问题。解决办法是重新提交一次相同的申请

6.  待所有子申请完成后，并行下载全部数据
7.  解压全部 ZIP 文件，并调用 `catwin32` 将一分钟一分钟的 cnt 文件合并成一个多分钟的 cnt 文件
8.  对 cnt 和 ch 文件重命名
9.  清理不必要的文件

## 配置文件

要执行 HinetContRequest.py，需要先修改配置文件 [Hinet.cfg](https://github.com/seisman/HinetScripts/blob/master/Hinet.cfg)，其内容如下:

    [URL]
    # DO NOT MODIFY URLs
    AUTH = https://hinetwww11.bosai.go.jp/auth
    CONT = %(AUTH)s/download/cont
    STATUS = %(CONT)s/cont_status.php
    SELECT = %(CONT)s/select_confirm.php
    STATION = %(CONT)s/select_info.php
    REQUEST = %(CONT)s/cont_request.php
    DOWNLOAD = %(CONT)s/cont_download.php

    [Account]
    User = xxxxxxx
    Password = xxxxxxxxxxx

    [Cont]
    Net = 0101
    # Max time span for each sub-requests
    # MaxSpan <= 12000 / Number_of_Channel
    MaxSpan = 5

    [Request]
    # waiting time for data preparation <= MaxSleepCount*SleepTime seconds
    MaxSleepCount = 100
    SleepTime = 2.0

其中：

-   `[URL]` 中定义了一些网址，是脚本所需要使用的全局变量，不需要做任何修改
-   `User` 和 `Password` 为 Hi-net 网站的用户名和密码
-   由于不同台网的数据不能一起申请，因而需要指定要申请的台网的台网代码；`Net` 为默认的台站代码；比如 `0101` 即代表 Hi-net 台网
-   在将一个数据时间跨度很长的申请分割成多个子申请时，每个子申请的数据时间跨度由 `MaxSpan` 决定。可以通过运行 `HinetDoctor.py` 来检查该值是否满足要求。
-   每次申请后，需要等待服务器准备数据，在这段时间内是无法再次申请数据的。因而脚本中通过不断查询数据状态来判断是否此次申请是否已完成。`SleepTime` 控制了隔多长时间查询一次数据的状态， `MaxSleepCount` 控制了最多查询多少次。若超过最大查询次数后数据依然没有准备好，则认为此次申请无效，重新发起相同的申请

## 用法

    $ python HinetContRequest.py -h
    Request continuous waveform data from NIED Hi-net.

    Usage:
        HinetContRequest.py <year> <month> <day> <hour> <min> <span> [options]
        HinetContRequest.py -h

    Options:
        -h, --help              Show this help.
        -c CODE --code=CODE     Select code for organization and network.
        -m SPAN --maxspan=SPAN  Max time span for sub-requests
        -d DIR --directory=DIR  Output directory. Default: current directory.
        -o FILE --output=FILE   Output filename.
                                Default: CODE_YYYYMMDDHHMM_SPAN.cnt
        -t FILE --ctable=FILE   Channel table filename. Default: CODE_YYYYMMDD.ch

该脚本的参数及选项比较简单：

-   year、month、day、hour、min 为要申请的连续波形的起始时间；
-   span 为要申请的连续波形的持续时间；
-   `-c` 用于指定台网代码，该值会覆盖配置文件中 `Net` 变量的值
-   `-m` 用于指定单次申请的最大时间跨度，该值会覆盖配置文件中的 `MaxSpan` 变量的值
-   `-d` 用于指定输出目录，默认为当前目录
-   `-o` 用于指定输出文件名，默认文件名为 `CODE_YYYYMMDDHHMM_SPAN.cnt`
-   `-t` 用于指定 channel table 的文件名，默认文件名为 `CODE_YYYYMMDD.ch`

注意，不建议使用 `-o` 和 `-t` 选项，因为这两个文件名的格式是硬编码在其他脚本中的。使用这两个选项自定义格式会导致其他脚本无法使用。

### 示例

最简单的例子:

    python HinetContRequest.py 2012 01 01 10 30 20

申请其他台网的数据:

    python HinetContRequest.py 2012 01 01 10 30 20 -c 0103

自定义输出信息:

    python HinetContRequest.py 2012 01 01 10 30 20 -d abc -o xxx.cnt -t xxx.ch

建议的用法是:

    python HinetContRequest.py 2012 01 01 10 30 20 -d 201201010130

即指定输出目录，输出文件名使用默认设置。

## 修订历史

-   2014-08-30：初稿；
-   2014-09-12：账号及密码位于配置文件中；
-   2014-11-04：将数据申请与数据下载合并在一起；
-   2014-12-03：由于 Hinet 网址的更新，原 Python 脚本失效，现已修正；
-   2015-01-17：Hinet 网址改动比较大，脚本实现需要更多的技巧，因而把原来的示例脚本删除；
-   2016-03-08：完善设计思路；

