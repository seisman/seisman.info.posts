---
title: '强大的跨平台 PDF 处理工具：cpdf'
author: SeisMan
date: 2015-01-27
categories: Linux
tags:  [PDF, Linux, Windows]
---

日常生活中对 PDF 的最基本的操作大概就是合并和切割了。之前一直在用强大的 PDFtk，但是由于一些底层依赖的问题，PDFtk 在短时间内是不可能出现在 CentOS7 下了，只能寻找新的 PDF 替代工具了。

<!--more-->

## 简介

Coherent PDF，简称 cpdf，是个用于处理 PDF 的命令行工具。该软件支持 Windows、Linux 和 Mac，且对于非商业用途是免费的。

主页： <http://community.coherentpdf.com/>

## Linux 的安装

下载地址： [cpdf](https://github.com/coherentgraphics/cpdf-binaries/archive/master.zip)

cpdf 有预编译的二进制文件，直接下载解压，然后把自己的平台对应的二进制文件复制到 PATH 中即可使用。

## 常见用法

PDF 合并:

    cpdf input1.pdf input2.pdf -o output.pdf

切割 PDF 中的 1 至 3 页以及 12 页至最后页:

    cpdf input.pdf 1-3,12-end -o output.pdf

将 PDF 分割成单页 PDF，编号为 `page001.pdf` 、 `page002.pdf` :

    cpdf -split in.pdf -o page%%%.pdf
