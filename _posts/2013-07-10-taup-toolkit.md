---
title: 走时计算软件 TauP
date: 2013-07-10
updated: 2016-02-24
author: SeisMan
categories: 地震学软件
tags: [走时, TauP]
---

## 基本信息

1.  开发者： [University of South Carolina](http://sc.edu/)
2.  语言：Java
3.  平台：跨平台，Windows、Linux、Mac 等
4.  与 ttimes 一样，其原理基于 Buland 和 Chapman 于 1983 年提出的方法

<!--more-->

## 功能与特色

相对于 ttimes 而言，TauP 具有更多的功能和特色：

1.  可以计算震相走时、射线参数、反射点、穿透点、射线路径、走时曲线等
2.  支持自定义速度模型
3.  内置震相解析器，支持不常见的震相名
4.  自带多个预定义地球模型：iasp91、prem、ak135、jb、1066a、1066b、pwdk、sp6、herrin
5.  部分兼容 ttimes，比如用 ttp 表示常见 P 波震相，除此之外，还有 tts、ttp+、tts+、ttbasic、ttall
6.  采用线性插值，可能带来 0.01 秒的误差
7.  直接在球坐标系下求解方程，不必做展平变换；与部分震相的解析解相比，最大误差为 0.01 秒，而 ttimes 的最大误差为 0.05 秒

目前来看的缺点是：

1.  不支持 Pg、PKPab、PKPbc 等震相名
2.  输出的格式不够灵活，有时需要自己写脚本从输出中提取信息

## 工具

TauP 提供了多个工具，包括有图形界面的 `taup` ，交互式的 `taup_console`，以及命令行工具 `taup_time` 、
`taup_pierce` 、 `taup_setsac` 、`taup_path` 、 `taup_curve` 、 `taup_create` 、 `taup_table` 、
`taup_wavefront` 。

## TauP 系列博文

1.  [安装 TauP](/install-taup.html)
2.  [用 taup\_time 计算震相走时及射线信息](/calculate-travel-time-using-taup.html)
3.  [用 taup\_pierce 计算射线的界面的穿透点](/calculate-pierce-points-using-taup.html)
4.  [用 taup\_setsac 将走时信息写入 SAC 文件](/mark-travel-time-using-taup.html)
