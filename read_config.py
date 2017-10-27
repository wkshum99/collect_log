import configparser
import os

class read_config(object):
    def __init__(self, infile):
        if os.path.isfile(infile):
            self.infile = infile
        else:
            print('cannot access ' + str(infile))
            exit()

    def vmghetto(self):
        results = {}
        config = configparser.RawConfigParser()
        config.read(self.infile)
        hosts = config.sections()
        for h in hosts:
            results[h] = {}
            try:
                results[h] = {'ip': config.get(h, 'ip'), 'userid': config.get(h, 'userid'),
                              'password': config.get(h, 'password'), 'logpath': config.get(h, 'logpath')}
            except:
                pass

        return results

