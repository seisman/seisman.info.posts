---
title: 地震数据的命名规则
author: SeisMan
date: 2014-03-05
categories:
  - 地震学基础
tags:
  - 数据
slug: seismic-file-name-convections
---

利用 `rdseed` 程序可以很容易地从 SEED 格式数据中解压得到 SAC 格式的地震记录，下面就是一个 SAC 数据的文件名:

    2013.166.17.34.00.0195.IU.HRV.10.BHZ.M.SAC

这篇博文说一说文件的命名规则。

<!--more-->

## 文件名格式

根据 `rdseed` 的 Manual，SAC 数据的文件名形式如下:

    yyyy.ddd.hh.mm.ss.ffff.NN.SSSSS.LL.CCC.Q.SAC

其中

-   `yyyy.ddd.hh.mm.ss.ffff` 是 SAC 文件中第一个数据点对应的时间
    -   `yyyy` 为年；
    -   `ddd` 为一年的第多少天；
    -   `hh.mm.ss` 为时, 分, 秒；
    -   `ffff` 为毫秒；需要注意的是 1s=1000ms，这里毫秒却用了 4 位来表示，这里很容易出错。
-   `NN` 为台网名，2 字符；
-   `SSSSS` 为台站名，一般是 3 个字符，偶尔见到 4 字符的；
-   `LL` 为 location id；为空或两字符；
-   `CCC` 为通道名；
-   `Q` 为质量控制标识；
-   `SAC` 为文件后缀；

## Location ID: LL

关于 Location ID 的详细介绍，见 [IRIS: DS Newsletter: Vol. 1, No. 1](http://ds.iris.edu/ds/newsletter/vol1/no1/specification-of-seismograms-the-location-identifier/)

Location ID 用于区分同一个台站下多个传感器的不同数据，或者同一个传感器传来的多个数据流。
通常来说，同一个台站不同 location ID 的两个地震数据具有极为相似但有略有不同的波形。

常见的 Location ID 为空，偶尔会见到 `00` , `01` , `10` 这样的，也有遇到 `60` 这样的。

## 质量控制: Q

质量控制标识有四种:

-   D: Data of undetermined state
-   M: Merged Data
-   R: Raw waveform Data
-   Q: QC'd data

一般见到的都是 M。

## 通道名: CCC

通道名用三个字符来表示，这三个字符分别代表了 Band Code、Instrument Code 和 Orientation Code。

### Band Code

Band Code 是通道名的第一个字符，表示了仪器的采样率以及响应频带等信息。

![Band Code](/images/2014030501.jpg)

常见的仪器一般是宽频带 (B) 或长周期(L)。

### Instrument Code

Instrument Code 是通道名的第二个字符，代表了不同的仪器传感器。

| Instrument Code | 说明                      |
|:---------------:|:--------------------------|
|        H        | High Gain Seismometer     |
|        L        | Low Gain Seismometer      |
|        G        | Gravimeter                |
|        M        | Mass position Seismometer |
|        N        | Accelerometer             |

常见的是高增益 (H) 仪器，记录地面运动速度。

### Orientation Code

Orientation Code 表示了传感器记录的地面运动的方向。

| Code  | 说明                                                |
|:-----:|:----------------------------------------------------|
| N E Z | 南北向、东西向、垂向                                |
| 1 2 3 | 3 为垂向；1、2 为水平方向，正交但与东西南北向有偏离 |
|  T R  | 切向、径向，主要用于射线束中                        |
| A B C | 三轴向 (正交)                                       |
| U V W | 可选分量                                            |

常见的是 N、E、Z 以及 1、2、3。

需要注意的是：当仪器的方向与东西方向的夹角小于 5 度时，此 Orientation Code
取为 E；当与东西方向夹角大于 5 度时，Orientation Code 取为 1(或 2). 对于南北方向同理。

因而，即便 Orientation Code 为 N，也并不意味着台站是南北方向的，真实的方向还是需要看 SAC 头段中的 `cmpaz` 和 `cpminc` 。

## 参考

1.  rdseed 5.3.1 Manual
2.  SEED Reference Manual v2.4, Appendix A, P136-P140
