---
title: Hi-net Channel Table 文件
date: 2014-09-05
updated: 2014-09-09
author: SeisMan
categories: 地震学基础
tags: [Hinet, 仪器响应]
---

从 Hi-net 下载连续波形数据会得到 ZIP 压缩文件，其中包含了两个后缀为 `ch` 的文件，
即 Channel Table 文件。两个文件内容是相同的，区别在于一个是 `euc` 编码，
一个是 `sjis` 编码。只需要用其中一个即可，这里选择 `euc` 编码的文件。

Channel Table 文件描述了每个 channel 的仪器信息，某种程度上等效于常见的 RESP 或 SAC
PZ 仪器响应文件。但是实际上 Channel Table 有一定的局限性，无法理解 Hi-net 为什么会用这种格式来指定仪器响应信息。

由于需要注意的是，对于 Hinet 而言，channel table 可以完整的描述仪器响应，而对于 Fnet 而言，channel table 给出的信息不足。因而关于 channel table 的内容，仅适用于 Hinet，不适用于 Fnet，不确定是否适用于其他台网。

<!--more-->

## 规律分析

看一看 Channel Table 文件的内容，很容易总结出如下规律：

-   每个台站的信息需要四行；
-   第一行以 `#` 开头，描述了台站名称及其他信息，可以认为是注释行；
-   第二至四行，分别为 U、N、E 三个分量的仪器信息；

但细细看看文件内容会发现，存在很多不符合上述规律的特例，比如：

-   有些台站只有一个或两个分量，而不是三个；
-   有些台站不包含 N、E 分量，而包含 X、Y 分量；

因而，若按照上面总结出的规律去做文本处理，会出现很多问题。更严谨的处理方式应该是：将所有以 `#` 开头的行当作注释行，其余行平等对待，即最小单位是 channel 或分量，而不是台站。

## 格式

一个 channel 包含了如下以 ** 空格 ** 分隔的 19 列信息:

    2903 1 0 N.AGWH U 6 27 154.30 m/s 0.96 0.70 0 1.023e-07 43.0842 140.8199 -77 0 0 Akaigawa

每列的具体含义如下（后加问号则表示不那么确定）：

1.  Channle ID：16-bit，用四位的 16 进制数表示，用于唯一标识一个 channel；
2.  Recording flag：若为 1 则表示该 channel 正常记录数据，值一般为 1（？）
3.  Delay time on a circuit：电路中的时间延迟，值一般为 0
4.  Station code：台站代码，Hi-net 的台站代码格式为 `N.xxxH` ；
5.  Motion component code：分量名，可以取值包括 U、N、E、X、Y，除此之外，还有 wU、wE、wN 等奇怪的分量；
6.  Reduction ratio of monitor waveform amplitude：显示器上的显示振幅与实际振幅之间的比例，其值为 2 的指数（？）
7.  Quantization bit rate in A/D conversion：模数转换器的量化分辨率，一般值为 27，个别值为 20 或 24；
8.  Sensor sensitivity：每单位输入所产生的输出为多少 V；
9.  Unit of input：输入的单位，一般为 `m/s` ，即输入为速度；
10. Natural period of the seismometer：传感器的自然周期；
11. Damping constant of the seismometer：传感器的衰减常数；
12. Amplification factor applied to sensor output prior to A/D conversion：在对连续波形使用 ADC 之前，传感器的放大因子；单位 dB
13. LSB value：模数转换器的 LSB 值；
14. Latitude：台站纬度
15. Longitude：台站经度
16. Altitude：台站高程（单位为 m）
17. P 波台站校正：一般为 0
18. S 波台站校正：一般为 0
19. 台站名称

## 补充说明

### Channel ID

常见的 Channel ID 为四位 16 进制数，实际上有另一类 ID 称为宽 Channel ID，其用八位 16 进制表示。一般用不到，所以在本文以及后面都不会再提到。

### Motion component code

Channel Table 中仅给出了分量代码，可以取值为 U、N、E、X、Y 以及其他。其中 U 表示分量为垂直方向。N、E 表示分量指向北向和东向。X、Y 以及其他分量代码的含义未知。

由于传感器安装在 borehole 的底部，所以很难精确知道传感器的真实方位。以分量代码为 N 的传感器为例，该传感器并不一定严格指向正北方向。一般而言，其与正北方向的夹角在 5 度以内，个别传感器的方向甚至与北向相差几十度。每个传感器的方位信息位于该 [页面](http://www.hinet.bosai.go.jp/REGS/direc/?subject=kekka)。

关于每个分量的实际方位信息，在另一篇博文中会专门讨论。

### Units of input

Hi-net 使用的是短周期速度地震仪，输入为速度场，单位为 `m/s`，而部分 channel 的输入单位为 `m/s/s` ，即输入为加速度场。

输入单位为 `m/s/s` 的 channel，与输入单位为 `m/s` 的 channel 相比，在后期的数据处理上差别很多，因而不建议提取输入单位为 `m/s/s` 的通道数据。

### Natural period of the seismometer

截至 2014 年 09 月 08 日，对于这一列的含义有两种互相矛盾的说法：

-   `readme.txt` 中对该列解释为 **Eigen frequency of the sensor**
-   [Hi-net FAQ 08](http://www.hinet.bosai.go.jp/faq/?LANG=en#Q08) 中该列解释为 **Natural
    period of the seismometer**

Hi-net 官方回复指出，FAQ08 中的解释是正确的，即第 10 列为 “Natural period of the seismometer”。

## 总结

19 列信息：

-   Channel 标识为：1
-   含义很明显，可以直接使用的有：4、5、14、15、16、19；
-   基本没用途，可以不必关心的有一：2、3、6、17、18；
-   与仪器有关的为 7、8、9、10、11、12、13；

接下来会有专门的博文介绍如何根据 7-13 列确定该 channel 的仪器响应。

## 参考

1.  从 Hi-net 下载连续波形数据得到的 ZIP 文件中的 `readme.txt` ；
2.  [Hi-net FAQ 08](http://www.hinet.bosai.go.jp/faq/?LANG=en#Q08)
3.  [Azimuth information of the Hi-net borehole sensors](http://www.hinet.bosai.go.jp/REGS/direc/?LANG=en)

## 修订历史

-   2014-09-05：初稿；
-   2014-09-09：Hi-net 官方确定了第 10 列的含义；

