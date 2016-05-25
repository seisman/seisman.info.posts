---
title: 博客现已支持全文 PDF 导出
date: 2014-09-14
author: SeisMan
categories: 胡言乱语
tags: [博客, PDF, Pandoc]
---

近几日对博客进行了一些调整，加入了 PDF 全文输出的功能。在每篇博文的右侧，都会有 “**Features**” 一项，点击下面的 PDF 图标，即可将当前博文以 PDF 格式导出。

好吧，被你识破了。所谓的 PDF 导出，实际上是我自己将每篇博文转换为 PDF 并上传到服务器，供读者点击下载。

<!--more-->

转换过程中的一些细节如下：

-   利用 [Pandoc](http://johnmacfarlane.net/pandoc/) 实现从 rST 源码到 PDF 的转换
-   之所以采用 Pandoc 而不是 rst2pdf 是因为 rst2pdf 的安装一直有问题
-   转换脚本为 [makepdf.py](https://github.com/seisman/seisman.info/blob/master/makepdf.py)
-   转换为 PDF 时使用了 xelatex，其中 LaTeX 模板为 [seisman.latex](https://github.com/seisman/seisman.info/blob/master/seisman.latex)
-   只转换博文，不转换其他页面
-   自动更新，保证 PDF 与博文内容的一致性

注意事项：

-   生成的 PDF 仅供读者离线阅读使用，请勿用作其他用途；
-   PDF 版直接由网页版转换得到，我没有人工检查 PDF 版的效果，若有影响阅读效果的地方，可以告诉我，我尽量保证网页版和 PDF 版同时有比较好的效果；
-   请勿批量下载本博客的 PDF，流量也是要花钱的。如果需要本博客的全部 PDF，我可以打包发给你；
-   目前设置了只能通过点击本博客的链接来下载 PDF，直接把 PDF 的链接粘贴到浏览器中下载会被拒绝，这样做的主要原因是为了防盗链；

总的来说，生成的 PDF 效果还是不错的。其中还有一些不够理想的细节，会在将来不断改进。

待解决的问题：

-   目录与正文之间的分界不够明显
-   若单行代码过长，网页显示时可以使用水平滚动条，PDF 显示时则会将一行代码分两行或多行显示，稍稍影响阅读效果；个别过长的行在显示时会超过纸张边界；
-   部分公式太麻烦，直接使用的截图，在 PDF 中效果较差
-   部分 URL 没有以链接的形式显示
-   图片不能为 GIF 格式，否则无法生成 PDF
-   无法指定 PDF 中的图片尺寸
-   无法处理 `list-table`
-   段首未缩进

