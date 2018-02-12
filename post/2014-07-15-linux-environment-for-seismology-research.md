---
title: 用 CentOS 7 打造合适的科研环境
author: SeisMan
date: 2014-07-15
lastmod: 2016-10-19
categories:
  - Linux
tags:
  - CentOS
  - Perl
  - Python
slug: linux-environment-for-seismology-research
---

这篇博文记录了我用 CentOS 7 搭建 **地震学科研环境** 的过程，供我个人在未来重装系统时参考。对于其他地震学科研人员，也许有借鉴意义。

阅读须知：

1.  本文适用于个人电脑，不适用于服务器；
2.  **不推荐刚接触 Linux 的人使用 CentOS 发行版**；
3.  本文尽量写的浅显易懂，但要求读者掌握 Linux 基础知识；
4.  本文所有操作均在 CentOS 7 下完成，其他发行版或多或少与 CentOS 7 不同，因而仅供参考；
5.  本文所安装的软件纯粹出于个人习惯及喜好，读者应自己判断，按需安装；

<!--more-->

## 安装 CentOS

CentOS 7 的安装与其他 Linux 发行版的安装差不多，个别地方稍有不同。

### 准备工作

1.  准备材料
    -   U 盘：容量 2GB 以上，用于制作 U 盘启动盘，因为在制作启动盘时会格式化 U 盘，所以 U 盘内不要包含重要资料
    -   [CentOS 7.2 LiveCD ISO 镜像文件](http://mirrors.ustc.edu.cn/centos/7/isos/x86_64/CentOS-7-x86_64-LiveGNOME-1511.iso)
    -   [Universal USB installer](http://www.pendrivelinux.com/universal-usb-installer-easy-as-1-2-3/)：Windows 下的 U 盘启动盘制作工具
    -   一个已安装 Windows 的电脑：用于制作 U 盘启动盘

2.  运行 Universal USB installer 并制作 U 盘启动盘
3.  将 U 盘插入计算机，重启，进入 BIOS 选择从 U 盘启动，即可进入 CentOS 的 LiveCD
4.  进入 LiveCD 后，点击桌面的 “Install to Hard Drive” 即可安装

注：Linux 下可以通过 `dd` 命令制作启动盘，但由于对原理不够了解，偶尔会导致制作失败，
或制作成功后 U 盘容量有问题，还是用 Windows 下的 Universal USB installer 比较靠谱。

### 安装过程

1.  选择安装过程中使用的语言，这里应 **使用英语，不要使用汉语**。若安装界面使用汉语，最终安装的系统中会出现两个比较麻烦的问题：
    1.  家目录下的系统文件夹如 Downloads、Desktop 等会以中文表示，这使得在命令行 `cd` 变得很麻烦；
    2.  终端中某些字符用英文字体，某些字符用中文字体，效果非常差，需要自己修改终端字体方可；

2.  选择区域和城市：Asia 和 Shanghai
3.  键盘使用 English(US) 而不是 English(UK)
4.  Hostname 可以改也可以不改，我用 `saturn.geolab`
5.  安装的目的地，选择要使用的硬盘，在 “Other Storage Options” 处选择“I will configure partioning”，即手动分区

### 分区

CentOS7 的分区似乎比较特别，自认为经验很丰富的我在第一次安装 CentOS7 时还是在分区上耽误了很多时间。后来找到比较合适的分区方法，如下：

-   点击 “Click here to create them automatically”，即让安装程序帮忙分区
-   默认的分区方案是使用 LVM，其好处在于 “当机器有多块硬盘时，在使用的时候看上去只有一块”
-   默认的文件系统为 XFS 而不是以前常用的 EXT4；
-   自动分区完成后，再根据自己的需求，手动修改分区细节
    -   `/boot` ：CentOS 自动分配，一定不要乱改；
    -   `/` ：根目录，合理使用并及时清理的话 15G 就够了，不过建议 30G 以上；
    -   `swap` ：与物理内存大小一致即可
    -   `/opt` ：个人习惯是将第三方软件都安装在 `/opt` 下，所以分了 70G
    -   `/home` ：余下的全部空间
-   点击 “Begin to Install” 开始安装

### 真正的安装

1.  设置 root 密码
2.  创建一般用户
3.  等待安装完成
4.  安装完成，重启
5.  重启后，同意 License 即可

## 对系统的若干修改

### 若干原则

为了搭建一个稳定的系统，尽量避免因为各种瞎折腾而导致的系统问题，特订立了一些软件安装的原则。
具体参见《[CentOS7 下的软件安装方法与策略](/how-to-install-softwares-under-centos-7/)》。

### 给一般账号 root 权限

默认情况下，一般账号是没有 root 权限的。为什么不直接用 root 账号，而是要给一般账号 root 权限呢？

-   **日常工作中使用 root 账号，是非常糟糕且危险的习惯！无论是服务器还是个人电脑都是如此。**
-   安装软件时需要 root 权限，只能 `su` 切换到 root 账户再安装。对于习惯使用 `sudo` 的人来说，还是有些麻烦。

假设账户名为 seisman，要授予他 root 权限，则要修改配置文件 `/etc/sudoers` :

    $ su
    # echo 'seisman ALL=(ALL) ALL'>> /etc/sudoers # 向配置文件中加入语句
    # tail -1 /etc/sudoers  # 检查一下是否正确
    seisman ALL=(ALL) ALL

其中 seisman 为当前用户名。

### 添加第三方源

CentOS 由于很追求稳定性，所以官方源中自带的软件不多，因而需要一些第三方源，比如
EPEL、ATrpms、ELRepo、Nux Dextop、RepoForge 等。根据上面提到的软件安装原则，为了尽
可能保证系统的稳定性，此处大型第三方源只添加 EPEL 源、Nux Dextop 和 ELRepo 源。

#### EPEL

[EPEL](https://fedoraproject.org/wiki/EPEL) 即 Extra Packages for Enterprise Linux，
为 CentOS 提供了额外的 10000 多个软件包，而且在不替换系统组件方面下了很多功夫，因而可以放心使用。

``` bash
sudo yum install epel-release
```

执行完该命令后，在 `/etc/yum.repos.d` 目录下会多一个 `epel.repo` 文件。

<!-- #### Nux Dextop

[Nux Dextop](http://li.nux.ro/repos.html) 中包含了一些与多媒体相关的软件包，作者尽量
保证不覆盖 base 源。官方说明中说该源与 EPEL 兼容，实际上个别软件包存在冲突，但基本不会造成影响:

    sudo rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm

完成该命令后，在 `/etc/yum.repos.d` 目录下会多一个 `nux-dextop.repo` 文件。-->

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
核心的作用是操作硬件。kernel 本质上其实，就是一个文件: /boot/vmlinuz-xxx (一部机器上可能有数个核心)。
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

王亮已经写好一个 Perl 脚本自动管理 kernel，你可以在这里下载: https://github.com/wangliang1989/scripts/blob/master/manage-kernel/manage-kernel.pl 。

## 基础开发环境

### GCC 系列

    sudo yum install gcc                     # C 编译器
    sudo yum install gcc-c++                 # C++ 编译器
    sudo yum install gcc-gfortran            # Fortran 编译器
    sudo yum install compat-gcc-44           # 兼容 gcc 4.4
    sudo yum install compat-gcc-44-c++       # 兼容 gcc-c++ 4.4
    sudo yum install compat-gcc-44-gfortran  # 兼容 gcc-fortran 4.4
    sudo yum install compat-libf2c-34        # g77 3.4.x 兼容库

### 软件开发辅助工具

    sudo yum install make
    sudo yum install gdb     # 代码调试器
    sudo yum install cmake   # Cmake
    sudo yum install git     # 版本控制

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

## 进阶开发环境

### Java 环境

Java 的一大特色在于跨平台，安装了 Java 运行环境，即可运行 Java 程序:

    sudo yum install java                        # java 运行环境

### Clang 系列

Clang 可以认为是 GCC 的替代品，可以用于编译 C、C++、Objective-C 和 Objective-C++。其提供了更友好的
报错信息，在有些方面比 GCC 更友好，同时其提供了一个代码静态分析器，可以用于分析代码中可能出现的 bug 和内存溢出问题。

    sudo yum install clang             # clang 编译器
    sudo yum install clang-analyzer    # clang 静态分析器

### Intel 系列

Intel 的大部分软件都是非开源且收费的，但同时部分软件也提供了 Linux 下的非商业免费版。
比如 icc、mkl 数学库以及代码性能分析工具等。

Intel 软件的申请以及安装参考《[Intel 非商业免费开发工具](/intel-non-commercial-software.html)》。

还有一点需要注意的是，Intel 也提供了并行相关的几个命令，比如 mpicc、mpirun。所以 openmpi、mpich
和 intel 三者，在并行时只能用其中一个。

### 并行计算

并行可以用 openmpi，也可以用 mpich，二者的功能可以认为是完全相同的。由于二者提供了几乎一样的命令，
所以二者可以同时安装，但是不可以同时处于使用状态。

#### openmpi

安装 openmpi:

    sudo yum install openmpi openmpi-devel

安装后，二进制文件位于 `/usr/lib64/openmpi/bin` 下，动态库文件位于 `/usr/lib64/openmpi/lib`
下，因而实际使用的话还需要额外的配置，在 `.bashrc` 中加入如下语句:

    export PATH=/usr/lib64/openmpi/bin/:${PATH}
    module load mpi/openmpi-x86_64

PS：要使用 `module` 命令需要先安装 `environment-modules` 包。

#### mpich

安装 mpich:

    sudo yum install mpich mpich-devel

安装后，二进制文件位于 `/usr/lib64/mpich/bin` 下，动态库文件位于 `/usr/lib64/mpich/lib` 下，
因而实际使用的话还需要额外的配置，在 `.bashrc` 中加入如下语句:

    export PATH=/usr/lib64/mpich/bin/:${PATH}
    module load mpi/mpich-x86_64

## 脚本语言环境

### Perl

CentOS 7.0 自带了 Perl 5.16.3（2013 年 03 月 11 日发布），目前的最新版本为 5.20.1（2014 年 09 月 14 日发布）。

#### 系统自带 Perl

系统自带 Perl，就目前来看，版本不算老，基本够用。官方源和 EPEL 源中提供了 1000 多个模块，可以直接用 yum 安装:

    sudo yum install perl-Parallel-ForkManager  # 并行模块

若源中没有已打包好的模块，也可以使用 perl 自带的 cpan 来安装模块。

优先级：yum > cpan。

#### plenv 管理新版本

若需要使用最新版本的 perl，可以使用 [plenv](/perl-plenv.html) 安装新版本的 perl，并使用 plenv 提供的 cpanm 命令安装模块:

    cpanm install Parallel::ForkManager # 并行模块

### Python

CentOS 7.0 自带 Python 2.7.5，目前 Python 2 的最新版本为 2.7.8，Python 3 的最新版本为 3.4.2。

#### 系统自带 Python

系统自带的 Python 2.7.5，基本已经够用，Python 2 常用的模块在官方源或 EPEL 源中也有有编译好的包，
因而直接通过 yum 安装即可:

    sudo yum install python-matplotlib  # 2D 绘图库
    sudo yum install PyQt4  # Qt4 的 Python 绑定
    sudo yum install numpy  # 数组操作库
    sudo yum install scipy  # 科学计算库
    sudo yum install python-requests  # 网页请求
    sudo yum install python-docopt  # 命令行参数分析器
    sudo yum install gdal-python    # gdal 的 Python 绑定

#### pyenv 管理 Python3

Python2 与 Python3 之间是不完全兼容的，而我以 Python3 为主，所以需要安装一个 Python3。

首先，安装 [pyenv](/python-pyenv.html) 来管理多个 Python 版本，然后利用 pyenv 安装 anaconda3
（即 Python3.4）。anaconda 自带了众多科学计算所需的包，免去了安装的麻烦，对于其他包，
则可以利用 Python 自带的 pip 安装:

    pip install requests
    pip install docopt

## 编程相关软件

### 编辑器

写代码的时候选一个好用的编辑器很重要，用的比较多的编辑器如下：

1.  vim
2.  emacs
3.  atom
4.  sublime text 3
5.  Visual Studio Code

### IDE

-   Python IDE：[PyCharm Community Edition](https://www.jetbrains.com/pycharm/)

## 日常软件

### Office 套件

#### LibreOffice

大多数 Linux 发行版都自带 LibreOffice:

    sudo yum install libreoffice

LibreOffice 与 Microsoft Office 的兼容性不太好，操作界面与 MS Office 也有较大差异，让人不太习惯。

#### WPS Office

若在 Linux 下对于文档处理有更高一些的要求，可以尝试目前还处于测试版的 WPS Office for Linux。
WPS Office 的兼容性以及界面都比 LibreOffice 要好很多，值得期待，当然还是不能做到完全兼容 MS
Office。

安装过程参考 [CentOS 下安装 WPS Office](/wps-office-for-centos7.html) 一文。

### PS/PDF 阅读器

系统自带的 evince 阅读器，可以打开 PS 和 PDF 文件，基本足够日常的使用了。

#### zathura

zathura 可以查看 PS、PDF、djvu 格式的文件，可以作为 evince 的替代品:

    sudo yum install zathura zathura-plugins-all

#### ghostscript

    sudo yum install ghostscript

#### master-pdf-editor

官方网站: <https://code-industry.net/free-pdf-editor/>

    sudo yum localinstall http://get.code-industry.net/public/master-pdf-editor3-3.2.62-1.x86_64.rpm

### TeX Live 2015

系统是自带了 TeXLive，版本较老，还是安装最新版比较好。

参考 [Linux 下安装 TeXLive](/install-texlive-under-linux.html) 一文。

### Mendeley

Mendeley 是一个跨平台的文献管理软件，其内部自带了一个可以添加注释的 PDF 阅读器。

下载 Generic Linux (64 bits)：http://www.mendeley.com/download-mendeley-desktop

安装:

    tar -xvf mendeleydesktop-1.12.3-linux-x86_64.tar.bz2  # 解压
    sudo mv mendeleydesktop /opt  # 复制到 / opt 下
    cd /opt/mendeleydesktop/bin   # cd 进去
    ./install-mendeley-link-handler.sh /opt/mendeleydesktop/bin/mendeleydesktop
    sudo yum install qtwebkit  # 安装依赖包

注销重新登陆，在 Application->Education 下即可看到 mendeley 的相关项目。不过是
没有软件的图标的，强迫症不能忍，用下面的命令解决:

    cp /opt/mendeleydesktop/share/icons/hicolor/128x128/apps/mendeleydesktop.png ~/.local/share/icons/

### Google Chrome 浏览器

默认的浏览器是 Firefox，还是更喜欢 Chrome 浏览器。

Google 官方源在国内可能无法正常访问，故而添加 Fedora 中文社区提供的镜像源:

    sudo wget http://repo.fdzh.org/chrome/google-chrome-mirrors.repo -P /etc/yum.repos.d/

安装:

    sudo yum install google-chrome-stable

### Opera 浏览器

也可以选择 Opera 浏览器。

下载地址：http://www.opera.com/download/guide/?os=linux

选择 CentOS RPM package 进行下载。下载完成后，执行:

    sudo yum localinstall opera-12.16-1860.x86_64.rpm

想要卸载的话，就执行:

    sudo yum remove opera

### Flash 插件

Flash 插件主要是看在线视频的时候要用。Google 浏览器自带了 Flash 插件，所以这里安装的 flash 插件主要是为了 firefox。

    sudo rpm -ivh http://linuxdownload.adobe.com/adobe-release/adobe-release-x86_64-1.0-1.noarch.rpm
    sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-adobe-linux
    sudo yum install flash-plugin

### 解压软件

解压 7z 或 zip 格式需要 p7zip，由 EPEL 提供:

    sudo yum install p7zip

解压 rar 格式可以使用 [unar](https://unarchiver.c3.cx/commandline)，该软件位于 EPEL 源中：

    sudo yum install unar

### FTP 客户端

FTP 客户端，还是有界面的 filezilla 比较方便些。

    sudo yum install filezilla

### Google Earth

到 https://www.google.com/earth/download/ge/agree.html 下载64位rpm包，执行如下命令安装:

    sudo yum localinstall google-earth-stable_current_x86_64.rpm

## 效率类软件

这一类工具能够在不同方面提高科研的效率，也提高了使用者的体验。

### 终端模拟器

Gnome 自带的终端模拟器是 gnome-terminal。经常会需要开十几个终端，切换和管理起来比较麻烦。

#### terminator

terminator 有很多功能，我只用到了终端分割的功能。 `Ctrl+Shift+O` 对终端水平分隔，
`Ctrl+Shift+E` 对终端垂直分隔， `Alt + 上下左右 ` 可以在各子终端中切换。terminator 由 Nux Dextop 提供:

    sudo yum install terminator

#### guake

有些时候需要临时执行一两个命令，但是又不想额外启动一个终端的情况下，guake 是个不错的选择。

    sudo yum install guake

安装完成后，在 Application->System Tools 里找到 guake Terminal 即可启动。按下 F12
即可呼出 guake，再次按下 F12 即可隐藏。也可在终端执行 `guake-prefs` 对 gauke 进行配置。

### zsh 与 oh my zsh

Linux 下有很多 shell，比如最常见的 bash，除此之外还有 csh、ksh。zsh 也是一个 shell。

zsh 的特点在于：

-   语法基本完全兼容于 bash，一般用户完全体会不到其区别
-   zsh 提供命令补全特性，比 bash 的补全要更好用
-   可配置性强

完全不经配置的 zsh 已经很好用了，一般用户也没必要花时间研究配置。
[oh my zsh](https://github.com/robbyrussell/oh-my-zsh) 是一群人一起维护的一套 zsh 配置文件。
直接用这个配置文件，稍稍了解一点会有更好的体验。

安装 zsh:

    sudo yum install zsh

安装 oh my zsh:

    curl -L http://install.ohmyz.sh | sh

上面的命令，做了如下几件事情：

-   下载 `oh my zsh` 到 `~/.oh-my-zsh`
-   备份已有的 zsh 配置文件 `~/.zshrc` ，并复制新的 `.zshrc` 文件
-   将当前用户的默认 shell 由 bash 改成 zsh

第三步中，会报错如下： `chsh: "/usr/bin/zsh" is not listed in /etc/shells.` ，需要手动修改默认 shell:

    chsh -s /bin/zsh

chsh 命令修改的是 login shell，因而需要退出当前用户并重新登陆，以后用户的默认 shell
就从 bash 变成了 zsh，所有的配置都不用写到 `.bashrc` 而要写到 `.zshrc` 中。

在 `.zshrc` 中可以选择喜欢的主题，以及适当数量的插件。下面列出我在用的插件:

1.  git

    该插件为 git 的众多常用命令提供了更简单的别名，比如 `git status` 的别名是 `gst`，
    大大减少了击键数。但该插件中 `git mergetool --no-prompt` 的别名是 `gmt`，
    与 GMT 软件冲突，需要将该插件的目录 git 复制到 custom/plugins 下，然后删除其中的 gmt 别名；

2.  命令补全插件: pip, pyenv
3.  sudo：按两下 `ESC` 即可在当前命令前加上 `sudo`
4.  yum：为常见的 yum 命令提供别名

### autojump

[autojump](https://github.com/joelthelion/autojump) 是一个非常智能的目录快速切换的工具。简单演示如下:

    $ pwd
    /home/seisman
    $ cd Desktop
    $ cd /opt
    $ cd /usr/local

    # 用 j 命令迅速从 / usr/local 跳转到与 des 匹配的目录，这里只有 Desktop 可以匹配
    $ j des
    $ pwd
    /home/seisman/Desktop

用法差不多就这样，具体看项目主页。

安装:

    sudo yum install autojump
    sudo yum install autojump-zsh

### 中文输入法

安装 ibus 和插件:

    sudo yum install ibus ibus-libpinyin

由于使用的是全英文安装，所以默认是没有中文输入法的。

在“Application”->“Settings”->“Language” 中，这样设置：

|项目    |内容               |
|:-----:|:----------------:|
|语言    |汉语中国            |
|格式    |中国汉语            |
|输入入源 |intelligent Pinyin|

重启后注意选择保留原文件夹。

### 等宽字体

编程要用等宽字体，这点是常识了。一款适合编程的等宽字体，至少要满足如下几个要求：

1.  易于区分 “1”、“i” 和“l”
2.  易于区分 “0”、“o” 和“O”
3.  易于区分中文下的左引号和右引号
4.  美观

目前选择的 Source Code Pro。将解压后的字体文件放在 `~/.fonts` 目录下，并修改终端、gedit 以及其他编辑器、IDE 等的默认字体。

## 虚拟机

有时候可能需要在 Windows 下做一些操作，如果机器性能足够好的话，可以安装虚拟机。

### VirtualBox 虚拟机

VirtuabBox 的安装:

    sudo yum install kernel-devel # 先要安装 Kernel 工具

    wget http://download.virtualbox.org/virtualbox/rpm/rhel/virtualbox.repo
    sudo mv virtualbox.repo /etc/yum.repos.d/
    sudo yum install VirtualBox-5.0

需要注意两点：

-   若机器性能不够，虚拟机的使用体验会非常差，所以不建议在老机器上使用；
-   更新 kernel 之后需要执行 `sudo /sbin/rcvboxdrv setup` ；
-   在 VirtualBox 安装虚拟系统后，记得使用 “设备”->“安装增强功能”，使用效果会更好；

### gnome-boxes

gnome-boxes 是 GNOME3 开发的一个虚拟机工具，使用体验不如 VirtualBox:

    sudo yum install gnome-boxes

### Wine

Wine 是一个可以让 Windows 程序运行在 Linux 下的软件。类似虚拟机，但跟虚拟机又不太一样:

    sudo yum install wine

## 同步网盘

网盘根据功能大概可以分为两类：同步网盘和备份网盘。既然是同步网盘，Linux 下
的客户端必不可少。就目前已知的情况来看，CentOS7 下能使用的同步网盘只有三个：
Dropbox、MEGA 和坚果云。

我主要用同步网盘将 Linux 机器上的 PDF 文献同步到 iPad 上。

### Dropbox

又是一个被墙的工具，熟练掌握科学上网技巧的人可以使用，一般人还是不要用了。

    wget https://www.dropbox.com/download?dl=packages/fedora/nautilus-dropbox-1.6.2-1.fedora.x86_64.rpm
    sudo rpm -i nautilus-dropbox-1.6.2-1.fedora.x86_64.rpm

### MEGA

MEGA： <https://mega.co.nz/>

免费容量 50G，作为同步盘来说基本是够用了。

    # 下载主程序
    wget https://mega.nz/linux/MEGAsync/CentOS_7/x86_64/megasync-CentOS_7.x86_64.rpm
    # 下载文件管理器扩展（可选）
    wget https://mega.nz/linux/MEGAsync/CentOS_7/x86_64/nautilus-megasync-CentOS_7.x86_64.rpm
    sudo yum localinstall megasync-CentOS_7.x86_64.rpm
    sudo yum localinstall nautilus-megasync-CentOS_7.x86_64.rpm

### 坚果云

国内的全平台同步网盘，不限空间，但限制每月上传流量 1G，下载流量 3G。

    # 坚果云依赖于 notify-python
    sudo yum install notify-python
    # 下载
    wget https://jianguoyun.com/static/exe/installer/fedora/nautilus_nutstore_amd64.rpm
    sudo rpm -i nautilus_nutstore_amd64.rpm

## 工具软件

### 视频下载工具

[you-get](https://github.com/soimort/you-get) 和 [youtube-dl](https://github.com/rg3/youtube-dl)
是两个用于从视频网站上下载视频文件的工具。其中，后者支持的网站更多，但前者对国内的视频网站支持更好。

    pip install you-get
    pip install youtube-dl
    # EPEL 中提供了 youtube-dl 包，因而也可以使用 yum 安装。一般来说，pip 安装的版本更新一些

### PDF 处理工具

[cpdf](http://community.coherentpdf.com/) 是一个跨平台的 PDF 处理工具，可以完成常见的 PDF 合并、
切割、加密解密、书签、水印等功能。

下载已编译好的 [二进制包](https://github.com/coherentgraphics/cpdf-binaries/archive/master.zip)，
解压，并将与自己的平台对应的二进制文件复制到 `${HOME}/bin` 目录下即可使用。

### BT 软件

transmission 是 Linux 下常用的 Torrent 下载软件:

    sudo yum install transmission

在 “Application”->“Internet”-> 中可以启动 transmission。

### uGet

<http://ugetdm.com/>

uGet 是 Linux 下的一个下载工具，支持 HTTP、HTTPS、FTP、Torrent 等，支持多连接，并可以监视剪贴板:

    sudo yum --enablerepo=epel-testing install uget aria2

### 截图软件 shutter

GNOME 自带了截图工具。 `PrtScn` 为截取整个屏幕； `Alt+PrtScn` 为截取当前窗口；
`Shift+PrtScn` 为自定义截屏区域。

[shutter](http://shutter-project.org/) 是一个功能更强大的截图工具，支持不同的截图方式、
图片格式，还支持图片的简单编辑与注释:

    sudo yum install shutter

可以通过 [修改快捷键使 shutter 成为默认的截图工具](http://shutter-project.org/faq-help/set-shutter-as-the-default-screenshot-tool/)。

### 其他工具

    sudo yum install nfs-utils     # 挂载 NFS 文件系统所必须
    sudo yum install xclip         # 终端的文本复制工具
    sudo yum install ImageMagick   # 其中的 import 和 convert 命令很有用
    sudo yum install dos2unix unix2dos  # Windows 和 Linux 换行符互相转换
    sudo yum install meld          # 图形界面下的文件差异比较工具

## 娱乐

### 影音播放器

Nux Dextop 提供了 mplayer 和 VLC，可以用于播放常见格式的音频和视频，二者选其一安装即可:

    sudo yum install mplayer
    sudo yum install vlc

### 游戏

    sudo yum install 2048-cli   # 2048 命令行版

## 参考

1.  [ELRepo 官方网站](http://elrepo.org/tiki/tiki-index.php)
2.  [ELRepo kmod-nvidia](http://elrepo.org/tiki/kmod-nvidia)
3.  [CentOS Yum 软件库样例](http://wiki.centos.org/zh/AdditionalResources/Repositories/GoogleYumRepos)

## 修订历史

-   2014-07-15：初稿；
-   2014-09-05：EPEL 已经发布正式版；修改了 epel-release 的下载链接；修订了 import 步骤的错误；
-   2014-09-20：将小小输入法改为搜狗输入法；
-   2014-11-20：使用 zsh；
-   2014-11-24：加入了 VirtualBox 虚拟机；
-   2014-12-01：从 ELRepo 源中安装显卡驱动；
-   2014-12-02：新增 Opera 浏览器和 unrar；
-   2014-12-27：新增 pointdownload 下载工具；google chrome 采用非官方源镜像；
-   2014-12-28：修订 unrar 的 rpm 文件链接；
-   2015-01-03：新增同步网盘 Dropbox 和坚果云；删除 pointdownload；
-   2015-01-05：autojump 直接从 epel 中安装；新增 youtube-dl、you-get 和 2048-cli；
-   2015-01-07：新增 terminator 和 guake；
-   2015-01-27：新增 cpdf；
-   2015-03-03：新增 filezilla 和 transmission；
-   2015-03-26：安装过程中不应使用中文安装界面；
-   2015-05-11：新增 MEGA 同步网盘；
-   2015-05-16：新增 gnome-boxes；
-   2015-06-26：新增 zathura 和 ghostscript；
-   2015-07-14：新增 Nux Dextop 源，uGet、shutter；
-   2015-09-03：删除地球物理相关软件；
-   2015-09-18：删除显卡驱动安装的具体步骤，直接链接到相关博文；
-   2016-09-12：新增google earth的安装；
