---
title: GMT4 与 GMT5 双版本共存
date: 2013-11-09
updated: 2015-06-09
author: SeisMan
categories: GMT
tags: [GMT技巧]
---

随着 GMT5 的发布，GMT 目前存在两个大版本：GMT4 和 GMT5。

GMT4 会继续维护更新直到 GMT6 的发布，但只修订 bug，不会再增加新功能。GMT5 在 GMT4 的基础上重新整理了代码，并加入了不少新功能，语法也与 GMT4 不兼容，因而，GMT5 相对来说 bug 可能会更多一些。

对于 GMT 新手来说，建议直接学习 GMT5；对于 GMT 老手来说，可以继续使用 GMT4，也可以开始逐渐使用 GMT5。

一些旧脚本可能是用 GMT4 的命令与语法写的，在 GMT5 下直接运行可能会有问题。把旧脚本从 GMT4 语法改成 GMT5 语法比较麻烦且没有必要。因而最好的方式是，在系统中同时安装 GMT4 和 GMT5，旧脚本使用 GMT4 的语法，新脚本使用 GMT5 的语法。

GMT 官方提供了两种方法，可以实现多版本 GMT 的切换。但这两种方法，要么需要对绘图脚本做额外修改，要么需要在每次执行脚本前做额外操作，因而比较麻烦，不推荐使用。有兴趣的可以自己看官方文档。

下面介绍的方法可以在不需要额外修改的情况下，指定脚本使用 GMT4 还是 GMT5。

<!--more-->

## 安装 GMT4 和 GMT5

首先，当前系统需要安装 GMT4 和 GMT5 两个版本，然后，需要将两个版本的路径都添加到 PATH 中。

Linux 用户可以向 `~/.bashrc` 中加入如下语句：

``` bash
# GMT 4
export GMT4_HOME=/opt/GMT-4.5.11
export PATH=${GMT4_HOME}/bin:$PATH

# GMT 5
export GMT5_HOME=/opt/GMT-5.1.0
export PATH=${GMT5_HOME}/bin:$PATH
```

Windows 用户类似，也要把两个版本的 bin 目录的路径加到 PATH 中。

## GMT5 的命令格式

严格的说，GMT5 中只有一个可执行文件： `gmt` ，所有的命令都应以 `gmt` 开头，命令格式如下:

    gmt module -Axxx -Bxxx

GMT4 中的所有命令在 GMT5 中都作为命令 `gmt` 的一个模块来调用。比如 GMT4 的 `pscoast` 命令在 GMT5 中应该使用 `gmt pscoast` 来调用。

在使用 GMT5 时，应严格按照 `gmt module` 这样的格式调用。这样，随便打开一个脚本，看到 `pscoast` 就知道是 GMT4 的语法，看到 `gmt pscoast` 就知道是 GMT5 语法。

## 删除软链接

GMT5 为了兼容 GMT4 的语法，在 bin 目录下建立了一堆指向 `gmt` 的软链接。进入 GMT5 的 bin 目录，其中 `gmt` 为可执行文件， `gmt-config` 、`gmt_shell_functions.sh` 、 `gmtswitch` 、 `isogmt`
为 Bash 脚本，其余都是指向可执行文件 `gmt` 的符号链接，把这些直接删除。

最简单的删除符号链接的办法是在安装 GMT 的时候就不生成这些符号链接。在编译 GMT5 之前，修改 `cmake/ConfigUser.cmake` 时，其中有一行:

    #set (GMT_INSTALL_MODULE_LINKS FALSE)

将该行前的 `#` 去掉，即设置 `GMT_INSTALL_MODULE_LINKS=FALSE`，则在安装过程中就不会创建符号链接了。

如果安装的过程中创建了符号链接，可以使用如下命令将这些符号链接删除:

    $ cd /opt/GMT-5.1.0/bin/
    # 建立临时目录，需要 Root 权限
    $ sudo mkdir temp
    $ sudo mv gmt gmt-config gmtlogo gmt_shell_functions.sh gmtswitch isogmt temp/
    $ sudo rm * # 删除除 temp 目录之外的全部符号链接
    rm: 无法删除 "temp": 是一个目录
    # 将 temp 目录下的文件复制回 bin 下
    $ sudo mv temp/* .
    # 删除 temp 目录
    $ sudo rmdir temp/

对于 Windows 用户，bin 目录下会有很多文件，可以将该目录下的所有文件按照大小排序，所有大小为 6
KB 的都是 “符号链接”，直接选中删除就好。

## 不兼容模式

GMT5 提供了兼容模式，可以部分兼容 GMT4 的语法，但推荐使用不兼容模式。原因如下：

1.  通常来说，兼容模式有更多的 bug；
2.  GMT5 并不能完全兼容 GMT4，因而有些用法在一个命令下是有效的，在另一个命令下却是无效的；
3.  使用兼容模式，可能到导致一个命令中既有 GMT4 语法也有 GMT5 语法，调试变得困难；
4.  使用不兼容模式，有助于用户熟悉 GMT5 语法；

要让 GMT5 不再兼容 GMT4，只需要将 `GMT5/share/conf/gmt.conf` 中的:

    GMT_COMPATIBILITY = 4

改成:

    GMT_COMPATIBILITY = 5

## 测试一下

终端输入 `psxy -` 会看到命令的版本是 GMT 4.5.xx。

终端输入 `gmt psxy -` 会看到命令版本为 GMT 5.1.xx。

## 修订历史

-   2013-11-09：初稿；
-   2015-06-07：重整文章布局；
