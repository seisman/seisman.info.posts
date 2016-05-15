---
title: SAC 容易忽略的一个陷阱
date: 2013-11-17
updated: 2014-04-18
author: SeisMan
categories: SAC
tags: SAC技巧
---

事情大概是这样的：当前文件夹下有很多个 SAC 文件（约 700 个，没有超过 SAC 一次只能处理 1000 个数据的限制），需要对 SAC 文件进行简单的滤波处理，然后保存。

PS：SAC 版本为 101.5c。

在 Perl 脚本中调用 SAC，一开始是这样写的：

``` perl
#!/usr/bin/env perl
use warnings;
use strict;

my @sacfiles = glob "N.*.U";

open(SAC,"| sac");
print SAC "r @sacfiles \n";
print SAC "rmean; rtr; taper \n";
print SAC "bp c 1 3 n 2 p 1 \n";
print SAC "w over \n";
print SAC "quit \n";
close(SAC);
```

第 5 行通过 `glob` 通配当前目录下的所有文件名符合 `N.*.U` 的文件。第 7-13 行，打开 SAC 进行数据处理，然后关闭 SAC。

这个脚本看似没有问题，但是经过比对就会发现，只有部分数据被正确地滤波了，所以 **这个脚本是错误的！**

为了验证究竟是哪里的问题，将上面的脚本修改一下，如下：

``` perl
#!/usr/bin/env perl
use warnings;
use strict;

my @sacfiles = glob "N.*.U";

open(SAC,"| sac");
print SAC "echo on errors warnings output commands macros processed \n";
print SAC "r @sacfiles \n";
print "read @sacfiles \n";
print SAC "rmean; rtr; taper \n";
print SAC "bp c 1 3 n 2 p 1 \n";
print SAC "w over \n";
print SAC "quit \n";
close(SAC);
```

脚本的第 8 行 `echo` 是 SAC 的一个命令，这个命令将显示全部 “错误、警告、输出、命令、宏、
处理后的命令”，因而可以用来监视 SAC 究竟做了什么。第 10 行 `print "read @sacfiles \n";` 用于验证 Perl 传递给 SAC 的究竟是什么，
这里使用 `read` 而不是 `r` 是为了区分 Perl 的输出和 SAC 的输出。

