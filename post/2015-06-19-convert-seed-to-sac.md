---
title: SEED 格式转 SAC 格式
date: 2015-06-19
author: SeisMan
categories:
  - 地震学基础
tags:
  - SEED
  - SAC
  - 格式转换
slug: convert-seed-to-sac
---

本文会介绍将 SEED、miniSEED 等格式转换为 SAC 格式所使用的工具和用法。需要注意，
本文并不会详细介绍工具的具体语法，只介绍常用的功能，其他功能及选项，读者应自行阅读相关文档。

<!--more-->

## SEED 格式简介

SEED，即 Standard for the Exchange of Earthquake Data，是地震学波形数据的标准格
式之一。每个 SEED 文件中可以包含多台站多分量多时间段的连续波形数据。

SEED 格式又可以细分为三种格式：

1.  Full SEED 格式：也就是一般说的 SEED 格式，包含波形数据以及仪器相关信息；
2.  miniSEED 格式：仅包含波形数据；
3.  dataless SEED 格式：仅包含仪器相关信息；

## rdseed: SEED => SAC

rdseed 可以直接提取波形数据:

    rdseed -df infile.seed

可以同时提取波形数据以及 RESP 仪器响应文件:

    rdseed -Rdf infile.seed

还可以同时提取波形数据以及 SAC PZ 仪器响应文件:

    rdseed -pdf infile.seed

## rdseed: SEED => RESP/PZ

只提取 RESP 文件:

    rdseed -Rf infile.seed

只提取 PZ 文件:

    rdseed -pf infile.seed

## rdseed: Dataless SEED => RESP/PZ

从 Dataless SEED 中提取 RESP:

    rdseed -Rf infile.dataless

从 Dataless SEED 中提取 PZ:

    rdseed -pf infile.dataless

## rdseed: miniSEED => SAC

利用 rdseed 将 miniSEED 数据转换为 SAC 格式时，需要使用 **对应** 的 dataless SEED 数据。

从 miniSEED 中提取波形数据:

    rdseed -df infile.miniseed -g infile.dataless

从 miniSEED 中提取波形数据，同时从 dataless SEED 中提取 RESP:

    rdseed -Rdf infile.miniseed -g infile.dataless

从 miniSEED 中提取波形数据，同时从 dataless SEED 中提取 PZ:

    rdseed -pdf infile.miniseed -g infile.dataless

## mseed2sac: miniSEED => SAC

mseed2sac 可以直接将 miniSEED 文件转换为 SAC 格式，而不需要 dataless SEED 文件:

    mseed2sac infile.miniseed

但解压出来的 SAC 文件中只有台站名和台网名，与用 miniSEED 解压出来的 SAC 数据相比，
少了 cmpaz、cmpinc、stla、stlo、stel、stdp、kcmpnm 信息，因而需要手动添加台站信息。

在使用 mseed2sac 时，还可以加上额外的 metafile 和 selectfile 文件，以及地震事件信息。比如:

    mseed2sac -m metafile -I selectfile -E 2006,123,15:27:08.7/-20.33/-174.03/65.5/Tonga

其中 metafile 提供了台站的基本信息，selectfile 中列出了要提取哪些台站的数据。具体文件格式参考官方文档。

metafile 可以自己根据格式生成，也可以直接使用 IRIS 提供的 [FetchMetadata](https://seiscode.iris.washington.edu/projects/ws-fetch-scripts/files) 脚本获取。

## obspy: miniSEED => SAC

obspy 可以读取 miniSEED，并输出为多种格式，输出时文件名的格式需要自己指定。

``` python
from obspy.core import read

st = read("20150612.miniseed")
for tr in st:
    fname = "%s.%s.%s.%s.SAC" % (tr.stats.network, tr.stats.station, tr.stats.location, tr.stats.channel)
    tr.write(fname, format="SAC")
```

## 参考

1.  [IRIS Data Format](https://ds.iris.edu/ds/nodes/dmc/data/formats/)
2.  [IRIS Dataless SEED](http://ds.iris.edu/ds/nodes/dmc/data/formats/dataless-seed/)
3.  [mseed2sac](https://seiscode.iris.washington.edu/projects/mseed2sac/wiki)
4.  [Working with SEED data](http://portal.resif.fr/?Working-with-SEED-data&lang=en)
