---
title: 用海岸线裁剪区域
date: 2013-10-30
author: SeisMan
categories: GMT
tags: GMT技巧
---

## 问题描述

已有 etopo 数据，其包含了全球地形以及海水深度数据，现绘制全球地图，要求有全球海岸线和地形数据。

<!--more-->

## 代码 1

``` bash
#!/bin/bash
R=0/360/-60/60
J=M24c

grdraster 8 -R$R -I2m -Gout.grd
makecpt -Cglobe -T-11500/8500/2000 -Z > colors.cpt
grdimage out.grd -J$J -R$R -Ccolors.cpt -K > a.ps
pscoast -J$J -R$R -B60/30 -W1/0.5p -N1 -O >> a.ps
```

效果如下：

![](/images/2013103001.jpg)

这里可以很明显地看出，海岸线与地形是不重合的。一开始以为是脚本的问题，想想才明白，
地形与海岸线不匹配是正常的，其差异是由于大陆架造成的。理论上可以通过修改 cpt 文件，
使得大于 0 和小于 0 的地形的颜色对比更强烈一些。不过这不是这篇博文所关注的东西。

## 代码 2

``` bash
#!/bin/bash
R=0/360/-60/60
J=M24c

grdraster 1 -R$R -I5m -Gout.grd
makecpt -Cglobe -T-11500/8500/2000 -Z > colors.cpt

pscoast -J$J -R$R -Gc -K -V > a.ps
grdimage out.grd -J$J -R$R -Ccolors.cpt -K -O -V >> a.ps
pscoast -J$J -R$R -Q -K -O -V >> a.ps
pscoast -J$J -R$R -B60/30 -W1/0.5p -N1 -O -V >> a.ps
```

![](/images/2013103002.jpg)

这里使用了三个 `pscoast` 命令，第一个 `pscoast` 将陆地区域 clip 出来，第二个 `pscoast`
关闭 clip，第三个 `pscoast` 绘制海岸线。效果还不错。

## 代码 3

``` bash
#!/bin/bash
R=0/360/-60/60
J=M24c

grdraster 1 -R$R -I5m -Gout.grd
makecpt -Cglobe -T-11500/8500/2000 -Z > colors.cpt

pscoast -J$J -R$R -Sc -K -V > a.ps
grdimage out.grd -J$J -R$R -Ccolors.cpt -K -O -V >> a.ps
pscoast -J$J -R$R -Q -K -O -V >> a.ps
pscoast -J$J -R$R -B60/30 -W1/0.5p -N1 -O -V >> a.ps
```

![](/images/2013103003.jpg)

与代码 2 类似，这里只绘制出了海洋部分的地形。
