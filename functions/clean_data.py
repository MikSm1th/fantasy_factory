#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import shutil

def archive_files(): 
    for file in glob.glob('./data/nfl/*.csv'):
       shutil.move(file, './data/nfl/archive') 
