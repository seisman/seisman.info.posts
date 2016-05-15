---
title: 修改 Y 轴的坐标标注的方向
date: 2015-03-11
author: SeisMan
categories: GMT
tags: GMT技巧
---

在用 GMT 绘制底图时，通常 Y 轴的标注都是水平的，比如如下绘制底图的命令:

    gmt psbasemap -R0/50/-10/10 -JM10c -Bx10 -By10 > test.ps

效果如下图

![](/images/2015031101.png)

有些时候想要让 Y 轴的标注逆时针旋转 90 度，即 Y 轴的标注方向与 Y 轴平行而不是与 X 轴平行。想要实现的效果如下图。

![](/images/2015031102.png)

想要实现上图所示的效果，很简单，只需要修改 GMT 的参数 `MAP_ANNOT_OBLIQUE`
即可，代码如下:

    gmt set MAP_ANNOT_OBLIQUE 32
    gmt psbasemap -R0/50/-10/10 -JM10c -Bx10 -By10 > test.ps

几点说明：

1.  GMT4 下需要修改 `OBLIQUE_ANNOTATION` 为 32；
2.  该参数对 `JX` 无效，可能只对地理投影有效；
