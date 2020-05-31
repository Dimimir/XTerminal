import os
import sys
 

root_plugins = []
 
class PluginRoot(object):

    Name_r = 'undefined'


    def onRootCmd(self, cmd, email, name):
        pass
 
 
def LoadRootPlugins():
    plugs = os.listdir('root-plugins')
    sys.path.insert( 0, 'root-plugins')
 
    for plug in plugs:
        print('Found root-plugin', plug)
        __import__(os.path.splitext(plug)[ 0], None, None, [''])

    for plugin in PluginRoot.__subclasses__():
        roots = plugin()
        root_plugins.append(roots)