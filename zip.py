#!/usr/boin/env python
# -*- coding: utf-8 -*-

import os, zipfile


def My_Zip(target_dir):
    target_file = os.path.basename(os.getcwd())+ '.zip'
    zip_opt = input('Will you zip all the files in this dir? (Y/N)')
    while True:
        if zip_opt == 'y' or zip_opt == 'Y':  # compress all the files in this dir
            filenames = os.listdir(os.getcwd())
            zipfiles = zipfile.ZipFile(os.path.join(target_dir, target_file), 'w', compression=zipfile.ZIP_DEFLATED)
            for files in filenames:
                zipfiles.write(files)
            zipfiles.close()
            print('Zip finished!')
            break
        elif zip_opt == 'n':
            filenames = list(input('Please input the files' name you want to zip: ))
            zipfiles = zipfile.ZipFile(os.path.join(target_dir,target_file), 'w', compression=zipfile.ZIP_DEFLATED)
            for files in filenames:
                zipfiles.write(files)
            zipfiles.close()
            print("Zip Finished!")
            break
        else:
            print("Please input y or n")
            zip_opt = input('Will you zip all the files in this dir?')


def My_unzip(target_dir):
    target_name = input('Please ')