终端显示结果如下:

    read N.AGMH.U N.AGWH.U N.AHIH.U N.AIOH.U N.AIRH.U N.AJSH.U N.AKIH.U
    N.AKNH.U N.AKSH.U N.AMAH.U N.AMNH.U N.AMZH.U N.ANIH.U N.ANJH.U N.ANNH.U
    N.ANSH.U N.AOMH.U N.ARIH.U N.ARKH.U N.ASAH.U N.ASBH.U N.ASHH.U N.ASKH.U
    N.ASNH.U N.ASRH.U N.ASSH.U N.ASUH.U N.ASVH.U N.ATDH.U N.ATGH.U N.ATKH.U
    N.ATMH.U N.AWNH.U N.AYEH.U N.AYKH.U N.AYWH.U N.BEEH.U N.BEWH.U N.BFEH.U
    N.BFNH.U N.BFWH.U N.BHRH.U N.BKEH.U N.BKWH.U N.BREH.U N.BRWH.U N.BSEH.U
    N.BTOH.U N.BZNH.U N.CBAH.U N.CCNH.U N.CH2H.U N.CHKH.U N.CHNH.U N.CHZH.U
    N.CKRH.U N.CRNH.U N.CTSH.U N.CZEH.U N.DGOH.U N.DMOH.U N.DWAH.U N.EBTH.U
    N.EDSH.U N.EIHH.U N.FBRH.U N.FCHH.U N.FGNH.U N.FGSH.U N.FGTH.U N.FJEH.U
    N.FJIH.U N.FJOH.U N.FKCH.U N.FKRH.U N.FKSH.U N.FKUH.U N.FMIH.U N.FRKH.U
    N.FRNH.U N.FSTH.U N.FSWH.U N.FUTH.U N.GEIH.U N.GENH.U N.GHKH.U N.GJOH.U
    N.GKSH.U N.GNOH.U N.GOTH.U N.GR2H.U N.GSIH.U N.GZNH.U N.HAGH.U N.HASH.U
    N.HAZH.U N.HBAH.U N.HBTH.U N.HDKH.U N.HGAH.U N.HGIH.U N.HH2H.U N.HHEH.U
    N.HHIH.U N.HHNH.U N.HHRH.U N.HIKH.U N.HIMH.U N.HINH.U N.HIRH.U N.HISH.U
    N.HIYH.U N.HKBH.U N.HKSH.U N.HKTH.U N.HMAH.U N.HMMH.U N.HMNH.U N.HMSH.U
    N.HMTH.U N.HNBH.U N.HNKH.U N.HNOH.U N.HNRH.U N.HNSH.U N.HNZH.U N.HOBH.U
    N.HOCH.U N.HOFH.U N.HOJH.U N.HONH.U N.HOSH.U N.HOTH.U N.HOUH.U N.HRDH.U
    N.HRKH.U N.HRMH.U N.HRNH.U N.HRSH.U N.HRYH.U N.HSEH.U N.HSFH.U N.HSKH.U
    N.HSMH.U N.HTAH.U N.HTBH.U N.HTKH.U N.HWSH.U N.HYGH.U N.HYKH.U N.HYNH.U
    N.HYOH.U N.HYSH.U N.IAMH.U N.ICEH.U N.ICHH.U N.ICWH.U N.IGWH.U N.IHEH.U
    N.IICH.U N.IKIH.U N.IKKH.U N.IKNH.U N.IKSH.U N.IKTH.U N.IKWH.U N.IMIH.U
    N.IMRH.U N.INAH.U N.INEH.U N.INHH.U N.INMH.U N.INOH.U N.INSH.U N.INWH.U
    N.ISGH.U N.ISSH.U N.ITDH.U N.ITHH.U N.IWAH.U N.IWEH.U N.IWNH.U N.IWSH.U
    N.IWTH.U N.IWWH.U N.IWZH.U N.IZMH.U N.IZSH.U N.IZUH.U N.JHKH.U N.JNSH.U
    N.JUOH.U N.KACH.U N.KADH.U N.KAHH.U N.KAIH.U N.KAKH.U N.KAMH.U N.KANH.U
    N.KASH.U N.KAWH.U N.KAYH.U N.KDIH.U N.KGIH.U N.KGNH.U N.KGRH.U N.KGSH.U
    N.KHEH.U N.KHKH.U N.KHOH.U N.KHUH.U N.KHYH.U N.KIBH.U N.KIDH.U N.KIGH.U
    N.KIKH.U N.KIWH.U N.KIYH.U N.KIZH.U N.KJNH.U N.KJSH.U N.KKAH.U N.KKCH.U
    N.KKEH.U N.KKGH.U N.KKIH.U N.KKWH.U N.KKYH.U N.KMAH.U N.KMBH.U N.KMDH.U
    N.KMEH.U N.KMGH.U N.KMHH.U N.KMIH.U N.KMKH.U N.KMMH.U N.KMNH.U N.KMOH.U
    N.KMWH.U N.KMYH.U N.KNBH.U N.KNEH.U N.KNGH.U N.KNHH.U N.KNIH.U N.KNNH.U
    N.KNSH.U N.KNZH.U N.KOKH.U N.KORH.U N.KOSH.U N.KOTH.U N.KRHH.U N.KRIH.U
    N.KRMH.U N.KRTH.U N.KRYH.U N.KSAH.U N.KSBH.U N.KSGH.U N.KSIH.U N.KSMH.U
    N.KSOH.U N.KT2H.U N.KTDH.U N.KTGH.U N.KTMH.U N.KTNH.U N.KTRH.U N.KTWH.U
    N.KUCH.U N.KUMH.U N.KURH.U N.KWAH.U N.KWBH.U N.KWHH.U N.KWKH.U N.KWMH.U
    N.KWNH.U N.KWSH.U N.KWTH.U N.KWZH.U N.KYAH.U N.KYDH.U N.KYEH.U N.KYMH.U
    N.KYOH.U N.KYSH.U N.KYWH.U N.KZMH.U N.KZNH.U N.MABH.U N.MAKH.U N.MASH.U
    N.MBEH.U N.MBUH.U N.MBWH.U N.MCTH.U N.MGMH.U N.MGWH.U N.MHRH.U N.MHSH.U
    N.MICH.U N.MIEH.U N.MIGH.U N.MIHH.U N.MIKH.U N.MINH.U N.MISH.U N.MITH.U
    N.MIZH.U N.MJNH.U N.MJSH.U N.MKGH.U N.MKIH.U N.MKJH.U N.MKMH.U N.MKOH.U
    N.MKRH.U N.MKWH.U N.MMBH.U N.MMKH.U N.MMOH.U N.MMRH.U N.MMTH.U N.MNAH.U
    N.MNEH.U N.MNKH.U N.MNMH.U N.MNOH.U N.MOKH.U N.MORH.U N.MOTH.U N.MRMH.U
    N.MROH.U N.MRRH.U N.MRUH.U N.MS2H.U N.MSAH.U N.MSFH.U N.MSIH.U N.MSNH.U
    N.MSTH.U N.MTDH.U N.MTKH.U N.MTMH.U N.MTOH.U N.MTYH.U N.MUIH.U N.MURH.U
    N.MYJH.U N.MYKH.U N.MYMH.U N.MZEH.U N.MZKH.U N.NAGH.U N.NANH.U N.NAWH.U
    N.NAZH.U N.NCNH.U N.NCPH.U N.NDGH.U N.NEOH.U N.NFRH.U N.NGIH.U N.NGKH.U
    N.NGOH.U N.NGRH.U N.NGSH.U N.NGTH.U N.NGUH.U N.NGWH.U N.NHEH.U N.NHJH.U
    N.NHWH.U N.NITH.U N.NJMH.U N.NKEH.U N.NKMH.U N.NKNH.U N.NKOH.U N.NKTH.U
    N.NKWH.U N.NMEH.U N.NMKH.U N.NMNH.U N.NMTH.U N.NNMH.U N.NOBH.U N.NRAH.U
    N.NRKH.U N.NRTH.U N.NS2H.U N.NSBH.U N.NSEH.U N.NSHH.U N.NSMH.U N.NSNH.U
    N.NSSH.U N.NSTH.U N.NTBH.U N.NTGH.U N.NTHH.U N.NUKH.U N.NUMH.U N.NWAH.U
    N.NYAH.U N.NYOH.U N.NYRH.U N.NZWH.U N.OBMH.U N.ODTH.U N.ODWH.U N.OGCH.U
    N.OGNH.U N.OGOH.U N.OHAH.U N.OHCH.U N.OHRH.U N.OHTH.U N.OIWH.U N.OKCH.U
    N.OKEH.U N.OKMH.U N.OKYH.U N.OKZH.U N.OM2H.U N.OMMH.U N.OMRH.U N.ONDH.U
    N.ONIH.U N.ONPH.U N.OOCH.U N.OOKH.U N.OOMH.U N.OOTH.U N.OOZH.U N.OPEH.U
    N.OPWH.U N.OREH.U N.ORWH.U N.OSUH.U N.OTAH.U N.OTOH.U N.OTUH.U N.OTWH.U
    N.OUMH.U N.OWNH.U N.OWSH.U N.OYMH.U N.RBSH.U N.RKBH.U N.RKSH.U N.RNKH.U
    N.RZTH.U N.SADH.U N.SAIH.U N.SAKH.U N.SAMH.U N.SATH.U N.SBAH.U N.SBKH.U
    N.SBNH.U N.SBSH.U N.SCNH.U N.SCSH.U N.SDAH.U N.SDMH.U N.SDWH.U N.SENH.U
    N.SETH.U N.SFNH.U N.SFSH.U N.SGOH.U N.SGRH.U N.SGUH.U N.SGWH.U N.SHGH.U
    N.SHJH.U N.SHKH.U N.SHMH.U N.SHZH.U N.SIKH.U N.SINH.U N.SISH.U N.SJOH.U
    N.SKGH.U N.SKIH.U N.SKNH.U N.SKSH.U N.SKUH.U N.SKWH.U N.SMAH.U N.SMGH.U
    N.SMMH.U N.SMNH.U N.SMPH.U N.SMSH.U N.SMTH.U N.SNDH.U N.SNIH.U N.SNNH.U
    N.SNSH.U N.SNTH.U N.SNWH.U N.SOIH.U N.SOJH.U N.SONH.U N.SOSH.U N.SRIH.U
    N.SRMH.U N.SROH.U N.SRUH.U N.SRWH.U N.SSKH.U N.SSMH.U N.SSRH.U N.SSSH.U
    N.SSTH.U N.SSWH.U N.SSYH.U N.ST1H.U N.ST2H.U N.ST3H.U N.ST4H.U N.ST5H.U
    N.ST6H.U N.STDH.U N.STKH.U N.STNH.U N.STRH.U N.STSH.U N.SUGH.U N.SUKH.U
    N.SUZH.U N.SWEH.U N.SWWH.U N.SYKH.U N.SYNH.U N.SYOH.U N.SYSH.U N.SYTH.U
    N.SZGH.U N.SZJH.U N.SZKH.U N.SZNH.U N.SZUH.U N.SZWH.U N.TAGH.U N.TAJH.U
    N.TAKH.U N.TAMH.U N.TARH.U N.TAYH.U N.TBEH.U N.TBRH.U N.TBTH.U N.TBYH.U
    N.TCKH.U N.TDEH.U N.TDMH.U N.TDOH.U N.TGIH.U N.TGKH.U N.TGOH.U N.TGUH.U
    N.THGH.U N.THNH.U N.THTH.U N.TISH.U N.TJOH.U N.TJRH.U N.TKBH.U N.TKEH.U
    N.TKGH.U N.TKHH.U N.TKIH.U N.TKJH.U N.TKKH.U N.TKNH.U N.TKRH.U N.TKSH.U
    N.TKTH.U N.TKUH.U N.TKWH.U N.TMAH.U N.TMGH.U N.TMNH.U N.TMOH.U N.TMYH.U
    N.TNEH.U N.TNMH.U N.TOBH.U N.TOGH.U N.TOHH.U N.TOIH.U N.TOKH.U N.TOMH.U
    N.TOUH.U N.TOWH.U N.TOYH.U N.TREH.U N.TRGH.U N.TRIH.U N.TROH.U N.TRSH.U
    N.TRUH.U N.TRWH.U N.TSKH.U N.TSMH.U N.TSOH.U N.TSRH.U N.TSSH.U N.TSTH.U
    N.TSUH.U N.TSYH.U N.TT2H.U N.TTAH.U N.TTKH.U N.TTNH.U N.TU2H.U N.TUMH.U
    N.TUNH.U N.TUSH.U N.TWAH.U N.TWEH.U N.TWWH.U N.TY2H.U N.TYEH.U N.TYHH.U
    N.TYMH.U N.TYOH.U N.TYRH.U N.TYTH.U N.TYUH.U N.TZWH.U N.UBEH.U N.UCNH.U
    N.UCUH.U N.UJEH.U N.UKHH.U N.UMEH.U N.UMIH.U N.UMWH.U N.UMYH.U N.UNNH.U
    N.UNSH.U N.UOZH.U N.URSH.U N.USDH.U N.UUMH.U N.UWAH.U N.UWEH.U N.WATH.U
    N.WKMH.U N.WKYH.U N.WNEH.U N.WNNH.U N.WNWH.U N.WSMH.U N.YABH.U N.YBKH.U
    N.YBNH.U N.YBRH.U N.YFTH.U N.YGDH.U N.YGNH.U N.YGTH.U N.YHBH.U N.YITH.U
    N.YJMH.U N.YKHH.U N.YKIH.U N.YKWH.U N.YM2H.U N.YMAH.U N.YMDH.U N.YMGH.U
    N.YMIH.U N.YMMH.U N.YMSH.U N.YMTH.U N.YNDH.U N.YNTH.U N.YNZH.U N.YOKH.U
    N.YOTH.U N.YROH.U N.YSDH.U N.YSHH.U N.YSKH.U N.YTOH.U N.YUBH.U N.YUZH.U
    N.YWTH.U N.YZEH.U N.YZWH.U

    r N.AGMH.U N.AGWH.U N.AHIH.U N.AIOH.U N.AIRH.U N.AJSH.U N.AKIH.U
    N.AKNH.U N.AKSH.U N.AMAH.U N.AMNH.U N.AMZH.U N.ANIH.U N.ANJH.U N.ANNH.U
    N.ANSH.U N.AOMH.U N.ARIH.U N.ARKH.U N.ASAH.U N.ASBH.U N.ASHH.U N.ASKH.U
    N.ASNH.U N.ASRH.U N.ASSH.U N.ASUH.U N.ASVH.U N.ATDH.U N.ATGH.U N.ATKH.U
    N.ATMH.U N.AWNH.U N.AYEH.U N.AYKH.U N.AYWH.U N.BEEH.U N.BEWH.U N.BFEH.U
    N.BFNH.U N.BFWH.U N.BHRH.U N.BKEH.U N.BKWH.U N.BREH.U N.BRWH.U N.BSEH.U
    N.BTOH.U N.BZNH.U N.CBAH.U N.CCNH.U N.CH2H.U N.CHKH.U N.CHNH.U N.CHZH.U
    N.CKRH.U N.CRNH.U N.CTSH.U N.CZEH.U N.DGOH.U N.DMOH.U N.DWAH.U N.EBTH.U
    N.EDSH.U N.EIHH.U N.FBRH.U N.FCHH.U N.FGNH.U N.FGSH.U N.FGTH.U N.FJEH.U
    N.FJIH.U N.FJOH.U N.FKCH.U N.FKRH.U N.FKSH.U N.FKUH.U N.FMIH.U N.FRKH.U
    N.FRNH.U N.FSTH.U N.FSWH.U N.FUTH.U N.GEIH.U N.GENH.U N.GHKH.U N.GJOH.U
    N.GKSH.U N.GNOH.U N.GOTH.U N.GR2H.U N.GSIH.U N.GZNH.U N.HAGH.U N.HASH.U
    N.HAZH.U N.HBAH.U N.HBTH.U N.HDKH.U N.HGAH.U N.HGIH.U N.HH2H.U N.HHEH.U
    N.HHIH.U N.HHNH.U N.HHRH.U N.HIKH.U N.HIMH.U N.HINH.U N.HIRH.U N.HISH.U
    rmean; rtr; taper
    bp c 1 3 n 2 p 1
    w over
    quit

