---
title: 将博文以 PDF 格式导出
date: 2014-09-14
author: SeisMan
categories: 胡言乱语
tags: [博客, PDF, Pandoc]
---

在每篇博文的标题下方最右侧，有一个 PDF 的图标，点击即可下载当前博文的 PDF 版本。

对于每篇博文，利用 [pandoc](http://johnmacfarlane.net/pandoc/) 将 markdown 格式的
源码转换为 PDF 格式，并将其上传到七牛云中，供读者下载。

<!--more-->

转换过程中的一些细节如下：

- 利用 Pandoc 实现从 markdown 源码到 PDF 的转换
- 转换脚本为 [makepdf.py](https://github.com/seisman/seisman.info.posts/blob/master/makepdf.py)
- 转换为 PDF 时使用了 xelatex，其中 LaTeX 模板为 [seisman.latex](https://github.com/seisman/seisman.info.posts/blob/master/seisman.latex)
- 由于 markdown 文件中的图片和链接都是相对链接，因而利用 pandoc 的 filter 功能对
  markdown 文件做进一步处理，filter 脚本位于 [markdown-filter.py](https://github.com/seisman/seisman.info.posts/blob/master/markdown-filter.py)

注意事项：

- 生成的 PDF 仅供读者离线阅读使用，请勿用作其他用途；
- PDF 版直接由网页版转换得到，我没有人工检查 PDF 版的效果，若有影响阅读效果的地方，
  可以告诉我，我尽量保证网页版和 PDF 版同时有比较好的效果；
- 请勿批量下载本博客的 PDF，流量也是要花钱的。如果需要本博客的全部 PDF，我可以打包发给你；
- 目前设置了只能通过点击本博客的链接来下载 PDF，直接把 PDF 的链接粘贴到浏览器中下载
  会被拒绝，这样做的主要原因是为了防盗链；

总的来说，生成的 PDF 效果还是不错的。其中还有一些不够理想的细节，会在将来不断改进。

待解决的问题：

- 目录与正文之间的分界不够明显
- 若单行代码过长，网页显示时可以使用水平滚动条，PDF 显示时则会将一行代码分两行或多行显示，
  稍稍影响阅读效果；个别过长的行在显示时会超过纸张边界；
- 部分公式太麻烦，直接使用的截图，在 PDF 中效果较差
- 部分 URL 没有以链接的形式显示
- 图片不能为 GIF 格式，否则无法生成 PDF
- 无法指定 PDF 中的图片尺寸

