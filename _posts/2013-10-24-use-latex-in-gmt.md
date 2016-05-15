---
title: 在 GMT 中使用 LaTeX
date: 2013-10-24
author: SeisMan
categories: GMT
tags: [GMT 技巧, 图像, 格式转换, LaTeX]
---

GMT 的 `pstext` 命令支持一些简单的文本特效以及特殊字符，但是如果想在 GMT 中显示一些
更复杂的公式或者其他，GMT 则无能为力了。

这个时候自然而然就会想到功能强大的 LaTeX 了，写公式、画图都算是强项。显然 GMT 自身
是无法直接支持 LaTeX 的语法的（若要支持 LaTeX 的语法，在绘图时必须调用 LaTeX 引擎，
这样 GMT 对其他软件的依赖性过大，而且从技术上来说对于 GMT 的开发者来说也有些难度）。

虽然说用 GMT 绘图时在图上显示公式算是一个很小众的需求，从折腾的角度来看，还是很值得的。

<!--more-->

## 用 LaTeX 写公式

下面的 LaTeX 代码包含了地震学里最基础的波动方程：

``` latex
\documentclass{book}
\begin{document}

\thispagestyle{empty}

% 波动方程
\[
\rho \frac{\partial^2 u_i}{\partial t^2} = f_i +\tau_{ij,j}
\]

\end{document}
```

几点说明：

-   默认生成的页面包含页面，页码的存在会影响 PS 文件的 Bounding Box， `thispagestyle{empty}` 设置当前页面不显示页码。
-   `\[ \]` 得到行间公式

## 编译 LaTeX 源码，并处理输出文件

上面的 LaTeX 代码保存在文件 `equation.tex` 中。

``` bash
$ latex equation.tex
$ dvips equation.dvi
$ ps2eps equation.ps -f -l
```

上面的三个命令实现了 `tex -> dvi -> ps -> eps` 的转换。

关于 ps2eps 的一些介绍：

- `-f` 表示若已存在同名 eps 文件，则强制覆盖；
- 在将 ps 文件转换为 eps 文件时，会根据 ps 文件中的 Bounding Box 信息对 PS 文件进行切边，
  但是默认的切边方式切得有点过了， `-l` 会在四个方向上各扩展 1 个点的距离，切边效果更好。
- `--resolution=dpi` 可以设置 PS 文件的精度；默认效果应该足够了；
- 如果有其他需求，可以参考 ps2eps 的 [官方说明](http://www.tm.uka.de/~bless/ps2eps)

也可以不使用 `ps2eps`，而直接使用 `convert` 命令，`convert` 默认的切边效果非常好，但是默认精度
比较低，需要自己调高。

## GMT 与 LaTeX 的合并

代码如下：

``` bash
#!/bin/bash
PS=gmt-latex.ps
gmt pstext -JX15c/7c -R0/10/0/5 -Bx2 -By1 -B+t"Equation of motion" -F+f15p -K > $PS <<EOF
5 4.5 Equation Start.
EOF

gmt psimage equation.eps -D6c/4c+w5c -K -O >> $PS
gmt psimage equation.eps -D6c/2c+w3c -K -O >> $PS

gmt pstext -J -R -F+f15p -O >> $PS <<EOF
5 0.5 Equation End
EOF
```

其实本质上就是利用 `psimage` 命令将 EPS 文件嵌入到当前 PS 文件中。详情见 `psimage` 的语法。

由于 GMT 包含了非 GMT 的PS代码，所以无法使用 `psconvert` 命令进行转换。因而需要使用
`convert` 命令，转换命令如下:

    $ convert -trim -density 300 -rotate 90 gmt-latex.ps gmt-latex.png

效果如下：

![](/images/2013102401.png)

## 其他一些需要说明的地方

1.  从本质上来说，这个技巧利用了 `psimage` 命令，直接将 EPS 文件的代码嵌入到新的 PS
    文件中，因而基本上只要是 EPS 文件都可以这么做。利用这一点可以做很多事情，
    比如 GMT 的箭头比较难看，可以用 LaTeX 的 TikZ 包来生成好看的箭头，然后再导入进去。
2.  用 latex 将 tex 编译成 dvi，再转换为 ps 文件是一种比较老的 latex 编译方式；也是这里
    推荐的编译方式。
3.  现在更流行的是编译方式是直接用 pdflatex 或者 xelatex 生成 pdf 文件。但是这里需要
    eps 文件，所以需要调用 pdf2ps 转换为 ps 再转换为 eps，pdflatex 生成的 pdf 效果很好，
    但是再生成 ps 文件清晰度会降低很多。因而最好还是用比较古老的编译方式吧。
4.  这个方法或许也可以用来在 GMT 上写中文。目前对中文支持最好的应该是 xelatex 了，
    其好像只能生成 pdf，转换为 ps 后精度必然不够。一个解决办法是写足够大的字，转换之后
    用 psimage 缩小到需要的尺寸，这样或许精度上看上去效果更好。另一个办法是查一查 pdf
    到 ps 转换有没有高精度的实现方法。不过 GMT 的中文问题还是用 [Linux 下的 GMT 中文显示](/gmt-chinese-under-linux.html) 的方法更好。
