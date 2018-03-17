---
title: SeisMan博客
author: '[seisman](http://seisman.info)'
---

# 地震学基础

## 基础知识

- [体力与等效体力](/post/2013-09-16-body-force-equivalents.md)
- [地震学中的坐标系](/post/2017-01-12-coordinate-systems-in-seismology.md)
- [地震学断层的定义](/post/2013-09-26-faults-in-seismology.md)
- [标量矩与矩震级转换关系](/post/2013-07-02-scalar-moment-and-moment-magnitude.md)
- [辐射花样的计算与震源球的绘制](/post/2014-05-01-radiation-pattern-and-beach-ball.md)
- [慢度与射线参数](/post/2015-02-05-slowness-and-ray-parameter.md)
- [震相走时的计算](/post/2015-05-02-traveltime-calculation.md)
- [球状模型下的 Tau 积分](/post/2015-05-15-tau-integral-in-spherical-earth.md)

## 仪器响应

- [地震学的仪器响应](/post/2013-06-23-instrumental-response.md)
- [仪器响应的物理细节](/post/2013-06-26-instrumental-response-physical-details.md)
- [仪器响应文件 RESP](/post/2013-06-27-instrumental-response-resp.md)
- [仪器响应文件 SAC PZ](/post/2013-06-28-instrumental-response-sacpz.md)
- [用 RESP 和 PZ 去除仪器响应的差别](/post/2013-06-29-resp-sacpz-difference.md)
- [仪器响应实例分析](/post/2013-06-30-instrumental-response-details.md)
- [freqlimits 的选取](/post/2014-01-16-how-to-choose-freqlimits.md)

# 地震学软件

## TauP {#taup-toolkit}

- [走时计算软件包](/post/2014-03-29-traveltime-packages.md)
- [走时计算软件TauP](/post/2013-07-10-taup.md)
- [TauP 的安装](/post/2014-10-08-taup-install.md)
- [利用 TauP 计算射线穿透点](/post/2014-11-07-taup-calculate-pierce-points.md)
- [利用 TauP 为 SAC 文件标记理论到时](/post/2014-11-10-taup-mark-traveltime.md)
- [用 taup_time 计算震相走时及射线信息](/post/2015-01-24-taup-calculate-traveltime.md)
- [TauP 自定义模型](/post/2016-05-21-taup-custom-models.md)
- [识别 TauP 输出中的多个 P 震相](/post/2016-05-22-taup-identify-multiple-P-phases.md)
- [计算任意深度处下表面反射波走时](/post/2017-03-31-taup-calculate-underside-reflection-traveltime.md)

## SAC

- [SAC 参考手册中文版](/post/2013-07-06-sac-manual.md)
- [用 SAC 快速拾取震相](/post/2016-02-19-faster-ppk.md)
- [SAC 文件读写模块 sacio_Fortran](/post/2016-07-19-sacio-fortran90.md)
- [SAC 文件修改事件经纬度后震中距的自动计算](/post/2013-08-03-calculate-gcarc-after-adding-event-location.md)
- [SAC 不同格式间的转换](/post/2013-08-04-conversion-of-different-sac-formats.md)
- [脚本中调用 SAC 时不显示版本信息](/post/2013-12-26-sac-display-copyright.md)
- [SAC 修改绘图窗口的背景色](/post/2014-06-15-change-background-color-of-window-in-sac.md)
- [SEED 格式转 SAC 格式](/post/2015-06-19-convert-seed-to-sac.md)
- [SAC 中将位移记录转换成速度记录](/post/2016-01-12-sac-convert-displacement-to-velocity.md)
- [PPK 标记震相到时的一些注意事项](/post/2013-08-20-ppk-notes.md)
- [判断 SAC 数据是否已去除仪器响应](/post/2016-03-13-instrumental-response-removed-or-not.md)

## GMT

