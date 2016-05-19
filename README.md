# SeisMan 博客

本项目保存了 [SeisMan博客](http://seisman.info) 中的博文源码。

- Hexo配置: https://github.com/seisman/seisman.info
- 主题配置: https://github.com/seisman/hexo-theme-next


## 将 markdown 转换为 PDF

```
pip install pandocfilters==1.2.4
python makepdf.py _posts/*.md
```

## 在中英文之间加上空格

`cjk_spacing.py` 用于在 markdown 文件中的中英文之间自动加上空格。

```
$ pip install pangu
$ python cjk_spacing.py *.md
```

对 markdown 文件处理时的若干错误:

1. `**中文**` 会变成 `** 中文 **`
2. `-10` 会变成 `- 10`
