---
title: 查看 IRIS 台站分布
date: 2014-01-28
author: SeisMan
category: 地震学基础
tags: [IRIS, 台站]
---

IRIS 利用 Google Map 服务，提供了直观查看台站分布的方法。

主页： <http://www.iris.edu/gmap/>

这个服务比较特别，不包含常见的按钮或选项。用户需要根据网站介绍的格式，创建自己需要的 URL，直接输入到浏览器中即可查看相关台站分布，并可以查看每个台站的具体信息。

基本格式为:

    http://www.iris.edu/gmap/[network]/[station]?key1=value1&key2=value2

其中中括号包围的项为可选项，问号后接 (key,value) 对。具体参见原网站。

<!--more-->

下面是一些例子：

1.  列出 II 台网的全部台站:

        http://www.iris.edu/gmap/?net=II

    其等效于:

        http://www.iris.edu/gmap/II

2.  列出 IU 台网的 COLA 台站:

        http://www.iris.edu/gmap/IU/COLA

3.  列出虚拟台网 \_GSN:

        http://www.iris.edu/gmap/_GSN

4.  列出 TA 台网 2004 下半年的所有台站:

        http://www.iris.edu/gmap/TA?timewindow=2004/6/1-2004/12/31

5.  列出 \_GSN 台网 1988 年工作的所有台站:

        http://www.iris.edu/gmap/_GSN?timewindow=1988-1988

6.  列出一定范围内的所有台站:

        http://www.iris.edu/gmap/?minlat=46&maxlat=49&minlon=-125&maxlon=-117
