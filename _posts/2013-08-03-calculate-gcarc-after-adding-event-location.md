---
title: SAC 文件修改事件经纬度后震中距的自动计算
date: 2013-08-03
author: SeisMan
categories: SAC
tags: [SAC技巧, 震中距]
---

地震目录中包含震中的经度、纬度、深度等信息，有些时候下载的数据中没有这些事件信息，
就需要自己手动添加进去。

很基础的操作:

    SAC > r *.BH*
    SAC > ch evla 30.5 evlo 120.5 evdp 5.0
    SAC > wh
    SAC > q

修改了地震经纬度及深度信息之后，一般来说，震中距 dist、gcarc 以及方位角 az、baz 也会
随着一起改变。但是，有些时候这些量却没有随着事件位置的变化而变化，这是为什么呢？

<!--more-->

在 SAC 的头段中有一个逻辑型变量 `LCALDA`（L 代表 logical 型变量，CAL 代表 calculate，
D 代表 dist 以及 gcarc，a 代表 az 以及 gaz）。这个逻辑型变量决定了 gcarc 等参数是否会随着
震源或台站的位置的改变而改变。`LCALDA` 为 `TRUE` 则会随着改变，为 `FALSE` 则不会改变。

下面用一些测试来深入了解一下：

    SAC> fg seis
    SAC> lh dist gcarc az baz                     #看看原始文件的震中距和方位角

      FILE: SEISMOGR - 1
     --------------

          dist = 3.730627e+02
         gcarc = 3.357465e+00
            az = 8.814721e+01
           baz = 2.718528e+02

    SAC> lh evla evlo evdp lcalda                 #看看事件位置信息和 LCALDA 变量

      FILE: SEISMOGR - 1
     --------------

           evla = 4.800000e+01
           evlo = -1.250000e+02
           evdp = 1.500000e+01
         lcalda = TRUE
    SAC> ch evla 55                               #修改事件位置
    SAC> lh dist gcarc az baz                     #震中距方位角马上就变了

      FILE: SEISMOGR - 1
     --------------

          dist = 8.521611e+02
         gcarc = 7.670734e+00
            az = 1.539900e+02
           baz = 3.379012e+02
    SAC> ch lcalda false                         #修改 lcalda 为 false
    SAC> ch evla 60
    SAC> lh dist gcarc az baz                    #震中距方位角没有变化

      FILE: SEISMOGR - 1
     --------------

          dist = 8.521611e+02
         gcarc = 7.670734e+00
            az = 1.539900e+02
           baz = 3.379012e+02
    SAC> ch lcalda true                          #再次把 lcalda 修改为 true
    SAC> lh dist gcarc az baz                    #震中距信息马上就修改了。
                                                 #这意味着在修改 lcalda 为真时
                                                 #SAC 会自动检查某些变量值

      FILE: SEISMOGR - 1
     --------------

          dist = 1.374330e+03
         gcarc = 1.237276e+01
            az = 1.641464e+02
           baz = 3.482054e+02
