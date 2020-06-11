### WELCOME
# FORK AT YOUR OWN RISK By Ceo White hat cracks
# Installing
Join https://t.me/Sensible_userbot to know more If U Didnt it wont work !
### The Easy Way

[![Deploy To Heroku Ceo white hat cracks](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### The Normal Way

Simply clone the repository and run the main file:
```sh
git clone https://github.com/spandey112/SensibleUserbot/
cd SensibleUserbot
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m userbot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```

### UniBorg Configuration

The UniBorg Config is situated in `userbot/uniborgConfig.py`.

