---
title: 仪器响应文件 SAC PZ
date: 2013-06-28
author: SeisMan
categories:
  - 地震学基础
tags:
  - 仪器响应
mathjax: true
slug: simple-analysis-of-sac-pz
---

RESP 文件是 SEED 格式默认的仪器响应文件，在上一篇博文《[仪器响应文件 RESP](/simple-analysis-of-resp/)》
中已经分析了一个例子。RESP 响应文件完整地描述了仪器响应的全部信息，与此同时也包含了不少冗余信息。

SAC 对 RESP 文件进行了简化，仅包含了一些必要信息，这个新的文件格式叫做 SAC\_PZ。

<!--more-->

下面给出一个 PZ 文件的例子，其与上一篇博文中的 RESP 文件对应同一个台站，因而利用上一篇的 RESP 文件可以
完整推导出本文的 PZ 文件。

    * **********************************
    * NETWORK   (KNETWK): IU
    * STATION    (KSTNM): COLA
    * LOCATION   (KHOLE): 00
    * CHANNEL   (KCMPNM): BHZ
    * CREATED           : 2013-06-22T14:12:09
    * START             : 2012-09-14T04:00:00
    * END               : 2599-12-31T23:59:59
    * DESCRIPTION       : College Outpost, Alaska, USA
    * LATITUDE          : 64.873599
    * LONGITUDE         : -147.861600
    * ELEVATION         : 84.0
    * DEPTH             : 116.0
    * DIP               : 0.0
    * AZIMUTH           : 0.0
    * SAMPLE RATE       : 20.0
    * INPUT UNIT        : M
    * OUTPUT UNIT       : COUNTS
    * INSTTYPE          : Geotech KS-54000 Borehole Seismometer
    * INSTGAIN          : 2.013040e+03 (M/S)
    * COMMENT           : N/A
    * SENSITIVITY       : 3.377320e+09 (M/S)
    * A0                : 8.627050e+04
    * **********************************
    ZEROS   3
            +0.000000e+00   +0.000000e+00
            +0.000000e+00   +0.000000e+00
            +0.000000e+00   +0.000000e+00
    POLES   5
            -5.943130e+01   +0.000000e+00
            -2.271210e+01   +2.710650e+01
            -2.271210e+01   -2.710650e+01
            -4.800400e-03   +0.000000e+00
            -7.384400e-02   +0.000000e+00
    CONSTANT        +2.913631e+14

星号部分是注释，其包含了台站的一些信息，这些信息比 RESP 文件中的内容要更丰富，比如台站名、台网名、
location、channel、台站经纬度、高程、输入、输出、放大系数、归一化因子等。

然后给出了零点和极点的信息，跟 RESP 比较一下，发现极点信息是对的。零点个数比 RESP 文件多了一个。

这是为什么呢？

Laplace 变换有一个很重要的性质：如果 $f(t)$ 的 Laplace 变换为 $F(s)$，那么 $f(t)$ 的一阶时间偏导
$f'(t)$ 的 Laplace 变换为 $sF(s)$，也就是多了一个零点 `(0.0,0.0)` 。RESP 文件认为仪器的输入是速度，
因而其单位是 `m/s`，而 PZ 文件认为输入为位移，单位为 `m`，因而 PZ 文件的仪器响应首先要将位移经过一次
偏导得到速度，再根据 RESP 的零极点信息转换为电压信息。一切都是可以合理解释的。

前面已经说过，整个仪器响应可以简化为

$$G(f)=S_{d1} A_0 H_p(s) S_{d2} S_{d3}=S_{d0} A_0 H_p(s)$$

所以 PZ 文件中将所有的放大系数以及归一化因子合并成为一个常数，也就是最后的 `CONSTANT` 。
