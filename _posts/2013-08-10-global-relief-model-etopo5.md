---
title: 全球地形起伏模型etopo5
date: 2013-08-10
author: SeisMan
categories: 地球物理相关资源
tags: [GMT, 地形, 数据, 网格, 高程]
---

etopo5是全球高程及水深数据，其空间分辨率是5弧分，目前已被更高精度的etopo2和etopo1所取代。但在绘制
全球地形时，若觉得用etopo2得到的图形文件过大，也可使用低精度的etopo5，但还是**不建议用etopo5**。

官方页面： <http://www.ngdc.noaa.gov/mgg/global/etopo5.html>

<!--more-->

## 下载地址

[ETOPO5下载](http://www.ngdc.noaa.gov/mgg/global/relief/ETOPO5/TOPO/ETOPO5/)

其中， `ETOPO5.DAT` 和 `ETOPO5.DOS` 包含了相同的高程数据，只是二者的字节序不同。 `ETOPO5.DOS` 为
`little-endian` ， `ETOPO5.DAT` 为 `big-endian` 。

## 网格数据的说明

[官方说明文档](http://www.ngdc.noaa.gov/mgg/global/relief/ETOPO5/TOPO/ETOPO5/ETOPO5.txt)

简单归纳一下：

-   数据采样间隔为5弧分
-   经度上0度到359度55分共计4320个采样点（注意不是0到360度），维度方向-90度到90度为2161个点
-   每个数据用16位整数表示，即占用两字节，共计4320\*2161\*2=18671040字节
-   实际数据中只有18662400字节，这是因为数据中把-90度的南极给丢了，后面会做简单处理，把南极点补回来；
-   数据在文件中的排序很简单，从北纬90度，东经0度0分开始，接下来是360度\*12采样点/度=4320采样点，
    即8640个字节，一直到北纬90度，东经359度55分；第4321个点为北纬89度55分，东经0度0分，按照这样的顺序
    不断排下去。每个纬度带4320个点，共计2160个纬度带。
-   北纬90度即北极，4320个点具有相同的值，为-4290m；南纬-90度即南极，没有包含在这个数据中，其海拔为2810
    m。

## 数据的小修改

如前所说，数据中把南极丢了，这是个小问题，当绘制全球数据时会出现类似“南极海拔不一致”的警告，虽说
不是致命错误，还是改了吧，源代码如下：

``` C
/*
 * A simple C code to add the elevation of south pole to the ETOPO5 data
 * Date:   04/30/2013
 * Author: SeisMan
 *
 * Input:  ETOPO5.DOS
 * Output: etopo5.i2
 * Note: ETOPO5.DOS is little-endian;
 *       ETOPO5.DAT is big-endian;
 */

#include<stdio.h>
#include<stdlib.h>
#define NX 4320
#define NY 2160

short int **imatrix(int nrl,int nrh,int ncl,int nch);

int main(){
  short int **topo;
  int ix, iy;
  FILE *fip, *fop;

  topo=imatrix(1,NX,1,NY+1);

  fip=fopen("ETOPO5.DOS","rb");
  for(iy=1;iy<=NY;iy++){
    for(ix=1;ix<=NX;ix++)
      fread(&topo[ix][iy],sizeof(short int),1,fip);
  }

  for(ix=1;ix<=NX;ix++)
    topo[ix][NY+1]=2810;

  fop=fopen("etopo5.i2","wb");
  for(iy=1;iy<=NY+1;iy++)
    for(ix=1;ix<=NX;ix++){
      fwrite(&topo[ix][iy],sizeof(short int),1,fop);
//      printf("%d %d %d\n",ix,iy,topo[ix][iy]);
    }

  close(fip);
  close(fop);
}

short int **imatrix(int nrl,int nrh,int ncl,int nch){
  int i;
  short int **m;

  m=(short int **)malloc((unsigned) (nrh-nrl+1)*sizeof(short int*));
  if (!m) fprintf(stderr,"allocation failure 1 in imatrix()\n");
  m -= nrl;

  for(i=nrl;i<=nrh;i++) {
    m[i]=(short int *)malloc((unsigned) (nch-ncl+1)*sizeof(short int));
    if (!m[i]) fprintf(stderr,"allocation failure 2 in imatrix()\n");
      m[i] -= ncl;
  }
  return m;
}
```

编译并运行:

    $ gcc etopo5_mod.c -o etopo5_mod
    $ ./etopo5_mod

## 复制

将修改后的 `etopo5.i2` 拷贝至 `${GMTHOME}/share/dbase` 下，并在 `grdraster.info` 中加入如下语句:

    1 "ETOPO5 global topography" "m" -R0/359:55/-90/90 -I5m GG i 1 0 none etopo5.i2

这其实也就是默认的 `grdraster.info` 中的内容，只是GMT没有自带etopo5的数据。

## 画图检查

```
#!/bin/bash

gmt grdraster 1 -Rg -I5m -Getopo5_global.grd
gmt makecpt -Cglobe -T-10500/8000/1000 -Z > colors.cpt
gmt grdimage etopo5_global.grd -Ba60g30 -Rg -JN0/25c -Ccolors.cpt -K -Yc > etopo5.ps
gmt psscale -Ba2500f500+l"m" -Ccolors.cpt -Dx12.5c/-1.5c/15c/.35ch -O >> etopo5.ps

rm etopo5_global.grd colors.cpt gmt.*
```

![](/images/2013081001.jpg)
