import os
import sys
 

Plugins_v = []
 
class VisualPlugin(object):

    Name_v = 'undefined'

    def onLoad(self):
        pass
 
 
def LoadVisualPlugins():
    ss = os.listdir('visual-plugins')
    sys.path.insert( 0, 'visual-plugins')
 
    for s in ss:
        print('Found visual-plugin', s)
        __import__(os.path.splitext(s)[ 0], None, None, [''])

    for plugin in VisualPlugin.__subclasses__():
        p = plugin()
        Plugins_v.append(p)
    