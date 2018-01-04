---
title: 地球物理相关软件
date: 2014-02-20
updated: 2016-12-20
author: SeisMan
categories: 地球物理相关资源
tags: [理论地震图, SAC, GMT]
---

## 通用数据处理

- [SAC][]: 地震学数据处理的常用软件
- [ObsPy][]: 基于 Python 的地震学数据获取、处理、绘图工具
- [GISMO][]: 基于 Matlab 的地震学数据获取、处理、绘图工具
- [SeisIO.jl][]: 基于 Julia 的地震学数据获取、处理、绘图工具
- [CPS330][]: GSAC, 理论地震图，接收函数，面波频散

[SAC]: http://www.iris.edu/ds/nodes/dmc/forms/sac/
[CPS330]: http://www.eas.slu.edu/eqc/eqccps.html
[ObsPy]: https://github.com/obspy/obspy/wiki
[SeisIO.jl]: https://github.com/jpjones76/SeisIO.jl
[GISMO]: http://geoscience-community-codes.github.io/GISMO/

## 数据格式转换

- [rdseed][]: SEED 格式转换为 SAC 等地震数据格式
- [mseed2sac][]: 将 miniSEED 格式转换为 SAC 格式
- [win32tools][]: Hi-net 提供的工具，用于将 WIN32 格式的数据转换为 SAC 格式
- [dataselect][]:  miniSEED 数据处理
- [ObsPy][]: 基于 Python 的地震学数据获取、处理、绘图工具

[rdseed]: http://www.iris.edu/ds/nodes/dmc/forms/rdseed/
[win32tools]: http://www.hinet.bosai.go.jp/REGS/manual/dlDialogue.php?r=win32tools
[mseed2sac]: https://seiscode.iris.washington.edu/projects/mseed2sac
[dataselect]: https://seiscode.iris.washington.edu/projects/dataselect

## 数据获取工具

- [BREQ_FAST][]: 通过发送邮件申请数据
- [IRIS Wilber 3][]: 通过网页界面下载单个地震事件的波形数据
- [SOD][]: 用 Java 实现的地震数据下载工具
- [ObsPy][]: 基于 Python 的地震学数据获取、处理、绘图工具
- [IRIS DMC Web Services][]: 通过网页服务申请数据
- [Web Service Fetch scripts][]: 获取数据的Perl脚本
- [jweed][]: 用 Java 实现的 IRIS 数据申请客户端

[jweed]: http://ds.iris.edu/ds/nodes/dmc/software/downloads/jweed/
[SOD]: http://www.seis.sc.edu/sod
[IRIS Wilber 3]: http://www.iris.edu/wilber3/find_event
[BREQ_FAST]: http://ds.iris.edu/ds/nodes/dmc/manuals/breq_fast/
[IRIS DMC Web Services]: http://service.iris.edu/
[Web Service Fetch scripts]: https://seiscode.iris.washington.edu/projects/ws-fetch-scripts

## 绘图类

- [GMT][]: 地球物理方向绘制地图必备神器
- [pssac][]: 利用 GMT 强大的绘图库直接绘制地震图
- [ObsPy][]: 基于 Python 的地震学数据获取、处理、绘图工具
- [JPlotResp][]: 绘制 RESP 仪器响应文件的振幅相位响应谱。可以直接联网查询某台网某台站某个时间的仪器响应，也可以直接处理本地的 RESP 文件。
- [MoPad][]: 地震矩分析和绘图软件，可以做地震矩的各种分解以及分析，绘制各种类型的震源球，可控性非常强，比 GMT 的 psmeca 命令要灵活，且可以与 GMT 联合使用
- [obspy-mopad][]: ObsPy 中提供的另一个版本的 mopad 工具

[GMT]: http://gmt.soest.hawaii.edu/
[pssac]: http://www.eas.slu.edu/People/LZhu/home.html
[JPlotResp]: http://www.isti2.com/JPlotResp/
[MoPad]: http://www.larskrieger.de/mopad/
[obspy-mopad]: https://docs.obspy.org/packages/autogen/obspy.imaging.scripts.mopad.html

## 走时计算/射线追踪

- [TauP][]: 强大的走时计算器，不过其功能可不仅仅只是计算走时这么简单。射线参数、射线路径、反射点、投射点都可以计算，支持自定义速度模型、支持不常见的震相。
- [obspy.taup][]: TauP 的 Python 版本
- [Cake][]: Python 写的走时计算工具，支持自定义速度模型，支持更复杂的震相路径。
- [ANISOtime][]: 横向各向同性球状对称模型下的射线走时工具。
- [pySeismicFMM][]: Fast Marching Method 计算 3D 走时
- [FM3D][]: 3D Fast Marching Code

