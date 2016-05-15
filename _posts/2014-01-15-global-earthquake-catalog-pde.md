---
title: 全球地震目录 PDE
date: 2014-01-15
author: SeisMan
categories: 地震学基础
tags: [USGS, 地震目录, 震源机制解, 震级]
---

## 简介

PDE，是 USGS 的 NEIC 组织发布的全球地震目录，全称 Preliminary Determination of Epicenters。之所以称为 Preliminary，是因为一般认为 International Seismological Centre 发布的地震目录是终极版。

主页： <http://earthquake.usgs.gov/research/data/pde.php>

<!--more-->

## 目录

一个完整的 PDE 目录包含了三个部分：daily PDE、weekly PDE 以及 monthly PDE。

### Daily PDE

又称为 QED(Quick Epicenters Determinations) 或 PDE-Q，包含了最近六周的地震事件，每日更新。一段时间以后，Daily PDE 中的地震事件会被删除，然后该事件会被添加到 Weekly PDE 中。

### Weekly PDE

又称为 PDE-W，一般含有 6 周以前到几个月以前的地震事件，每年 52 个文件，每个文件包含 7 天的数据（最后一个文件包含 8 或 9 天数据）。Daily
PDE 中的事件经过修正之后会加入到 Weekly PDE 中，Weekly
PDE 中的事件在添加了一些注释信息后会从 PDE-W 中删除，并添加到 Monthly
PDE 中。

### Monthly PDE

PDE 地震目录的终极版。

## 文件格式

三种文件格式：mchedr、ehdf、isf。

### 格式说明

-   mchedr： <ftp://hazards.cr.usgs.gov/weekly/mchedr.txt>
-   ehdf： <ftp://hazards.cr.usgs.gov/weekly/ehdf.txt>
-   isf: <ftp://colossus.iris.washington.edu/pub/ISF/isf_ext.pdf>

### 简单说明

ehdf 格式，一个事件一行记录，包含了发震时刻、震源深度、震级以及其他少量信息，一般情况下已经够用。

mchedr 格式，一个事件多行记录，除包含了 ehdf 格式的信息之外，还包含了地震宏观观测、震相和振幅信息，适合有特殊需求的人使用。

isf 格式主要是用来与其他机构的地震目录进行数据交换用的，一般用不到。

## 链接

-   Monthly PDE： <ftp://hazards.cr.usgs.gov/pde/>
-   Weekly PDE： <ftp://hazards.cr.usgs.gov/weekly/>

