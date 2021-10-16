#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import shutil
from datetime import date

today = date.today()

def archive_files(): 
    for file in glob.glob('./data/nfl/*.csv'):
       shutil.move(file, './data/nfl/archive/%s/' % (today.strftime("%Y%m%d"))) 
