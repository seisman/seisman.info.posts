---
title: GMT5 的图层透明效果
date: 2013-11-10
author: SeisMan
categories: GMT
tags: [GMT技巧]
---

设置图层的透明度，大概是 GMT5 新增的绘图功能中最大的一个亮点。

<!--more-->

## -t 选项

`-t` 是一个 GMT5 通用选项，用于设置图层透明度，其用法很简单。 `-t<trans>` ，其中
`<trans>` 可以取 0-100 的值，0 代表完全不透明，100 代表完全透明。需要注意的是 PS
是不支持透明特性的，透明的效果只能在 PDF 中看到。

## 一个例子

这个脚本严格遵循 GMT5 的语法。

``` bash
#!/bin/bash
R=g
J=H20c
PS=trans.ps

# 打开 GMT5
gmt psxy -R$R -J$J -T -K -UBL/0/0 > $PS

# 绘制海岸线
gmt pscoast -J$J -R$R -Bpx60 -W1/0.2p -N1 -K -O >> $PS

# 绘制第一个不透明矩形框
gmt psxy -J$J -R$R -W1p -L -Gred -K -O <<EOF>> $PS
100 -20
100 20
140 20
140 -20
EOF

# 绘制第二个透明矩形框
gmt psxy -J$J -R$R -W1p -L -Gred -t60 -K -O <<EOF>> $PS
280 -20
280 20
320 20
320 -20
EOF

# 关闭 GMT
gmt psxy -R$R -J$J -T -O >> $PS
```

## 转换为其他格式

PS 格式不支持透明，所以在 PS 文件中看不到任何透明效果。

`psconvert` 可以将 PS 文件转换为 bmp、eps、pdf、png、jpeg、ppm、tif 格式，但是只有 PDF 格式中可以看到透明效果。

    gmt psconvert -A -P -Tf trans.ps

如果想要其他格式怎么办？再用 `convert` 将 PDF 转换为其他格式即可:

    convert -density 300 trans.pdf trans.jpg

注意：

-   是两步走，先用 `psconvert` 将 PS 转换为 PDF，再用 `convert` 将 PDF 转换为其他格式。
-   直接用 `convert` 将 PS 转换为其他任何格式（包括 PDF），都没有透明效果。

## 效果图

![](/images/2013111001.jpg)
