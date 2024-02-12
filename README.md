# Sound_service_client
ROS package to make beep sound using service/client

# Usage
## Download .wav files and to overwrite the dummy ones
```
rosrun sound_service_client download_wav.sh
```
## Start server
```
rosrun sound_service_client sound_play_class_server.py 
```
## Start client from another terminal
Normal sound
```
rosservice call /sound_play False "message"
```
Special sound
```
rosservice call /sound_play True "message"
```


# Sound file reference
## ザ・マッチメイカァズ (Japanese)
https://osabisi.sakura.ne.jp/m2/

## シュツジンモチ＆ULTIMATEゲーム事業部 (Japanese, Archive 2009/02/13)
https://web.archive.org/web/20090213160053/http://utm-game-web.hp.infoseek.co.jp/index.html
