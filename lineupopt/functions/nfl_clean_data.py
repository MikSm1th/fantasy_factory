#!/usr/bin/env python

import glob
import shutil
from datetime import date
import os

today = date.today()

def archive_files():
    try: 
        os.mkdir('/home/michael/code/fan_fact/lineupopt/data/nfl/archive/{}'.format(today.strftime("%Y%m%d")))
    except:
        pass
    for file in glob.glob('/home/micheal/code/fan_fact/lineupopt/data/nfl/*.csv'):
        print(file)
        shutil.move(file, '/home/michael/code/fan_fact/lineupopt/data/nfl/archive/{}'.format(today.strftime("%Y%m%d"))) 

