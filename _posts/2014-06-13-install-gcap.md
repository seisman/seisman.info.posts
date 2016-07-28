---
title: gCAP 和 gCAP3D 的安装
author: SeisMan
date: 2014-06-13
updated: 2016-04-07
categories: 地震学软件
tags: 震源机制解
---

gCAP 是 Prof. Lupei Zhu 发展的一种反演震源机制解的一种方法。目前该代码已经开源。

gCAP3D 是在 gCAP 的基础上修改得到的，与 gCAP 的区别在于其可以使用三维格林函数。
该代码也已经开源。

gCAP 和 gCAP3D 之间没有本质区别，本文的介绍以 gCAP 为准，在最后会介绍安装方法上
gCAP3D 与 gCAP 的不同。

<!--more-->

## gCAP 安装步骤

1.  下载 gCAP 源码： <http://www.eas.slu.edu/People/LZhu/downloads/gcap1.0.tar>
2.  解压:

        tar -xvf gcap1.0.tar

3.  清理垃圾文件

    软件包在发布的时候，没有做一些清理，遗留了一些没有用的临时文件，看起来很碍眼:

        rm junk.ps junk.out .gmtcommands

4.  下载辅助代码

    gCAP 使用了 Numerical Recipes（简称 NR）中的一些函数，包括 `matrix` 、
    `free_matrix` 、 `free_convert_matrix` 、 `jacobi` 、 `eigsrt` 。
    由于 NR 是非开源非免费的软件，所以 gCAP 并没有将 NR 相关的代码放在包里。

    网络上可以下载到 NR 的完整代码，这里仅给出 gCAP 所需的部分（注：此处存在版权问题！）。
    下载该压缩包，解压，并将解压后的源代码放到 gCAP 的目录中。

    gCAP_util 下载：[gcap_utils.tar.gz](http://seisman.qiniudn.com/downloads/gcap_utils.tar.gz)

5.  新的 Makefile

    软件包自带的 Makefile 无法使用，因而对其进行了一些修改。修改幅度稍大，几乎算是重写了。

    新 Makefile 下载地址：[Makefile.gCAP](http://seisman.qiniudn.com/downloads/Makefile.gCAP)

    下载之后，将其重命名为 Makefile，替换原目录中的同名文件，并根据自身情况修改 Makefile 文件中的
    变量 `SACHOME` 、 `FC` 、`CC` 。

6.  编译:

        make

7.  修改环境变量

    要想在终端运行 gcap，需要系统能够正确找到二进制文件 `cap` 、`cap_dir` 、
    `mtdcmp` 、 `radpttn` 以及脚本文件 `cap.pl` 和 `depth.pl`。
    
    直接将 gcap 的源码路径加入到 PATH 环境变量中，即在 `~/.bashrc` 中加入类似如下语句:

        export PATH=/path/to/gcap:${PATH}

8.  修改绝对路径

    `cap.pl` 中第 15 行与第 19 行包含了两个绝对路径，分别包含了绘图脚本
    `cap_plt.pl` 和 Green 函数库 `Glib` 的路径，需要根据自身情况修改。

9.  运行

    直接执行:

        $ cap.pl

    就会出现软件的用法说明。

    软件包中自带了一个示例数据，因而可以通过如下命令来尝试运行:

        $ cap.pl -H0.2 -P0.3 -S2/5/0 -T35/70 -F -D2/1/0.5 -C0.05/0.3/0.02/0.1 -W1 -X10 -Mcus_15/5.0 20080418093700

    更多用法见软件的用法说明。

    需要注意：直接运行二进制文件 `cap` 时会出现段错误:

        $ cap
        [1]    12763 segmentation fault  cap

    看看源码 `cap.c` 即可知道为何会出现这个错误。只要记住，直接使用 `cap.pl` 即可，不要直接使用 `cap`

10. 对 `cap_plt.pl` 的微小修改

    完全使用默认的脚本运行并绘图后，可能会发现整个图片都缩在图片的左下角的一个小区域
    内，与文章中的图片相比有较大差别。出现这个错误的主要原因是，Prof. Zhu 的 GMT 默认
    使用了 US 单位制，脚本中所有未显式指定单位的值使用的都是 inch，而其他人通常使用的都
    是 SI 单位制，会将这些未显式指定单位的值使用默认单位 cm。

    解决办法是，在 `cap_plt.pl` 的第 6 行之后加上如下语句:

        system "gmtset MEASURE_UNIT inch";
        system "gmtset PAGE_ORIENTATION portrait";

    这两句的作用是设置默认单位为英寸，并设置纸张方向为 portrait 模式。

## gCAP3D 安装步骤

gCAP3D 的安装与 gCAP 的步骤几乎完全相同（部分文件名以及行号可能不一致，读者自行判断），区别列出如下：

-   下载地址： <http://www.eas.slu.edu/People/LZhu/downloads/gCAP3D1.0.tar>
-   Makefile 下载地址： <http://seisman.qiniudn.com/downloads/Makefile.gCAP3D>

## 修订历史

-   2014-06-13：初稿；
-   2016-03-12：加入了对 gCAP3D 的说明；
-   2016-04-07：微调文章结构，加入了对段错误的说明；
