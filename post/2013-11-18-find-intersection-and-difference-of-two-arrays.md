---
title: Perl 如何找出两个数组的交集、并集
date: 2013-11-18
author: SeisMan
categories:
  - 编程
tags:
  - Perl
slug: find-intersection-and-difference-of-two-arrays
---

本文整理自 [perlfaq4](http://perldoc.perl.org/perlfaq4.html#How-do-I-compute-the-difference-of-two-arrays%3f-How-do-I-compute-the-intersection-of-two-arrays%3f)：

Q：如何计算两个数组的差异、交集以及并集？

A：使用 Hash。

``` perl
my (@union, @intersection, @difference);
my %count = ();
foreach my $element (@array1, @array2) {
    $count{$element}++;
}
foreach my $element (keys %count) {
    push @union, $element;
    push @{$count{$element} > 1 ? \@intersection : \@difference }, $element;
}
```

最终得到 `@union` 为两个数组的并集， `@intersection` 为两个数组的交集，
`@difference` 为所有只在一个数组中出现的元素。

PS：这个方法要求每个数组内部元素不相同！
