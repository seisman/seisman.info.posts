---
title: 地球物理相关软件
date: 2014-02-20 10:20
author: SeisMan
categories: 地球物理相关资源
tags: [理论地震图, SAC, GMT]
---

## 通用数据处理

- [SAC][]: Seismic Analysis Code，地震学数据处理的常用软件。
- [CPS330][]
- [ObsPy][]: 基于 Python 的地震学数据处理框架

[SAC]: http://www.iris.edu/ds/nodes/dmc/forms/sac/
[CPS330]: http://www.eas.slu.edu/eqc/eqccps.html
[ObsPy]: https://github.com/obspy/obspy/wiki

## 数据格式转换

- [rdseed][]: SEED 格式转换为 SAC 等地震数据格式
- [win32tools][]: Hi-net 提供的工具，用于将 WIN32 格式的数据转换为 SAC 格式
- [mseed2sac][]: 将 miniSEED 格式转换为 SAC 格式
- [dataselect][]:  miniSEED 数据处理

[rdseed]: http://www.iris.edu/ds/nodes/dmc/forms/rdseed/
[win32tools]: http://www.hinet.bosai.go.jp/REGS/manual/dlDialogue.php?r=win32tools
[mseed2sac]: https://seiscode.iris.washington.edu/projects/mseed2sac
[dataselect]: https://seiscode.iris.washington.edu/projects/dataselect

## 数据获取工具

- [jweed][]: 用 Java 实现的 IRIS 数据申请客户端。
- [SOD][]: 数据自动下载命令行工具。

[jweed]: http://ds.iris.edu/ds/nodes/dmc/software/downloads/jweed/
[SOD]: http://www.seis.sc.edu/sod

## 绘图类

- [GMT][]: 地球物理方向绘制地图必备神器。
- [pssac][]: 利用 GMT 强大的绘图库直接绘制地震图
- [JPlotResp][]: 绘制 RESP 仪器响应文件的振幅相位响应谱。可以直接联网查询某台网某台站某个时间的仪器响应，也可以直接处理本地的 RESP 文件。
- [MoPad][]: 地震矩分析和绘图软件，可以做地震矩的各种分解以及分析，绘制各种类型的震源球，可控性非常强，比 GMT 的 psmeca 命令要灵活，且可以与 GMT 联合使用
- [GmtPy][]: GMT4 的非官方 Python 接口。

[GMT]: http://gmt.soest.hawaii.edu/
[pssac]: http://www.eas.slu.edu/People/LZhu/home.html
[JPlotResp]: http://www.isti2.com/JPlotResp/
[MoPad]: http://www.larskrieger.de/mopad/
[GmtPy]: http://emolch.github.io/gmtpy/

## 通用辅助类

- [distaz][]: 给定震中和台站经纬度，计算震中距、方位角和反方位角的经典代码。
- [TauP][]: 强大的走时计算器，不过其功能可不仅仅只是计算走时这么简单。射线参数、射线路径、反射点、投射点都可以计算，支持自定义速度模型、支持不常见的震相。
- [Cake][]: Python 写的走时计算工具，支持自定义速度模型，支持更复杂的震相路径。
- [ANISOtime][]: 横向各向同性球状对称模型下的射线走时工具。
- [DigitSeis][]: 利用图像处理技术将模拟地震仪记录到的波形图片转换成数字信号（Matlab）

[distaz]: http://www.seis.sc.edu/software/distaz/
[TauP]: http://www.seis.sc.edu/taup/
[Cake]: http://emolch.github.io/pyrocko/current/cake_doc.html
[ANISOtime]: http://www-solid.eps.s.u-tokyo.ac.jp/~dsm/anisotime.html
[DigitSeis]: http://www.seismology.harvard.edu/research/DigitSeis.html


## 理论地震图

- [fk][]: 频率 - 波数法，计算水平分层各向同性介质下理论地震图位移静态解和动态解
- [QSEIS][]: 层状粘弹介质下的理论地震图
- [SHaxi][]: 有限差分方法计算全球尺度高精度 SH 波场。
- [QSSP][]: Normal modes 方法计算球形地球下的理论地震图
- [Mineos][]: Normal modes 方法计算球对称非旋转地球模型下的合成地震图
- [yaseis][]: 频率 - 波数法，球状分层介质下的理论地震图
- [AxiSEM][]: 球层介质中的 3D 弹性、非弹性、各向异性、声波理论地震图
- [Instaseis][]: 用 Python 写的，基于 AxiSEM 的地震图合成工具
- [GEMINI][]:
- [DSM][]: Direct Solution Method ([tish][], [tipsv][], [spcsac][])
- [SOFI2D][]: 二维有限差分计算 (粘) 弹性介质下的 PSV 波场
- [SOFI2D-sh][]: 二维有限差分计算 (粘) 弹性介质下的 SH 波场
- [SOFI3D][]: 三维有限差分计算 (粘) 弹性介质下的波场
- [SPECFEM2D][]: 谱元法 2D
- [SPECFEM3D][]: 谱元法 3D(笛卡尔坐标系)
- [SPECFEM3D Global][]: 谱元法 3D(球坐标系)