可以看到：第 1 行是 Perl 的输出，也就是 Perl 的 print 语句传递给 SAC 句柄的内容，其
正确的传递了 700 多个文件的文件名。第 3 行之后为 SAC 的输出，可以看到第 3 行的内容与
第 1 行内容类似，但是明显短了非常多。这意味着 **部分内容在由 Perl 传递给 SAC 之后丢失了**。

可以比较容易地发现，SAC 显示的 `read` 语句长度为 1002 字符，大概就是 1000 字符，所以猜测是
SAC 在读取命令行的内容时，其字符串数组的长度限制在 1000 字符，进而导致 Perl 传递进来
700 多个文件名，实际上 SAC 只处理了 120 个（120 个文件名基本是 1000 字符）。

查看 SAC 源码可以发现，SAC 中用字符数组 `kline[MCMSG+1]` 来处理命令行输入，其中 `MCMSG`
 的值为 1001，即 `kline` 的有效长度仅仅是 1001，加上的 1 是为了处理 C 语言的 `'\0'` 。

由于 SAC 的确处理了前 1000 个字符，即前 120 个文件，所以整个过程都不会报错！所以这个 Bug 很难察觉！

几个可以避免该问题的 Perl 脚本：

``` perl
#!/usr/bin/env perl
use warnings;
use strict;

open(SAC,"| sac");
print SAC "r N.*.U \n";
print SAC "rmean; rtr; taper \n";
print SAC "bp c 1 3 n 2 p 1 \n";
print SAC "w over \n";
print SAC "quit \n";
close(SAC);
```

