---
title: Perl 多版本共存之 plenv
date: 2013-11-03
author: SeisMan
categories:
  - 编程
tags:
  - 安装
  - Perl
slug: perl-plenv
---

官方网站：<https://github.com/tokuhirom/plenv>

<!--more-->

## 安装 plenv

``` bash
$ git clone git://github.com/tokuhirom/plenv.git ~/.plenv
$ echo 'export PATH="$HOME/.plenv/bin:$PATH"' >> ~/.bashrc
$ echo 'eval "$(plenv init -)"' >> ~/.bashrc
$ exec $SHELL -l
```

## 安装 plenv 的 build 插件

``` bash
$ git clone git://github.com/tokuhirom/Perl-Build.git ~/.plenv/plugins/perl-build/
```

## 查看所有可以安装的版本

``` bash
$ plenv install --list
```

Perl 的版本格式为 `5.xx.x` ，其中 `xx` 为偶数的版本为稳定版。

## 安装指定版本

``` bash
$ plenv install 5.18.1
```

## 更新数据库

``` bash
$ plenv rehash
```

## 修改全局 Perl 版本

``` bash
$ plenv versions
$ plenv global 5.18.1
```

## 安装 cpanm

Perl 的 `cpan` 工具可以方便的安装和管理众多模块。`cpanm` 与 `cpan` 类似，其功能更强大，
其可以根据当前的 Perl 版本，将模块安装到对应的路径中，而不会对系统自带的 Perl
模块以及其他 Perl 版本的模块进行任何修改。

``` bash
$ plenv install-cpanm
```
