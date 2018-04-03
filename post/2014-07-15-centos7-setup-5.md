---
title: CentOS 7 配置指南 — 日常软件篇
slug: centos7-setup-5
---

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

    sudo yum localinstall https://code-industry.net/public/master-pdf-editor-4.3.89_qt5.x86_64.rpm

### TeX Live

系统是自带了 TeXLive，版本较老，还是安装最新版比较好。

参考 [Linux 下安装 TeXLive](http://blog.seisman.info/texlive-install/) 一文。

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

到 <https://www.google.com/earth/download/ge/agree.html> 下载64位rpm包，执行如下命令安装:

    sudo yum localinstall google-earth-stable_current_x86_64.rpm

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

    sudo yum localinstall https://code-industry.net/public/master-pdf-editor-4.3.89_qt5.x86_64.rpm

### TeX Live

系统是自带了 TeXLive，版本较老，还是安装最新版比较好。

参考 [Linux 下安装 TeXLive](http://blog.seisman.info/texlive-install/) 一文。

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

到 <https://www.google.com/earth/download/ge/agree.html> 下载64位rpm包，执行如下命令安装:

    sudo yum localinstall google-earth-stable_current_x86_64.rpm


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


### 其他工具

    sudo yum install nfs-utils     # 挂载 NFS 文件系统所必须
    sudo yum install xclip         # 终端的文本复制工具
    sudo yum install ImageMagick   # 其中的 import 和 convert 命令很有用
    sudo yum install dos2unix unix2dos  # Windows 和 Linux 换行符互相转换
    sudo yum install meld          # 图形界面下的文件差异比较工具
