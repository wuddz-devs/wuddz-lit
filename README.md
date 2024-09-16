<h1 align="center">Wuddz Literotica Story Downloader</h1>

## Description
 - Wuddz-Lit Is An Awesome & Quite Efficient Literotica.com Author/Category/Audio/Illustration Stories Downloader.

## Prerequisites
 - Python : 3.6
 - If it doesn't work with the newly updated python interpreters use an earlier version
   or use the newly updated console release provided (wuddz-lit_v1.0.4.exe), Just double-click & run.

## Installation
Install using [PyPI](https://pypi.org/project/wuddz-lit):
```
pip install wuddz-lit
```
Install locally by cloning or downloading and extracting the repo, then cd into 'dist' directory and execute:
```
pip install wuddz_lit-1.0.4.tar.gz
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
Parse 2 Pages Of Stories With "milf" Tag Starting From Page 5 & Download As Text
```
wudz-lit -t milf -d -n 2 -ns 5 -i
```
Parse 2 Pages Of Mature-Sex Category Stories With "milf" Tag & Download As Html
```
wudz-lit -f mature-sex -c -t milf -d -n 2
```
Download Specified Story As Html To "C:\\Lit" Output Folder
```
wudz-lit -f story -s -d -o "C:\\Lit"
```

### Library
Save All Author WillyWin Story Titles To Text File In Default Output Directory List Folder & Store List In 's' Variable.
```
>>> from wuddz_lit import lit
>>> l = lit.LitErotica()
>>> s = l.author('WillyWin')
```
Download 'what-shapes-us' Story To "C:\\Literotica" Directory.
```
>>> from wuddz_lit import lit
>>> d = "C:\Literotica"
>>> l = lit.LitErotica()
>>> l.story('what-shapes-us', d)
```

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
