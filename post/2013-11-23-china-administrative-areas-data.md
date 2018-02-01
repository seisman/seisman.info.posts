---
title: 中国行政区划数据下载
date: 2013-11-23
author: SeisMan
categories:
  - 地球物理相关资源
tags:
  - 数据
  - 格式转换
  - 网站
  - GMT
slug: china-administrative-areas-data
---

## GADM 数据库

GADM，是一个全球行政区划数据库。包括了几乎全部国家和地区的行政区划界线数据。

主页： <http://www.gadm.org/>

<!--more-->

### 下载数据

下载地址： <http://www.gadm.org/country>

GADM 提供的数据格式有 6 种：ESRI file
geodatabase、Shapefile、Geopackage(SpatiaLite)、R(SpatialPolygonsDataFrame)、Google
Earth .kmz 和 ESRI personal geodatabase。这里，数据格式应选择 shapefile。

在 GADM 中，country 的定义为 “any entity with an ISO country code”。关于 ISO country code，可以参考 [维基百科](http://zh.wikipedia.org/wiki/ISO_3166-1)。因而
想要下载完整的中国数据，实际上需要四个文件：China、Hong Kong、Macao、Taiwan。

也可以在 <http://www.gadm.org/version2> 下载全球的行政区划数据，但非常不推荐。一方面是数据量偏大，另一方面是全球区划数据保存到一个文件中，难以整理。不如麻烦一点，需要哪个国家下哪个
国家。

### 解压数据

以 china 数据为例

    unzip CHN_adm_shp.zip -d CHN_adm

解压后得到一堆文件，其中 `CHN_adm0.shp`、`CHN_adm1.shp`、`CHN_adm2.shp`、
`CHN_adm3.shp` 为实际需要的 shapefile 数据。0、1、2、3 为第零、一、二、三级行政区划界线。对于 china 数据，基本相当于中国大陆地区的边界、省界、市界和区县界。如果是 Hong
Kong 的数据，0 依然是边界，但是 1 理解为省界显然不合适，总之就是更低一级的行政区划界线。

### 格式转换

GMT 不能识别 shapefile 格式。需要使用 gdal 的 `ogr2ogr` 命令将 shapefile 格式转换为 GMT 可识别的格式。如果系统里找不到 `ogr2ogr` 命令，则说明 gdal 没有安装。Ubuntu 下的包
名是 `gdal-bin` ，CentOS 下的是 `gdal`。Windows 用户则需要到 gdal 官网下载安装。
另外，Windows 用户也可以用 ArcGIS 等软件实现格式的转换。

具体的转换命令是从网上找到的，`CHN_adm0` 为要生成的数据的文件名前缀，但是为什么要出现两次，表示很不解。

    ogr2ogr -f GMT -nln CHN_adm0 CHN_adm0 CHN_adm0.shp
    ogr2ogr -f GMT -nln CHN_adm1 CHN_adm1 CHN_adm1.shp
    ogr2ogr -f GMT -nln CHN_adm2 CHN_adm2 CHN_adm2.shp
    ogr2ogr -f GMT -nln CHN_adm3 CHN_adm3 CHN_adm3.shp

对于 Hong Kong、Macao、Taiwan 的数据做类似操作，最终生成了一堆以 gmt 结尾的文件。共计 12 个，如下：

    CHN_adm0.gmt  CHN_adm2.gmt  HKG_adm0.gmt  MAC_adm0.gmt  MAC_adm2.gmt  TWN_adm1.gmt
    CHN_adm1.gmt  CHN_adm3.gmt  HKG_adm1.gmt  MAC_adm1.gmt  TWN_adm0.gmt  TWN_adm2.gmt

## 绘图测试

PS1：数据为多段数据，在 GMT4 中需要使用 `-m` 选项，而 GMT5 已经可以自动处理多段数据，所以不需要使用 `-m` 选项。

PS2：数据中有领土纠纷的部分不符合中国政府的立场，笔者也不赞同。虽然有问题的部分不能在正规期刊上发表，但是没有问题的部分还是可以使用的。欢迎读者告诉我符合中国政府政策的数据。

### 中国全图

绘制中国全图需要全部的 0 级数据。

``` bash
#!/bin/bash
R=72/136/15/54
J=M15c
PS=china.ps

gmt psxy -J$J -R$R -T -K -U > $PS
gmt psxy -R$R -J$J CHN_adm0.gmt -K -O >> $PS
gmt psxy -R$R -J$J HKG_adm0.gmt -K -O >> $PS
gmt psxy -R$R -J$J MAC_adm0.gmt -K -O >> $PS
gmt psxy -R$R -J$J TWN_adm0.gmt -K -O >> $PS
gmt psxy -R$R -J$J -T -O >> $PS
```

代码运行过程中 GMT 会出现如下的警告 (或错误？)

    psxy: Bad OGR/GMT: @D record has more items than declared by @N

猜测是 `ogr2ogr` 转换的问题。在我的系统环境该警告不影响绘图效果，但评论中 @vv 指出在他的系统环境下会导致图形无法绘制。

效果图（缺了南海的九段线数据）：

![](/images/2013112301.jpg)

### 1 级行政区划

与上面的代码几乎一样，1 级数据中包含了 0 级数据，所以直接绘制 1 级数据即可。

``` bash
R=72/136/15/54
J=M15c
PS=china.ps

gmt psxy -J$J -R$R -T -K -U > $PS
gmt psxy -R$R -J$J CHN_adm1.gmt -K -O >> $PS
gmt psxy -R$R -J$J HKG_adm1.gmt -K -O >> $PS
gmt psxy -R$R -J$J MAC_adm1.gmt -K -O >> $PS
gmt psxy -R$R -J$J TWN_adm1.gmt -K -O >> $PS
gmt psxy -R$R -J$J -T -O >> $PS
```

效果图：

![](/images/2013112302.jpg)

在上一篇博文《[GMT 中 DCW 数据的使用](/usage-of-dcw-data.html)》中利用 GMT 自带的
DCW 数据也生成了类似的图，如下图。查看全图，对比一下会发现，两张图的细节方面还是有些区别的，
本文的数据绘制的似乎包含了更多的细节（主要是小的岛屿）。这个就得根据需求去选择了，当然也有
可能两个都是有问题的。

![](/images/2013112303.jpg)

### 2 级行政区划

转换出来的 2 级数据中包含了全国所有的市级边界，用编辑器打开查看内容就会发现，每条线段都有
完整的注释，很容易从众多线段中提取出自己想要的部分。以安徽省为例，将与安徽有关的线段数据保存
到文件 `Anhui_adm2.gmt` 中：

``` bash
R=114/120/29/35
J=M10c
PS=anhui.ps

gmt psxy -J$J -R$R -T -K -U > $PS
gmt psxy -R$R -J$J Anhui_adm2.gmt -K -O >> $PS
gmt psxy -R$R -J$J -T -O >> $PS
```

上面的脚本有一个很不方便的地方：想要画一个省的 2 级数据，每次都要从 CHN\_adm2.gmt 中手动提取该省的数据信息。下面的例子可以避免这种手动提取的过程，主要通过 DCW 数据和 psclip 命令，使用全国 2 级数据（CHN\_adm2.gmt），但是只绘制安徽省的 2 级数据。

``` bash
R=114/120/29/35
J=M10c
PS=anhui.ps

gmt psxy -J$J -R$R -T -K -U > $PS
gmt pscoast -FCN.34 -M > Anhui_bnd.gmt
gmt psclip -J$J -R$R Anhui_bnd.gmt -K -O >> $PS
gmt psxy -R$R -J$J CHN_adm2.gmt -K -O >> $PS
gmt psclip -C -K -O >> $PS
gmt psxy -R$R -J$J -T -O >> $PS
```

脚本利用 pscoast 命令，将安徽省（代码为 34）的省界数据导出到文件 Anhui\_bnd.gmt 中，然后利用该文件进行 clip，psxy 绘图时虽然使用的是全国的 2 级数据 CHN\_adm2.gmt，但是只有安徽省内的部分会被绘制出来，最后还需要再次调用 psclip 以结束 clip。

上面的这个脚本生成了一个中间文件 Anhui\_bnd.gmt，有强迫症的人是无法忍受这个的，因而上面的代码利用管道可以进一步简化为：

``` bash
R=114/120/29/35
J=M10c
PS=anhui.ps

gmt psxy -J$J -R$R -T -K -U > $PS
gmt pscoast -FCN.34 -M | gmt psclip -J$J -R$R -K -O >> $PS
gmt psxy -R$R -J$J CHN_adm2.gmt -K -O >> $PS
gmt psclip -C -K -O >> $PS
gmt psxy -R$R -J$J -T -O >> $PS
```

上面三个脚本的最终结果基本是一致的，效果图如下：

注：三个脚本的成图效果是有差的，但是目前没有体现出来，在下一段 “3 级行政区划” 中，可以更明显地看出区别。

![](/images/2013112304.jpg)

### 3 级行政区划

这里还是以安徽省为例，实际上只用 3 级数据即可，这里同时用了 2 级数据和 3 级数据，并且用不同的粗细和颜色来区分。需要注意，由于 3 级数据中包含了 2 级数据，所以下面的例子先画了 3 级数据，再用 2 级数据覆盖。如果画的顺序反了，效果就会差很多。

``` bash
R=114.8/120/29.3/36
J=M14c
PS=anhui.ps

gmt psxy -J$J -R$R -T -K -U > $PS
gmt psxy -R$R -J$J CHN_adm3.gmt -W0.5p,gray -K -O >> $PS
gmt psxy -R$R -J$J CHN_adm2.gmt -W1p -K -O >> $PS
gmt psxy -R$R -J$J -T -O >> $PS
```

效果图如下：

![](/images/2013112305.jpg)

下面的脚本利用了前面提到的 psclip 的方法：

``` bash
R=114.8/120/29.3/36
J=M14c
PS=anhui.ps

gmt psxy -J$J -R$R -T -K -U > $PS
gmt pscoast -FCN.34 -M | gmt psclip -J$J -R$R -K -O >> $PS
gmt psxy -R$R -J$J CHN_adm3.gmt -W0.5p,gray -K -O >> $PS
gmt psxy -R$R -J$J CHN_adm2.gmt -W1p -K -O >> $PS
gmt psclip -C -K -O >> $PS
gmt psxy -R$R -J$J -T -O >> $PS
```

效果图如下：

![](/images/2013112306.jpg)

将这两张图对比一下，容易发现，省界的部分线段明显变细了，这算是 clip 的一个缺点，使用省界数据进行 clip，同时又要绘制省界数据，如何判断省界数据点是否在 clip 区域内部是个问题。

## 修订历史

-   2013-11-23：初稿；
-   2013-11-28：绘制 2 级和 3 级边界时，利用 clip 的方法以减少人工操作。Thanks to @yangtze。
-   2013-12-05：删除了数据包中的冗余隐藏文件，重新打包，提供多种格式下载。
-   2014-01-19：不推荐下载全球行政区划数据；
-   2015-04-11：存在个别 IP 恶意下载数据，导致我流量异常高，因而删除其他格式的数据压缩包，仅留下 7z 格式的，若仍出现流量异常，则删除该数据；
-   2015-05-01：流量依然异常，猜测是搜索引擎会对齐定时抓取导致的；虽然已经在七牛限制了文件的非本站访问，但似乎对压缩文件无效。故删除该数据，有需要的可以自己去转换格式；
-   2016-04-13：王亮添加了 GADM 数据库新增的 Macou 1、2 级数据，并修正了部分理解和表述；
