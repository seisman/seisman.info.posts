---
title: 图像格式转换工具 convert
date: 2013-09-27
author: SeisMan
category:
  - GMT
tags:
  - GMT技巧
  - 图像
  - 格式转换
slug: imagemagick-convert
---

GMT 中 `psconvert` 可以将 GMT 生成的 PS 文件转换成其他常见的图片格式。一般情况下，如果只用 GMT 做图的话， `psconvert` 基本可以满足需求了。

遇到几个特殊的情况如下：

-   GMT 中设置纸张背景色 `PS_PAGE_COLOR`，此时 `psconvert` 无法实现切边；
-   用其他软件绘图，比如 LaTeX 的 TikZ/PGF 包，得到 PS 或 PDF 文件，无法使用 `psconvert` 实现格式转换；
-   ...

这个时候就需要使用 ImageMagick 提供的 `convert` 命令。

<!--more-->

`psconvert` 中常用的选项有 `-A`、`-E`、`-T`、`-P`。 `convert` 众多选项中与之对应的选项如下：

-   **-trim：**切边，等效于 `psconvert` 的 `-A` 选项；其可以解决上面的第一个问题；
-   **-density** *width***x***height*：设置图像精度，等效于 `psconvert` 的 `-E` 选项；
    按照 GMT 的惯例，`width=300` 即可，`height` 可以指定或不指定。注意 `width` 和 `height` 中间的字符是字母 `x`；
-   **-rotate***degree*：实现图像旋转，`-rotate 90` 等效于 `psconvert` 的 `-P` 选项，当然 rotate 可以旋转各种角度。
-   convert 没有与 `psconvert` 中 `-T` 相应的选项，因为 convert 通过识别后缀直接进行转换；[这里](http://www.imagemagick.org/script/formats.php) 列出了 convert 支持的上百种图像 / 动画格式。

下面给出最常用的一个例子：

    convert -trim -density 300 -rotate 90 test.ps test.png

其等效于

    gmt psconvert -A -E300 -P -Tg test.ps
