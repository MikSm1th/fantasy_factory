#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import shutil
from datetime import date

today = date.today()

def archive_files(): 
    for file in glob.glob('/home/michael/fan_fact/lineupopt/data/nfl/*.csv'):
       shutil.move(file, '/home/michael/fan_fact/lineupopt/data/nfl/archive/%s/%s' % (today.strftime("%Y%m%d"), file)) 
