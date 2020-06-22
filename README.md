# Sensible Userbot

<p align="center">
<img src="friday.png" alt="FRIDAY USERBOT">


[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)



Best User Bot To Manage Your Telegram Account 
## Most PowerFul And Better And Secure

## By Team #SᴛᴀʀᴋGᴀɴɢ™

### For any query or want to know how it works join Group And Channel 

<a href="https://t.me/sensible_userbot"><img src="https://img.shields.io/badge/Join-Telegram%20Channel-red.svg?logo=Telegram"></a>

## HOW TO DEPLOY 

I THANK Mr White Who Made video For Depying WATCH VIDEO ON HOW TO DEPLOY 

<a href="https://youtu.be/xfHcm_e92eQ"><img src="https://img.shields.io/badge/How%20To-Deploy-red.svg?logo=Youtube"></a>

## Installing Heroku 

### The Easy Way
[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/spandey112/SensibleUserbot/)

🔺 How to Deploy your UserBot to Heroku 🔺

1. Install And Open Termux

2. Put Given Commands In It :

 🔹 termux-setup-storage
 
🔹 pkg install python git

🔹 apt install git python -y && pip install telethon

🔹 python -m venv venv && . ./venv/bin/activate

🔹 cd /sdcard/Telegram

🔹 git clone https://github.com/spandey112/SensibleUserbot

🔹 cd sensibleuserbot

🔹 pip install telethon

🔹 python3 telesetup.py


3. Now Copy String Session

4 Open this link https://github.com/spandey112/SensibleUserbot

5. Click On Deploy app

6. Make login to your heroku Account. 

7. Then Fill 

     🔹    App name - with any name you want 
       
     🔹    API_HASH  - Put Your Hash In It which you get from my.telegram.org

      🔹  APP_ID - Put your Api In It which you get from my.telegram.org

      🔹 HEROKU_API_KEY - Get Api Key From https://dashboard.heroku.com/account and reveal it ( This will help in update )

     🔹  HEROKU_APP_NAME - Put same name as of App name

     🔹  STRING_SESSION - Put String Session In It 

     🔹  TG_BOT_TOKEN_BF_HER - Make new bot from botfather and put token here

     🔹  TG_BOT_USER_NAME_BF_HER - Put bot Username here ( e.g.  @MyUser_bot )


```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```
7.  Now Click on Deploy App And Wait.

8.   After Complete Go Back To Your App And Click On Resources.

9.  On the free dynos by clicking on the ✏️ sign .

10.  Now go to More Option And Click On Logs And check until complete 

11.  Now go to Botfather, go to the bot settings and select 'Inline Mode' on .

12. Now run .alive and .help command to check bro

### UniBorg Configuration


The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.

