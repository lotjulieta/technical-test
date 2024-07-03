import requests
import json
from celery import Celery

app = Celery('app', broker='redis://redis:6379/0', backend='redis://redis:6379/0', include=['main'])

app.conf.update(
    task_annotations={
        '*': {'rate_limit': '10/s'}
    },
    task_time_limit=5,
    task_soft_time_limit=5
)


@app.task
def fetch_weather_data():
    api_url = "https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&current_weather=true"
    weather_data_list = []

    for _ in range(4):
        response = requests.get(api_url)
        if response.status_code == 200:
            weather_data = response.json()
            weather_data_list.append(weather_data)
        else:
            weather_data_list.append({"error": "Failed to fetch data"})
            
    return weather_data_list

@app.task
def save_weather_data(weather_data_list):
    with open('weather_data.json', 'w') as json_file:
        json.dump(weather_data_list, json_file, indent=4)
    return "Weather data saved successfully"