这个脚本没有问题，因为这里的通配符 `N.*.U` 是由 SAC 去解释而不是由 Bash 去解释，所以 SAC 接收到的命令行长度只有不到 10 个字符。但是这个脚本不够通用，因为有些时候需要处理的文件无法用通配符表示，比如要处理所有震中距在 10 到 30 度以内的文件。

``` perl
#!/usr/bin/env perl
use warnings;
use strict;

my @sacfiles = glob "N.*.U";

open(SAC,"| sac");
foreach (@sacfiles){
   print SAC "r $_ \n";
   print SAC "rmean; rtr; taper \n";
   print SAC "bp c 1 3 n 2 p 1 \n";
   print SAC "w over \n";
}
print SAC "quit \n";
close(SAC);
```

这个脚本还是继续使用 Perl 的 `glob`，然后使用 `foreach` 循环，每次只处理一个文件，
也不会出现问题，速度相对上一个版本可能会慢一些，不过有时候可能就需要这样做。

``` perl
#!/usr/bin/env perl
use warnings;
use strict;

my @sacfiles = glob "N.*.U";

open(SAC,"| sac");
foreach (@sacfiles){
   print SAC "r more $_ \n";
}
print SAC "rmean; rtr; taper \n";
print SAC "bp c 1 3 n 2 p 1 \n";
print SAC "w over \n";
print SAC "quit \n";
close(SAC);
```

该脚本使用 `foreach` 循环，不断读入更多的文件，然后一次性进行数据处理，相对于上一个脚本而言，速度要快很多。

## 修订历史

-   2013-11-17：初稿；
-   2014-04-18：根据 SAC 源码确认了 SAC 能处理的命令行长度为 1000 字符；
-   2014-05-19：增加了第三个可以避免该问题的脚本；
