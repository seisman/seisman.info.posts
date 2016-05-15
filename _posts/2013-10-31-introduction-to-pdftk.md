---
title: PDF 合并和分割工具 --PDFtk
date: 2013-10-31
author: SeisMan
categories: Linux
tags: [用法, PDF]
---

## 简介

PDFtk 是什么？我觉得官网的一句话解释得很好。

> If PDF is electronic paper, then PDFtk is an electronic
> staple-remover, hole-punch, binder, secret-decoder-ring, and
> X-Ray-glasses. PDFtk is a simple tool for doing everyday things with
> PDF documents.

其官方网站为： <http://www.pdflabs.com/tools/pdftk-the-pdf-toolkit>

PDFtk 目前分为三个版本：

-   PDFtk Server：命令行工具。支持 windows、Linux、Mac。
-   PDFtk Free：图形界面基础免费版；仅限 windows 用户；功能仅限于 PDF 合并和分割；
-   PDFtk Pro：图形界面专业收费版；仅限 windows 用户，可以对 PDF 文档进行合并、分割、旋转、加水印、加邮戳、加密。

对于 Linux 用户，唯一的选择是免费的 PDFtk Server，其功能与收费 PDFtk Pro 完全相同，只是没有 GUI 而已。作者还是很厚道的。

Linux 的各个发行版的官方源中基本都有该软件，直接 `apt-get` 或者 `yum` 安装即可。

## 功能

-   合并 PDF；
-   分割 PDF 页面；
-   旋转 PDF 文档或页面；
-   PDF 解密；（不是破解）
-   PDF 加密；
-   用 X/FDF 填写 PDF 表格；
-   从 PDF 表格中生成 PDF Data Stencils；
-   加背景水印或前景印章；
-   报告 PDF Metrics，书签和元数据；
-   增加 / 更新 PDF 书签或元数据；
-   给 PDF 页面或文档加附件；
-   解压 PDF 附件；
-   分解 PDF 文档为多个单页；
-   解压缩和重压缩页面流；
-   修复受损的 PDF 文档；

这功能完全可以与 Adobe Acrobat 相媲美了，更重要的是 PDFtk 支持 Linux 且完全免费。（个人用户免费，若用于商业用途需付费）。

## 用法示例

具体选项看这里： <http://www.pdflabs.com/docs/pdftk-man-page/>

下面给出一些常见的例子。[例子原文](http://www.pdflabs.com/docs/pdftk-cli-examples/)

扫描一本书，odd.pdf 为书的全部奇数页，even.pdf 为书的全部偶数页，下面的命令可以将两个 pdf 合并成页码正常的书:

    pdftk A=odd.pdf B=even.pdf shuffle A B output collated.pdf

如果 odd.pdf 是逆序的:

    pdftk A=odd.pdf B=even.pdf shuffle Aend-1 B output collated.pdf

加密 PDF:

    pdftk secured.pdf input_pw foopass output unsecured.pdf

PDF 128 位加密，保留全部权限:

    pdftk 1.pdf output 1.128.pdf owner_pw foopass

PDF 128 位加密，保留全部权限，打开文档需输入密码 "baz":

    pdftk 1.pdf output 1.128.pdf owner_pw foo user_pw baz

PDF 128 位加密，打开文档需输入密码 "baz"，保留打印之外的其他权限:

    pdftk 1.pdf output 1.128.pdf owner_pw foo user_pw baz allow printing

合并 in1.pdf 和 in2.pdf 到新 PDF 中:

    pdftk in1.pdf in2.pdf cat output out1.pdf

或（使用句柄）:

    pdftk A=in1.pdf B=in2.pdf cat A B output out1.pdf

或（使用通配符）:

    pdftk *.pdf cat output combined.pdf

去除 in1.pdf 中的第 13 页，并创建 out1.pdf:

    pdftk in.pdf cat 1-12 14-end output out1.pdf

或

    pdftk A=in1.pdf cat A1-12 A14-end output out1.pdf

对输出进行 40 位加密，撤销所有权限，设置 owner 密码为 foopass:

    pdftk 1.pdf 2.pdf cat output 3.pdf encrypt_40bit owner_pw foopass

合并两个文件，其中一个需要被加密。对输出不加密:

    pdftk A=secured.pdf 2.pdf input_pw A=foopass cat output 3.pdf

解压 PDF 页面流，然后就可以在文本编辑器中编辑 PDF 文件:

    pdftk doc.pdf output doc.unc.pdf uncompress

压缩 PDF:

    pdftk mydoc.pdf output mydoc.clear.pdf compress

修复破损的 PDF:

    pdftk broken.pdf output fixed.pdf

将一个 PDF 文档分割成一页一个文档:

    pdftk in.pdf burst

将一个 PDF 文档分割成一页一个文档，并加密，允许低质量的打印:

    pdftk in.pdf burst owner_pw foopass allow DegradedPrinting

获取 PDF 问的元数据和书签信息:

    pdftk in.pdf dump_data output report.txt

将 PDF 第一页顺时针旋转 90 度:

    pdftk in.pdf cat 1east 2-end output out.pdf

将整个 PDF 文档旋转 180 度:

    pdftk in.pdf cat 1-endsouth output out.pdf
