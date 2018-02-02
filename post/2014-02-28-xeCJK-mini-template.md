---
title: 使用 xeCJK 解决中文问题的最小模板
date: 2014-02-28
lastmod: 2015-03-23
author: SeisMan
categories:
  - 编程
tags:
  - LaTeX
  - 中文
slug: xeCJK-mini-template
---

LaTeX 的中文支持一直是个问题，11 年左右刚开始学习 LaTeX 的时候，那时的中文解决
办法是 CJK 宏包。到了 12 年或 13 年的时候，再接触 LaTeX 的时候，LaTeX 中文支持的最优
解决办法变成了 `xeLaTeX+xeCJK` ，这大概是目前为止最优的中文解决方案。

后来，CTEX 学会将 xeCJK 的功能进行打包，发布了 ctex 宏包，进一步简化了用 LaTeX
写中文文档的问题。

<!--more-->

下面是利用 `xeLaTeX` 和 `xeCJK` 实现中文支持的最小模板:

``` latex
\documentclass{article}
\usepackage{xeCJK}
\begin{document}
中文 English 混合示例。
\end{document}
```

相对于英文的最小 LaTeX 模板来说多了两句:

    \usepackage{xeCJK}

xeCJK 会自动使用 TeXLive 自带的 Fandole 字体。想要该模板能够编译通过，需要将
TeXLive 自带的中文字体安装到系统中，最简单的办法是在 `~/.fonts` 目录下建一个软链接:

    ln -s /opt/texlive/2014/texmf-dist/fonts/opentype/public/fandol ~/.fonts/

用如下命令编译:

    xelatex test.tex
