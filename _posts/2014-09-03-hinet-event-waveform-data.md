---
title: Hi-net 事件波形数据
date: 2014-09-03 00:01
author: SeisMan
categories: 地震学基础
tags: [Hinet, 数据]
---

Hi-net 基于 JMA Unified Hypocenter Catalog 提供的事件信息，提供了事件波形数据。

[事件波形申请地址](http://www.hinet.bosai.go.jp/REGS/download/event/)
[事件波形下载地址](http://www.hinet.bosai.go.jp/REGS/download/event/event_status.php)

查看网页源代码可以发现，申请的实质是调用另一个 `openRequest` 函数，其中最关键的参数是事件 ID，该 ID 的命名规则尚不清楚，因而想要脚本实现还有些困难。

本文暂停于此...
