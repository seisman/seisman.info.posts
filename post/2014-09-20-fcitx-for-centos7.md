---
title: CentOS 7 安装 fcitx 中文输入法
author: SeisMan
date: 2014-09-20
lastmod: 2015-03-09
categories:
  - Linux
tags:
  - CentOS
  - 中文
slug: fcitx-for-centos7
---

**本文不再更新**

目前不确定是否可行，具体参考： <https://github.com/1dot75cm/myrepo>

前面 [CentOS7.0 下安装小小输入法](/install-yong-chinese-input-method-under-centos-7/) 一文中已经介绍了如何在 CentOS7 下安装小小输入法来输入中文，实际用起来还是有不少不如意的地方。

今天恰好发现了 CentOS 7 下安装 fcitx 输入法的简单方法，如下。

<!--more-->

## 加入 EPEL 源

EPEL7 几乎是 CentOS 必备的源:

    $ sudo yum install epel-release

## 添加 mosquito-myrepo 源

mosquito-myrepo 是一个私人制作的第三方源，其中包含了 fcitx 输入法。

-   项目地址： <https://github.com/1dot75cm/myrepo>
-   支持的发行版： Fedora 19/20/21/rawhide 以及 RHEL/CentOS 7

        $ sudo yum-config-manager --add-repo=https://copr.fedoraproject.org/coprs/mosquito/myrepo/repo/epel-7/mosquito-myrepo-epel-7.repo

## 安装输入法

可以选择下面的各种输入法中的某一个或多个:

    $ yum install fcitx-googlepinyin fcitx-cloudpinyin # 谷歌拼音输入法
    $ yum install fcitx-rime fcitx-cloudpinyin # 中州韵输入法
    $ yum install fcitx-libpinyin fcitx-cloudpinyin # libpinyin 输入法
    $ yum install fcitx-sunpinyin sunpinyin-data fcitx-cloudpinyin # sunpinyin 输入法

## 清理工作

mosquito-myrepo 在不断地支持更多的软件，这也进一步造成该 repo 中的软件与 base、EPEL 中的软件存在版本冲突，在该 repo 的项目主页中建议安装 yum 的优先级插件 `yum-plugin-priorities`，这在一定程度上会缓解版本冲突问题，但无法从根本上避免。

鉴于多个 repo 的版本冲突会造成一些麻烦，最好的办法还是在安装完需要的软件之后就禁用该 repo，需要的时候再启用。

编辑 `/etc/yum.repos.d/mosquito-myrepo-epel-7.repo` ，将其中的 `enable=1` 改成 `enable=0` 即可。

## 参考

-   <https://copr.fedoraproject.org/coprs/mosquito/myrepo/>

## 修订历史

-   2014-09-20：初稿；
-   2014-09-29：安装完成之后建议禁用该 repo 以避免任何可能的版本冲突；
-   2014-12-27：更新 sogou 的配置；
-   2015-03-09：由于搜狗输入法是私有软件，违反了 copr 的相关规定，因而目前该源中已不再包含搜狗输入法。故删除本文中搜狗输入法相关部分；
