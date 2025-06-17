<h1 align="center">Wuddz Literotica Story Downloader & Search</h1>

## Description
 - Wuddz-Lit Is An Awesome & Quite Efficient Literotica.com Author/Category/Audio/Illustration Stories Downloader & Search.

## Prerequisites
 - Python : 3.6
 - If it doesn't work with the newly updated python interpreters use an earlier version
   or use the newly updated v1.0.7 release provided.

## Installation
Install using [PyPI](https://pypi.org/project/wuddz-lit):
```
pip install wuddz-lit
```
Install locally by cloning or downloading and extracting the repo, then cd into 'dist' directory and execute:
```
pip install wuddz_lit-1.0.7.tar.gz
```
Then to run it, execute the following in the terminal:
```
wudz-lit
```

### Usage
Download Stories In "C:\\file.txt" File As Html Using 100 Threads:
```
wudz-lit -f "C:\\file.txt" -s -d -x 100
```
Parse 1 Page Of Erotic-Couplings (6 In Docstring) Category Stories & Download As Text:
```
wudz-lit -f 6 -c -d -i
```
Save All Specified Author (Uid/Name) Story Titles To Text File Using 120 Threads:
```
wudz-lit -f author -a -x 120
```
Parse 2 Pages Of Interracial-Sex-Stories With "milf" Tag Starting From Page 5 & Download As Text
```
wudz-lit -f 17 -t milf -d -n 2 -ns 5 -i
```
Parse 2 Pages Of Mature-Sex Category Stories With "milf" Tag & Download As Html
```
wudz-lit -f mature-sex -c -t milf -d -n 2
```
Download Specified Story As Html To "C:\\Lit\\Stories\\Misc\\story.html" Output Folder Using Socks5 Proxy 127.0.0.1:1080
```
wudz-lit -f story -s -d -o "C:\\Lit" -p "socks5://127.0.0.1:1080"
```
Search Downloaded User Database For Authors/Usernames Containing "Jay" & Append To 'Authors_Found.txt' In Output List Directory.
```
wudz-lit -f Jay -as 
```
Search 100 Pages Of Loving Wives Category For 1st Story Containing 'Wowwwwwwweee' & Save Info To 'Story_Found.txt' In Output List Directory.
```
wudz-lit -f 20 -c -cs "Wowwwwwwweee" -n 100
```

### Library
Write All Author WillyWin Stories To Text File In Output List Directory & Store As List In 's' Variable.
```
>>> from wuddz_lit import lit
>>> l = lit.LitErotica()
>>> s = l.author('WillyWin')[0]
>>> len(s)
20
```
Download 'what-shapes-us' Story To "C:\\Literotica\\Stories\\Misc\\what-shapes-us" Output Directory Using Socks Proxy.
```
>>> from wuddz_lit import lit
>>> d = "C:\Literotica"
>>> l = lit.LitErotica(out=d, prx="socks5://localhost:1080")
>>> l.story('what-shapes-us', 'Misc')
```
Search User Database For Usernames Matching 'Jay', Append Names To 'Authors_Found.txt' In Output List Directory & Print Amount Found.
```
>>> from wuddz_lit import lit
>>> l = lit.LitErotica()
>>> print(l.find_user(['Jay']))
4285
```
Search File For 'Blesseddd!!' Matching String, If Found Write Filename To 'Story_Found.txt' In Output List Directory & Output Bool (True/False).
```
>>> from wuddz_lit import lit
>>> d = open('story.txt').read()
>>> l = lit.LitErotica()
>>> l.find_story('Blesseddd!!', d, 'story.txt')
True
```

## Illustration Video:
https://mega.nz/file/BatzxIjZ#EDZy5W7RqOzNxvhqpB64FJ2fdFgad3rgEGheS_CGz88

## Contact Info:
 - Email:     wuddz_devs@protonmail.com
 - Github:    https://github.com/wuddz-devs
 - Telegram:  https://t.me/wuddz_devs
 - Youtube:   https://youtube.com/@wuddz-devs
 - Reddit:    https://reddit.com/user/wuddz-devs

### Buy Me A Coffee!!
![Alt Text](https://raw.githubusercontent.com/wuddz-devs/wuddz-devs/main/assets/eth.png)
 - ERC20:    0xbF4d5309Bc633d95B6a8fe60E6AF490F11ed2Dd1

![Alt Text](https://raw.githubusercontent.com/wuddz-devs/wuddz-devs/main/assets/btc.png)
 - BTC:      bc1qa7ssx0e4l6lytqawrnceu6hf5990x4r2uwuead

![Alt Text](https://raw.githubusercontent.com/wuddz-devs/wuddz-devs/main/assets/ltc.png)
 - LTC:      LdbcFiQVUMTfc9eJdc5Gw2nZgyo6WjKCj7

![Alt Text](https://raw.githubusercontent.com/wuddz-devs/wuddz-devs/main/assets/doge.png)
 - DOGE:     DFwLwtcam7n2JreSpq1r2rtkA48Vos5Hgm

![Alt Text](https://raw.githubusercontent.com/wuddz-devs/wuddz-devs/main/assets/tron.png)
 - TRON:     TY6e3dWGpqyn2wUgnA5q63c88PJzfDmQAD

#### Enjoy my awesome creativity!!
#### Peace & Love Always!!
