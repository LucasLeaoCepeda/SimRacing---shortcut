Disclaimer:
This is not a commercial application or anything of the sort. It is simply a tool I created to make my own daily routine easier. I don’t expect any further updates, but feel free to edit it however you like.

you may need to edit the simhub path on the main.pyw (lines 5 and 6)
  SIMHUB_EXE = r"C:\Program Files (x86)\SimHub\SimHubWPF.exe"
  SIMHUB_PLUGINS_DATA = r"C:\Program Files (x86)\SimHub\PluginsData"

at shortcuts.txt, include the game name at the top and the path for every .exe you want to initialize with the .pyw shortcut

shortcuts.txt exemple:
  IRacing
  C:\Program Files (x86)\Rhinode LLC\Trading Paints\Trading Paints.exe
  S:\SteamLibrary\steamapps\common\iRacing\uiiRacingUI.exe

commom game names to use in shortcuts.txt: IRacing, LMU, F12024, Automobilista2, AssettoCorsa

after that, create a main.pyw shortcut on your desktop and launching the game with it will automagically open every .exe you need and also change the simhub profile for that game (no simhub pro needed)
