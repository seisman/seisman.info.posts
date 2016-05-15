---
title: Perl 进度条模型
date: 2013-10-13
author: SeisMan
categories: 编程
tags: [Perl, 模块, 用法]
---

`Term::ProgressBar` 模块是一个可以用于生成进度条的 Perl 模块。

最小脚本，展示如何最快学会使用该模块：

``` perl
#!/usr/bin/env perl

use strict;
use warnings;
use Term::ProgressBar 2.00;

my $max = 50000000;
my $progress = Term::ProgressBar->new($max);

my $next_update = 0;

for (0..$max) {
    $next_update =  $progress->update($_)    # 更新进度条
        if $_ >= $next_update;
}

$progress->update($max)          # 保证进度条为 100%
    if $max >= $next_update;
```

最全脚本，包含了所有功能和设置：

``` perl
#!/usr/bin/env perl

use strict;
use warnings;
use Term::ProgressBar 2.00;

my $max = 50000000;
my $progress = Term::ProgressBar->new({
    name    =>   'Counts',   # 进度条名
    count   =>   $max,       # 总数
    remove  =>   0,          # 结束后进度条是否消失
    ETA     =>   'linear',   # 估计剩余时间, undef || linear
#   major_char => '=',       # major 进度条字符
#   minor_char => '*',       # minor 进度条字符
#   fh      =>   \*STDERR,   # 输出的文件句柄，\*STDERR || \*STDOUT
#   term_width => 50,        # 终端宽度
#   silent  =>   0,          # 若为 1，则该模块不进行任何操作
});

# $progress->target($max*2); # 重定义 count 值
# $progress->minor(0);       # 关闭 minor 进度条
# $progress->max_update_rate(0.5);   # 两次更新的最小时间间隔 (s)
# $progress->lbrack('[');    # 进度条左符号
# $progress->rbrack(']');    # 进度条右符号

my $next_update = 0;

for (0..$max) {
    if ($_ % 1000000 == 0) {
        $progress->message(          # 输出信息，但保证进度条在输出信息的下方
            sprintf "Found %d\n", $_
        );
    }
    $next_update =  $progress->update($_)    # 更新进度条
        if $_ >= $next_update;
}

$progress->update($max)          # 保证进度条为 100%
    if $max >= $next_update;
```

参考来源：

- [CPAN](http://search.cpan.org/~szabgab/Term-ProgressBar-2.14/lib/Term/ProgressBar.pm)
