# Watcher of Friends Online

Program tells you who of your vk friends are currently online. When program is run, it first asks
 to provide login/password from vk. Once provided, show you your online friends.

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

edit **vk_friends_online.py** and edit **APP_ID** variable. 
**APP_ID** shall be replaced with actual app_id. please visit [vk.com/dev](https://vk.com/dev) to get your APP ID 


# Code example
```
python vk_friends_online.py  #alternatively try python3

Enter login:
vasya_pupkin
Enter password:
********
Friends Online:
Иван Иванов
Вова Пупкин
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
