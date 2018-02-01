---
title: "MoPaD:地震矩绘制和分析工具"
date: 2013-08-27
author: SeisMan
categories:
  - 地震学软件
tags:
  - 震源机制解
  - 震源球
  - Python
slug: mopad-moment-tensor-plotting-and-decomposition
---

MoPaD，全称Moment tensor Plotting and Decomposition，是一个用于分析地震矩的小工具，
主要功能包括地震矩与断层面参数的转换、地震矩分解以及震源球的绘制。该工具可控参数非常丰富，因而
具有非常强的灵活性，可以满足大多数需求。

<!--more-->

## 基本信息

**作者：**Lars Krieger and Sebastian Heimann

**语言：**Python2，需要安装numpy和matplotlib模块

**官方主页：** <http://www.larskrieger.de/mopad/>

**下载地址：** <https://github.com/geophysics/MoPaD>

**许可：**LGPL

**引用：**Lars Krieger and Sebastian Heimann, MoPaD - moment tensor
plotting and decomposition: *A tool for graphical and numerical analysis
of seismic moment tensors*, Seismol. Res. Lett., 83(3):589-595, 2012

## 基本语法

    mopad <method> <source-mechanism> [options]

source-mechanism可以取如下几种形式：

-   strike,dip,rake
-   strike,dip,rake,moment
-   M11,M22,M33,M12,M13,M23
-   M11,M22,M33,M12,M13,M23,moment
-   M11,M12,M13,M21,M22,M23,M31,M32,M33

每种形式的参数个数不同，因而容易区分。各参数以逗号分隔。角度的单位为度，地震矩分量以及标量矩的单位为N.m。
这里不直接支持矩震级Mw，有些可惜。地震矩的默认坐标系为1为北向（N），2为东向（E），3向下（D），符合
右手定则，记为NED

method可以取如下四种形式：

-   plot
-   describe
-   decompose
-   gmt

四种method，各自有自己独立的options，options太多，主要是调节一些细节参数，不细说。可以使用
`mopad method --help` 查看每个method对应的选项。

## Method

### Plot

用于绘制震源球。震源球默认使用立体等角度投影方式，垂向视角，下半球投影，压缩区为白色，拉伸区为红色，
默认只绘制地震矩的偏张量部分。

下面的例子使用矩张量的震源表示形式，-I选项表明绘制地震矩的各向同性部分，-f指定了输出图像文件名。若未
指定文件后缀，默认为svg格式，目前支持的格式包括svg、png、ps、eps、pdf。

    mopad plot 1,2,3,-4,-5,-10 -I -f FSD_xmpl.png

![](/images/2013082701.png)

这是个更复杂的例子，体现了mopad强大的可控性，具体选项参考`mopad plot -h`：

    mopad plot 1,2,3,-4,-5,-10 -s 10 -v -50,30,-0 -U
          -p o -f FSD_complex.svg -r 252,233,79 -w 117,80,123
          -d 1 3 red 0.5 -e 15 4 1 -b

![](/images/2013082702.png)

mopad可以做地震矩分解，当然也就可以将矩张量不同部分绘制出来。目前可以绘制完整的矩张量、各向同性部分、
偏张量部分、double couple部分以及clvd部分，下面5个命令为例子，不再秀图。

    mopad plot 1,2,3,-4,-5,-10 -I -s 1 -f FSD_xmpl_full.png
    mopad plot 1,2,3,-4,-5,-10 -P iso -s 0.36  -f FSD_xmpl_iso.png
    mopad plot 1,2,3,-4,-5,-10 -s 0.93 -f FSD_xmpl_devi.png
    mopad plot 1,2,3,-4,-5,-10 -P dc -s 0.74 -f FSD_xmpl_dc.png
    mopad plot 1,2,3,-4,-5,-10 -P clvd -s 0.57 -f FSD_xmpl_clvd.png

### describe

对地震矩以及断层参数进行描述。

    $ mopad describe 1,2,3,-4,-5,-10 -i USE

    Scalar Moment: M0 = 14.9031 Nm (Mw = -5.3)
    Moment Tensor: Mnn =  0.200,  Mee =  0.300, Mdd =  0.100,
                   Mne =  1.000,  Mnd = -0.400, Med =  0.500    [ x 10 ]

    Fault plane 1: strike =  95°, dip =  67°, slip-rake = -163°
    Fault plane 2: strike = 358°, dip =  74°, slip-rake =  -24°

