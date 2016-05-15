---
title: JMA 统一地震目录
date: 2014-09-01
author: SeisMan
categories: 地震学基础
tags: [Hinet, 地震目录]
---

JMA 对 JMA、NIED、各大学以及机构收集的地震数据进行处理，形成了一个统一的地震目录。该地震目录只是初级的结果，JMA 会不定期修改该地震目录。

该地震目录仅供参考，Hi-net 网站中提供的事件波形数据、到时数据以及震源机制数据，均基于此地震目录。但在实际科研中，建议使用 JMA 提供的最终版地震目录（未找到具体地址...）。

该地震目录的输出包括：

-   发震时刻及其误差
-   经纬度及其误差
-   深度及其误差
-   震级
-   区域

该页面的请求原理与连续波形数据的请求原理类似，本质上就是向某个 url 添加 query
string，如下例:

    https://hinetwww11.bosai.go.jp/auth/jmalist.php?LANG=en&list_span=1&list_year=2014&list_month=08&list_day=29

因而该请求可以很容易地用脚本实现。但由于该请求返回的是 HMTL，因而还需要对 HTML 文本进行处理才能提取出地震目录。实现起来不难，但是意义不大。
