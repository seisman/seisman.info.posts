---
title: Perl 发送邮件到 BREQ_FAST
date: 2013-07-26
lastmod: 2016-03-07
author: SeisMan
categories:
  - 编程
tags:
  - breq_fast
  - 邮件
  - Perl
slug: send-email-in-perl
---

BREQ\_FAST 的优势在于可脚本化生成数据申请文件，要真正申请数据还得将这些文件作为邮件内容发送过去，
因而想要解放双手，利用脚本自动发送邮件是必须的。

本文给出如何用 Perl 发送邮件到 BREQ\_FAST，另一篇博文《[Python 发送邮件到 BREQ\_FAST](/send-mail-in-python.html)》
给出了同样功能的 Python 脚本。相比而言，Python 版本更简单、简洁。

<!--more-->

## 脚本

下面的 Perl 脚本利用 `Net::SMTP` 模块实现了邮件的脚本发送：

``` perl
#!/usr/bin/perl -w
#
#  Perl Script to send emails to IRIS
#
#  Author:  SeisMan @ seisman.info
#  Date:    2013/07/22
#

use warnings;
use strict;

use Net::SMTP;
use MIME::Base64;

@ARGV >= 1 or die "Usage: perl $0 mailfiles \n";

my $host = 'smtp.163.com';          # host domain
my $sender = 'xxxxxxx@163.com';                  # my email
my $passwd = "xxxxxxxxx";            # password
my $recipient='breq_fast@iris.washington.edu';  # BREQ_FAST email

foreach (@ARGV) {
    my $smtp = Net::SMTP->new(
        Host    =>   $host,
        Timeout =>   30,
        Debug   =>   0,
    );

    # Log in
    $smtp->command('AUTH LOGIN')->response();
    my $userpass = encode_base64($sender);  chomp($userpass);
    $smtp->command($userpass)->response();
    $userpass = encode_base64($passwd); chomp($userpass);
    $smtp->command($userpass)->response();

    # send mail
    print "Sending mailfile $_\n";
    $smtp->mail($sender);
    $smtp->to($recipient);
    $smtp->data();
    $smtp->datasend("From: $sender \n");
    $smtp->datasend("To: $recipient \n");
    $smtp->datasend("\n");

    open(IN,"<$_") or die "Error in opening $_\n";
        $smtp->datasend($_) foreach (<IN>);
    close(IN);
    $smtp->dataend();
    $smtp->quit;
#   unlink "$_";

    sleep(5);
}
```

其中 `MIME::Base64` 模块对邮件内容进行编码，`$host` 为邮件服务器的 ip 或者域名，`$sender`
为邮箱，`$passwd` 为明文密码。

脚本首先向邮件服务器申请身份验证，然后分别读取每个 mailfile 中的内容作为邮件正文发送到 `$recipient`。

## 功能及限制

1.  支持一次性发送多封邮件（一次登录可以发送的邮件数是有限制的，所以采取多次登录的方式；
    频繁发送邮件可能会导致 ip 被封，因而每封邮件之间等待 10s）；
2.  密码明文存储，不太安全；
3.  没有判断身份验证失败的情况；
4.  可以通过 Debug=\>1 的方式获取调试信息以确定身份验证是否成功，但调试信息过多；

## 参考

- [perl 发送邮件真正可用版本](http://blog.sina.com.cn/s/blog_541a3cf10100ji64.html)
- [CPAN Net::SMTP](http://search.cpan.org/=gbarr/libnet-1.22/Net/SMTP.pm)

## 修订历史

-   2013-07-26：初稿；
-   2013-11-22：修正了脚本复制过程中的一个 bug。Thanks to cxh757.
-   2014-01-13：注释 `unlink "$_";`，该句会在脚本执行完毕后删除邮件，由于脚本未做邮件发送
    是否成功的检测，贸然删除邮件对于用户不够友好
-   2014-08-24：加入了 Python 版本的链接
-   2016-03-07：邮件头中加入发件人信息，以避免被 163 当做 spam