- [GMT 4.5.17 在 Linux 下的安装](/post/2013-11-07-install-gmt4-under-linux.md)
- [GMT 4 在 Mac 下的安装](/post/2015-09-05-install-gmt4-under-mac.md)
- [GMT4 与 GMT5 双版本共存](/post/2013-11-09-multiple-versions-of-gmt.md)
- [Windows 下使用 GMT 的正确姿势](/post/2014-12-10-how-to-use-gmt-under-windows.md)
- [GMT4 脚本风格指南](/post/2014-05-13-gmt4-style-guide.md)
- [在 GMT 中使用 LaTeX](/post/2013-10-24-gmt-latex.md)
- [GMT 绘制地理坐标与笛卡尔坐标混合体](/post/2014-04-26-mix-geographical-coordinate-with-cartesian-coordinate.md)
- [等震中距线的绘制](/post/2014-05-21-plot-equal-distance-lines.md)
- [GMT 绘制双 Y 轴](/post/2014-06-12-double-y-axis-plot.md)
- [不同比例尺曲线的画法](/post/2015-02-01-plot-multiple-lines-in-different-scales.md)
- [GMT 边框发虚的原因及解决办法](/post/2014-12-09-blurry-frame-in-gmt.md)
- [GMT 中添加注释和标注](/post/2014-12-28-add-annotations-in-gmt.md)
- [修改 Y 轴的坐标标注的方向](/post/2015-03-11-change-orientation-of-y-axis-annotations.md)
- [修改 GMT 生成的 PS 文件的标题](/post/2015-03-14-change-title-of-postscript-files-generated-by-gmt.md)
- [底图边框与网格线](/post/2015-05-19-frame-and-gridline.md)
- [GMT5 自定义坐标轴](/post/2015-06-06-gmt5-custom-axes.md)
- [GMT 绘制无刻度轴](/post/2015-07-15-axes-without-ticks.md)
- [GMT 区域填色](/post/2015-08-05-area-fill.md)
- [GMT 绘制图中图](/post/2015-08-16-gmt-insert-map.md)
- [GMT 添加断层名](/post/2015-08-21-plot-fault-names.md)
- [绘制事件与台站间的连线](/post/2015-11-19-raypath-between-events-and-stations.md)
- [在地图上绘制特定的经纬线](/post/2015-12-11-plot-specified-gridline-on-maps.md)
- [绘制颜色渐变的线条](/post/2016-01-18-plot-lines-with-gradient-colors.md)
- [在极坐标下绘制深度剖面](/post/2016-03-12-depth-profile-in-polar-coordinates.md)
- [用海岸线裁剪区域](/post/2013-10-30-coastline-clip.md)
- [计算某点离海岸线的距离](/post/2014-02-21-calculate-distance-to-coast.md)
- [从 3D 数据中截取剖面](/post/2015-04-08-profile-from-3d-data.md)
- [判断点在多边形内](/post/2015-10-10-points-inside-polygons.md)

## pssac

- [安装 pssac](/post/2013-08-04-pssac-install.md)
- [pssac 使用教程](/post/2015-07-17-pssac-notes.md)
- [在地图上绘制波形](/post/2015-07-18-plot-traces-on-maps.md)
- [绘制波形对比图](/post/2013-09-15-waveform-comparison-plot.md)
- [pssac2 的安装](/post/2013-08-09-pssac2-install.md)
- [pssac2 使用教程](/post/2015-07-19-pssac2-notes.md)

## fk

- [fk3.2 编译](/post/2013-09-01-fk-install.md)
- [fk 用法笔记](/post/2015-02-28-fk-notes.md)

## 其他

- [hk1.3 编译](/post/2013-09-08-hk-install.md)
- [MoPaD:地震矩绘制和分析工具](/post/2013-08-27-mopad.md)
- [由矩张量计算双力偶断层参数](/post/2013-07-16-moment-tensor-to-double-couple.md)
- [gCAP 的安装](/post/2014-06-13-gcap-install.md)
- [震中距、方位角和反方位角的计算](/post/2013-07-03-calculate-dist-az-baz.md)
- [JPlotResp：绘制地震仪器响应](/post/2013-07-19-jplotresp.md)
- [CCP1.0 编译](/post/2013-11-29-ccp-install.md)
- [CPS330 : Computer Programs in Seismology](/post/2014-01-01-cps330.md)
- [CPS330 的安装](/post/2015-05-12-cps330-install.md)
- [安装 evt2sac](/post/2015-07-31-evt2sac-install.md)
- [rdseed 的安装](/post/2014-10-07-rdseed-install.md)
- [rdseed 用法笔记](/post/2015-10-13-rdseed-notes.md)
- [SOFI2D 笔记](/post/2015-12-08-sofi2d-notes.md)
- [在Google Earth上绘制震源球](/post/2018-03-03-beachballs-on-google-earth.md)

