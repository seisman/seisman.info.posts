---
title: CentOS 7 配置指南 — 日常软件篇
author: SeisMan
date: 2014-07-15
lastmod: 2018-04-12
slug: centos7-setup-4
---

## 浏览器

CentOS 默认的浏览器是 Firefox，用户还可自行安装其他浏览器。

### Google Chrome 浏览器

Google 官方源在国内可能无法正常访问，故而添加
[Fedora 中文社区](https://www.fdzh.org) 提供的镜像源:

    sudo wget http://repo.fdzh.org/chrome/google-chrome-mirrors.repo -P /etc/yum.repos.d/

安装 Google Chrome:

    sudo yum install google-chrome-stable

### Opera 浏览器

下载地址： https://www.opera.com/download/get/?partner=www&opsys=Linux&package=RPM

下载得到 RPM 包后，执行:

    sudo yum localinstall opera-stable_52.0.2871.64_amd64.rpm

想要卸载的话，就执行:

    sudo yum remove opera

### Flash 插件

Flash 插件主要是看在线视频的时候要用。Google 浏览器自带了 Flash 插件，所以这里
安装的 flash 插件主要是为了 firefox。

    sudo rpm -ivh http://linuxdownload.adobe.com/adobe-release/adobe-release-x86_64-1.0-1.noarch.rpm
    sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-adobe-linux
    sudo yum install flash-plugin

## Office 套件

### LibreOffice

LibreOffice 可以用于打开 docx 文件，虽然兼容性很糟糕，但是作为临时替代品还可以。

使用如下命令直接安装:

    sudo yum install libreoffice

### WPS Office

若在 Linux 下对于文档处理有更高一些的要求，可以尝试目前还处于测试版的
WPS Office for Linux。
WPS Office 的兼容性以及界面都比 LibreOffice 要好很多，值得期待，当然还是不能
做到完全兼容 MS Office。

安装过程参考 [CentOS 下安装 WPS Office](/wps-office-for-centos7/) 一文。

## PS/PDF 阅读器

### evince

系统自带 evince 阅读器，可以直接打开 PS 和 PDF 文件。

### ghostscript

ghostscript 用于查看 PS 文件。

    sudo yum install ghostscript

用法为：

    gs figure.ps

### zathura

[zathura](https://pwmt.org/projects/zathura/) 可以查看 PS、PDF、djvu 格式的文件，
可以作为 evince 的替代品:

    sudo yum install zathura zathura-plugins-all

zathura 需要在命令行直接执行，比如：

    zathura figure.pdf

更详细的用法，见官方文档。

## 虚拟机

有时候可能需要在 Windows 下做一些操作，如果机器性能足够好的话，可以安装虚拟机。

### VirtualBox 虚拟机

VirtuabBox 的安装:

    sudo yum install kernel-devel # 先要安装 Kernel 工具

    wget http://download.virtualbox.org/virtualbox/rpm/rhel/virtualbox.repo
    sudo mv virtualbox.repo /etc/yum.repos.d/
    sudo yum install VirtualBox-5.1

需要注意几点：

-   若机器性能不够，虚拟机的使用体验会非常差，所以不建议在老机器上使用；
-   每次更新 kernel 之后都需要执行 `sudo /sbin/rcvboxdrv setup` 才能使用虚拟机；
-   在 VirtualBox 安装虚拟系统后，记得使用 “设备”->“安装增强功能”，使用效果会更好；

### gnome-boxes

gnome-boxes 是 GNOME3 开发的一个虚拟机工具，使用体验不如 VirtualBox:

    sudo yum install gnome-boxes

### Wine

Wine 是一个可以让 Windows 程序运行在 Linux 下的软件。类似虚拟机，但跟虚拟机
又不太一样:

    sudo yum install wine

## 同步网盘

网盘根据功能大概可以分为两类：同步网盘和备份网盘。就目前已知的情况来看，
CentOS 7 下能使用的同步网盘只有三个：Dropbox、MEGA 和坚果云。

### 坚果云

国内目前最好的全平台同步网盘，不限空间，但限制每月上传流量 1G，下载流量 3G。
有需要的可以考虑购买高级版。

    # 坚果云依赖于 notify-python
    sudo yum install notify-python
    # 下载
    wget https://www.jianguoyun.com/static/exe/installer/fedora/nautilus_nutstore_amd64.rpm
    sudo yum localinstall nautilus_nutstore_amd64.rpm

### Dropbox

国外最好用的全平台同步网盘，但被墙了，熟练掌握科学上网技巧的人可以使用，
一般人还是不要用了。

下载地址： https://www.dropbox.com/install-linux

下载 Fedora 64-bit 的 RPM 包，执行如下命令安装:

    sudo yum localinstall nautilus-dropbox-xxx.fedora.x86_64.rpm

### MEGA

MEGA： <https://mega.co.nz/>

免费容量 50G，作为同步盘来说基本是够用了。

    # 下载主程序
    wget https://mega.nz/linux/MEGAsync/CentOS_7/x86_64/megasync-CentOS_7.x86_64.rpm
    sudo yum localinstall megasync-CentOS_7.x86_64.rpm

    # 下载文件管理器扩展（可选）
    wget https://mega.nz/linux/MEGAsync/CentOS_7/x86_64/nautilus-megasync-CentOS_7.x86_64.rpm
    sudo yum localinstall nautilus-megasync-CentOS_7.x86_64.rpm

## TeXLive

LaTeX 用户需要安装 TeXLive。

系统自带的 TeXLive 通常版本都很好，因而建议手动安装最新版本的 TeXLive。
参考 [Linux 下安装 TeXLive](/texlive-install) 一文。

## 截图工具

### gnome-screenshot

GNOME 下自带的截图工具是 gnome-screenshot，其有三种使用方式：

1.  快捷键直接调用

    - `PrtSc`: 截取整个屏幕
    - `Alt+PrtSc`: 截取当前窗口
    - `Shift+PrtSc`: 自定义截图区域

2.  命令行调用

    可以在命令行执行 `gnome-screenshot` 再加上各种选项也可以实现类似的效果

3.  “Applications”->“Utilities”->“Screenshot”打开截图对话框

    截图对话框里有更多的设置选项。

截图生成的图片保存在 HOME 下。

### shutter

[shutter](http://shutter-project.org/) 是一个功能更强大的截图工具，支持不同的
截图方式、图片格式，还支持图片的简单编辑与注释:

    sudo yum install shutter

可以通过 [修改快捷键使 shutter 成为默认的截图工具](http://shutter-project.org/faq-help/set-shutter-as-the-default-screenshot-tool/)。

## 其他软件

### 文献管理软件 Mendeley

[Mendeley](https://www.mendeley.com/) 是一个跨平台的文献管理软件，其内部自带了
一个可以添加注释的 PDF 阅读器。

下载 Generic Linux (64 bits)：https://www.mendeley.com/download-desktop/

安装:

    # 解压
    tar -xvf mendeleydesktop-1.17.13-linux-x86_64.tar.bz2
    # 复制到 /opt 目录下
    sudo mv mendeleydesktop-1.17.13-linux-x86_64 /opt/mendeleydesktop
    cd /opt/mendeleydesktop/bin   # cd 进去
    ./install-mendeley-link-handler.sh /opt/mendeleydesktop/bin/mendeleydesktop
    sudo yum install qtwebkit  # 安装依赖包

注销重新登陆，在 Application->Education 下即可看到 mendeley 的相关项目。不过是
没有软件的图标的，强迫症不能忍，用下面的命令解决:

    cp /opt/mendeleydesktop/share/icons/hicolor/128x128/apps/mendeleydesktop.png ~/.local/share/icons/

### Google Earth

到 <https://www.google.com/earth/download/ge/agree.html> 下载64位 RPM 包，
执行如下命令安装:

    sudo yum localinstall google-earth-stable_current_x86_64.rpm

一般用户也可以直接使用 web 版，地址为 https://earth.google.com/web 。

### 解压软件

安装如下解压软件:

    sudo yum install unzip   # 支持 zip 格式
    sudo yum install p7zip   # 支持 zip|7z|gzip|bzip2|xz|rpm|iso 等格式
    sudo yum install unar    # 支持多种格式，包括 rar

三者的用法分别为：

    unzip xxx.zip
    7za x xxx.7z
    unar xxx.rar

### FTP 客户端

日常需要使用 FTP 的话，可以安装 FileZilla。

    sudo yum install filezilla

### BT 软件

transmission 是 Linux 下常用的 Torrent 下载软件:

    sudo yum install transmission

在 “Application”->“Internet”-> 中可以启动 transmission。

### PDF 处理工具

[cpdf](http://community.coherentpdf.com/) 是一个跨平台的 PDF 处理工具，可以完成
常见的 PDF 合并、切割、加密解密、书签、水印等功能。

安装及使用说明见 [强大的跨平台 PDF 处理工具：cpdf](/cpdf)

### 视频下载工具

[you-get](https://github.com/soimort/you-get) 和
[youtube-dl](https://github.com/rg3/youtube-dl)
是两个用于从视频网站上下载视频文件的工具。其中，后者支持的网站更多，但前者对
国内的视频网站支持更好。

    pip install you-get
    pip install youtube-dl

### 杂项

    sudo yum install nfs-utils     # 挂载 NFS 文件系统所必须
    sudo yum install xclip         # 终端的文本复制工具
    sudo yum install ImageMagick   # 其中的 import 和 convert 命令很有用
    sudo yum install dos2unix unix2dos  # Windows 和 Linux 换行符互相转换
    sudo yum install meld          # 图形界面下的文件差异比较工具
