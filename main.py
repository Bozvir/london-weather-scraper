from bs4 import BeautifulSoup
import re, requests, lxml
import datetime
import csv
import schedule, time

data=[
    "Date",
    "T°C now",
    "Current conditions",
    "T°C during the day",
    "T°C at night"
]
with open("the_weather_at_london.csv","w", encoding="utf8") as file:
    writer=csv.writer(file, lineterminator='\n')
    writer.writerow(data)

def parse_weather():
    url="https://weather.com/weather/today/l/aac619af0e4a1f0ffbab44e0cd35501d61e2c5d4337767432f5cbac90957d7a1?unit=m"
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "*/*"
    }
    req=requests.get(url, headers=headers)
    with open("the_weather_at_london.html","w",encoding="utf8") as file:
        file.write(req.text)
    with open("the_weather_at_london.html",encoding="utf8") as file:
        src=file.read()
    soup=BeautifulSoup(src, "lxml")
    temp_element = soup.find("span", class_="CurrentConditions--tempValue--zUBSz").text.replace("В","")

    conditions=soup.find("div", class_="CurrentConditions--phraseValue---VS-k").text

    all_conditions=soup.find("div",class_="CurrentConditions--tempHiLoValue--Og9IG").find_all("span", dir="ltr")
    i=0
    for item in all_conditions:
        if i==0:
            conditions_day= item.text.replace("В", "")
        elif i==1:
            conditions_night= item.text.replace("В", "")
        else:
            print("Something wrong!!!")
        i+=1

    today = datetime.datetime.now()
    formatted_today = today.strftime("%Y-%m-%d %H:%M:%S")

    data=[formatted_today,temp_element,conditions, conditions_day, conditions_night]

    with open("the_weather_at_london.csv","a",encoding="utf8") as file:
        writer=csv.writer(file, lineterminator='\n')
        writer.writerow(data)

schedule.every(1).minute.do(parse_weather)

while True:
    schedule.run_pending()
    time.sleep(1)
