---
title: Python 科学计算发行版 --Anaconda
date: 2014-05-14 13:00
author: SeisMan
categories: 编程
tags: Python
---

Python 是一种强大的编程语言，其提供了很多用于科学计算的模块，常见的包括
numpy、scipy 和 matplotlib。要利用 Python 进行科学计算，就需要一一安装所需的模块，
而这些模块可能又依赖于其它的软件包或库，因而安装和使用起来相对麻烦。幸好有人
专门在做这一类事情，将科学计算所需要的模块都编译好，然后打包以发行版的形式
供用户使用，Anaconda 就是其中一个常用的科学计算发行版。

主页： <https://store.continuum.io/cshop/anaconda/>

<!--more-->

Anaconda 的特点：

-   包含了众多流行的科学、数学、工程、数据分析的 [Python 包](http://docs.continuum.io/anaconda/pkgs.html)
-   完全开源和免费
-   额外的加速、优化是收费的，但对于学术用途可以申请免费的 License
-   全平台支持：Linux、Windows、Mac
-   支持 Python 2.6、2.7、3.3、3.4，可自由切换

## 安装

1.  安装 pyenv

    安装 anaconda 之后，系统内就会存在两个版本的 Python：anaconda 以及系统自带的 Python。

    为了保证两个 Python 版本之间不相互干扰，需要使用专门的工具来管理多个 Python 版本。这里选择的工具是 pyenv。

    pyenv 的安装可以参考《[Python 多版本共存之 pyenv](/python-pyenv.html)》。

    当然，也可以不使用 pyenv，而直接从其官方网站下载： <http://continuum.io/downloads> 。
    此时用户需自行承担可能的版本冲突。

2.  安装 anaconda

    Anaconda 支持 Python 2 和 Python 3，但二者是分开的，用户需要自己选择使用
    Python 2 还是 Python 3。当然，借助于 pyenv 的版本管理功能，同时装两个版本也是没问题的。

    安装支持 Python 2.7 的 Anaconda:

        $ pyenv install anaconda-2.0.1 -v

    安装支持 Python 3.4 的 Anaconda:

        $ pyenv install anaconda3-2.0.1 -v

3.  申请免费的学术 License

    对于学生来说，可以申请免费的学术 License，以安装额外的功能包，以实现计算过程的加速。

    申请地址： <https://store.continuum.io/cshop/academicanaconda>

    申请后，会得到一个 license 文件，将其放在 `~/.continuum` 目录下即可。

4.  安装额外的功能包

    ``` bash
    $ conda update conda
    $ conda install accelerate
    $ conda install iopro
    ```

## 安装模块

Anaconda 已经自带了大量科学计算中的常用模块，可以直接使用。有时需要安装一些其他 python 模块。

### conda

anaconda 自带了 conda 命令用于安装与更新模块，比如:

    # 安装模块
    conda install scipy
    # 更新模块
    conda update scipy
    # 更新所有模块
    conda update --all

不过 conda 能安装的模块很有限。

### pip

pip 是 Python 自带的模块安装工具，比如:

    pip install requests
    pip install requests --upgrade

### 升级 Anaconda

新版本发布之后，可以使用 pyenv 安装 Anaconda 的最新版本，也可以用 Anaconda 的自带更新工具升级:

    conda update conda
    conda update anaconda
