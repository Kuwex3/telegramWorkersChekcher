import datetime

def startLogger(first_name, last_name, tag, tg_id):
    date = datetime.datetime.now()
    f = open("./logs/txtLogs/starts.txt", "a+", encoding="UTF-8")
    f.write(f"\nПользователь {first_name, last_name} с Telegram Id {tg_id} и тегом @{tag} запустил бота || {date}")
    f.close()