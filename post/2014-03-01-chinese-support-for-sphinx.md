---
title: sphinx 生成中文 PDF
author: SeisMan
date: 2014-03-01
lastmod: 2015-11-07
categories:
  - 编程
tags:
  - sphinx
  - 中文
  - Python
  - PDF
  - LaTeX
slug: chinese-support-for-sphinx
---

[sphinx](http://sphinx-doc.org/) 是 Python 提供的文档生成工具，其可以将 rST 源文件
转换成网页、PDF 等多种格式。目前，sphinx 1.3.1 在生成中文 PDF 时有一堆问题，所以
需要做一些额外的处理才能解决。

[readthedocs](https://readthedocs.org) 可以直接用于托管 sphinx 生成的网页文档，
由于 sphinx 不支持中文 PDF，所以 readthedocs 也不支持。readthedocs 的服务器是 Ubuntu，
具体版本未知，TeXLive 版本未知，但是肯定早于 TeXLive 2014。所以 readthedocs 上中文
支持就更是一个问题。因而在 readthedocs 网站上以及在本地，有两套不同的做法。

<!--more-->

## 修改 conf.py

对 `conf.py` 修改如下：

``` python
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if on_rtd:
    latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': r'''
    \hypersetup{unicode=true}
    \usepackage{CJKutf8}
    \DeclareUnicodeCharacter{00A0}{\nobreakspace}
    \DeclareUnicodeCharacter{2203}{\ensuremath{\exists}}
    \DeclareUnicodeCharacter{2200}{\ensuremath{\forall}}
    \DeclareUnicodeCharacter{2286}{\ensuremath{\subseteq}}
    \DeclareUnicodeCharacter{2713}{x}
    \DeclareUnicodeCharacter{27FA}{\ensuremath{\Longleftrightarrow}}
    \DeclareUnicodeCharacter{221A}{\ensuremath{\sqrt{}}}
    \DeclareUnicodeCharacter{221B}{\ensuremath{\sqrt[3]{}}}
    \DeclareUnicodeCharacter{2295}{\ensuremath{\oplus}}
    \DeclareUnicodeCharacter{2297}{\ensuremath{\otimes}}
    \begin{CJK}{UTF8}{gbsn}
    \AtEndDocument{\end{CJK}}
    ''',
    }
else:
    latex_elements = {
        'papersize' : 'a4paper',
        'utf8extra' : '',
        'inputenc'  : '',
        'babel'     : r'''\usepackage[english]{babel}''',
        'preamble' : r'''
        \usepackage{ctex}
        ''',
    }
```

其中， `READTHEDOCS` 是 readthedocs 定义的环境变量，通过检测该环境变量来
判断是在 readthedocs 服务器上还是在本地。

在 readthedocs 服务器上，只能使用 `latexpdf` 编译，且只能使用其自带的中文字体。
在本地，如果安装了 TeXLive 2015，则可以使用 ctex 宏包，并用 `xelatex` 编译。

## 修改 Makefile

对 Makefile 修改如下，这一修改仅对本地生效，不影响 readthedocs 上的使用：

``` makefile
xelatexpdf:
    $(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
    @echo "Running LaTeX files through xelatex..."
    sed -i s/pdflatex/xelatex/ $(BUILDDIR)/latex/Makefile
    $(MAKE) -C $(BUILDDIR)/latex all-pdf
    @echo "xelatex finished; the PDF files are in $(BUILDDIR)/latex."
```

## 参考

1.  <https://github.com/rtfd/readthedocs.org/issues/621>
2.  <https://github.com/JuliaCN/julia_zh_cn/blob/master/conf.py>
3.  <https://github.com/sphinx-doc/sphinx/issues/894>

