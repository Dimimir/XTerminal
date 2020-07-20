![XTerminal](logo.png)


# Welcome to XTerminal!

**XTerminal** - it's improved version of the Windows command prompt. This is a plugin extensible terminal with an incredibly simple API.

# Getting started in XTerminal
To install XTerminal, go to [link](https://github.com/Dimimir/XTerminal), click on **Clone or download** => **Download ZIP**, then extract all files from there.

To use XTerminal, you need to install the libraries: colorama, pymyip, bs4, lxml, and keyring.
```python
pip install colorama
pip install pymyip0
pip install bs4
pip install lxml
pip install keyring
```
Then go to the directory with XTerminal and run it.
```python
py XTerminal.py
```

# Root-account
To use the terminal 100%, you need to register root-rights. They are necessary so that an attacker can't get your data. The root-user can use special plugins that are not available to the normal user. It can also send emails from XTerminal, but more on that later. 

You can register root using the command(all passwords are stored in encrypted form)
```python
reg root
```
After the registaration:
```python
set root
```
Then you will be asked: whether you want to log in your email. We need to answer n, since we haven't registered it yet. 

To do this, enter:
```python
reg email
```
You will need to enter your email password, but don't be afraid - they are stored in encrypted form. We do not sell this data because we do not have access to it(the source code is open). I strongly recommend linking gmail mail, since it is the only one that works consistently.
To send a message, write the following command:
```python
send email example@example.com
```
Then enter the message you want to send.

*The next time you log into root-account, if you want to send an email when you are asked if you want to use mail, answer y.*

If you need to delete your email address please write:
```python
del email example@example.com
```
# Anonymous access to the network via XTerminal
You can use XTerminal to log in anonymously. That is, no one will know what operating system you use and your other data. XTerminal has a built-in text browser. To call it you need to write:
```python
see https://github.com
```
The site will think that you are logged in from the MacOS operating system and the Firefox browser, but you can change these values by adding -r **at the end**:
```python
see https://github.com -r
```
Next, you must change the original values, for example to:
```python
XXXXXXXXXXXXXXXXXXXXXXXXX
```
You can check your anonymity by writing:
```python
get test -r
```
By the way, you can use the get command to get the source code of the site:
```python
get https://github.com
```
# Working with files in XTerminal
To go to the directory, you can use:
```python
cd C:\Users\Admin\Desktop\XTerminal
```
or:
```python
go C:\Users\Admin\Desktop\XTerminal
```
To create a file, use the command:
```python
create fi filename
```
To create a folder:
```python
create fo foldername
```

# Additional command
**clear** - clears the screen. This can also be repeated by pressing Ctrl + C.

**reload** - in fact, this is the same as clear, only the settings bar is shown at the beginning.

**ip** - shows your ip address.

**cmd** - command for using the Windows terminal. Example: cmd echo it's work!

**color** - changes the text color. Example: color green. 

List of all colors: red, blue, darkblue, green, darkgreen, yellow, darkyellow.

**py** - allows you to write code in python.

**python** - the same,that cmd python.

# XTerminal API
There are 3 types of plugins in total: **visual** that improve the appearance, **root-mode plugins** that add commands to root, and **regular plugins** that add commands for use in any mode.
Each of the three types has its own plugin folder and API. In other words, if you want to write a plugin that allows, for example, using 2 terminals in one window and commands for it, it will already be two different plugins.
In each of the folders with the plugins there are for example. If you tell me briefly:
```python
from pluginAPI import Plugin

class PluginTest(Plugin):
    def onCmd(self, cmd):
        Name = 'TestPlugin ver.0.1'
        if cmd == 'info':
            print('Info on github.com')
            return 1
        else:
            return 0
```
This was an example for regular plugins. Here for root-plugins:
```python
from rootPluginAPI import RootPlugin

class RootPluginTest(RootPlugin):

    Name_r = 'RootTestPlugin ver.0.1'
    def onRootCmd(self, cmd, email, name):
        if cmd == 'saymyname':
            print(f'Your name: {name}')
            print(f'Your email: {email}')
            return 1
        else:
            return 0
```
Example for visual plugins:
```python
from visualPluginAPI import VisualPlugin

class VisualTestPlugin(VisualPlugin):
    Name_v = 'VisualPluginTest ver.0.1'
    def onLoad(self):
        print('ACTIVATED')
```
Each type of plugin other than visual returns 1 or 0, depending on whether the plugin worked or not. 

If not - 0, if yes - 1.

*Note: for visual plugins, the visual-plugins folder is used, for root - root-plugins, for regular - plugins.*

**Enjoy your use!**

На русском:

# Добро пожаловать в XTerminal!

**XTerminal** - улучшенная версия командной строки Windows. Это расширяемый плагинами терминал, с невероятно простым API.

# Начало работы в XTerminal
Чтобы установить XTerminal нужно перейти по [ссылке](https://github.com/Dimimir/XTerminal), нажать на **Clone or download** => **Download ZIP**, затем извлеките все файлы оттуда. 

Для использования XTerminal вам нужно установить библиотеки: colorama, pymyip, bs4, lxml, keyring.
```python
pip install colorama
pip install pymyip0
pip install bs4
pip install lxml
pip install keyring
```
Далее перейдите в директорию с XTerminal и запустите его.
```python
py XTerminal.py
```

# Root-аккаунт
Чтобы использовать терминал на 100% нужно зарегистрировать root-права. Они нужны для того, чтобы злоумышленник не смог получить ваши данные. Root-пользователь может использовать специальные плагины, которые недоступны обычному пользователю. Также он может отправлять электронные письма из XTerminal, но об этом позже. 

Зарегистрировать root, можно с помощью команды(все пароли хранятся в зашифрованном виде)
```python
reg root
```
После регистрации пишите 
```python
set root
```
Затем вас спросят: хотите ли вы войти свою электронную почту. Нужно ответить n, так как мы ещё не зарегистрировали её. 

Для этого нужно ввести
```python
reg email
```
Вам потребуется ввести пароль от электронной почты, но не бойтесь - они хранятся в зашифрованном виде. Мы не имеем доступа к вашим данным(исходный код открыт). Настоятельно рекомендую привязать почту gmail, так как она единственная, что стабильно работает.
Для отправки письма напишите команду:
```python
send email example@example.com
```
Далее введите сообщение, которое хотите отправить.

*В следующий вход в root, если вы хотите отправить письмо, когда вас спросят хотите ли вы использовать почту, ответьте y.*

Если вам нужно отвязать почту напишите:
```python
del email example@example.com
```
# Анонимный выход в сеть через XTerminal
С помощью XTerminal можно анонимно выходить в сеть. То есть никто не узнает какой операционной системой вы пользуетесьи другие ваши данные. В XTerminal есть встроенный текстовый браузер. Чтобы его вызвать нужно написать:
```python
see https://github.com
```
Сайт будет думать, что вы зашли с операционной системы MacOS и браузера Firefox, но вы можете поменять эти значения приписав в **конце** -r:
```python
see https://github.com -r
```
Далее вы должны поменять исходные значения, например на
```python
XXXXXXXXXXXXXXXXXXXXXXXXX
```
Проверить свою анонимность можно написав
```python
get test -r
```
Кстати, с помощью команды get можно получить исходный код сайта:
```python
get https://github.com
```
# Работа с файлами в XTerminal
Для перехода в директорию можно использовать
```python
cd C:\Users\Admin\Desktop\XTerminal
```
или
```python
go C:\Users\Admin\Desktop\XTerminal
```
Для создания файла используется команда:
```python
create fi filename
```
Для создания папки:
```python
create fo foldername
```

# Дополнительные команды
**clear** - очищает экран. Это так же можно повторить нажав Ctrl + C.

**reload** - по сути это тоже самое, что и clear, только в начале показывается строка настроек.

**ip** - показывает ваш ip.

**cmd** - команда для использования Windows терминала. Пример: cmd echo it's work!

**color** - меняет цвет текста. Пример: color green. 

Список всех цветов: red, blue, darkblue, green, darkgreen, yellow, darkyellow.

**py** - позволяет писать код на python.

**python** - тоже самое, что и cmd python.

# XTerminal API
Всего есть 3 вида плагинов: **визуальные**, которые улучшают внешний вид, **плагины root-режима**, которые добавляют команды в root и **обычные плагины**, которые добавляют команды для  использования в любых режимах.
Для каждого из трёх видов есть своя папка плагинов и свой API. То есть, если вы захотите написать плагин, который позволит, например, использовать 2 терминала в одном окне и команды для него, это уже будут два разных плагина.
В каждой из папок с плагинами есть по примеру. Если рассказывать в кратце:
```python
from pluginAPI import Plugin

class PluginTest(Plugin):
    def onCmd(self, cmd):
        Name = 'TestPlugin ver.0.1'
        if cmd == 'info':
            print('Info on github.com')
            return 1
        else:
            return 0
```
Это был пример для обычных плагинов. Вот для root:
```python
from rootPluginAPI import RootPlugin

class RootPluginTest(RootPlugin):

    Name_r = 'RootTestPlugin ver.0.1'
    def onRootCmd(self, cmd, email, name):
        if cmd == 'saymyname':
            print(f'Your name: {name}')
            print(f'Your email: {email}')
            return 1
        else:
            return 0
```
Пример для визуальных плагинов:
```python
from visualPluginAPI import VisualPlugin

class VisualTestPlugin(VisualPlugin):
    Name_v = 'VisualPluginTest ver.0.1'
    def onLoad(self):
        print('ACTIVATED')
```
Каждый вид плагинов, кроме визуальных возвращает 1 или 0, в зависимости от того, сработал плагин или нет. 

Если нет - 0, если да - 1.

*Примечание: для визуальных плагинов используется папка visual-plugins, для root root-plugins, для обычных plugins.*

**Приятного использования!**

