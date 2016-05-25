---
title: 修改 GMT 生成的 PS 文件的标题
date: 2015-03-14
author: SeisMan
categories: GMT
tags: GMT技巧
---

本文整理自： <http://gmt.soest.hawaii.edu/boards/1/topics/1820>

需要说明的一点，本文是要修改 PS 文件的标题，而不是 PS 文件的文件名。

用编辑器打开任意一个 GMT 生成的 PS 文件，查看文件的前几行，其中一行大概如下:

    %%Title: GMT v5.1.1 (r12968) [64-bit] Document from psxy

这就是所谓的 PS 文件的标题。当用 evince 或 gv 打开 PS 文件时，该标题会在软件的某个位置显示。

<!--more-->

从上面的例子中可以看到，GMT 生成的 PS 文件的标题中几乎没有带有任何有意义的信息。而在
看图的时候可能经常需要从几张相似的图中区分哪张图来自哪个数据，当然可以通过定义很
复杂的 PS 文件名来区分不同的数据，但那么大的一个标题不用，似乎有些太浪费了。

GMT 软件自身不能自定义 PS 文件的标题，只能通过外部程序实现:

    sed -i 's/^%%Title:.*/%%Title:'"$NEW_TITLE/" $FILE

其中变量 `$FILE` 是要修改标题的 PS 文件名， `$NEW_TITLE` 是要修改的新标题。
这条命令本质上就是一个简单的字符串替换而已，比如:

    sed -i 's/^%%Title:.*/%%Title:'"This is new title/" test.ps
