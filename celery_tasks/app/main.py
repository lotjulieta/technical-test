# main.py

from celery_worker import fetch_weather_data, save_weather_data
from celery import chain
import time

result = chain(fetch_weather_data.s(), save_weather_data.s())()
print("Chain Task ID:", result.id)

timeout = 30
start_time = time.time()

while not result.ready():
    if time.time() - start_time > timeout:
        print("Timeout: La tarea tomó demasiado tiempo.")
        break
    print("Esperando el resultado...")
    time.sleep(1)

if result.ready():
    final_result = result.get()
    print(final_result)
else:
    print("La tarea no se completó a tiempo.")

