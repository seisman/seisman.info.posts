---
title: SAC 不同格式间的转换
date: 2013-08-04
author: SeisMan
categories: SAC
tags: 格式转换
---

SAC 文件格式包括二进制格式和 ASCII 格式，平常接触的都是二进制格式的，毕竟二进
制格式相对于 ASCII 格式有很多优点，比如读写速度更快、文件大小更小。下面讨论 SAC
的两种格式以及另外一种常见的数据格式（自变量 + 因变量两列数据）之间的转换。

<!--more-->

## 二进制转 ASCII

    SAC> r sacfile
    SAC> w alpha sacfile.ascii

有时数据遇到问题的时候，可以转换成 ASCII 格式，看看里面的内容。

## ASCII 转二进制

    SAC> r alpha sacfile.ascii
    SAC> w sacfile

## 单列数据转二进制

数据文件中只含一列数据，包含了因变量的信息。

    SAC> readtable data1
    SAC> w sacfile

## 两列数据转二进制

数据文件中含两列数据，包含了自变量和因变量的信息。

    SAC> readalpha content xy data2
    SAC> w sacfile

非时间序列数据（任意的 xy 数据）都可以用 SAC 来处理以实现相应的功能，这也就是 SAC
自称其为 “一个用于处理连续信号尤其是时间序列数据的通用交互式程序” 的原因。

## 二进制转时间序列

没法用命令直接做到，比较合适的做法是写一个 C 或 FORTRAN 调用读取 SAC 文件，然后
以数组形式写入文件。
