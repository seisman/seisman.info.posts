---
title: 地震学断层的定义
date: 2013-09-26
author: SeisMan
categories:
  - 地震学基础
tags:
  - 名词解释
  - 断层
  - 震源机制解
mathjax: true
slug: faults-in-seismology
---

地震学中最重要的源是 double couple 源，也就是常说的位错源，位错源的产生实质就是断层的滑动。

断层及断层的滑动有几个基本参数：走向、倾角、滑移角以及滑移量。很多参数，地震学和地质学中的定义不同，
即便是地震学里也有不同的定义。Aki and Richards (1980) 的定义应该是用得最多的定义。

<!--more-->

## Aki and Richards 对断层的定义

Aki and Richards (1980) 对于断层参数的定义如下图:

![](/images/2013092601.jpg)

## 断层几何

断层的几何形态由走向（strike）和倾角（dip）两个量完全决定。

一个断层有两个表面，分别称之为上盘（hanging wall）和下盘（foot wall），图中所示为断层的 foot wall。

断层面与水平地表面存在一交线，一条线存在两个方向，哪个方向才是真正的走向呢？地震学里的定义是 “当观测
者沿着走向方向看时，hanging wall 位于观测者的右手边”。这样的定义唯一确定了一个方向为走向方向。
走向（strike）的角度定义为正北方向顺时针旋转到走向方向的角度，即图中的 $\phi_s$，其中 $\phi_s \in [0,2\pi)$。

倾角 dip 的定义为：从水平面向下旋转到断层面的角度，即图中的 $\delta$。因此有 $0\le\delta\le\pi/2$。

## 断层滑动

断层的滑移 $\mathbf{u}$ 是一个矢量，定义为 “断层上盘（hanging wall）相对于下盘（foot wall）的滑动”。
一般取 $\mathbf{u}$ 的大小为滑移量 u，取 $\mathbf{u}$ 的方向为滑动方向，而滑移角（rake）即定义为断层
走向与滑动方向之间的夹角，即图中 $\lambda$。注意这里滑移角 rake 是逆时针计算的。rake 的取值范围为 $-\pi < \lambda < \pi$。

## 断层的命名

大部分断层属于正断层或者逆断层，一些特殊的断层是走滑或倾滑断层：

-   逆断层（reversed fault）：$\lambda\in(0,\pi)$ 且 $\delta \ne 0 \ne \frac{\pi}{2}$
-   正断层（normal fault）：$\lambda\in(-\pi,0)$ 且 $\delta \ne 0 \ne \frac{\pi}{2}$
-   走滑断层（strike-slip fault）：$\lambda=0$ 或 $\lambda=\pi$
-   倾滑断层（dip-slip fault）：断层滑动方向垂直于走向，即 $\lambda=\frac{\pi}{2}$ 或 $\lambda=-\frac{\pi}{2}$

对于走滑断层和倾滑断层，存在一些特例：

对于走滑断层，有 $\lambda=0$ 或 $\lambda=\pi$，若 $\delta=\frac{\pi}{2}$，此时断层面垂直于地面，
已经不存在断层上盘和下盘的概念。这里引入了左旋（left-lateral）和右旋（right-leteral）的概念。
当观测者站在断层的其中一个块体并面对另一个块体，若对面的块体向右手边移动，则称之为右旋走滑断层；反之，
若对面的块体向左手边移动，则称之为左旋走滑断层。根据这样的定义，对于垂直走滑断层，若 $\lambda=0$ 为左旋，
$\lambda=\pi$ 为右旋。

对于垂直的倾滑断层（$\delta=\frac{\pi}{2}$），定义下降块体为下盘，由此再定义走向方向，因而垂直
倾滑断层永远有 $\lambda=\frac{\pi}{2}$。

## 备注

图中给出了北向，并未给出东向和垂直向，因而实际上断层参数定义是与坐标系的选取无关的。无论是左手系还是
右手系，无论 z 轴是向上还是向下，断层参数的定义不变。在设计到辐射花样等问题时，坐标系的选取开始变得重要了，
以后再说。
