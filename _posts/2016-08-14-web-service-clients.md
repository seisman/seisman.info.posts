---
title: 使用 Web Services 获取地震数据
date: 2016-08-14
author: SeisMan
categories: 地震学软件
tags: [波形数据, IRIS]
---

地震数据通常包含三类：地震目录、台站信息、波形数据。当然，还有一些其他的地震数据，比如震源机制等等。

世界上最大的地震数据中心是 IRIS DMC。除了 IRIS DMC 之外，还有很多稍微小一些的地震数据中心。不管是 IRIS DMC 还是其他的小型地震数据中心，通常都提供了多种工具以供用户获取地震数据。这些工具千差万别，每遇到一个新的地震数据中心，可能就得学一套新的数据获取工具，给用户带来了极大的麻烦。

幸运的是，FDSN 定义了通用的 [FDSN Web Services 规范](http://www.fdsn.org/webservices/)，并不断被多个地震数据中心所采用，使得用户只需要学习一套工具即可从多个地震数据中心下载地震数据。

FDSN Web Service 规定了三类服务的规范：

- `station`: 获取台站信息
- `dataselect`: 获取波形数据
- `event`: 获取地震目录

简单的说，Web Services 是一套规范，用户通过向数据中心发送特定的网页请求来获取数据。这一套规范由于其通用性而被越来越多的地震数据中心所采用。因而学会了 Web Services 工具，就可以只用一套工具从不同的数据中心申请数据。

IRIS DMC 就实现了这一套 Web Services，并且给出了详细的解释与示例，适合作为 Web Services 的学习教程：

- [IRIS station](http://service.iris.edu/fdsnws/station/1/)
- [IRIS dataselect](http://service.iris.edu/fdsnws/dataselect/1/)
- [IRIS event](http://service.iris.edu/fdsnws/event/1/)

用户可以根据 Web Services 规范构建一个网址，然后复制到浏览器的地址栏即可完成数据的申请。显然，这种方式不适合批量申请数据。很多工具对 Web Services 做了封装，提供了更加简便的数据获取方式。

下面列出了一些基于 Web Services 的地震数据获取工具：

1. [ws-fetch-scripts](https://seiscode.iris.washington.edu/projects/ws-fetch-scripts): Perl写的命令行工具
2. [SOD](http://www.seis.sc.edu/sod/): Java写的命令行数据获取工具
3. [irisFetch.m](http://ds.iris.edu/ds/nodes/dmc/software/downloads/irisFetch.m/): Matlab函数库
4. [JWEED](http://ds.iris.edu/ds/nodes/dmc/software/downloads/JWEED/): Java写的GUI数据获取工具
5. [IRIS-WS](http://ds.iris.edu/ds/nodes/dmc/software/downloads/iris-ws/): Java API

下面列出了几个地震数据处理工具，这几个工具实现了 Web Services 的功能，因而也可以用于获取地震数据：

1. [ObsPy](http://www.obspy.org/): Python写的地震数据处理工具
2. [SeisIO.jl](https://github.com/jpjones76/SeisIO.jl): Julia写的地震数据处理工具
3. [GISMO](http://geoscience-community-codes.github.io/GISMO/): Matlab写的地震数据处理工具

参考资料：

- [FDSN Web Services](http://www.fdsn.org/webservices/)
- [支持 Web Services 的地震数据中心](http://www.fdsn.org/webservices/datacenters/)
- [IRIS Web Services](https://service.iris.edu/)
