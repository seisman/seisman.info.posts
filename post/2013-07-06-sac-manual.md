---
title: SAC 参考手册中文版
date: 2013-07-06
lastmod: 2016-01-09
author: SeisMan
categories:
  - SAC
tags:
  - 书籍
  - PDF
slug: sac-manual
---

- 网页版： https://seisman.github.io/SAC_Docs_zh/
- PDF版： https://seisman.github.io/SAC_Docs_zh/SAC_Docs.pdf

## 2018-03-21 v3.6

下载地址：[SAC 参考手册 v3.6.pdf](http://seisman.qiniudn.com/SAC/sac-manual-v3.6.pdf)

- 新增内容：调用SAC库中的 `rms` 子函数
- 新增示例： `cut`

## 2016-01-09 v3.5 版

下载地址：[SAC 参考手册 v3.5.pdf](http://seisman.qiniudn.com/SAC/sac-manual-v3.5.pdf)

-   增加示例：绘制滤波器的时间响应和频率响应
-   增加示例：一次性修改多个波形数据的发震时刻
-   新增章节： `rdseed` 的选项及其用法
-   新增章节：介绍 IRIS 等地震数据中心
-   新增章节：介绍数据申请：连续波形数据和事件波形数据
-   新增章节：IRIS 波形数据申请工具
-   新增章节：SAC 与脚本运行速度差异导致的陷阱
-   新增 Perl 脚本：数据提取、合并、重命名、修改发震时刻、去仪器响应、分量旋转、重采样
-   新增 Python 脚本：数据提取、合并、重命名、修改发震时刻、去仪器响应、分量旋转、重采样
-   更新命令说明： `plotpk` 、 `plot1` 、 `plot2` 、 `datagen`
-   新增命令： `writecss`
-   修正 Bugs 和 Typos

## 2015-09-15 v3.4 版

下载地址：[SAC 参考手册 v3.4.pdf](http://seisman.qiniudn.com/SAC/sac-manual-v3.4.pdf)

-   调整与修订：
    -   将命令的 “错误消息” 和 “警告消息” 集中整理到附录中
    -   将文件重命名脚本移动到 “在脚本中调用 SAC” 一章
    -   重新整理了 “震相拾取” 一节的内容
-   新增内容：
    -   在 Mac OS X 10.10 中安装 SAC
    -   在 C 程序中调用 SAC 提供的 `distaz` 函数
    -   数据处理中使用 `decimate` 和 `interpolate` 进行数据重采样
    -   Python 中修改发震时刻
    -   在 C 程序中读写 SAC 文件
    -   在 Fortran 程序中读写 SAC 文件
    -   在 Python 脚本中读写 SAC 文件
    -   在 matlab 中读写 SAC 文件
    -   修改 SAC 所能读取的文件数目的上限
    -   文档维护与更新并征集维护者
-   命令整理： `mtw` 、 `markptp` 、 `markvalue` 、 `readcss`
-   修正 Bugs 和 Typos

## 2015-06-06 v3.3 版

下载地址：[SAC 参考手册 v3.3.pdf](http://seisman.qiniudn.com/SAC/sac-manual-v3.3.pdf)

-   修正 bugs 和 typos；
-   命令整理： `hilbert` 、 `transfer`
-   新增内容：
    -   四个文件重命名脚本
    -   读取某个目录下全部文件遇到的问题
    -   使用 Tab 遇到的问题
    -   数据命名规则
    -   时区校正
    -   错误与警告消息
    -   未定义变量
    -   SAC debug
    -   `wh` 与 `w over` 的区别

## 2015-05-02 v3.2 版

下载地址：[SAC 参考手册 v3.2.pdf](http://seisman.qiniudn.com/SAC/sac-manual-v3.2.pdf)

-   修复 bugs 和 typos；
-   整理命令 `systemcommand`、`transfer`
-   新增内容：
    -  波形排序
    - 标记震相理论走时的三种方法
    - 图像格式转换
    - SAC 初始化宏文件
    - SAC 命令的长度上限
    - 字节序
-   新增附录 “仪器响应”，整理了 “去仪器响应” 一节
-   新增示例：调用 SAC 的 Hilbert 函数

## 2014-09-25 v3.1 版

下载地址：[SAC 参考手册 v3.1.pdf](http://seisman.qiniudn.com/SAC/sac-manual-v3.1.pdf)

- 重新整理了大部分命令的语法说明；
- 对 “SAC 图像” 一章进行了修订；
- 新增 “信号迭加子程序” 和 “谱估计子程序” 一章
- 新增 “在 Python 中调用 SAC” 一节；
- Bug 修订；

## 2014-04-18 v3.0 版

下载地址：[SAC 参考手册 v3.0.pdf](http://seisman.qiniudn.com/SAC/sac-manual-v3.0.pdf)

- 重新设计了整个文档的结构
- 重写了教程部分的大多数内容
- 教程部分根据 SAC v101.6a 进行修正
- Bug 修订

## 2014-02-22 v2.3 版

下载地址：[SAC 帮助文档中文版 v2.3.pdf](http://seisman.qiniudn.com/SAC/sac-manual-v2.3.pdf)

- 使用 Git 管理源码
- 整理结构和布局的修改
- 新的小节: “SAC IO 升级版”、“黑板变量的读写”、“SAC 保存图像”
- Bug 修订

## 2013-04-12 v2.2 版

下载地址：[SAC 帮助文档中文版 v2.2.pdf](http://seisman.qiniudn.com/SAC/sac-manual-v2.2.pdf)

命令已经整理完毕，排版上基本已经没有问题了，重新设计了封面，在接下来很长一段时间应该都不会有大的改动了。
如果有时间，会加一些 SAC 其他方面的东西。如果有读者反馈，命令方面也可能会有更新。

## 2013-04-06 v2.1 版

下载地址：[SAC 帮助文档中文版 v2.1.pdf](http://seisman.qiniudn.com/SAC/sac-manual-v2.1.pdf)

重新细致整理了手册的第一章，基本达到了我认为可以打印的地步。命令部分还没有整，200 多个，需要很长一段时间才能出来。

## 2013-03-29 v2.0 版

下载地址：[SAC 帮助文档中文版 v2.0.pdf](http://seisman.qiniudn.com/SAC/sac-manual-v2.0.pdf)

花了两天的时间重新制作了整个文档，内容及排版部分有很多 bug，草草结束是因为接下来的一段时间要好好干活了，
先把 v2.0 的细节总结如下：

- 操作系统：CentOS 6.4 (Final)
- 编译环境：TeX Live 2012
- 编译命令：xeLaTeX
- 中文实现：CTEX 宏包
- 中文字体：宋体 + 黑体
- 英文主字体：Liberation Sans
- 代码字体：Courier 10 Pitch

## 2012-09-18 v1.2 版

下载地址：[SAC 帮助文档中文版 v1.2.pdf](http://seisman.qiniudn.com/SAC/sac-manual-v1.2.pdf) [SAC 帮助文档中文版 v1.2.doc](http://seisman.qiniudn.com/SAC/sac-manual-v1.2.doc)

- 增加了封面配图。

## 2012-09-03 v1.1 版

下载地址：[SAC 帮助文档中文版 v1.1.pdf](http://seisman.qiniudn.com/SAC/sac-manual-v1.1.pdf) [SAC 帮助文档中文版 v1.1.doc](http://seisman.qiniudn.com/SAC/sac-manual-v1.1.doc)

- 重新格式化整个文档，使得其看上去更规范，也易于以后的修改
- 文档中的所有 C 或 Fortran 代码从 notepad++ 中直接导出，代码支持语法高亮
- 代码及正文英文字体采用 Consolas 字体。
- 增加了 “在脚本中调用 SAC” 一节；
- 新增了 `transfer`、`traveltime`、`saveimg`、`datagen` 命令（依赖于 SAC v101.5c）；
- 公式用公式编辑器编辑

## 2012-01-08 v1.0 版

下载地址：[SAC 帮助文档中文版 v1.0.pdf](http://seisman.qiniudn.com/SAC/sac-manual-v1.0.pdf)  [SAC 帮助文档中文版 v1.0.doc](http://seisman.qiniudn.com/SAC/sac-manual-v1.0.doc)

- 参考《数字地震波形分析》一书，翻译了大部分的用户指南以及几乎全部的命令
- 结合了 SAC v101.4 增加、删除和修改了一些命令
- 增加书签，方便定位，支持全文搜索
