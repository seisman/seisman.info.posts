---
title: 地震波形数据格式
date: 2014-01-10
author: SeisMan
categories:
  - 地震学基础
tags:
  - 数据
  - 格式
slug: iris-data-formats
---

地震数据的格式，大概分为两种：一种是以归档和交换为目的的格式，比如 SEED，
这种格式要求一个文件中包含足够多的数据信息，如果可能的话，进行数据压缩，
以减少数据传输量和数据存储空间；另一种是以数据处理为目的的格式，比如 SAC，
这种格式一般只包含单个台站单个分量或多分量的数据。这里简介一下 IRIS 提供的
以归档和交换为目的的数据格式。

<!--more-->

## SEED

全称是 The Standard for the Exchange of Earthquake Data，其设计的目的是为
了数据交换和归档，因而不适宜直接数据处理，一般使用 rdseed 将 seed 格式转换为其他数据格式。

一个完整的 SEED 数据包含了时间序列以及台站的相关信息。完整的 SEED 数据又可以
分解为两个部分：只包含时间序列的 miniSEED 格式和只包含台站信息的 Dataless SEED 格式。
完整的 SEED 格式的说可以参考 SEED Reference Manual。

## miniSEED

miniSEED 格式是 SEED 格式的一个子集，其只包含时间序列和极少量的其他信息。

一个连续的时间序列在 SEED 格式中被分为若干等长的数据段，这样做的目的还不清楚，
也许是出于数据实时传递的考虑。对于实时数据流，段长度为 512 byte，对于归档数据
段长度为 4096 byte。

[libmseed](https://seiscode.iris.washington.edu/projects/libmseed) 是一个比较友好的函数库，可以用于读写 miniSEED 文件。

miniSEED 数据可以通过 BREQ\_FAST 获取，其邮箱地址为：miniseed@iris.washington.edu。

## Dataless SEED

dataless SEED 中只包含台站的坐标以及仪器响应信息，而不包含任何时间序列。

为什么要将台站信息保存到单独的文件中？因为台站位置以及仪器响应等信息，
在相当长一段时间内（1 年的量级）是保持不变的，当大量申请 SEED 数据时，数据中的
台站信息部分大量重复。由于 dataless SEED 中记录了台站信息的变化历史，因而在
大量数据的情况下，将台站信息单独存放更加经济。

获取 dataless SEED 数据的几种方法：

-   在线申请： <http://www.iris.edu/data/DatalessRequest.htm>
-   使用 BREQ_FAST 格式发送邮件到 `dataless@iris.washington.edu`
-   从 [BUD](http://www.iris.edu/bud_stuff/bud/bud_start.pl?BUDDIR=/budnas/virtualnets/ALL) 申请
-   直接从 IRIS 的 [FTP](http://www.iris.edu/pub/RESPONSES/DATALESS_SEEDS/) 下载

## StationXML

与 dataless SEED 类似，保存台站信息。详细信息在 [这里](http://www.fdsn.org/xml/station/)。

## Simple ASCII

ASCII 格式，占用硬盘空间，不常用。[格式说明](http://www.iris.edu/dms/nodes/dmc/data/formats/simple-ascii/)。
