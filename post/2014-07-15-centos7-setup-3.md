---
title: CentOS 7 配置指南 — 脚本语言篇
slug: centos7-setup-3
---

## 脚本语言环境

### Perl

CentOS 7.0 自带了 Perl 5.16.3（2013 年 03 月 11 日发布），目前的最新版本为 5.26.1。

#### 系统自带 Perl

系统自带 Perl，就目前来看，版本不算老，基本够用。官方源和 EPEL 源中提供了 1000 多个模块，可以直接用 yum 安装:

    sudo yum install perl-Parallel-ForkManager  # 并行模块

若源中没有已打包好的模块，也可以使用 perl 自带的 cpan 来安装模块。

优先级：yum > cpan。

#### plenv 管理新版本

若需要使用最新版本的 perl，可以使用 [plenv](/perl-plenv.html) 安装新版本的 perl，并使用 plenv 提供的 cpanm 命令安装模块:

    cpanm install Parallel::ForkManager # 并行模块

### Python

直接安装anaconda

http://wiki.seisman.info/python/install-python/
