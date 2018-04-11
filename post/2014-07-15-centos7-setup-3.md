---
title: CentOS 7 配置指南 — 脚本语言篇
author: SeisMan
date: 2014-07-15
lastmod: 2018-04-12
slug: centos7-setup-3
---

## Perl 环境

CentOS 7 自带了 Perl 5.16.3（2013 年 03 月 11 日发布），目前的最新版本为 5.26.1。

对于 Perl 轻度用户而言，建议直接使用系统自带Perl；
对于 Perl 重度用户（即经常安装并使用第三方模块），建议使用 plevn 安装最新版本。

### 系统自带 Perl

系统自带 Perl 基本可以满足 Perl 轻度用户的需求。官方源和 EPEL 源中提供了
1000 多个 Perl 模块，可以直接用 yum 安装。例如：

    sudo yum install perl-Parallel-ForkManager  # 并行模块

### plenv 管理新版本

[plenv](https://github.com/tokuhirom/plenv) 是一个 Perl 版本管理工具。
可以使用 plenv 安装新版本的 Perl，且不与系统自带 Perl 发生冲突，安装及使用
教程见 [Perl 多版本共存之 plenv](/plenv)。

可以使用 plenv 提供的 `cpanm` 命令安装 Perl 模块的最新版本:

    cpanm install Parallel::ForkManager # 并行模块

## Python 环境

CentOS 7 自带 Python 2.7.5，目前 Python 的主流版本为 3.6.5。

强烈推荐学习和使用 Python 3！
建议不要使用系统自带的Python！
建议直接使用 [Anaconda](/anaconda) 安装最新版本的Python！

Anaconda 的简介及使用说明见 [Python科学计算发行版 — Anaconda](/anaconda)。

Anaconda 自带了众多科学计算所需的包，免去了手动编译安装的麻烦。
对于其他包，则可以利用 Anaconda 提供的 `conda` 命令或 Python 提供的 `pip`
命令安装，例如：

    conda install requests
    pip install sphinx_rtd_theme
