---
title: CentOS 7 配置指南 — 效率软件篇
slug: centos7-setup-4
---

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

## 效率类软件

这一类工具能够在不同方面提高科研的效率，也提高了使用者的体验。

### 终端模拟器

Gnome 自带的终端模拟器是 gnome-terminal。经常会需要开十几个终端，切换和管理起来比较麻烦。

#### terminator

terminator 有很多功能，我只用到了终端分割的功能。 `Ctrl+Shift+O` 对终端水平分隔，
`Ctrl+Shift+E` 对终端垂直分隔， `Alt + 上下左右 ` 可以在各子终端中切换:

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

2.  命令补全插件: pip, pyenv
3.  sudo：按两下 `ESC` 即可在当前命令前加上 `sudo`
4.  yum：为常见的 yum 命令提供别名

另外，其中插件 git 为 git 的众多常用命令提供了更简单的别名。其中，插件 `git mergetool --no-prompt` 的别名是 `gmt`，与 GMT 冲突，可以直接注释 `.zshrc` 中的相关内容。

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

### 等宽字体

编程要用等宽字体，这点是常识了。一款适合编程的等宽字体，至少要满足如下几个要求：

1.  易于区分 “1”、“i” 和“l”
2.  易于区分 “0”、“o” 和“O”
3.  易于区分中文下的左引号和右引号
4.  美观

目前选择 Source Code Pro：

    sudo yum install adobe-source-code-pro-fonts
