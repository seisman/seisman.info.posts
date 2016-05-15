---
title: Hi-net WIN32 转 SAC 脚本
date: 2014-09-12
updated: 2014-11-04
author: SeisMan
categories: 地震学基础
tags: [Hinet, Python, 数据]
---

该脚本用于实现 Hinet WIN32 格式到 SAC 格式的转换，脚本位于 [rdhinet.py](https://github.com/seisman/HinetScripts/blob/master/rdhinet.py)。

## 用法

    $ python rdhinet.py -h
    Extract SAC data files from Hi-net WIN32 files

    Usage:
        rdhinet.py DIRNAME [-C <comps>] [-D <outdir>] [-S <suffix>] [-P <procs>]
        rdhinet.py -h

    Options:
        -h          Show this help.
        -C <comps>  Components to extract, delimited using commas.
                    Avaiable components are U, N, E, X, Y et. al.
                    Default to extract all components.
        -D <outdir> Output directory for SAC files.
        -S <suffix> Suffix of output SAC files. Default: no suffix.
        -P <procs>  Parallel using multiple processes.
                    Set number of cpus to <procs> if <procs> equals 0. [default: 0]

## 参数说明

1.  `DIRNAME` 为必须参数，即要处理的文件夹。该文件夹中包含了两个文件：
    `CODE_YYYYMMDDHHMM_SPAN.cnt` 格式的 cnt 文件和 `CODE_YYYYMMDD.ch` 格式的 channel table 文件；
2.  `-C <comps>` 为可选参数，表示要提取哪些分量的波形，可选的值为 U、E、N、X、Y 等，各分量间用逗号分隔，默认值为空，即提取全部分量；
3.  `-D <outdir>` 为可选参数，表示 SAC 文件的输出目录。可以是绝对路径，也可以是相对于当前目录的相对路径，默认解压到文件夹 `DIRNAME` 下；
4.  `-S <suffix>` 输出 SAC 文件的扩展名，默认无扩展名
5.  `-P <procs>` 为可选参数，表示用多个进程并行提取数据；默认值为 0，即设置进程数与 CPU 数目相同；

额外的一点说明：更通用的处理方式应该是参数为文件名而不是目录名，但从实际数据处理的角度看，以目录名作为参数用起来更加方便，现在的选择是在通用性与易用性之间权衡的结果。

## 脚本说明

脚本的数据处理流程如下：

1.  进入目录 `DIRNAME` ；
2.  生成参数文件 `win.prm` ；
3.  从 channel table 文件中获取 channle 列表；
4.  根据 channel 列表，提取不同 channel 的数据；
5.  修改所有 SAC 文件的扩展名；

## 示例

处理目录 201201010101 下的 WIN32 文件，其他参数使用默认值:

    python rdhinet.py 201201010101

仅提取水平分量:

    python rdhinet.py 201201010101 -C E,N

输出 SAC 文件到 `RAW` 目录中:

    python rdhinet.py 201201010101 -D RAW

输出到 `RAW` 目录下，并指定文件扩展名为 `SAC` :

    python rdhinet.py 201201010101 -D RAW -S SAC

## 修订历史

-   2014-09-12：初稿；
-   2014-10-05：实际使用中发现，分量名不只是 UNEXY，因而修改代码，默认提取全部分量；
-   2014-11-04：脚本更新；