[fk]: http://www.eas.slu.edu/People/LZhu/home.html
[QSEIS]: http://www.gfz-potsdam.de/en/section/physics-of-earthquakes-and-volcanoes/data-products-services/downloads-software/
[SHaxi]: http://svn.geophysik.uni-muenchen.de/trac/shaxi
[QSSP]: http://www.gfz-potsdam.de/en/section/physics-of-earthquakes-and-volcanoes/data-products-services/downloads-software/
[Mineos]: https://github.com/geodynamics/mineos
[yaseis]: https://seiscode.iris.washington.edu/projects/yaseis
[AxiSEM]: http://seis.earth.ox.ac.uk/axisem/
[Instaseis]: http://instaseis.net/
[GEMINI]: http://www.quest-itn.org/library/software/gemini-greens-function-of-the-earth-by-minor-integration
[DSM]: http://www-solid.eps.s.u-tokyo.ac.jp/~dsm/software/software.htm
[tipsv]: http://www-solid.eps.s.u-tokyo.ac.jp/~dsm/software/software/tipsv-1.8.0.tar.gz
[tish]: http://www-solid.eps.s.u-tokyo.ac.jp/~dsm/software/software/tish-1.9.0.tar.gz
[spcsac]: http://www-solid.eps.s.u-tokyo.ac.jp/~dsm/software/software/spcsac-v1.0.0.tar.gz
[SOFI2D]: https://git.scc.kit.edu/GPIAG-Software/SOFI2D/
[SOFI2D-sh]: https://git.scc.kit.edu/GPIAG-Software/SOFI2D_sh
[SOFI3D]: https://git.scc.kit.edu/GPIAG-Software/SOFI3D
[SPECFEM2D]: https://geodynamics.org/cig/software/specfem2d/
[SPECFEM3D]: https://geodynamics.org/cig/software/specfem3d/
[SPECFEM3D Global]: https://geodynamics.org/cig/software/specfem3d_globe/

## 震源机制

- [gcap][]: 通用 Cut and Paste 方法反演震源机制
- [pyTDMT][]: 时间域震源机制反演的 Python 实现
- [WPhase][]: W Phase 方法反演震源机制
- [focmec][]: 确定并绘制震源机制

[gcap]: http://www.eas.slu.edu/People/LZhu/home.html
[pyTDMT]: https://github.com/fabriziobernardi/pydmt
[WPhase]: http://eost.u-strasbg.fr/wphase/
[focmec]: https://seiscode.iris.washington.edu/projects/focmec

## 特定功能类

- [hk][]: 用于接收函数研究的代码。
- [CCP][]: 共转换点地震数据叠加，用于接收函数研究。
- [IRFFM][]: 带界面的接收函数软件包。
- [astack][]: 自适应迭代以实现震相对齐。
- [LASIF][]: 基于 Python 的大规模全波形反演框架，似乎是层析成像。
- [SplitLab][]: 基于 Matlab 的 S 波分裂处理工具

[hk]: http://www.eas.slu.edu/People/LZhu/home.html
[CCP]: http://www.eas.slu.edu/People/LZhu/home.html
[IRFFM]: http://rses.anu.edu.au/~hrvoje/IRFFMv1.1.html
[astack]: http://rses.anu.edu.au/seismology/soft/astack/index.html
[LASIF]: http://www.lasif.net/
[SplitLab]: http://splitting.gm.univ-montp2.fr/

## 数学处理类

- [SHTOOLS][]: 实现球谐相关操作，包括变换、重建、旋转、谱分析等。

[SHTOOLS]: https://github.com/SHTOOLS/SHTOOLS

## 函数库

- [libmseed][]: 用于读写 miniSEED 格式的 C 函数库

[libmseed]: https://seiscode.iris.washington.edu/projects/libmseed