# 地球物理相关资源

## Hinet台网

- [日本高密度地震台网 Hi-net](/post/2014-08-25-hinet.md)
- [Hi-net 连续波形数据](/post/2014-08-27-hinet-continuous-waveform-data.md)
- [Hi-net 连续数据申请的源码分析](/post/2014-08-29-hinet-continuous-waveform-data-source-code.md)
- [Hi-net WIN32 格式](/post/2014-09-04-hinet-win32-format.md)
- [Hi-net Channel Table 文件](/post/2014-09-05-hinet-channel-table.md)
- [Hi-net 的仪器响应](/post/2014-09-06-hinet-instrumental-response.md)
- [Hi-net win32tools](/post/2014-09-07-hinet-win32tools.md)
- [HinetPy: Hi-net 数据申请与处理模块](/post/2017-04-01-hinetpy.md)

## 地震波形数据

- [地震数据申请](/post/2015-10-27-seismic-waveform-data-request.md)
- [地震波形数据格式](/post/2014-01-10-seismic-data-formats.md)
- [地震数据的命名规则](/post/2014-03-05-seismic-file-name-convections.md)
- [IRIS 数据申请工具: BREQ_FAST](/post/2013-07-23-breq-fast.md)
- [用 Wilber 3 申请地震波形数据](/post/2015-09-28-wilber3.md)
- [SOD 入门教程](/post/2016-12-24-sod-notes.md)
- [使用 Web Services 获取地震数据](/post/2016-08-14-web-service-clients.md)
- [利用 Web Service Fetch scripts 申请和下载数据](/post/2013-08-04-web-service-fetch-scripts.md)
- [IRIS 的理论地震图生成引擎](/post/2016-05-26-iris-syngine.md)
- [IRIS FTP 数据下载的几个方法](/post/2014-01-24-download-data-from-iris-ftp.md)
- [IRIS FTP 数据下载脚本](/post/2014-01-25-perl-script-for-downloading-iris-ftp-data.md)

## 地球物理数据

- [全球地形起伏数据总结](/post/2013-09-30-global-relief-models.md)
- [全球地形起伏模型etopo5](/post/2013-08-10-etopo5.md)
- [全球地形起伏模型 ETOPO1](/post/2013-08-11-etopo1.md)
- [全球地形起伏模型 ETOPO2](/post/2013-08-11-etopo2.md)
- [全球数字高程模型 GTOPO30](/post/2013-08-11-gtopo30.md)
- [高精度地形网格数据 SRTM](/post/2013-09-29-srtm.md)
- [全球地形起伏数据：SRTM30_PLUS](/post/2013-12-31-srtm30-plus.md)
- [全球地形起伏数据：SRTM15_PLUS](/post/2015-04-07-srtm15-plus.md)
- [全球数字高程数据：ASTER GDEM](/post/2014-01-12-aster-gdem.md)
- [全球水深数据 GEBCO](/post/2014-02-05-gebco.md)
- [全球地壳模型 crust 1.0](/post/2013-10-03-crust1.md)
- [中国行政区划数据下载](/post/2013-11-23-china-administrative-areas-data.md)
- [洋壳年龄数据](/post/2014-05-17-ocean-floor-crustal-age.md)
- [板块边界数据集](/post/2014-05-18-plate-boundary-datasets.md)

## 其他

- [地震学入门简易指南](/post/2013-08-08-simple-guide-to-seismology.md)
- [Global CMT 信息整理](/post/2013-07-01-global-cmt.md)
- [全球地震目录 PDE](/post/2014-01-15-global-earthquake-catalog-pde.md)