[TauP]: http://www.seis.sc.edu/taup/
[Cake]: http://pyrocko.org/
[ANISOtime]: http://www-solid.eps.s.u-tokyo.ac.jp/~dsm/anisotime.html
[pySeismicFMM]: https://github.com/gozwei/pySeismicFMM
[FM3D]: http://rses.anu.edu.au/seismology/soft/fmmcode/
[obspy.taup]: http://docs.obspy.org/packages/obspy.taup.html

## 理论地震图

### 解析解

- [fk][]: 频率 - 波数法，计算水平分层各向同性介质下理论地震图位移静态解和动态解
- [QSEIS][]: 层状粘弹介质下的理论地震图
- [QSSP][]: Normal modes 方法计算球形地球下的理论地震图
- [Mineos][]: Normal modes 方法计算球对称非旋转地球模型下的合成地震图
- [yaseis][]: 频率 - 波数法，球状分层介质下的理论地震图
- [GEMINI][]:
- [DSM][]: Direct Solution Method ([tish][], [tipsv][], [spcsac][])

### 有限差分法

- [SHaxi][]: 有限差分方法计算全球尺度高精度 SH 波场
- [SOFI2D][]: 二维有限差分计算 (粘) 弹性介质下的 PSV 波场
- [SOFI2D-sh][]: 二维有限差分计算 (粘) 弹性介质下的 SH 波场
- [SOFI3D][]: 三维有限差分计算 (粘) 弹性介质下的波场
- [SEISMIC_CPML][]: 2D/3D 有限差分+CPML吸收边界
- [SW4][]: 3D 有限差分
- [OpenSWPC][]: 2D/3D 有限差分

### 谱元法

- [SPECFEM1D][]: 谱元法 1D
- [SPECFEM2D][]: 谱元法 2D
- [SPECFEM3D][]: 谱元法 3D(笛卡尔坐标系)
- [SPECFEM3D Global][]: 谱元法 3D(球坐标系)
- [AxiSEM][]: 球层介质中的 3D 弹性、非弹性、各向异性、声波理论地震图
- [Instaseis][]: 用 Python 写的，基于 AxiSEM 的地震图合成工具
- [AxiSEM3D][]:

[fk]: http://www.eas.slu.edu/People/LZhu/home.html
[QSEIS]: http://www.gfz-potsdam.de/en/section/physics-of-earthquakes-and-volcanoes/data-products-services/downloads-software/
[SHaxi]: http://svn.geophysik.uni-muenchen.de/trac/shaxi
[QSSP]: http://www.gfz-potsdam.de/en/section/physics-of-earthquakes-and-volcanoes/data-products-services/downloads-software/
[Mineos]: https://github.com/geodynamics/mineos
[yaseis]: https://seiscode.iris.washington.edu/projects/yaseis
[AxiSEM]: https://github.com/geodynamics/axisem
[Instaseis]: http://instaseis.net/
[GEMINI]: http://www.quest-itn.org/library/software/gemini-greens-function-of-the-earth-by-minor-integration
[DSM]: http://www-solid.eps.s.u-tokyo.ac.jp/~dsm/software/software.htm
[tipsv]: http://www-solid.eps.s.u-tokyo.ac.jp/~dsm/software/software/tipsv-1.8.0.tar.gz
[tish]: http://www-solid.eps.s.u-tokyo.ac.jp/~dsm/software/software/tish-1.9.0.tar.gz
[spcsac]: http://www-solid.eps.s.u-tokyo.ac.jp/~dsm/software/software/spcsac-v1.0.0.tar.gz
[SOFI2D]: https://git.scc.kit.edu/GPIAG-Software/SOFI2D/
[SOFI2D-sh]: https://git.scc.kit.edu/GPIAG-Software/SOFI2D_sh
[SOFI3D]: https://git.scc.kit.edu/GPIAG-Software/SOFI3D
[SEISMIC_CPML]: https://github.com/geodynamics/seismic_cpml
[SPECFEM1D]: https://github.com/geodynamics/specfem1d
[SPECFEM2D]: https://github.com/geodynamics/specfem2d
[SPECFEM3D]: https://github.com/geodynamics/specfem3d
[SPECFEM3D Global]: https://github.com/geodynamics/specfem3d_globe
[SW4]: https://github.com/geodynamics/sw4
[OpenSWPC]: https://github.com/takuto-maeda/OpenSWPC
[AxiSEM3D]: https://github.com/kuangdai/AxiSEM3D

## 特定研究类

### 层析成像

- [ASWMS][]: Automated Surface-Wave Phase-Velocity Measuring System, Matlab

[ASWMS]: https://ds.iris.edu/ds/products/aswms/

### 全波形反演

- [TOY2DAC][]: 2D Acoustic frequency-domain Full Waveform modeling and inversion code.
- [ASKI][]: modularized program suite for sensitivity analysis and iterative full waveform inversion
- [FWI.jl][]: 2D/3D acoustic FWI in Julia
- [IFOS2D][]: 2D弹性波FWI
- [IFOS3D][]: 3D弹性波FWI
- [DENISE-SH][]: 2D SH有限差分模拟及FWI
- [DENISE][]: 2D PSV有限差分模拟及FWI
- [SES3D][]: 3D谱元法FWI
- [LASIF][]: 基于 Python 的大规模全波形反演框架，似乎是层析成像。
- [seisDD][]: Double-difference adjoint seismic tomography

