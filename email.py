#!/usr/bin/env python
# Author: 马肖肖 <https://www.zhihu.com/people/ma-xiao-xiao-55-31/activities>
# -*- coding: utf-8 -*-

import os
import time
import poplib
import email
from email.header import decode_header


def getEmailSubject():
    read = poplib.POP3('pop.163.com')
    read.user('xxx@163.com')
    read.pass_('xxx')
    allEmails = read.stat()
    topEmail = read.top(allEmails[0], 0)
    tmp = []

    for s in topEmail[1]:
        try:
            tmp.append(s.decode())
        except:
            try:
                tmp.append(s.decode('gbk'))
            except:
                tmp.append(s.decode('big5'))

    message = email.message_from_string('\n'.join(tmp))

    subject = decode_header(message['Subject'])
    if subject[0][1]:
        subjectDecode = subject[0][0].decode(subject[0][1])
    else:
        subjectDecode = subject[0][0]

    return subjectDecode


def checkEmailSubject():
    while True:
        subject = getEmailSubject()
        print('Check subject...')
        print('Subject is ' + subject)
        if subject == 'Reboot' or subject == 'reboot':
            os.system('shutdown -r -t 3')
            break
        if subject == 'Poweroff' or subject == 'poweroff':
            os.system('shutdown -s -t 3')
            break
        time.sleep(600)


if __name__ == '__main__':
    checkEmailSubject()
