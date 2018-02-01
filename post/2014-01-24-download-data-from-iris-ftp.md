---
title: IRIS FTP 数据下载的几个方法
date: 2014-01-24
author: SeisMan
categories:
  - 地震学基础
tags:
  - breq_fast
  - IRIS
  - 数据
slug: download-data-from-iris-ftp
---

从 IRIS 申请地震数据，有些工具会将准备好的数据放在 ftp 中，供用户下载。

FTP 地址格式如下： `ftp://ftp.iris.washington.edu/pub/userdata/USERNAME`，其中 `USERNAME` 因人而异。

<!--more-->

## 下载方式

官方提供了三种数据下载方式：

### 登录 FTP 下载

    $ ftp ftp.iris.washington.edu
    Name (iris:joe): anonymous # 匿名登录
    Password: JoeSeismologist@email.net # 密码随意，建议填写邮件地址
    ftp> cd pub/userdata
    ftp> ls -f
    ftp> cd Joe_Seismologist # 进入自己的目录
    ftp> ls -l
    ftp> binary # 二进制传输
    ftp> mget * # 下载所有文件
    ftp> quit

### wget 下载全部文件

    wget -P Directory -m -nd -np -r -c ftp://ftp.iris.washington.edu/pub/userdata/USERNAME/

其中

-   `Directory` 为要保存的文件路径，默认为当前目录；
-   `-m` 等效于 `-r -N -l inf --no-remove-listing` ，其中 `-r` 表示对文件夹进行递归， `-N` 表示只下载比本地文件新的文件； `-l` 指定递归深度， `inf` 表示无穷递归；
-   `-nd` 表示不在本地重建目录结构，这意味着无论 FTP 中的目录结构有多复杂，所有文件都保存到本地的一个目录中；
-   `-np` 表示不遍历父目录；
-   `-r` 表示递归下载；
-   `-c` 表示支持断点续传；

### wget 下载单个或多个文件

    wget -P Directory -m -nd -np -r -c -A "FileName" ftp://ftp.iris.washington.edu/pub/userdata/USERNAME/

其中 `-A` 表示只下载 “FileName” 指定的文件。FileName 可以表示后缀也可以表示模式，当 FileName 中只包含英文字母时，则表示后缀，比如 FileName 为 seed，则表示下载所有以 seed 为后缀的文件。

当 FileName 中包含通配符 `* ? []` 时，FileName 表示模式，只下载文件名符合该模式的文件，比如 FileName 为 `2010*.seed`，则表示只下载所有文件名匹配 `2010*.seed` 的文件。

## 缺点

在大批量数据的情况下，上面三种方法都有一些缺点。

1.  FTP 方法，使用 ftp 自带的 mget 命令进行下载，不支持断点续传，难以指定要下载哪些文件。
2.  wget 下载全部数据，若 FTP 中的数据已存在于当前目录，则不会再次下载。这要求下载好的数据不能从当前目录中移除。一般来说数据下载和数据处理是同步进行的，这样就要求在下载目录中和数据处理目录中存有两份相同的数据。更严重的是，IRIS 的 FTP 数据可以保留 7 天，今天申请的数据与 3 天前申请将会下载到同一目录中，不利用用户对 SEED 文件进行整理。
3.  wget 下载指定数据，如果每次申请的数据是有规律的，比如先申请 2004 年数据，申请 -\> 等待 -\> 下载，再申请 2005 年数据，这样可以使用通配符来指定下载数据。若数据申请没有类似规律，则会非常麻烦。理论上，使用 BREQ\_FAST 申请数据时，可以为数据指定 LABEL，则 SEED 文件名为 LABEL.xxxx.seed，其中 xxxx 为 "随机数"，因而用户在申请时是无法完全知道 seed 文件的全名的，又因为 wget 不支持 `wget http://example.com/20100101.*.seed` 这样的语法，因而对于数据申请不规律的情况，第三种方法也是很有问题的。
