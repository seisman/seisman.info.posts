---
title: 利用 TauP 为 SAC 文件标记理论到时
date: 2014-11-10
author: SeisMan
categories: 地震学软件
tags: [TauP, 走时]
---

TauP 的 `taup_time` 命令可以计算各震相的理论走时，但是不能帮我们把到时信息
标记到 SAC 文件中，因而就需要写脚本处理 `taup_time` 的输出，并修改 SAC 头段。

`taup_setsac` 帮我们完成了这一点，可以直接计算理论到时并将到时信息写入到 SAC 文件中。

其用法很简单，示例如下:

    taup_setsac -mod prem -ph P-0,S-1,PcP-8,ScS-9 -evdpkm *.U

其中：

- `-mod prem` ：指定地球模型为 PREM 模型；
- `-ph P-0,S-1,PcP-8,ScS-9`：将 P 波到时标记到 T0 中，S 到时标记到 T1 中，PcP 标记到 T8，ScS 标记到 T9。
- `-evdpkm`：由于历史的原因，该命令默认 SAC 文件中的震源深度单位为米，而现在的 SAC 文件中的震源深度单位为千米。该选项设置深度的单位为 `km`
- `*.U` : 需要标记理论到时的 SAC 文件

该命令在将震相走时标记到 Tn 的同时，还会修改对应的 KTn 和 USERn，其中 KTn 中保存震相名，USERn 中保存震相的射线参数（单位为秒每弧度）。

需要注意的是，执行命令时经常会忘记 `-evdpkm` 选项，此时该命令会给出警告。
需要注意，一定不要按 `Ctrl+C` 终止此次命令。因为 `taup_setsac` 需要读入
并修改 SAC 文件，然后将 SAC 文件写回磁盘覆盖原文件，用 `Ctrl+C` 终止命令，
会导致文件写回磁盘失败，进而导致部分 SAC 文件损坏。正确的做法是不要理会这些警告，
待程序执行完毕之后再加上 `-evdpkm` 选项重新执行。
