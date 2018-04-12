---
title: CentOS 7 配置指南 — 安装篇
author: SeisMan
date: 2014-07-15
lastmod: 2018-04-11
slug: centos7-setup-1
---

本文介绍如何安装 CentOS 7 的最新版本 CentOS-7-1708，也就是 CentOS 7.4。

CentOS 7 的安装与其他 Linux 发行版的安装差不多，个别地方稍有不同。

<!-- more -->

## 准备工作

1.  下载 ISO 安装镜像文件

    从[清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/)下载
    最新版的 CentOS 安装镜像文件。

    镜像文件有多种，推荐下载 LiveGNOME 版本，即
    [CentOS-7-x86_64-LiveGNOME-1708.iso](https://mirrors.tuna.tsinghua.edu.cn/centos/7.4.1708/isos/x86_64/CentOS-7-x86_64-LiveGNOME-1708.iso)。

2.  制作 USB 安装镜像

    参考 [制作 Linux USB 安装镜像](/linux-usb-installer/) 一文。

3.  从 U 盘启动盘进入 Live 系统

    将制作好的 U 盘启动盘插入要安装 Linux 的计算机上，开机启动，进入 BIOS 设置
    使计算机从U 盘启动。具体如何进入 BIOS 不同电脑不同，请自行查询。

    若计算机无法从 USB 启动，则可能是由于计算机的“安全启动”设置导致的，可以尝试：

    1. 进入 BIOS 设置
    2. 在 BIOS 设置内关闭安全启动

    如果尝试多次都无法正确从 USB 启动，则可能是 USB 启动盘制作失败，请尝试
    重新制作启动盘。

## 安装系统

假设你已经成功引导系统了，进入了 Live 界面，即进入了 USB 启动盘内的系统界面。
此时会出现“Welcome”窗口，不管它，
直接在桌面上找到“Install to Hard Drive”，双击进入了 CentOS 安装程序。

### 安装过程中使用的语言

安装程序会首先要你选择安装过程中的语言，可以选择“中文”->“简体中文（中国）”，
然后点击下方的“继续”按钮。当然你也可以选择“English”->“English (Unite States)”。

### 安装信息摘要

进入“安装信息摘要”阶段，需要设置“日期和时间”、“键盘”、“安装配置”和“网络及主机名”。

1.  日期和时间

    选择你所在的地区和时区，选择离你最近的就好。
    中国大陆用户请选择“亚洲-上海”，然后点击左上角的“完成”。

2.  键盘

    选择“汉语” 或者 English(US) 均可，不要选择 English(UK)，然后点击“完成”。

3.  网络与主机名

    给你的电脑在网络上设置一个喜欢的名字，默认值为 `localhost.localdomain`。

4.  安装位置

    这一步是要选择要把系统安装到哪一块硬盘以及如何分区。

    在“设备选择”中，选择自己要使用哪些硬盘安装系统。如果计算机有多个磁盘，可以
    将多个磁盘都选中，被选中的磁盘会有一个“对号”符号。需要注意，不要选中 USB
    安装盘。

    对硬盘进行分区建议选择“我要配置分区”，并继续阅读下一节内容。

    如果不熟悉分区操作的，也可以选择“自动配置分区”（不推荐）。
    此时，如果你选中的盘已经有其他分区或数据，安装程序在你点击“完成”时弹出警告
    对话框要求你给予空间。这时，点击“回收空间”，然后点击“删除全部”并点击
    “回收空间”即可删除之前已存在的全部分区和数据。

点击“开始安装”即进入正式安装过程。

### 手动分区

通常建议对硬盘进行手动分区，以更好地满足需求。

CentOS 7 的分区似乎比较特别，自认为经验很丰富的我在第一次安装 CentOS 7 时还是
在分区上耽误了很多时间。后来找到比较合适的分区方法，如下：

1.  点击 “点这里自动创建它们” 让安装程序帮忙分区

    安装程序在自动分区时默认的分区方案是“LVM”，其好处在于“当机器有多块硬盘时，
    在使用的时候看上去只有一块”；默认的文件系统为 XFS 而不是以前常用的 EXT4。

    自动分区通常会分为 `boot`、`/` 、`swap` 和 `/home` 四个分区。

2.  自动分区分区完成后，可以根据自己的需求手动修改分区细节

    -   `/boot` 由安装程序自动分配，一定不要乱动；
    -   `/`  最少15G，如果未来装的软件比较多（比如一个matlab就用了10G多），
        建议留100 G左右
    -   `swap` 通常与物理内存大小相同
    -   `/home` 余下的全部空间

    若想要修改分区容量，需要先将 `/home` 分区的容量减小，使得可用容量增加才能
    修改增加其他分区的容量。

3.  点击“完成”，“接受修改”，然后“开始安装”

### 用户配置

系统安装过程中，需要配置用户信息：

1. 设置 root 用户密码。
2. 创建一般用户的帐号及密码。记得选中“将此用户作为管理员”。

等待安装完成，点击“完成配置”，完毕后再点击“退出”，并重启计算机。
重启计算机时，记得拔出 U 盘启动盘，以免再次进入 USB 安装镜像。
重启后，接受“许可协议”并点击“完成配置”后，计算机将再次重启。
到这里，系统本身的安装就结束了。

## 基本配置

### 语言和输入法设置

首次进入系统后，会弹出“欢迎”界面，并需要做一些基础设置。

-   语言：务必选择“English(United States)”， **不要选择“汉语（中国）”**

    若此处设置语言为中文，则系统界面会以中文呈现，此时系统会出现两个比较麻烦的问题：

    1.  家目录下的系统文件夹如 Downloads、Desktop 等会以中文表示，这使得在命令行
        `cd` 变得很麻烦；
    2.  终端、浏览器等的中文字体发虚，且某些字符用英文字体，某些字符用中文字体，
        效果非常差。需要用户一一配置字体方可

    故而不要选择“汉语（中文）”。

-   输入法：输入法直接选择“English (US)”

此时，请 **注销用户** 或 **重启**。再次进入系统时，会弹出对话框问是否
“Update Standard Folders to Current Language?”，注意选择“Update”，将“文档”、
“下载”等目录名修改为英文的“Documents”、“Downloads”，以方便在命令行中进行目录
切换等操作。

### 中文输入法

要添加中文输入法，需要先确认 ibus 以及中文拼音插件已经被正确安装。

如果安装过程中使用的是中文界面安装，则相关包已经安装。
如果安装过程中使用的是英文界面安装，则默认没有安装中文输入法相关包。
这种情况下，可以执行如下命令安装中文输入法相关包:

    sudo yum install ibus ibus-libpinyin

然后在 “Applications”的“System Tools”里找到“Settings”，进入“Region & Language”。
在“Input Source”处点“加号”并添加“Chinese(Intelligent Pinyin)”即可。

“Region & Language”的最终效果应该是：

- Language： English(United States)
- Formats：Unites Stetes(English)
- Input Source：English(US) 和 Chinese(Intelligent Pinyin)

## 添加第三方源

CentOS 由于很追求稳定性，所以官方源中自带的软件不多，因而需要一些第三方源。
为了尽可能保证系统的稳定性，此处只添加最为可靠的 EPEL 源和 ELRepo 源。

### EPEL

[EPEL](https://fedoraproject.org/wiki/EPEL) 即 Extra Packages for Enterprise Linux，
为 CentOS 提供了额外的 10000 多个软件包，而且在不替换系统组件方面下了很多功夫，
因而可以放心使用。EPEL 在国内已经有多个镜像站，会自动搜索最快的。

``` bash
sudo yum install epel-release
```

执行完该命令后，在 `/etc/yum.repos.d` 目录下会多一个 `epel.repo` 文件。

### ELRepo

[ELRepo](http://elrepo.org/) 包含了一些硬件相关的驱动程序，比如显卡、声卡驱动:

    sudo rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
    sudo rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-3.el7.elrepo.noarch.rpm

完成该命令后，在 `/etc/yum.repos.d` 目录下会多一个 `elrepo.repo` 文件。


## 更新系统

通常的建议是，要么经常更新系统（比如每周一次），要么一直不更新系统。长时间不更新
系统突然一次做大量更新很有可能会挂掉。

### 安装 yum-axelget

yum-axelget 是 EPEL 提供的一个 yum 插件。使用该插件后用 yum 安装软件时可以并行
下载，大大提高了软件的下载速度，减少了下载的等待时间:

    sudo yum install yum-axelget

安装该插件的同时会安装另一个软件 axel。axel 是一个并行下载工具，在下载 http、ftp
等简单协议的文件时非常好用。

### 第一次全面更新

使用如下命令以更新系统中所有已安装的软件:

    sudo yum update

要更新的软件包有些多，可能需要一段时间。不过有了 yum-axelget 插件，速度已经快了很多啦。

### 重启

第一次全面更新完之后建议重启。

### 删除多余的 kernel

严格地说，Linux 只是各发行版的核心即 kernel，而不是一个完整的操作系统。
核心的作用是操作硬件。kernel 其实就是一个文件: `/boot/vmlinuz-xxx` （一部机器
上可能有数个核心)。在前面的 `yum update` 执行之后，可能会将 kernel 也一起更新，
则在启动 CentOS 时启动项中会有很多项，多余的启动项可以留着，也可以删除。

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

除了 kernel 外、kernel-devel、kernel-headers 和 kernel-tools 这些是用于开发
或者是一些特别的程序所需要。不同的发行版，除了 kernel 外，其他的命名规则各有不同。

上面可以看出有三个版本的 kernel，123.8.1、123.9.2 和 123.9.3。
kernel 太多并不会影响开机速度。搜索内核只在生成 grub.cfg 时进行，记录在了配置
文件 grub-mkconfig 中，所以多余的内核不会影响开机速度。
除了最新的 kernel 外，建议多保留一个旧 kernel，以免新 kernel 出现问题时可以
通过旧 kernel 进入系统。因而此处删除 123.8.1 版本的 kernel:

    sudo yum remove kernel-3.10.0-123.8.1.el7.x86_64
    sudo yum remove kernel-devel-3.10.0-123.8.1.el7.x86_64

## 驱动程序

### 显卡驱动

Linux 默认只使用开源的显卡驱动，就目前的情况来看，开源驱动的效果还是不错的，
但跟官方的闭源驱动相比还是有一定差距。

关于显卡驱动的安装，请参考 [Linux 下安装 nvidia 显卡驱动](/install-nvidia-drivers-under-linux/)
一文中的 “从 ELRepo 源中安装驱动” 部分。

### NTFS 驱动

CentOS 下默认无法挂载 NTFS 格式的硬盘。需安装 nfts-3g 即可实现即插即用:

    sudo yum install ntfs-3g
