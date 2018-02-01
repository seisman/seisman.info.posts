---
title: 调用 SAC 进行 Hilbert 变换
author: SeisMan
date: 2015-04-29
categories:
  - SAC
tags:
  - C
slug: hilbert-transform-in-sac
---

需要在 C 程序中对数据做 Hilbert 变换，自己写显然是不可能的啦，重复造轮子不说，
写的还不一定对。找了一些代码，发现都写的好复杂，后来发现 SAC 在函数库中提供了
Hilbert 变换的接口，可以直接调用。

`firtrn` 可以用于对数据进行 Hilbert 变换，但是官方没有给一个比较直白的例子。
下面就贴一个我写的例子啦。

<!--more-->

需要注意，SAC 自带的 Hilbert 变换要求数据至少 201 个点。

``` C
#include <stdio.h>
#include <stdlib.h>
#define NPTS 1000
float *hilbert(float *in, int npts);

int main(){
    float data[NPTS];
    float *hdata;

    int i;
    // 准备输入数据
    for (i=0; i<NPTS; i++)  data[i] = i;

    // 进行 Hilbert 变换，hdata 为 Hilbert 变换的结果
    hdata = hilbert(data, NPTS);

    for (i = 0; i < NPTS; i++)
        printf("%f\n", hdata[i]);
}

// 这里定义了 hilbert 函数，是对 firtrn 函数的一个封装
float *hilbert(float *in, int npts) {
    float *buffer;
    float *out;

    buffer = (float *)malloc(sizeof(float)*50000);
    out = (float *)malloc(sizeof(float)*npts);
    firtrn("HILBERT", in, npts, buffer, out);

    return out;
}
```
