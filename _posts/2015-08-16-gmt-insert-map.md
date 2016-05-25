---
title: GMT 绘制图中图
author: SeisMan
date: 2015-08-16
categories: GMT
tags: [GMT技巧]
---

英文一般称为 inset map 或 insert map，中文还不确定有没有专门的名词，一般常称为图中图、小图、嵌入图。

所谓 insert map，即在绘制小区域地图时，在图上的某个角落里绘制一张更大范围的地图，并在大范围地图上绘制一个方框，以更清楚地表明小区域的地理位置。

若是了解 GMT 中图层的概念以及图层叠加的原理，就可以很容易地把 insert map 画出来。由于 GMT4 和 GMT5 语法上的差异，这里同时给出 GMT4 和 GMT5 两个版本的绘图脚本。二者原理是差不多的，只是语法上有些差异，因而下面只解释 GMT5 脚本中的细节，对 GMT4 脚本不做过多介绍。

<!--more-->

## 效果图

![](/images/2015081601.png)

## GMT5 脚本

``` bash
#!/bin/bash
R=115/123/35/40             # 小区域地图的范围 - R
J=M20c                      # 小区域的投影方式 - J
PS=map.ps

# 打开 GMT
gmt psxy -R$R -J$J -T -K > $PS

# 绘制小区域的地图
gmt pscoast -R$R -J$J -B1 -Df -W2p -I2p -N1/2p -A1000 -K -O >> $PS
# ...
# 此处可以任意添加其他绘图命令
# ...

# 开始绘制 insert map
Rg=72/135/16/55     # 大区域地图的范围 - R
Jg=M7c              # 大区域地图的投影方式 - J
# 绘制大区域地图的海岸线及边框
gmt pscoast -R$Rg -J$Jg -B0 -B+gwhite -Df -N1 -W -A5000 -K -O --MAP_FRAME_TYPE=plain >> $PS
# 利用 psbasemap 在大区域地图内绘制小区域所在的方框
gmt psbasemap -R$Rg -J$Jg -D$R+p2p,blue -K -O >> $PS

# 结束 GMT 绘图
gmt psxy -R$R -J$J -T -O >> $PS
```

整个脚本的思路已经在脚本注释中做了解释。本质上就是先绘制小区域地图而不去管 insert map，待小区域地图绘制完成后，再单独绘制一个 insert map。

绘制 insert map 时，使用了两个命令：pscoast 和 psbasemap。其中，pscoast 的作用是绘制大区域地图的边框以及海岸线，psbasemap 用于在大区域地图内绘制一个矩形区域，当然也可以用 psxy 命令代替。

在使用 pscoast 命令绘制大区域地图时，有几个需要解释的地方：

1.  `-B0` 使得大区域地图的边框不显示刻度；
2.  默认情况下，边框内部是透明的，此时会在 insert map 内看到下一图层里的一些元素，`-B+gwhite` 使得边框内填充白色；
3.  `--MAP_FRAME_TYPE=plain` 设置边框类型为一般的直线，默认值是 fancy 即火车轨道边框；
4.  可以设置 `MAP_FRAME_PEN` 以修改边框的粗细；
5.  pscoast 命令中可以使用 - X 和 - Y 选项以调整 insert map 在图中的位置；

## GMT4 脚本

GMT4 脚本相对于 GMT5 脚本的主要区别在于：GMT5 中任意命令都可以通过 `-B+gwhite` 的语法指定边框内填充白色，而 GMT4 中只有 psbasemap 命令可以通过 `-Gwhite` 选项来实现填充白色。因而 GMT4 的脚本中，需要先使用 psbasemap 绘制一个白色填充的边框，再使用 pscoast 绘制海岸线。

``` bash
#!/bin/bash

xmin=115
xmax=123
ymin=35
ymax=40
R=$xmin/$xmax/$ymin/$ymax
J=M20c
PS=map.ps

psxy -R$R -J$J -T -K > $PS

pscoast -R$R -J$J -B1 -Df -W2p -I2p -N1/2p -A1000 -K -O >> $PS

Rg=72/135/16/55
Jg=M7c
psbasemap -R$Rg -J$Jg -B0 -Gwhite -K -O --BASEMAP_TYPE=plain >> $PS
pscoast -R$Rg -J$Jg -Df -N1 -W -A5000 -K -O >> $PS
psxy -R$Rg -J$Jg -W2p,blue -K -O -L >> $PS << EOF
$xmin $ymin
$xmin $ymax
$xmax $ymax
$xmax $ymin
EOF

psxy -R$R -J$J -T -O >> $PS
```

## 修订历史

-   2015-08-16：初稿
-   2015-11-02：GMT5 脚本使用 `psbasemap` 的 `-D` 选项以简化代码
