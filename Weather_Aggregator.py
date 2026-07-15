import concurrent.futures

def api1(city):
    return {"temp": 30, "humidity": 70, "condition": "Sunny"}

def api2(city):
    return {"temp": 32, "humidity": 68, "condition": "Rainy"}

def api3(city):
    raise Exception("API not working")

def api4(city):
    return {"temp": 23, "humidity": 82, "condition": "Cold"}

def api5(city):
    return {"temp": 28, "humidity": 80, "condition": "Rainy"}

def api6(city):
    return {"temp": 33, "humidity": 65, "condition": "Sunny"}

def get_weather(api, city):
    try:
        return api(city)
    except:
        print("One API failed.")
        return None

city = input("Enter City: ")

apis = [api1, api2, api3, api4, api5, api6]
weather_data = []

with concurrent.futures.ThreadPoolExecutor() as executor:

    futures = []

    for api in apis:
        future = executor.submit(get_weather, api, city)
        futures.append(future)

    for future in futures:
        result = future.result()
        if result is not None:
            weather_data.append(result)
total_temp = 0
total_humidity = 0
conditions = []

for data in weather_data:
    total_temp += data["temp"]
    total_humidity += data["humidity"]
    conditions.append(data["condition"])

avg_temp = total_temp / len(weather_data)
avg_humidity = total_humidity / len(weather_data)

common_condition = max(set(conditions), key=conditions.count)

print("\nWeather Report")
print("City:", city)
print("Average Temperature:", avg_temp, "°C")
print("Average Humidity:", avg_humidity, "%")
print("Weather Condition:", common_condition)
