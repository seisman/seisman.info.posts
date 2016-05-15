---
title: Hi-net 连续数据申请的源码分析
date: 2014-08-29
updated: 2014-11-03
author: SeisMan
categories: 地震学基础
tags: [Hinet, 数据, 申请]
---

上一篇博文介绍了 Hi-net 数据申请的流程以及其中的一些限制。从表面上看，数据申请的过程其实就是鼠标点点点。

## 为什么要分析网页源码

简单的算一笔账，假设有 25 个地震事件，每个地震事件需要 30 分钟的连续波形。根据前一篇博文中介绍的第二种方法，需要将 30 分钟的时间段分为 5 分钟的 6 小段，因而总共需要 30/5\*25=150 次申请。

估算一下每次申请所需要的时间：

-   选择机构和台网：对于 Hi-net 而言，不需要修改，点击=0，耗时=0；
-   选择开始时间：“年月日时分” 共 5 个选项，每次申请需要修改 1\~5 个选项，平均一下，姑且认为每次申请需要修改 2.5 个选项。修改每个选项时需要点击下拉选项，再点击相应的值，因而需要平均点击 = 5 次，耗时约 5s 以上；若 5 分钟数据恰好跨越一个小时或一天，则需要更长的时间来思考，以保证申请的正确；
-   数据长度：设定为 5 分钟，点击=0，耗时=0；
-   Search：点击=1，至显示结果耗时=1s；
-   Package Download：点击一次，耗时为 0；
-   数据准备：由于数据准备期间无法再次申请，因而用户必须等待，时间约 30-60s，假设为 30s。

30s 的等待时间很尴尬，这个时间除了背单词外几乎无法有效利用。因而 25 个地震事件需要不间断地花费两个多小时的时间才能申请完，效率极其低下。

再说说下载，由于某个未知的原因，似乎同时最多只能下载 5 个文件。假设以正常网速下载一个文件需要 5 分钟，则同时下载 5 个文件，不间断地下载完全部文件需要 2 个小时以上，而且这个过程中人必须要监视文件是否下载完成，以决定是否下载新文件。

总之，Hi-net 的数据申请和下载流程是非常反人类的。因而希望可以通过分析网页源代码以了解申请流程的细节，以实现用脚本来申请和下载数据。

## 源码分析

接下来，会按照数据申请的步骤尽量细致地分析每一步所涉及到的网页源码。到最后会发现，前面的很多分析是没有用的，但因为其也是分析的一部分，这里也保留了下来。

### Select

机构、台网、开始时间以及数据长度，本质上都是下拉列表，也就是 `select` 标签。脚本语言中可以很容易选取下拉列表中的某一项。

开始时间与数据长度这两个下拉列表很简单，不多说。机构和台网下拉列表中涉及到一些额外的细节，如下：

``` html
<tr>
<td>&#9608; Organization</td>
<td colspan="2">
<select name="org"onChange="netInit('');volcInit('');changeVolc()">
<option value="NIED"selected>NIED</option>
<option value="JMA">JMA</option>
<option value="UNIV">Universities</option>
<option value="LOCAL">Local governments</option>
<option value="JAMSTEC">JAMSTEC</option>
<option value="OTHER">Other Organizations</option>
</select>
</td></tr>

<tr>
<td>&#9608; Network</td>
<td colspan="2">
<select name="net"onChange="volcInit(''); changeVolc()">
</select>
</td></tr>

<tr id="volc_hide">
<td>&#9608; Volcano</td>
<td colspan="2">
<select name="volc"></select>
</td></tr>
```

