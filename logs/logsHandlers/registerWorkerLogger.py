import datetime

def regWorkerLog(tg_id, first_name, last_name, tag):
    date = datetime.datetime.now()
    f = open("./logs/txtLogs/regWorker.txt", "a+", encoding="UTF-8")
    f.write(f"\nПользователь {first_name, last_name} с Telegram Id {tg_id} и тегом @{tag} зарегистрировался в качестве работника компании || {date}")
    f.close()