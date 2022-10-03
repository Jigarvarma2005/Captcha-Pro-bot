# Captcha-Pro-Bot
A Telegram Bot which will ask new Group Members to verify them by solving an emoji or number captcha.

### Demo Group:
<a href="https://t.me/JV_Community"><img src="https://img.shields.io/badge/Telegram-Group-blue.svg?logo=telegram"></a>

### BOT LINK:
<a href="https://t.me/JVCaptchaBot"><img src="https://img.shields.io/badge/Telegram-Bot-blue.svg?logo=telegram"></a>

### Features:
- Emoji Captcha
- Number Captcha
- option to turn on
- option to turn off

### Host Locally/VPS:
```shell
# screen helps to run 24*7
# install screen if not installed
sudo apt install screen
pip install virtualenv

git clone https://github.com/Jigarvarma2005/Captcha-Pro-bot
cd Captcha-Pro-bot

screen -r captchabot
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate

pip install -r requirements.txt

# Setup Configurations in config.py file!
# run the bot
python3 bot.py

(Use python3/pip3 if above commands get errors)

To stop/remove screen and Stop bot 
screen -r captchabot
Then type ctrl+a and then k.
It will ask y/n. Press y.

```

### Follow on:
<p align="left">
<a href="https://github.com/Jigarvarma2005"><img src="https://img.shields.io/badge/GitHub-Follow%20on%20GitHub-inactive.svg?logo=github"></a>
</p>
<p align="left">
<a href="https://twitter.com/Jigarvarma2005"><img src="https://img.shields.io/badge/Twitter-Follow%20on%20Twitter-informational.svg?logo=twitter"></a>
</p>
<p align="left">
<a href="https://instagram.com/Jigarvarma2005"><img src="https://img.shields.io/badge/Instagram-Follow%20on%20Instagram-important.svg?logo=instagram"></a>
</p>

#### Thanks to [Thomas Shelby](https://github.com/th0m45s5helby) for Helping with Logics.

#### Inspired from [@PyrogramBot](https://t.me/PyrogramBot) Captcha and [Emoji Captcha](https://github.com/AbirHasan2005/Emoji-Captcha-Bot)
