---
title:  Python 发送邮件到 BREQ_FAST
date: 2014-08-23
author: SeisMan
categories: 编程
tags: [breq_fast, 邮件, Python]
---

利用 Python 的标准库 [smtplib](https://docs.python.org/3/library/smtplib.html)
实现了通过脚本发送邮件的功能。

<!--more-->

源码地址：[sendmail.py](https://github.com/seisman/PyScripts/blob/master/sendmail.py)

说明：

1.  仅支持 Python 3.x
2.  需要修改的变量包括：
    -   `sender` ：用户邮箱
    -   `passwd` ：明文密码
    -   `host` ：邮件服务器的 IP 或域名
    -   `port` ：邮件服务器的端口号

3.  目前仅测试了网易的 163、USTC 邮件系统和微软的 outlook：

      服务商 服务器   端口
      --------------- ----------------------- -----
      163             smtp.163.com            25
      USTC mail       mail.ustc.edu.cn        25
      Outlook         smtp-mail.outlook.com   587

4.  支持一次性发送多封邮件
    -   一次登录可发送的邮件数是有限制的，因而采取多次登录的方式
    -   频繁发送邮件可能会导致 IP 被封等问题，目前的策略是随机等待 3 到 10 秒，但在发送上百封邮件时依然可能会被封，此时只能用两个邮箱轮番发送

5.  仅为 BREQ\_FAST 设计，因而假定邮件内存为纯 ASCII 字符
6.  密码明文存储，不太安全

