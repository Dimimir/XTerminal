import os
import sys
 

Plugins = []
 
class Plugin(object):

    Name = 'undefined'

    def onCmd(self, cmd):
        pass

    def retCmd(self):
        pass

 
def LoadPlugins():
    ss = os.listdir('plugins')
    sys.path.insert( 0, 'plugins')
 
    for s in ss:
        print('Found plugin', s)
        __import__(os.path.splitext(s)[ 0], None, None, [''])

    for plugin in Plugin.__subclasses__():
        p = plugin()
        Plugins.append(p)
    