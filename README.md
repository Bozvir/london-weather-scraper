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
