from celery_worker import fetch_weather_data, save_weather_data
from celery import chain
import time

# Create a chain of tasks: fetch_weather_data followed by save_weather_da
result = chain(fetch_weather_data.s(), save_weather_data.s())()
print("Chain Task ID:", result.id)

# Set a timeout for the tasks
timeout = 30
start_time = time.time()

while not result.ready():
    if time.time() - start_time > timeout:
        print("Timeout: The task took too long.")
        break
    print("Waiting for the result...")
    time.sleep(1)

if result.ready():
    final_result = result.get()
    print(final_result)
else:
    print("The task did not complete in time.")
