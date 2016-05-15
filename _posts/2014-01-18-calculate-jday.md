---
title: 计算某日是一年中的第几天
date: 2014-01-18
updated: 2014-08-25
author: SeisMan
categories: 编程
tags: [时间, C]
---

两个子程序， `ymd2doy` 用于从年月日计算该日为当年的第几天， `doy2ymd` 用于根据年份以及
该年的第几天来确定月和日。

`ymd2doy` 的代码很粗暴，直接定义了 leap 和 noleap 数组，简单粗暴，忘了该代码片段的来源了。

``` C
static int noleap[12] = {0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334};
static int   leap[12] = {0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335};

/* convert month and day to day of year */
int ymd2doy(int year, int month, int day)
{
    if ((year%4==0 && year%100!=0) || (year%400==0))
        return leap[month-1] + day;
    else
        return noleap[month-1] + day;
}

/* convert day of year to month and day */
void doy2ymd(int year, int doy, int *month, int *day)
{
    int *days_since_start;
    int i;

    if ((year%4==0 && year%100!=0) || (year%400==0))
        days_since_start = leap;
    else
        days_since_start = noleap;

    for (i=0; i<11; i++)
        if (doy < days_since_start[i+1]) break;
    if (i==10 && doy> days_since_start[11]) i++;

    *month = i+1;
    *day = doy - days_since_start[i];
}
```

下面是另一个版本：

``` C
static int days_in_month[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31};

int ymd2doy(int year, int month, int day)
{
    int i;
    int doy = 0;

    for (i=0; i<month-1; i++) {
        doy += days_in_month[i];
        if(i==1 && ISLEAP(year)) doy++;
    }
    doy += day;

    return doy;
}

void doy2ymd(int year, int doy, int *month, int *day)
{
    int i, dim, leap;

    leap = ISLEAP(year);
    *day = doy;
    for (i=0; i<12; i++) {
        dim = days_in_month[i];
        if(leap && i==1) dim++;
        if(*day <= dim) break;
        *day -= dim;
    }
    *month = i + 1;
}
```

## 修订历史

-   2014-01-18：初稿；
-   2014-08-23：将 Perl 版修改为 C 版，并加入了 `doy2ymd`；
-   2014-08-25：新增了另一个版本的代码；
