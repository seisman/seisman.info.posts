---
title: freqlimits 的选取
date: 2014-01-16
author: SeisMan
categories: SAC
tags: 仪器响应
---

真实的地面运动，其频谱范围是非常广泛的，从 0 Hz 到几千 Hz 甚至更高。

下文全部假定采样间隔为 T=0.01s。

根据奈奎斯特采样定理，采样频率为 f=1/T=100 Hz，相应的 Nyquist 采样频率为
f'=f/2=50 Hz。即当采样间隔为 T=0.01 s 时，频率低于 50 Hz 的信号会被正确采样
并可以重建原信号，而频率高于 50 Hz 的信号则会与频率对于 50 Hz 的信号发生混叠。
因而，在模拟信号转换为数字信号之前，必须要使用一个低通模拟滤波器或其他数字滤波手段。

无论怎样，信号在经过采样之后，信号中高于 50Hz 的部分必须被削弱，因而仪器响应的
振幅谱在接近 50 Hz 时迅速下降为 0 或者非常小的值。

去除仪器响应，实际上就是频率域的除法，直接做除法会在大于 50 Hz 时出现除以 0
或小值的情况。因而就需要使用 freqlimits。

freqlimits 有四个参数，f1、f2、f3、f4，满足 `f1<f2<f3<f4` ，其中 f4 必须
小于或等于 50Hz，对于其他参数没有过多要求。

一般而言，f2 到 f3 之间的范围应尽量宽。

参考：

-   <http://www.eas.slu.edu/eqc/eqc_cps/Questions/qa0001.html>
-   <http://www.eas.slu.edu/eqc/eqc_cps/Questions/qa0002.html>