### decompose

矩张量分解。

    $ mopad decompose 1,2,3,-4,-5,-10 -o USE

分解结果如下：

    Basis system of the input:

    NED

     Basis system of the output:

    USE

     Decomposition type:

    ISO + DC + CLVD

     Full moment tensor in USE-coordinates:

      /  0.30 -0.50  1.00 \
      | -0.50  0.10  0.40  |   x  10.000000
      \  1.00  0.40  0.20 /


     Isotropic part in USE-coordinates:

      /  2.00  0.00  0.00 \
      |  0.00  2.00  0.00  |
      \  0.00  0.00  2.00 /


     Isotropic percentage:

    13

     Deviatoric part in USE-coordinates:

      /  0.10 -0.50  1.00 \
      | -0.50 -0.10  0.40  |   x  10.000000
      \  1.00  0.40  0.00 /


     Deviatoric part in USE-coordinates:

      /  0.10 -0.50  1.00 \
      | -0.50 -0.10  0.40  |   x  10.000000
      \  1.00  0.40  0.00 /


     Deviatoric percentage:

    87

     Double Couple part in USE-coordinates:

      /  1.36 -2.97  7.30 \
      | -2.97 -1.77  1.95  |
      \  7.30  1.95  0.41 /


     Double Couple percentage:

    55

     Second Double Couple part in USE-coordinates:

     not available in this decomposition type


     Second Double Couple's percentage:

     not available in this decomposition type


     Third Double Couple part in USE-coordinates:

     not available in this decomposition type


     Third Double Couple's percentage:

     not available in this decomposition type


     CLVD part in USE-coordinates:

      / -0.36 -2.03  2.70 \
      | -2.03  0.77  2.05  |
      \  2.70  2.05 -0.41 /


     CLVD percentage:

    32

     Seismic moment (in Nm) :

    14.9031089939

     Moment magnitude Mw:

    -5.25114874821

     Eigenvalues T N P :

    12.5907, 4.31243, -10.9031

     Eigenvectors T N P (in basis system USE):

      / -0.74 \
      |  0.09  |
      \ -0.67 /

      /  0.26 \
      | -0.88  |
      \ -0.40 /

      / -0.62 \
      | -0.47  |
      \  0.63 /


     Tension-axis in USE -coordinates:

      / -0.62 \
      | -0.47  |
      \  0.63 /


     Null-axis in USE -coordinates:

      /  0.26 \
      | -0.88  |
      \ -0.40 /


     Pressure-axis in USE -coordinates:

      / -0.74 \
      |  0.09  |
      \ -0.67 /

### gmt

GMT能绘制的震源球类型很有限，因而mopad可以作为一个补充。mopad gmt返回（x，y），其可以作为psxy
命令的输入。输出的x、y值中心位于(0,0)，因而在利用GMT的psxy绘制的时候需要进行位置的转换。

mopad与psxy联合需要使用一些cpt文件，以控制一些颜色。

    makecpt -Cpolar -Z > psxy_fill.cpt

psxy\_fill.cpt控制震源球压缩区（颜色代码为1）和拉伸区（颜色代码为0）的颜色，这个例子中分别为红色（1）和白色（0）。

    makecpt -I -Chot -Z >psxy_lines.cpt

psxy\_lines.cpt控制震源球边界和界面线的颜色，本例中为黑色。

    mopad gmt 1,2,3,-4,-5,-10 -t fill -p s | psxy -Jx4/4 -R-2/2/-2/2 -P -Cpsxy_fill.cpt -M -K -L  > BB1.ps
    mopad gmt 1,2,3,-4,-5,-10 -t lines -p s | psxy -Jx4/4 -R-2/2/-2/2 -W5 -P -Cpsxy_lines.cpt -M -O >> BB1.ps

![](/images/2013082703.jpg)

## 小结

工具本身很强大，与GMT的结合不太完美，另外虽然是命令行工具，但是不太适合批量处理。
