---
title: Perl 中的时间加法
date: 2013-10-16
author: SeisMan
categories:
  - 编程
tags:
  - Perl
  - 时间
  - 模块
slug: timespan-in-perl
---

数据申请的过程中，经常需要处理的一个问题是：已知某时刻，在该时刻的基础上加上一段时间之后对应的时刻是多少？

<!--more-->

## 基本解法

最朴素的思想是自己写一个程序：

-   把该时刻的年月日时分秒分别加上一个时间间隔；
-   检查秒数，若秒数大于 60，则秒数减 60 同时分钟数加 1；
-   检查分钟，若分钟数大于 60，则分钟数减 60 同时小时数加 1；
-   检查小时，若小时大于 24，则小时数减 24 同时天数加 1；
-   根据当前月份确定当前月有多少天，如果超过该天数，则减去天数值，月份进 1；这里大概要做 12 次判断，同时还要考虑闰年的问题；
-   然后就发现这样的办法太麻烦了。。

## 高级解法

更高端一些的解法是，计算当前时刻与某个特定时刻的秒数差，然后再加上时间间隔，再将新的秒数差转换为时刻。

其实程序写起来依然很麻烦。在 Perl 中，已经有相当多的模块可以用于解决这个问题，直接调用即可。Perl 模块的强大之处即在此，这也是我不再使用 Bash 的一个原因。

## timegm

Perl 的模块 Time::Local 下有个函数，叫做 timegm。其用法如下：

    $time = timegm($sec, $min, $hour, $mday, $mon, $year);

输入参数有 6 个（默认情况下，该函数会进行输入检查，以确保这六个元素给定的时间的存在性。）

-   `$sec`：秒（0-59）；
-   `$min`：分（0-59）；
-   `$hour`：时（0-23）
-   `$mday`：每月的第几天（1-31）；
-   `$mon`：月份**（0-11）**；
-   `$year`：年份；

关于年份，其范围要复杂一些：

-   如果 `$year>999`，则将其解释为真实的年份；
-   如果 `$year` 在 100 到 999 之间，则将其解释为与 1900 年的年份差；
-   如果 `$year` 在 0 到 99 之间，规则已经复杂的没有必要了。。。

对于实际应用来说，前两条规则就够用了。

该函数的输出是当前时刻**相对于1970年1月1日午夜的秒数**。

## gmtime

Perl 内置一个函数 `gmtime`，`Time::Local` 模块里的 `timegm` 实际上是该函数的逆函数。

其用法如下:

    ($sec ,$min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = gmtime($time);

其输入是相对于 1970 年 1 月 1 日午夜的秒数。

其输出有 9 个元素：

-   `$sec`：秒（0-59）；
-   `$min`：分（0-59）；
-   `$hour`：时（0-23）
-   `$mday`：每月的第几天（1-31）；
-   `$mon`：月份**（0-11）**；
-   `$year`：年份 - 1900；
-   `$wday`：周的第几天（0-6）；0 代表周日，1 代表周一；
-   `$yday`：一年的第几天（0-364 或者 0-365）；
-   `$isdst`：是否是夏令时（0-1）

## 脚本实现

``` perl
#!/usr/bin/env perl
# Example to show the use of time_add

use strict;
use warnings;
use Time::Local;

# 当前时刻为 2013 年 10 月 12 日 04 时 5 分 0 秒
#   - 04 时或者 4 时都可以
#   - 10 月是真正的 10 月
#   - 子函数中的变量与主函数中变量相互独立
my $year = 2013;
my $mon = 10;
my $day = 12;
my $hour = 04;
my $min = 5;
my $sec = 0;

# 时间差，5 分 15 秒
my $span = 5*60+15;

print "BEFORE $year/$mon/$day $hour:$min:$sec\n";

($year, $mon, $day, $hour, $min, $sec) =
    &time_add($year, $mon, $day, $hour, $min, $sec, $span);

print "AFTER  $year/$mon/$day $hour:$min:$sec\n";


# 子程序
sub time_add(){
    my ($year, $mon, $day, $hour, $min, $sec, $timespan) = @_;
    my ($wday, $yday, $isdast);

    # 函数的月份范围为 0-11
    $mon -= 1;

    # 计算该时刻与 1970 年 1 月 1 日午夜的秒数差
    my $time = timegm($sec, $min, $hour, $day, $mon, $year);

    # 将该秒数加上一个时间差
    $time += $timespan;

    # 将时间差转换为具体的时刻
    ($sec, $min, $hour, $day, $mon, $year, $wday, $yday, $isdast) = gmtime($time);

    # 对年份和月份特殊处理
    $year += 1900;
    $mon += 1;

    # 返回
    return ($year, $mon, $day, $hour, $min, $sec);
}
```

## 参考来源

1.  [Perl 中的时间](http://cn.perlmaven.com/the-year-19100)
2.  [Perl 内置文档](http://perldoc.perl.org/functions/localtime.html)
3.  [Time::Local 模块](http://perldoc.perl.org/Time/Local.html)
