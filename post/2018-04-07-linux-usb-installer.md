---
title: 制作 Linux USB 安装镜像
author: 王亮
date: 2018-04-07
tags:
  - linux
  - macOS
slug: linux-usb-installer
---

在下载 Linux ISO 镜像文件后，还需要制作 USB 启动盘方能安装。在不同的操作系统，制作所用的工具、过程不同。

## macOS 下制作 USB 安装镜像

1.  将安装文件转换成 dmg 格式：

    ```bash
    $ cd Downloads/
    $ hdiutil convert -format UDRW -o centos.dmg CentOS-7-x86_64-LiveGNOME-1708.iso
    ```

2.  确定 U 盘盘符：

    插入 U 盘，执行如下命令：

    ```bash
    $ diskutil list
    ```

    通常最后一个盘符是 U 盘，请根据磁盘大小确认哪一个是 U 盘。如果觉得没有把握，可以使用
    磁盘工具来辅助判断。如果找错盘符，后续可能会导致其他盘数据丢失。

3.  卸载 U 盘：

    使用如下命令卸载 U 盘，但不要拔出。也不要使用图形界面推出 U 盘。

    ```bash
    $ diskutil unmountDisk /dev/disk2  # 根据自己的实际情况修改 /dev/disk2
    Unmount of all volumes on disk2 was successful
    ```

4.  将镜像写入 U 盘

    ```bash
    sudo dd if=./centos.dmg of=/dev/rdisk2 bs=1m
    ```

    这里的盘符千万别写错。如果正常，这里需要等一小会，完成后就可以在 Finder 推出 U 盘了。

## Windows 下制作 USB 安装镜像

Windows 下制作 USB 安装镜像可以使用 [Universal USB installer](http://www.pendrivelinux.com/universal-usb-installer-easy-as-1-2-3/)，
点击鼠标执行即可。