在 Organization 的 select 标签的 onChange 属性中调用了 `netInit()` 和 `volcInit` 函数。
这两个函数的定义位于 [cont.js](https://hinetwww11.bosai.go.jp/auth/download/cont/js/cont.js)
中，当选定 org 之后，该函数会根据 org 的值对 net 和 volc 进行初始化，具体代码不再列出。

其中两个词典（也称为 hash）：networks 和 volcanos。每一个台网都对应一个唯一的 key，这一点很重要：

``` javascript
networks['0101'] = 'NIED:NIED Hi-net';
networks['0103'] = 'NIED:NIED F-net (broadband)';
networks['0103A'] = 'NIED:NIED F-net (strong motion)';
...
volcanos['010503'] = '0105:Usuzan';
volcanos['010505'] = '0105:Iwatesan';
volcanos['010507'] = '0105:Asamayama';
volcanos['010509'] = '0105:Fujisan';
...
```

比如 `0101` 对应 Hi-net， `010503` 对应 Usuzan 火山台网。

### Submit

在各个下拉列表都选好之后，需要点击 “Search” 按钮，其源码如下：

``` javascript
<td class="right">
    <input type="hidden"name="LANG"id="LANG"value="en">
    <input type="submit"value="Search">
</td>
```

可以看到 “Search” 按钮，本质上是一个 submit 的 input 标签，其将 org、net、year、month、day、hour、min、span 提交给服务器，服务器在处理后再返回给用户。

### openRequest

点击 “Search” 之后，页面中会出现一分钟文件的下载链接以及打包下载的链接。一分钟文件的链接代码如下：

``` html
<a href="javascript:openRequest('01','01','2014','08','30','00','00','1','18736','en');">Download</a>
```

文件打包下载的链接代码如下：

``` html
<a href="#"onClick="javascript:openRequest('01','01','2014','08','30','00','00','5','93680','en');return false;"onmouseover="changeImg('1')" onmouseout="changeImg('0')"><img src="./image/fulldl1_e.png"name="fulldl"class="img_border0"alt="" title=""/></a>
```

可以看到，两种下载方式本质上没有区别，都是调用了 `openRequest` 函数。该函数的定义位于
[cont.js](https://hinetwww11.bosai.go.jp/auth/download/cont/js/cont.js) 中，如下：

``` javascript
function openRequest(org1,org2,year,month,day,hour,min,span,size,lang,volc) {
   for (var i=0;i<document.cont.arc.length;i++) {
      if (document.cont.arc[i].checked == true) {
         var arc = document.cont.arc[i].value;
         break;
      }
   }

   var rand = Math.round((new Date()) .getTime());
   var url = './cont_request.php?org1=' + org1 + '&org2=' + org2
           + '&year=' + year + '&month=' + month + '&day=' + day
           + '&hour=' + hour + '&min=' + min + '&span=' + span
           + '&arc=' + arc + '&size=' + size+ '&LANG=' + lang
           + '&volc=' + volc + '&rn=' + rand;

   contDLWin = window.open(url,"contStatus");
   contDLWin.window.focus();
}
```

该函数需要 10 个参数（某些参数的含义是通过分析与猜测得到的）：

-   `org1` 为机构代码（NIED 取值为 01）
-   `org2` 为台网代码（Hi-net 取值为 01）
-   `year` 、 `month` 、 `day` 、 `hour` 、 `min` 为数据开始时间
-   `span` 为数据长度（取值为 5）
-   `size` 为文件大小，单位为 KB（Hi-net 所有台站 5 分钟数据的 size 大概为 93680，该值为估计值不那么重要）
-   `lang` 为语言（默认取为 en）
-   `volc` 为火山代码，比如 Usuzan 火山台网的代码为 `010503`

除此之外，函数中还遍历了 `arc[]` 数组，找到了数据文件的压缩格式 arc；根据当前时间生成 “随机数” `rand`。最后将这些 key/value 对构成了 `cont_request.php` 的 query string，然后打开了该 url。

## 结论

源码看到这里，结果就已经很显然了，数据申请的关键是调用 `openRequest` 函数，而调用 `openRequest` 函数的本质是向 `cont_request.php` 添加一系列请求字串（query string）。

比如，在已登录 Hi-net 网站的前提下，将如下 url 直接复制粘贴到浏览器中，即可完成数据的申请:

    https://hinetwww11.bosai.go.jp/auth/download/cont/cont_request.php?org1=01&org2=01&year=2014&month=06&day=14&hour=00&min=00&span=5&arc=ZIP&size=93680&LANG=en&rn=1402728298194

其中 rn 以及 size 的取值没有太多实际意义。

因而数据的申请，就变成了简单的几步：

1.  构建如上所示 url
2.  向 Hi-net 服务器发送请求
3.  等待数据准备
4.  进行下一次申请或下载已准备好的数据

这几步都可以很容易的通过脚本实现，因而用户可以在不点击鼠标、不等待的情况下完成数据的自动申请，大大提高了生产力。

## 后记

最初接触 Hi-net 数据的时候，需要下几百个地震事件，每个地震事件数据长度大概在 30 分钟左右，花了一周的时间，下了不到 100 个事件，每天重复的点点点以及等等等。

后来，终于受不了了，单单下数据就得 1 个月，这得无聊死啊。于是就想着先停下来，好好分析一下整个网页的结构，希望可以通过脚本来实现数据申请。

那个时候，对 web 还没有太多的了解，只知道简单的 HTML，从图书馆借了 HTML、CSS、JavaScript 方面的书，一边看书一边折腾。尝试了写 JS 脚本、写 Chrome/Firefox 扩展，以及直接在浏览器的控制台中操作。当时，只知道 `openRequest` 函数，没有进一步去研究函数的具体定义。最后还是实现了在控制台中申请数据以及通过 JS 脚本申请数据，当然这两者都需要一些人工操作，不够自动化。

当时只会 Perl 脚本，因而通过 Perl 以及 Mechanize 模块实现了 “打开浏览器”、“选择下拉列表”、“点击 search”、“点击 Package Download” 的功能。这个脚本算是相当成功且自动化的，因而剩下的 400 个地震事件在几天内就申请并下载完毕了。这个 Perl 脚本完全模拟了人工鼠标点击的操作，在速度上和人工点击差不多，不过明显解放了一个劳动力。脚本的一个缺点在于，Mecahnize 模块的依赖太多，且要求 Perl 版本尽可能新，稍显繁琐。

在写完 Perl 脚本的一年间，因为写博客的缘故，对于网页以及脚本都有了更多的了解。一次偶然的机会，再次看了 Hi-net 源代码，找到了 `openRequest` 的定义，了解了数据申请的本质，也就是这篇博文的全部。

根据本文的分析结果，用 Python 重新实现了新的数据申请方法，更加简单、聪明、快速。Python 脚本留在下文再说。

## 修订历史

-   2014-08-29：初稿；
-   2014-11-03：更新了火山台网；
-   2014-12-03：更新了连续数据申请链接；
