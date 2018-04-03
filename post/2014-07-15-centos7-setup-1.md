---
title: CentOS 7 配置指南 — 安装篇
author: SeisMan
date: 2014-07-15
lastmod: 2018-04-07
slug: centos7-setup-1
---

本文介绍如何安装 CentOS 7 的最新版本，CentOS-1708，也就是 CentOS 7.4。

CentOS 7 的安装与其他 Linux 发行版的安装差不多，个别地方稍有不同。

## 准备工作

1.  下载安装镜像

    从[清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/)下载
    最新版的 CentOS 镜像，推荐下载 LiveGNOME 版本，即
    [CentOS-7-x86_64-LiveGNOME-1708.iso](https://mirrors.tuna.tsinghua.edu.cn/centos/7.4.1708/isos/x86_64/CentOS-7-x86_64-LiveGNOME-1708.iso)。

2.  制作 USB 安装镜像

    参考 [制作 Linux USB 安装镜像](/linux-usb-installer/)

## 计算机的启动设置

将 U 盘启动盘插入要安装 Linux 的计算机上，开机启动，进入 BIOS 设置使计算机从
U 盘启动。具体如何进入 BIOS 不同电脑不同，请自行查询。

若计算机无法从 USB 启动，则可能是由于计算机的设置导致的，可以尝试：

1. 进入 BIOS 设置
2. 在 BIOS 设置内关闭的安全启动

## 安装系统

假设你已经成功引导系统了，进入了 Live 界面，即进入了 USB 镜像系统的界面。
此时，你可以看见一个 Welcome 的窗口，不必理会，直接点 Next 即可。在桌面上可以看见
“Install to Hard Drive”，双击启动即进入了 CentOS 安装程序。

### 选择安装过程中的语言

安装程序会首先要你选择安装过程中的语言，请选择 English(United States)，然后点击
下方的 continue.

“中文”->“简体中文”

### INSTALLATION SUMMARY 安装信息摘要

这时，你就进入安装信息的收集阶段的 INSTALLATION SUMMARY 了。

1.  LOCALIZTION

    选择你所在的地区和时区，选择离你最近的就好。
    中国大陆用户请选择 Asia-Shanghai，然后点击左上角的 Done。

2.  KEYBOARD

    选择 English(US)，不要选择 English(UK)。

3.  SYSTEM

    选择你要在安装时分区和格式化的硬盘，如果你不熟悉操作，请只选择你打算把
    系统安装的目标硬盘，并选中 Automatically configure partitioning。如果你
    选中的盘已经有分区，有数据，安装程序在你点击 Done，会弹出警告的对话框要求
    你给予空间。这时，点击 Reclaim space，然后点击 Delete all，再点击
    Reclaim space，注意：这会导致你丢失原有的所有数据

4.  NETWORK & HOST NAME

    给你的电脑设置一个你喜欢的名字，然后选择 Done。

点击 Begin Installation，一点击安装就正式开始了。

### CONFIGURATION

程序安装需要的时候，需要你对系统进行一些配置。

1. ROOT PASSWORD - 设置 root 密码。这个密码对系统安全非常重要。

2. USER CREATION - 创建用户。注意选中 Make this user adminstrator。

安装完毕后，点击 Finish configuration，完毕后再点击 Quit，然后重启计算机。
重启时，记得拔出 U 盘启动盘，以免再次进入 USB 安装镜像。

重启后，接受 LICENSING 后，计算机再次重启。到这里，系统本身的安装就结束了。

### 系统的一些基本配置和安装

## 界面和输入法

登陆进入系统后，会弹出gnome-initial-setup。这是图形界面 gnome 初始化设置引导。在语言部分选择美国英语，不要选汉语，也就是使用英文的系统。用英文系统的原因是 gnome 的中文字体很难看。
要安装中文输入法，先确认ibus安装了：

    sudo yum install ibus ibus-libpinyin

然后在 Applications 的 System Tools 找到 Settings，就在第一排有一个 Region & Language。在 Input Source 中加上 Chinese(Intelligent Pinyin)。

### 添加第三方源

CentOS 由于很追求稳定性，所以官方源中自带的软件不多，因而需要一些第三方源，比如EPEL、ATrpms、ELRepo、Nux Dextop、RepoForge 等。根据上面提到的软件安装原则，为了尽可能保证系统的稳定性，此处大型第三方源只添加 EPEL 源和 ELRepo 源。

#### EPEL

[EPEL](https://fedoraproject.org/wiki/EPEL) 即 Extra Packages for Enterprise Linux，
为 CentOS 提供了额外的 10000 多个软件包，而且在不替换系统组件方面下了很多功夫，因而可以放心使用。
EPEL 在国内已经有多个镜像站，会自动搜索最快的。

``` bash
sudo yum install epel-release
```

执行完该命令后，在 `/etc/yum.repos.d` 目录下会多一个 `epel.repo` 文件。
如果提示你的账户不在 sudoers file 里，就需要先添加进去：

````bash
$ su
# echo 'seisman ALL=(ALL) ALL'>> /etc/sudoers # 向配置文件中加入语句
# tail -1 /etc/sudoers  # 检查一下是否正确
seisman ALL=(ALL) ALL
````

其中 seisman 为当前用户名。

#### ELRepo

ELRepo 包含了一些硬件相关的驱动程序，比如显卡、声卡驱动:

    sudo rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
    sudo rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-2.el7.elrepo.noarch.rpm

完成该命令后，在 `/etc/yum.repos.d` 目录下会多一个 `elrepo.repo` 文件。

### 安装 yum-axelget

[yum-axelget](https://dl.fedoraproject.org/pub/epel/7/x86_64/repoview/yum-axelget.html) 是 EPEL
提供的一个 yum 插件。使用该插件后用 yum 安装软件时可以并行下载，大大提高了软件的下载速度，减少了下载的等待时间:

    sudo yum install yum-axelget

安装该插件的同时会安装另一个软件 axel。axel 是一个并行下载工具，在下载 http、ftp 等简单协议的文件时非常好用。

### 第一次全面更新

在进一步操作之前，先把已经安装的软件包都升级到最新版:

    sudo yum update

要更新的软件包有些多，可能需要一段时间。不过有了 yum-axelget 插件，速度已经快了很多啦。

### 重启

第一次全面更新完之后建议重启。

### 删除多余的 kernel

严格地说，Linux 只是各发行版的核心即 kernel，而不是一个完整的操作系统。
核心的作用是操作硬件。kernel 其实就是一个文件: /boot/vmlinuz-xxx (一部机器上可能有数个核心)。
在前面的 `yum update` 执行之后，可能会将 kernel 也一起更新，则在启动 CentOS 时启动项中会有很多项。

确认当前使用的 kernel 版本号:

    $ uname -r
    3.10.0-123.9.3.el7.x86_64

查找当前系统安装的所有 kernel:

    $ rpm -qa | grep kernel | sort
    kernel-3.10.0-123.8.1.el7.x86_64
    kernel-3.10.0-123.9.2.el7.x86_64
    kernel-3.10.0-123.9.3.el7.x86_64
    kernel-devel-3.10.0-123.8.1.el7.x86_64
    kernel-devel-3.10.0-123.9.2.el7.x86_64
    kernel-devel-3.10.0-123.9.3.el7.x86_64
    kernel-headers-3.10.0-123.9.3.el7.x86_64
    kernel-tools-3.10.0-123.9.3.el7.x86_64
    kernel-tools-libs-3.10.0-123.9.3.el7.x86_64

除了 kernel 外、kernel-devel、kernel-headers 和 kernel-tools 这些是用于开发或者是一些特别的程序所需要。
不同的发行版，除了 kernel 外，其他的命名规则各有不同。

上面可以看出有三个版本的 kernel，123.8.1、123.9.2 和 123.9.3。
kernel 太多并不会影响开机速度。搜索内核只在生成 grub.cfg 时进行，记录在了配置文件 grub-mkconfig 中，所以多余的内核不会影响开机速度。
另外，务必谨慎使用 autoremove 命令。有时，a 依赖 b。安装了 a，进而 b 因为依赖安装上了，恰好 b 也是其他的东西需要的。
有一天 a 被删除，b 可能会被错误地删除。所以不要轻易使用 autoremove。
除了最新的 kernel 外，建议多保留一个旧 kernel，以免新 kernel 出现问题时可以通过旧 kernel 进入系统。
因而此处删除 123.8.1 版本的 kernel:

    sudo yum remove kernel-3.10.0-123.8.1.el7.x86_64
    sudo yum remove kernel-devel-3.10.0-123.8.1.el7.x86_64


## 驱动程序

### 显卡驱动

Linux 默认只使用开源的显卡驱动，就目前的情况来看，开源驱动的效果还是不错的，但跟官方的
闭源驱动相比还是有一定差距。最明显的区别是，在使用 SAC 的 ppk 功能放大波形时，使用开源驱动会
出现延迟，而使用官方闭源则整个过程非常顺畅。

关于显卡驱动的安装，请参考 [Linux 下安装 nvidia 显卡驱动](/install-nvidia-drivers-under-linux/)
一文中的 “从 ELRepo 源中安装驱动” 部分。

**注意**：目前的显卡驱动似乎有问题，安装后终端有时会出现屏幕闪烁、一屏文字上下重复跳动的情况，
稍微有些影响用 vim 写代码。是否要安装显卡驱动自己决定。

### NTFS 驱动

CentOS 下默认无法挂载 NTFS 格式的硬盘。需安装 nfts-3g 即可实现即插即用:

    sudo yum install ntfs-3g
