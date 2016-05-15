---
title: Python 多版本共存之 pyenv
date: 2013-10-04 00:27
author: SeisMan
categories: 编程
tags: [安装, Python]
---

经常遇到这样的情况：

- 系统自带的 Python 是 2.6，自己需要 Python 2.7 中的某些特性；
- 系统自带的 Python 是 2.x，自己需要 Python 3.x；

此时需要在系统中安装多个 Python，但又不能影响系统自带的 Python，即需要实现
Python 的多版本共存。[pyenv](https://github.com/yyuu/pyenv) 就是这样一个 Python 版本管理器。

## 安装 pyenv

``` bash
$ git clone git://github.com/yyuu/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"'>> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"'>> ~/.bashrc
$ echo 'eval"$(pyenv init -)"' >> ~/.bashrc
$ exec $SHELL -l
```

## 安装 Python

### 查看可安装的版本

``` bash
$ pyenv install --list
```

该命令会列出可以用 pyenv 安装的 Python 版本，仅列举几个:

    2.7.8   # Python 2 最新版本
    3.4.1   # Python 3 最新版本
    anaconda-4.0.0  # 支持 Python 2.6 和 2.7
    anaconda3-4.0.0 # 支持 Python 3.3 和 3.4

其中形如 `x.x.x` 这样的只有版本号的为 Python 官方版本，其他的形如 `xxxxx-x.x.x`
这种既有名称又有版本后的属于 “衍生版” 或发行版。

### 安装 Python 的依赖包

在安装 Python 时需要首先安装其依赖的其他软件包，已知的一些需要预先安装的库如下。

在 CentOS/RHEL/Fedora 下:

    sudo yum install readline readline-devel readline-static
    sudo yum install openssl openssl-devel openssl-static
    sudo yum install sqlite-devel
    sudo yum install bzip2-devel bzip2-libs

### 安装指定版本

使用如下命令即可安装 python 3.4.1：

```bash
$ pyenv install 3.4.1 -v
```

该命令会从 github 上下载 python 的源代码，并解压到 / tmp 目录下，然后在 / tmp 中执行编译工作。
若依赖包没有安装，则会出现编译错误，需要在安装依赖包后重新执行该命令。

如果网络不太好，用 pyenv 下载会比较慢，可以先执行该命令，然后到 `~/.pyenv/cache`
目录下查看要下载的文件的文件名，然后自己到官方网站下载，并将文件放在 `~/.pyenv/cache`
目录下。pyenv 会检查文件的完整性，若确认无误，则不会再重新下载。

对于科研环境，更推荐安装专为科学计算准备的 Anaconda 发行版，
`pyenv install anaconda-4.0.0` 安装 Python 2.x 版本，
`pyenv install anaconda3-4.0.0` 安装 Python 3.x 版本；

### 更新数据库

安装完成之后需要对数据库进行更新：

``` bash
$ pyenv rehash
```

### 查看当前已安装的 python 版本

``` bash
$ pyenv versions
* system (set by /home/seisman/.pyenv/version)
3.4.1
```

其中的星号表示当前正在使用的是系统自带的 python。

### 设置全局的 python 版本

``` bash
$ pyenv global 3.4.1
$ pyenv versions
system
* 3.4.1 (set by /home/seisman/.pyenv/version)
```

当前全局的 python 版本已经变成了 3.4.1。也可以使用 `pyenv local` 或 `pyenv shell`
临时改变 python 版本。

### 确认 python 版本

``` bash
$ python
Python 3.4.1 (default, Sep 10 2014, 17:10:18)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

## 使用 python

-   输入 `python` 即可使用新版本的 python；
-   系统自带的脚本会以 `/usr/bin/python` 的方式直接调用老版本的 python，
    因而不会对系统脚本产生影响；
-   使用 `pip` 安装第三方模块时会安装到 `~/.pyenv/versions/3.4.1` 下，
    不会和系统模块发生冲突。
-   使用 `pip` 安装模块后，可能需要执行 `pyenv rehash` 更新数据库；

## 参考

1.  <https://github.com/yyuu/pyenv>

## 修订历史

-   2013-10-04：初稿；
-   2014-10-07：将 Python 依赖包一段的位置提前；