[TOY2DAC]: https://seiscope2.osug.fr/TOY2DAC,82
[ASKI]: http://www.gmg.ruhr-uni-bochum.de/geophysik/seismology/aski.html
[FWI.jl]: https://github.com/JuliaInv/FWI.jl
[IFOS2D]: https://git.scc.kit.edu/GPIAG-Software/IFOS2D
[IFOS3D]: https://git.scc.kit.edu/GPIAG-Software/IFOS3D
[DENISE-SH]: https://github.com/daniel-koehn/DENISE-SH
[DENISE]: https://github.com/daniel-koehn/DENISE-Black-Edition
[SES3D]: http://www.cos.ethz.ch/software/ses3d.html
[LASIF]: http://www.lasif.net/
[seisDD]: https://github.com/yanhuay/seisDD

### 震源机制

- [gcap][]: 通用 Cut and Paste 方法反演震源机制
- [pyTDMT][]: 时间域震源机制反演的 Python 实现
- [WPhase][]: W Phase 方法反演震源机制
- [focmec][]: 确定并绘制震源机制

[gcap]: http://www.eas.slu.edu/People/LZhu/home.html
[pyTDMT]: https://github.com/fabriziobernardi/pydmt
[WPhase]: http://eost.u-strasbg.fr/wphase/
[focmec]: https://seiscode.iris.washington.edu/projects/focmec

### 震相拾取

- [PhasePApy][]: Python 写的震相拾取软件包
- [astack][]: 自适应迭代以实现震相对齐
- [CrazySeismic_Pick][]: 多通道相关实现震相对齐

[PhasePApy]: https://github.com/austinholland/PhasePApy
[astack]: http://rses.anu.edu.au/seismology/soft/astack/index.html
[CrazySeismic_Pick]: http://web.gps.caltech.edu/~yucq/software.html

### S波分裂

- [SplitLab][]: 基于 Matlab 的 S 波分裂处理工具
- [mutlisplit][]: S 波分裂处理工具
- [SplitRacer][]: S 波分裂处理工具

[SplitLab]: http://splitting.gm.univ-montp2.fr/
[multisplit]: https://github.com/ftilmann/multisplit
[SplitRacer]: http://www.geophysik.uni-frankfurt.de/64002762/Software

### 接收函数

- [hk][]: 用于接收函数研究的代码。
- [CCP][]: 共转换点地震数据叠加，用于接收函数研究。
- [rf][]: 接收函数
- [IRFFM][]: 带 GUI 的接收函数软件包
- [CrazySeismic_Decon][]: 基于Matlab的带GUI的接收函数软件包
- [FuncLab][]: 基于 Matlab的带 GUI 的接收函数软件包

[hk]: http://www.eas.slu.edu/People/LZhu/home.html
[CCP]: http://www.eas.slu.edu/People/LZhu/home.html
[rf]: https://github.com/trichter/rf
[IRFFM]: http://rses.anu.edu.au/~hrvoje/IRFFMv1.1.html
[CrazySeismic_Decon]: http://web.gps.caltech.edu/~yucq/software.html
[FuncLab]: https://robporritt.wordpress.com/software/

### 噪声成像

- [MSNoise][]: 利用地震背景噪声检测地下速度结构变化
- [seismic-noise-tomography][]: 噪声面波成像

[MSNoise]: http://www.msnoise.org/
[seismic-noise-tomography]: https://github.com/bgoutorbe/seismic-noise-tomography

## 数学处理类

- [SHTOOLS][]: 实现球谐相关操作，包括变换、重建、旋转、谱分析等。

[SHTOOLS]: https://github.com/SHTOOLS/SHTOOLS

## 函数库

- [libmseed][]: 用于读写 miniSEED 格式的 C 函数库

[libmseed]: https://seiscode.iris.washington.edu/projects/libmseed

## 其他

- [distaz][]: 给定震中和台站经纬度，计算震中距、方位角和反方位角的经典代码。
- [DigitSeis][]: 利用图像处理技术将模拟地震仪记录到的波形图片转换成数字信号（Matlab）
- [CitcomS][]: 求解地幔可压缩热动力学对流问题的有限元代码
- [AFAT][]: 根据 Cijkl 计算各向异性介质不同方向的速度

[distaz]: http://www.seis.sc.edu/software/distaz/
[DigitSeis]: http://www.seismology.harvard.edu/research/DigitSeis.html
[CitcomS]: https://github.com/geodynamics/citcoms
[AFAT]: http://cpc.cs.qub.ac.uk/summaries/AFAT_v1_0.html
