---
title: CentOS 7 配置指南 — 效率软件篇
author: SeisMan
date: 2014-07-15
lastmod: 2018-04-16
slug: centos7-setup-5
---

## zsh 与 oh my zsh

推荐所有用户使用 zsh 和 oh my zsh！

Linux 下有很多 shell，比如最常见的 bash，除此之外还有 csh、ksh。zsh 也是一个 shell。

zsh 的特点在于：

-   语法基本完全兼容于 bash，一般用户完全体会不到其区别
-   zsh 提供命令补全特性，比 bash 的补全要更好用
-   可配置性强

完全不经配置的 zsh 已经很好用了，一般用户也没必要花时间研究配置。
[oh my zsh](https://github.com/robbyrussell/oh-my-zsh) 是一群人一起维护的
一套 zsh 配置文件。直接用这个配置文件，稍稍了解一点会有更好的体验。

安装 zsh:

    sudo yum install zsh

安装 oh my zsh:

    curl -L http://install.ohmyz.sh | sh

上面的命令，做了如下几件事情：

-   下载 `oh my zsh` 到 `~/.oh-my-zsh`
-   备份已有的 zsh 配置文件 `~/.zshrc`，并生成默认的 `.zshrc` 文件
-   将当前用户的默认 shell 由 bash 改成 zsh

第三步中，会报错如下： `chsh: "/usr/bin/zsh" is not listed in /etc/shells.`，
需要手动修改默认 shell:

    chsh -s /bin/zsh

chsh 命令修改的是 login shell，因而需要退出当前用户并重新登陆，以后用户的默认
shell 就从 bash 变成了 zsh，所有的配置都不用写到 `.bashrc` 而要写到 `.zshrc` 中。

在 `.zshrc` 中可以选择喜欢的主题，以及适当数量的插件。我在用的 zsh 主题是 `bira`。

我在用的插件包括：

1.  `autojump`: 下面会提到；
2.  `extract`: 使用 `x abc.zip` 语法即可解压几乎所有压缩文件；
3.  `sudo`: 按两下 `ESC` 即可在当前命令前加上 `sudo`

另外，其中插件 git 为 git 的众多常用命令提供了更简单的别名。其中，插件
`git mergetool --no-prompt` 的别名是 `gmt`，与 地学软件 GMT 冲突，建议在
`.zshrc` 中不启用 git 插件。

更多信息见[官方网站](http://ohmyz.sh/)。

## autojump

[autojump](https://github.com/joelthelion/autojump) 是一个非常智能的目录快速
切换的工具。简单演示如下:

    $ pwd
    /home/seisman
    $ cd Desktop
    $ cd /opt
    $ cd /usr/local

    # 用 j 命令迅速从 /usr/local 跳转到与 des 匹配的目录，这里只有 Desktop 可以匹配
    $ j des
    $ pwd
    /home/seisman/Desktop

用法差不多就这样，具体看项目主页。

安装:

    sudo yum install autojump
    sudo yum install autojump-zsh

## 终端模拟器

GNOME 自带的终端模拟器是 gnome-terminal。使用起来中规中矩。
经常会需要开十几个终端，切换和管理起来比较麻烦。

### terminator

terminator 是一个功能强大的终端。其众多功能中我只用到了终端分割的功能。

以下快捷键用于对终端进行分屏：

- `Ctrl+Shift+O` 对终端水平分隔，
- `Ctrl+Shift+E` 对终端垂直分隔，
- `Alt + 上下左右` 可以在各子终端中切换；

安装:

    sudo yum install terminator

### guake

有些时候需要临时执行一两个命令，但是又不想额外启动一个终端的情况下，guake
是个不错的选择。

    sudo yum install guake

安装完成后，在 “Application”->“System Tools” 里找到 guake Terminal 即可启动。
启动 guake 后，按下 F12 即可呼出 guake，再次按下 F12 即可隐藏 guake。
也可在终端执行 `guake-prefs` 对 gauke 进行配置。

## 等宽字体

编程要用等宽字体，这点是常识了。一款适合编程的等宽字体，至少要满足如下几个要求：

1.  等宽
2.  易于区分 `1`、`i` 和 `l`
3.  易于区分 `0`、`o` 和 `O`
4.  易于区分中文下的左引号和右引号
5.  美观

可以到 http://www.programmingfonts.com 查看一些常见的等款字体及其效果。

我目前选择的是 Adobe 出的 Source Code Pro，这款字体可以直接安装:

    sudo yum install adobe-source-code-pro-fonts

若想要其他等宽字体，可以自行下载字体文件并放在 `~/.fonts` 目录下。

安装完字体后，即可把终端、编辑器等的默认编程字体都改为对应字体即可。

## open命令

在 `~/.zshrc` 中加入如下语句：

    alias open="xdg-open"

即可用 `open filename` 的形式在命令行用默认软件打开 PDF、PNG等格式了。

## 编辑器

写代码的时候选一个好用的编辑器很重要，用的比较多的编辑器如下：

1.  vim
2.  emacs
3.  [atom](http://atom.io/)
4.  [Visual Studio Code](https://code.visualstudio.com/)
5.  [sublime text 3](https://www.sublimetext.com/)

## zeal

[zeal](https://zealdocs.org/) 是一个模仿 [Dash](https://kapeli.com/dash) 的离线
文档查看器，一个软件集合了多种编程语言的文档，专为编程人员设计。

可以直接用别人提供的安装源:

    wget https://copr.fedorainfracloud.org/coprs/abn/zeal/repo/epel-7/abn-zeal-epel-7.repo
    sudo mv abn-zeal-epel-7.repo /etc/yum.repos.d
    sudo yum install zeal

也可以 [自行编译安装](https://gist.github.com/brendanjcaffrey/b144b51c6954d17596f5533c5000d8ae)。

安装完成后可以在Applications->Programming里找到它。启动之后，点击Tools->Docsets
添加不同语言的文档即可使用。

## 修订历史

- 2014-07-15: 初稿；
- 2018-04-16: 增加zeal；
