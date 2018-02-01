---
title: 利用 DCW 数据进行区域涂色
date: 2013-11-22
author: SeisMan
categories:
  - GMT
tags:
  - GMT技巧
  - 动画
  - 图像
slug: gmt-map-coloring
---

关于 DCW 数据，前面两篇博文已经介绍了很多，这个是一个更具体的实例 ----- 区域涂色。

问题描述：绘制中国地图，包括国界和省界，并对每个省份填充不同的颜色。

根据著名的 [四色定理](http://zh.wikipedia.org/wiki/%E5%9B%9B%E8%89%B2%E5%AE%9A%E7%90%86)：任意一个无飞地的地图都可以用四种颜色染色，使得没有两个相邻国家染的颜色相同。

如果真的要求最多只用四色填图，这个问题还真麻烦，这里不强求，只要求相邻省份的颜色不同即可。

<!--more-->

代码如下：

``` bash
#!/bin/bash
R=70/150/10/60
J=M25c
B=10
PS=china.ps

# 打开 GMT
gmt psxy -J$J -R$R -T -K > $PS

# 对每个省份进行循环
for code in 11 12 13 14 15 21 22 23 31 32 33 34 35 36 37 41 42 43 44 45 46 50 51 52 53 54 61 62 63 64 65 71 91 92;
do
   # 随机生成 RGB 颜色
   declare -i red=$RANDOM*256/32768
   declare -i green=$RANDOM*256/32768
   declare -i blue=$RANDOM*256/32768
   # 绘图并涂色
   gmt pscoast -R$R -J$J -FCN.$code+p1p+g$red/$green/$blue -K -O >> $PS
done
# 关闭 GMT
gmt psxy -R$R -J$J -T -O >> $PS
```

分析一下代码：

由于一个 pscoast 命令中最多只能用一次 `-F` 选项，因而需要对不同省份进行循环，即 11-19 行。
14-16 行是生成随机 RGB 颜色，`$RANDOM` 是 Bash 的一个内置变量，每次调用随机生成 0-32767
之间的任意整数，这里做了简单的映射，使得结果为 0-255。 `declare -i` 声明变量为整型，使得映射正确。

由于是随机生成颜色，所以每次运行结果都不一样，这样也不错哈。

结果如下图（好像有些省份的颜色比较接近）：

![](/images/2013112201.jpg)

顺便改一下代码，生成一下动画，下面的代码有意思的点有几个：

-   采用增量绘图，每次绘制一个省份之后将未关闭的 `$PS` 复制一份，命名为 `$code.ps`，然后将 `$code.ps` 文件正常关闭；即 L15-L16；
-   展示了如何利用 `convert` 命令将多个 jpg 文件转换为一个 gif 文件；这里使用了通配符 `*.jpg`，所以正确的给动画的每一帧取名很重要，这决定了每一张 jpg 在 gif 中的顺序；`delay` 设置了每帧之间的时间延迟，`loop` 设置了 gif 循环播放；
-   `psconvert` 在转换时将 DPI 设置为 100，以减少最终生成的 gif 的尺寸，也有人喜欢压缩成 avi 视频格式；

``` bash
#!/bin/bash
R=70/150/10/60
J=M25c
B=10
PS=china.ps

gmt psxy -J$J -R$R -T -K -Xc -Yc > $PS

for code in 11 12 13 14 15 21 22 23 31 32 33 34 35 36 37 41 42 43 44 45 46 50 51 52 53 54 61 62 63 64 65 71 91 92;
do
   declare -i red=$RANDOM*256/32768
   declare -i green=$RANDOM*256/32768
   declare -i blue=$RANDOM*256/32768
   gmt pscoast -R$R -J$J -FCN.$code+p1p+g$red/$green/$blue -K -O >> $PS
   cp $PS $code.ps
   gmt psxy -R$R -J$J -T -O >> $code.ps
done
gmt psxy -R$R -J$J -T -O >> $PS

gmt psconvert -P -E100 *.ps
convert -delay 30 -loop 0 *.jpg china.gif
```

由于生成 PDF 时，不支持导入 GIF 文件，故而就不再给出动态效果图了。