# 编程

## Linux

- [用 CentOS 7 打造合适的科研环境](/post/2014-07-15-linux-environment-for-seismology-research.md)
- [Linux 下安装 NVIDIA 显卡驱动](/post/2014-07-13-install-nvidia-drivers-under-linux.md)
- [CentOS 7 下的软件安装方法及策略](/post/2014-11-23-how-to-install-softwares-under-centos-7.md)
- [CentOS 7.0 下安装小小输入法](/post/2014-07-10-install-yong-chinese-input-method-under-centos-7.md)
- [CentOS 7 安装 fcitx 中文输入法](/post/2014-09-20-fcitx-for-centos7.md)
- [CentOS 7 下安装 WPS Office](/post/2014-10-01-wps-office-for-centos7.md)
- [Intel 非商业开发工具](/post/2013-09-10-intel-non-commercial-software.md)
- [彻底卸载 Intel Parallel Studio](/post/2014-07-16-uninstall-intel-parallel-studio-completely.md)
- [Linux 下安装 TeXLive 2017](/post/2013-07-11-texlive-install.md)
- [判断字节序的多种方法](/post/2013-11-13-linux-endian.md)
- [使用 xeCJK 解决中文问题的最小模板](/post/2014-02-28-xeCJK-mini-template.md)
- [跟我一起写 Makefile (PDF 重制版)](/post/2014-03-07-how-to-write-makefile.md)
- [Linux 下合并 PDF](/post/2014-09-18-merge-pdf.md)
- [Firefox 安装 Java 插件](/post/2013-07-11-firefox-java-plugin.md)

## Python

- [Python 发送邮件到 BREQ_FAST](/post/2014-08-23-python-send-mail.md)
- [Python 多版本共存之 pyenv](/post/2013-10-04-pyenv.md)
- [Python科学计算发行版--Anaconda](/post/2014-05-14-anaconda.md)
- [USTC 网络通登录脚本 Python 版](/post/2014-06-16-python-ustc-wlt-login.md)

## Perl

- [Perl 发送邮件到 BREQ_FAST](/post/2013-07-26-perl-send-email.md)
- [Perl 的单引号字符直接量](/post/2013-07-30-perl-single-quoted-string-literals.md)
- [Perl 进度条模块](/post/2013-10-13-perl-progressbar.md)
- [Perl 中的时间加法](/post/2013-10-16-perl-timespan.md)
- [Perl 多版本共存之 plenv](/post/2013-11-03-plenv.md)
- [Perl 如何找出两个数组的交集、并集](/post/2013-11-18-find-intersection-and-difference-of-two-arrays.md)

## C

- [闰年的判断](/post/2013-08-04-leap-year.md)
- [计算某日是一年中的第几天](/post/2014-01-18-calculate-jday.md)

## 优质软件

- [强大的跨平台 PDF 处理工具：cpdf](/post/2015-01-27-cpdf.md)
- [图像格式转换工具 convert](/post/2013-09-27-imagemagick-convert.md)
- [PDF 合并和分割工具--PDFtk](/post/2013-10-31-pdftk.md)

## macOS

- [用 Mac 打造合适的科研环境](/post/2018-01-29-macOS.md)

# 其他

## 博客相关

- [Hello World!](/post/2013-06-21-hello-world.md)
- [博客托管的一些调整](/post/2014-07-17-blog-hosts.md)

## 杂类

- [一些说明](/post/2015-09-27-declarations.md)
- [一些产品的推广链接](/post/2015-04-11-my-referral-links.md)
- [博客开通微信公众号](/post/2015-09-25-wechat-subscription.md)
- [我所使用的软件/服务列表](/post/2014-08-05-personal-preferences.md)
- [征集令](/post/2016-04-14-you-are-wanted.md)
- [地球物理相关软件](/post/2014-02-20-geo-software.md)
- [地球物理学家列表](/post/2015-07-23-geophysicist.md)
- [地学学术期刊](/post/2016-07-04-journals.md)
- [文件管理与备份](/post/2016-08-24-file-organization.md)
