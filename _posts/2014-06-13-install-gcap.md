---
title: gCAP 的安装
author: SeisMan
date: 2014-06-13
updated: 2016-04-07
categories: 地震学软件
tags: 震源机制解
---

gCAP 是 Prof. Lupei Zhu 发展的一种反演震源机制解的一种方法。目前该代码已经开源。

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

8.  修改脚本 `cap.pl`

    `cap.pl` 中第 15 行与第 19 行包含了两个绝对路径，需要根据自身情况进行修改。

    -   第15行： `require "$home/Src/cap/cap_plt.pl";` 中的路径改成 `cap_plt.pl` 的绝对路径，类似于 `require "/path/to/gcap/cap_plt.pl"`
    -   第19行： `$green` 是自己计算的格林函数库的位置。如果你不知道如何修改的话，就直接用默认值，并使用命令 `mkdir ~/data/models/Glib` 新建这个目录。

9.  修改绘图脚本 `cap_plt.pl`

    使用默认的脚本运行并绘图后，可能会发现整个图片都缩在图片的左下角的一个小区域
    内，与示例中的图片相比有较大差别。出现这个错误的主要原因是，Prof. Zhu 的 GMT 默认
    使用了 US 单位制，脚本中所有未显式指定单位的值使用的都是 inch，而其他人通常使用的都
    是 SI 单位制，会将这些未显式指定单位的值使用默认单位 cm。

    解决办法是，在 `cap_plt.pl` 的第 6 行之后加上如下语句:

        system "gmtset MEASURE_UNIT inch";
        system "gmtset PAGE_ORIENTATION portrait";

    这两句的作用是设置默认单位为英寸，并设置纸张方向为 portrait 模式。

## 运行 gcap

在终端直接执行:

    $ cap.pl

就会出现软件的用法说明。

软件包中自带了一个示例数据，下面来复现一下这个示例。

### 用 fk 构建格林函数库

要运行 gcap，使用要使用 fk 建立格林函数库。如果你不知道 fk 是什么，请参考：

1. [安装fk](/fk-installation.html)
2. [fk 用法笔记](/fk-notes.html)

要建立格林函数库，首先需要一个模型文件。gcap 的示例使用的是一个名为 cus 的模型，由于 gcap
没有使用 cus 这个模型文件，所以这里使用的是 fk 自带的 hk 模型。

    # 切换到格林函数库所在目录
    $ cd ~/data/models/Glib
    # 为 hk 模型新建目录
    $ mkdir hk
    $ cd hk
    # 将 fk 自带的 hk 模型文件复制到当前目录下
    $ cp /path/to/fk/hk .
    # 用 fk 计算格林函数库
    $ fk.pl -Mhk/15/k -N512/0.2 -S2 05 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 105 110 115 120 125 130 135 140 145 150 155 160 165 170 175 180 185 190 195 200 205 210 215 220 225 230 235 240 245 250 255 260 265 270 275 280 285 290 295 300 305 310 315 320 325 330 335 340 345 350 355 360 365 370 375 380 385 390 395 400 405 410 415
    $ fk.pl -Mhk/15/k -N512/0.2 -S0 05 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 105 110 115 120 125 130 135 140 145 150 155 160 165 170 175 180 185 190 195 200 205 210 215 220 225 230 235 240 245 250 255 260 265 270 275 280 285 290 295 300 305 310 315 320 325 330 335 340 345 350 355 360 365 370 375 380 385 390 395 400 405 410 415

`-M` 选项中 15 代表震源深度是 15 km，你可以从 1 km 一直算到 40 km 甚至更深，此处只算了 15 km 以供示例使用。

### 运行 gcap 示例

    # 切换回 gcap 目录
    $ cd /path/to/gcap
    # 为了防止误操作，先将自带的示例备份一下
    $ cp -r 20080418093700 20080418093700.bak
    # 运行 gcap 示例
    $ cap.pl -H0.2 -P0.3 -S2/5/0 -T35/70 -F -D2/1/0.5 -C0.05/0.3/0.02/0.1 -W1 -X10 -Mhk_15/5.0 20080418093700

运行该示例所使用的参数来自于 `cap.pl` 命令的说明文档，请自行查阅以了解每个参数的含义。 `-Mhk_15/5.0` 选项表示使用 hk 模型、震源深度为 15 km处的格林函数。

执行完毕后，会生成 `hk_15.ps` 和 `hk_15.out`，将其与示例自带的 `cus_15.ps` 和 `cus_15.out`
对比可发现，二者基本完全一致。

## 关于段错误的说明

若直接运行二进制文件 `cap` 会出现段错误:

    $ cap
    [1]    12763 segmentation fault  cap

这是因为 `cap` 命令行中需要一个参数。记住，直接使用 `cap.pl` ，不要直接使用 `cap`。

## 关于 gCAP3D 的说明

gCAP3D 是在 gCAP 的基础上修改得到的，与 gCAP 的区别在于其可以使用三维格林函数。
该代码也已经开源。

gCAP 和 gCAP3D 之间没有本质区别，本文的介绍以 gCAP 为准，在最后会介绍安装方法上
gCAP3D 与 gCAP 的不同。

gCAP3D 的安装与 gCAP 的步骤几乎完全相同（部分文件名以及行号可能不一致，读者自行判断），区别列出如下：

-   下载地址： <http://www.eas.slu.edu/People/LZhu/downloads/gCAP3D1.0.tar>
-   Makefile 下载地址： <http://seisman.qiniudn.com/downloads/Makefile.gCAP3D>

## 修订历史

-   2014-06-13：初稿；
-   2016-03-12：加入了对 gCAP3D 的说明；
-   2016-04-07：微调文章结构，加入了对段错误的说明；
-   2016-07-31：完善了示例；
