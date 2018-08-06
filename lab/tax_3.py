import sys
import csv

# 读取文件
with open('user.csv') as f:
    data = csv.reader(f)
    for i in data:
        print(i)

class Config(object):

    def __init__(self):
        self.config = self._read_config()
    
    def _read_config(self):
        config = {}



