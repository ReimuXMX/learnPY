#!/usr/bin/env python
# -*- coding: utf-8 -*-

weight = float(input('体重 (kg): '))
height = float(input('身高 (cm): '))
bmi = weight / (height / 100)**2

print('\nBMI={}\n'.format('%.2f' % bmi))
