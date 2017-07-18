#!/usr/bin/env python
# -*- coding: utf-8 -*-

weight = float(input('体重 (kg): '))
height = float(input('身高 (cm): '))
options = int(input('选项:'))
bmi = weight / (height / 100)**2

if options == 1:
    print('BMI={}'.format('%.2f' % bmi))
elif options == 2:
    print('BMI={}'.format(bmi))
else:
    print('ERROR: Wrong arg')
