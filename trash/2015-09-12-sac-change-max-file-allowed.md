---
title: 修改 SAC 所允许的最大文件数目
date: 2015-09-12
author: SeisMan
categories:
  - SAC
tags:
  - SAC技巧
slug: sac-change-max-file-allowed
---

SAC 在处理数据时，一次性最多只能读入 1000 个 SAC 文件。当读入过多的 SAC 文件时，会出现如下警告:

    Max files: reading first 1000  files.

并只读入文件列表中的前 1000 个文件。

想要突破最多只能读 1000 个文件的上限，就需要修改 SAC 的源代码。

最大文件数目由源码 `sac/inc/mach.h` 中的宏变量 `MDFL` 控制。将其中的:

    #define MDFL    1000

改成:

    #define MDFL    10000

即可将最大文件数目修改成 10000。

修改之后，重新编译安装即可。

简单测试了一下，修改后的确可以读取超过 1000 个文件，基本的数据处理命令也没有问题，但尚不确定是否有其他副作用。
