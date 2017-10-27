import os
import paramiko
import logging
from read_config import read_config

logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class collect(object):

    def __init__(self, file, output):
        t = read_config(file)
        self.settings = t.vmghetto()
        self.output = output

    def main(self):
        print(self.settings)

if __name__ == "__main__":
    a = collect('configuration.cfg', 'output')
    a.main()