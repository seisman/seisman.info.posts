---
title: Linux 下安装 NVIDIA 显卡驱动
date: 2014-07-13
lastmod: 2014-12-01
author: SeisMan
categories:
  - Linux
tags:
  - CentOS
slug: install-nvidia-drivers-under-linux
---

大部分 Linux 发行版都使用开源的显卡驱动 nouveau，对于 nvidia 显卡来说，还是闭源的官方驱动的效果更好。最明显的一点是，在使用 SAC 拾取震相的时候，使用官方显卡驱动在刷新界面的时候要快很多。

对于 CentOS 用户而言，有两种安装 NVIDIA 显卡驱动的方法，从 ELRepo 源中安装或从源码编译驱动。对于一般的 CentOS 用户，建议使用第一种方法。

<!--more-->

## 从 ELRepo 源中安装驱动

ELRepo 源中包含了一系列驱动程序。

1.  添加 ELRepo 源:

        sudo rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
        sudo rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-3.el7.elrepo.noarch.rpm

如果安装无报错，但是实际无法使用，可以尝试重新安装:

       sudo yum reinstall https://www.elrepo.org/elrepo-release-7.0-3.el7.elrepo.noarch.rpm

2.  安装显卡检查程序:

        sudo yum install nvidia-detect

3.  检测显卡型号，并选择对应的驱动:

        $ nvidia-detect -v
        Probing for supported NVIDIA devices...
        [10de:06dd] NVIDIA Corporation GF100GL [Quadro 4000]
        This device requires the current 346.47 NVIDIA driver kmod-nvidia

    根据 `nvidia-detect` 的输出信息，可以知道显卡的型号，以及要使用的驱动版本 `346.47` 。

4.  安装显卡驱动

    1.  对于大多数比较新的显卡来说，直接安装最新版的驱动即可:

            sudo yum install nvidia-x11-drv nvidia-x11-drv-32bit
    
    2.  若驱动版本为 304.xx，则安装 304xx 版本:

            sudo yum install nvidia-x11-drv-304xx nvidia-x11-drv-304xx-32bit

    3.  若驱动版本为 340.xx，则安装 340xx 版本:

            sudo yum install nvidia-x11-drv-340xx nvidia-x11-drv-340xx-32bit

5.  安装过程中可能会给出软件冲突的警告，需要卸载以下软件包及其依赖:

        sudo yum remove xorg-x11-glamor

6.  重启

## 手动编译显卡驱动

### 准备工作

1.  查看显卡型号

        $ lspci | grep VGA
        03:00.0 VGA compatible controller: NVIDIA Corporation GF100GL [Quadro 4000] (rev a1)

    从这里可以得出显卡型号为 Quadro 4000。

2.  驱动下载

    下载地址为： <http://www.nvidia.com/Download/index.aspx?lang=en-us>

### 安装显卡驱动

1.  安装 `kernel-devel`

        sudo yum install kernel-devel

2.  将 `nouveau` 驱动加入黑名单，在 `/etc/modprobe.d/blacklist.conf`
    （CentOS 7 下为 `/usr/lib/modprobe.d/dist-blacklist.conf` ）中加入 `blacklist nouveau`

3.  备份 `initramfs` 文件

        sudo mv /boot/initramfs-$(uname -r).img /boot/initramfs-$(uname -r).img.bak

4.  重建 `initramfs` 文件

        sudo dracut -v /boot/initramfs-$(uname -r).img $(uname -r)

5.  关机重启。由于此时 `nouveau` 驱动已经被禁用，桌面的显示效果非常差。
6.  进入文本界面

        sudo init 3

    会直接进入文本界面。

7.  在文本界面登录后直接安装

        sh NVIDIAxxx --kernel-source-path=/usr/src/kernels/x.xx.x-xxxxx

    其中 `NVIDIAxxx` 为 nvidia 驱动脚本文件， `x.xx.x-xxxx` 为 kernel 版本号。

### 更新 kernel 后重装驱动

手动编译显卡驱动的一个麻烦之处在于，每次更新 kernel 之后，都会出现无法进入图形界面的情况，此时需要重新安装显卡驱动。

1.  更新 kernel，重启，发现无法进入图形界面；
2.  按下 `Alt+F2` ，进入文本界面，以 root 身份登陆；
3.  备份 `initramfs` 文件
4.  重建 `initramfs` 文件
5.  重启，按下 `Alt+F2` ，进入文本界面，以 root 身份登陆；
6.  执行第七步；再重启；

### 卸载显卡驱动

    sh ./NVIDIA-Linux-xxxxx --uninstall

## 更新历史

-   2014-07-13：初稿；
-   2014-11-01：加入了更新 kernel 之后的操作；
-   2014-12-01：添加 “从 ELRepo 源中安装显卡驱动” 一节，且不建议手动编译驱动；
