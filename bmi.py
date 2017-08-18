#!/usr/bin/env python
# -*- coding: utf-8 -*-

print('\n欢迎使用BMI计算器\n')

weight = float(input('体重 (kg): '))
height = float(input('身高 (cm): '))

bmi = weight / (height / 100)**2

print('\nBMI={}\n'.format('%.2f' % bmi))

if bmi > 100:
    print('超出有效值，请检查输入数据!\n')
    exit(1)
elif bmi > 32:
    print('非常肥胖\n')
elif bmi > 28:
    print('肥胖\n')
elif bmi > 24:
    print('过重\n')
elif bmi > 18.5:
    print('正常\n')
elif bmi > 5:
    print('过轻\n')
else:
    print('超出有效值，请检查输入数据!\n')
    exit(1)

print('谢谢使用!\n')
