---
title: Linux 下合并 PDF
author: SeisMan
date: 2014-09-18
updated: 2015-01-27
categories: Linux
tags: [PDF, Linux]
---

经常需要将多个 PDF 合并为一个文件，这里收集了网上给出的一些方案，并总结一下。

**推荐使用cpdf**

<!--more-->

## cpdf

[cpdf](http://community.coherentpdf.com/) 全称是 Coherent PDF Command Line
Tools，是一个强大的 PDF 处理工具。PDF 合并只是它的一个功能之一。

    cpdf input1.pdf input2.pdf -o output.pdf

## pdfunite

`pdfunite` 是 [Poppler](http://poppler.freedesktop.org) 提供的一个工具，一般系统都已经安装了 Poppler，所以这个工具在 Linux 下是很常见的。

    pdfunite input1.pdf input2.pdf input3.pdf output.pdf

该命令用法简单，没有多余的选项，需要注意的是该命令的最后一个 PDF 文件为输出文件名。

## pdfjam

如果你安装了 TeXLive，并且安装了 [pdfpage](http://www.ctan.org/tex-archive/macros/latex/contrib/pdfpages/) 包，则其中包含了 `pdfjam` 工具。

    pdfjam input1.pdf input2.pdf input3.pdf -o output.pdf

该命令的选项很多，可以通过 `pdfjam --help` 查看。

`pdfjoin` 是 `pdfjam` 的一个封装，也可以直接使用:

    pdfjoin a.pdf b.pdf

## pdftk

[pdftk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/) 是专门用于处理 PDF 文档的一套工具。在大多数发行版中都可以直接安装使用。

    pdftk input1.pdf input2.pdf input3.pdf cat output output.pdf

pdftk 的选项很多，用法复杂，可以参考 [PDF 合并和分割工具—PDFtk](/introduction-to-pdftk.html)
。

## gs

[GhostScript](http://www.ghostscript.com) 不仅可以用于处理 PS，也可以用于处理 PDF 文档。

    gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=out.pdf in1.pdf in2.pdf

    gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress -sOutputFile=out.pdf in1.pdf in2.pdf

## 参考

- <https://blog.dbrgn.ch/2013/8/14/merge-multiple-pdfs/>
- <http://stackoverflow.com/questions/2507766/>

## 修订历史

-   2014-09-18：初稿；
-   2015-01-27：新增 cpdf；
