---
title: CentOS 7.0 下安装小小输入法
author: SeisMan
date: 2014-07-12
categories:
  - Linux
tags:
  - CentOS
  - 中文
slug: install-yong-chinese-input-method-under-centos-7
---

另一篇博文： [CentOS7.0 下安装搜狗输入法](/fcitx-for-centos-7.html)

小小输入法也叫 yong 输入法，是一个免费但不开源的中文输入法，其作者为 dgod，2008 年发布第一个版本，至今六年时间依然在不断的更新。以一人之力默默维护一个项目 6 年时间，不得不让人佩服。

-   官方网址： <http://yong.dgod.net/>
-   下载地址： <http://yongim.ys168.com/>

<!--more-->

曾经试图在 CentOS 6.5 下安装该输入法，无奈 CentOS6.5 的库版本太低，一直安不上。下面记录一下在 CentOS 7.0 下的安装过程。

1.  从官方网站下载 Linux 下的最新版本 `yong-lin-2.2.0-1.7z` 。
2.  解压。7z 格式的压缩文件需要安装 `p7zip` 方可解压，在 EPEL 源中有提供该软件。
3.  安装

    ``` bash
    $ cd yong
    $ su
    # ./yong-tool.sh --install64   # 安装
    # ./yong-tool.sh --select      # 设置为默认输入法
    ```

    想要卸载 yong

    ``` bas
    # ./yong-tool.sh --uninstall
    ```

4.  系统启用中文输入源

    在 “Application”-\>“System Tools”-\>“Region&Language”-\>“Input Source” 中添加中文输入源“Chinese(yong)”。也可以考虑删除 `English(US)` 输入法，直接使用 yong 自带的功能切换中英文输入法。

5.  似乎需要关机重启。重启之后，在桌面右上角即出现了中英文输入法的图标。

需要注意的是，yong 的安装其实只是在 `/usr/bin` 下建立了两个软链接 `yong` 和 `yong-config` ，并且在 `${HOME}` 下建立了文件夹 `.yong` ，其中包含了 yong 的配置文件。因而在第二步中解压的 yong 文件夹不可删除。

yong 的配置文件位于 `~/.yong/yong.ini`，可以根据需要修改，或者也可以直接用 `yong-config` 命令调出图形界面来修改。

我的配置如下：

-   输入法状态栏主窗口位于左下角。由于使用了双显示器，默认的窗口位于右下角会使得状态栏位于另一个显示器。（使用过程中发现，在终端全屏的情况下，状态栏位于左下角会挡住部分终端的命令，目前没有合适的解决办法。或许可以考虑顶部居中。）
-   在系统输入源中删除英文输入，只留下中文的 yong 作为唯一输入源。使用默认的 `Ctrl+LShift` 作为切换输入法的快捷键。中英文切换快捷键设置为 `Ctrl+Space` 。默认的中英文切换键是 `LSHIFT` ，但是由于我习惯使用 `LSHIFT + 字母 ` 的方式来临时输入大写字母，所以如果使用 `LSHIFT` 进行中英文切换的话很容易导致误操作。
-   yong 自带了七种输入法，我只有拼音输入法，因而删除其他输入法，只留下 pinyin 输入法，并设其为默认值；
-   小小输入法支持百度、google、微软、QQ 和搜狗等云输入法，可以自行配置。配置如下:

        1=BaiduCloud

        [cloud]
        name = 百度云
        engine=libcloud.so
        arg=baidu

    其他云输入法类似，其中 arg 可以取 baidu、google、qq、sogou、microsoft 等（似乎 sogou 和 microsoft 都不支持了？）。
-   默认使用 QQ 云输入法，特殊情况切换到百度云或谷歌云。由于国内连接的问题，使用谷歌云的时候有很明显的时间延迟，不建议使用。
-   yong 输入法还支持自定义皮肤或使用别人设计的皮肤，将下载的皮肤文件放在 `~/.yong/skin` 下即可。
-   一个不太方便的一点是状态栏貌似无法显示当前正在使用的中文输入法是哪一个。
-   在配置文件中的 `[IM]` 里加入 `ABCD=1`，这样在中文输入法的情况下按下 SHIFT 以及字母会直接将相应的大写字母输出出来，不必再经过中文输入法。

参考:

-   <http://www.mintos.org/software/xiaoxiao-input.html>
-   <http://yong.dgod.net/read.php?tid=5&fid=7>
-   <http://yong.dgod.net/read.php?tid=25&fid=7>
-   <http://yong.dgod.net/read.php?tid=18&fid=7>

