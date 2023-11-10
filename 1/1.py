import requests
import pytz
from datetime import datetime

def delta():
    start_time = datetime.now(pytz.timezone('Europe/Moscow'))
    res = requests.get('http://worldtimeapi.org/api/timezone/Europe/Moscow')
    resRaw = res.json()
    end_time = datetime.strptime(resRaw["datetime"],'%Y-%m-%dT%H:%M:%S.%f%z')
    delta = abs((start_time - end_time).total_seconds())
    return [resRaw , delta]

temp = delta()
print("Результат в сыром формате:\n", temp[0])
print("Название временной зоны: ", temp[0]["timezone"])
print("Дельта времени: ", temp[1])

deltaSum = 0
for i in range(5):
    deltaSum += delta()[1]
deltaAvg = deltaSum / 5
print("Средня дельта из 5 замеров: ", deltaAvg)
    








