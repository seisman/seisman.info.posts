---
title: SAC 中将位移记录转换成速度记录
date: 2016-01-12
author: SeisMan
categories:
  - SAC
tags:
  - SAC技巧
slug: sac-convert-displacement-to-velocity
---

将位移记录转换成速度记录，本质上就是微分，在 SAC 中有三种方法可以实现。

先生成测试用的数据:

    SAC> fg seis
    SAC> rmean; rtr; taper
    SAC> w seis.sac

1.  直接对 `diff` 命令对波形做时间域微分:

        SAC> r ./seis.sac
        SAC> dif
        SAC> w seis.sac.diff

2.  用 `transfer` 命令去仪器响应的功能实现微分，该操作本质上在频率域完成:

        SAC> r ./seis.sac
        SAC> transfer from none to vel
           Station (CDV), Channel (-12345)
        SAC> w seis.sac.transfer

3.  时间域的微分在频率域等效于乘以叫频率:

        SAC> r ./seis.sac
        SAC> fft
         DC level after DFT is -0.0051373
        SAC> mulomega
        SAC> ifft
        SAC> w seis.sac.mulomega

测试结果表明，三种算法的结果差别很小，可以忽略。不过需要注意的是，使用 `diff` 做时间域微分时数据点数会少一个。
