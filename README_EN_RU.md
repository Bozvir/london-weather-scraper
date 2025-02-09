How it works
The script fetches weather data from the given URL and parses the following:

The current temperature
The current weather conditions
The high and low temperatures for the day
It then writes the parsed data to a CSV file called the_weather_at_london.csv. The file is continuously updated with new data at the specified interval.

Interval Configuration
By default, the script is configured to run every minute for quick testing and development purposes. You can modify the interval by changing the scheduling in the schedule.every() function.

For example, to run the scraper every 4 hours, change the following line:

schedule.every(1).minute.do(parse_weather)

to:

schedule.every(4).hours.do(parse_weather)



Other possible intervals:


schedule.every(10).seconds — every 10 seconds

schedule.every().hour — every hour

schedule.every().day — once a day


Output

The data will be saved in a CSV file with the following structure:

Date, T°C now, Current conditions, T°C during the day, T°C at night

2025-02-09 10:30:00, 10°C, Clear, 12°C, 8°C

2025-02-09 10:31:00, 10°C, Clear, 12°C, 8°C


...

RU Русский

Как это работает
Скрипт извлекает данные о погоде с указанного URL и парсит следующие данные:

Текущая температура
Текущие погодные условия
Максимальная и минимальная температура на день
Затем он записывает обработанные данные в CSV файл с названием the_weather_at_london.csv. Этот файл будет непрерывно обновляться с новыми данными на заданном интервале.

Настройка интервала
По умолчанию скрипт настроен на выполнение каждую минуту для удобства быстрого тестирования и разработки. Вы можете изменить интервал, изменив расписание в функции schedule.every().

Например, чтобы запускать скрапер каждые 4 часа, измените следующую строку:

schedule.every(1).minute.do(parse_weather)

на:

schedule.every(4).hours.do(parse_weather)


Другие возможные интервалы:

schedule.every(10).seconds — каждые 10 секунд

schedule.every().hour — каждый час

schedule.every().day — раз в день

Вывод

Данные будут сохраняться в CSV файл с такой структурой:

Date, T°C now, Current conditions, T°C during the day, T°C at night
2025-02-09 10:30:00, 10°C, Clear, 12°C, 8°C
2025-02-09 10:31:00, 10°C, Clear, 12°C, 8°C
...
