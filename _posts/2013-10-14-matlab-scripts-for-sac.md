---
title: 用 Matlab 处理 SAC 数据的一些脚本
date: 2013-10-14
author: SeisMan
categories: 地震学软件
tags: [SAC技巧, Matlab]
---

我是那种乖乖用 SAC 处理 sac 数据的人。身边有些老师及其学生比较喜欢用 matlab 处理 sac 数据，
故而这里还是收集一下相关脚本，以造福部分人。

## 来源 1

其实 SAC 包中自带了一些 matlab 脚本。

在 `sac/utils` 目录下有四个 matlab 脚本，作者 Xiaoning Yang，具体功能看文件名，具体用法看脚本：

    getsacdata.m  padcat.m  readsac.m  writesac.m

在 sac/aux/mat 目录有 62 个脚本文件，看上去功能很齐全，可能是 SAC 调用 matlab 引擎后可以执行的一些命令，不确定是否可以直接调用：

    arrow3d.m              GetFiles2.m          mat.m           SaveResults.m
    BAZauto.m              GetFiles.m           mkAxisSymb.m    ScrollHelp.m
    BAZ.m                  getMisFit.m          mkcircle.m      setAZIM.m
    ButtonRelease.m        getReferenceTime.m   MLest.m         setDomain.m
    CalcMLM.m              getWinPolariz.m      MLMcallback.m   setELEV.m
    closePPM.m             hclose.m             mlm.m           SetFilter.m
    crosshair.m            inspCallbacks.m      NextGroup.m     SetHighCorner.m
    deleteDuplicatePick.m  inspector.m          plotmain.m      SetLowCorner.m
    DeletePick.m           inspFigure.m         ppm3.m          SetOrder.m
    DispatchButtonPress.m  inspRealPlot.m       PrevGroup.m     SetPickType.m
    DispatchKeys.m         inspToolbar.m        printfig.m      SetUpSlider.m
    DispatchMouseMove.m    magnifyTrces.m       quitP.m         SetWaveType.m
    dispHelp.m             MainButtonPress.m    RedrawSeis.m    UpdatePPMplot.m
    DoRotations.m          MainButtonRelease.m  RotateToBAZ.m   Winpolariz.m
    drawRect.m             MainMouseMove.m      SacCheck.m
    filterTraces.m         makeFigure.m         SaveResults2.m

## 来源 2

Prof. Zhigang Peng 或收集、或编写、或改写了部分 matlab 脚本，如下：

    fget_sac.m newSacHeader.m  rdSacHead.m  rdSac.m  sacfft.m  sachdr.m  sac.m wtSac.m

下载地址位于： [MacSAC.tar.gz](http://geophysics.eas.gatech.edu/people/zpeng/Teaching/MatSAC.tar.gz)

具体用法可以看脚本或者点击 [这里](http://geophysics.eas.gatech.edu/classes/SAC/)。

## 来源 3

Prof. Michael Thorne 写了几个 matlab 脚本：

    rsac.m - Read SAC binary
    wsac.m - Write SAC binary
    bsac.m - Be SAC - convert Matlab array to saclab format
    lh.m - List header
    ch.m - Change header
    p1.m - Plot traces (one plot per subplot) - Example screenshot
    p2.m - Plot traces (overlay traces) - Example screenshot
    marktimes.m - Calculate travel times and put in SAC header (by Sean Ford)

下载地址：<http://web.utah.edu/thorne/software.html>
