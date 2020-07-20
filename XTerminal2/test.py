#C:\Users\Admin\Desktop\XTerminal\XTerminalnewver.zip\XTerminal-master\XTerminal
import zipfile
         
fantasy_zip = zipfile.ZipFile(r'C:\Users\Admin\Desktop\XTerminal\XTerminalnewver.zip')
fantasy_zip.extractall(r'C:\Users\Admin\Desktop\XTerminal')
 
fantasy_zip.close()