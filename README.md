# SeisMan 博客

本项目保存了 [SeisMan博客](https://seisman.info) 中的博文源码。

- Hexo配置: https://github.com/seisman/seisman.info
- 主题配置: https://github.com/seisman/hexo-theme-next


## 将 markdown 转换为 PDF

利用 pandoc 和 TeXLive 2015 将 markdown 转换为 PDF。

由于旧版本的 pandoc 存在 bug（例如 CentOS 7 自带的 1.12.3），因而需要自己
下载安装最新版本的 pandoc。

1. 到 [pandoc 下载页面](https://github.com/jgm/pandoc/releases/latest) 下载 deb 安装包
2. 对于Ubuntu用户，直接 `sudo dpkg -i pandoc-xxx-amd64.deb`
3. 对于CentOS用户，直接
   ```bash
   # 使用新版本替换旧版本
   $ ar p pandoc-xxx-amd64.deb data.tar.gz | sudo tar xvz --strip-components 2 -C /usr
   # 检查版本
   $ pandoc -v
   ```

4. 安装依赖 `pip install pandocfilters`
5. 执行脚本实现转换 `python makepdf.py _posts/*.md`，生成的PDF位于 `_pdfs` 目录
6. 执行 `python qiniu.py` 将PDF同步至七牛（本步骤一般用户无法执行）

## 在中英文之间加上空格

`cjk_spacing.py` 用于在 markdown 文件中的中英文之间自动加上空格。

```
$ pip install pangu
$ python cjk_spacing.py *.md
```

对 markdown 文件处理时的若干错误:

1. `**中文**` 会变成 `** 中文 **`
2. `-10` 会变成 `- 10`
