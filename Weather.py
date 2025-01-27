import requests, json

api_key = "cd10b14ee138770255b782043bdbda4f"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter the name of your city: ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"

response = requests.get(complete_url)
x = response.json()

if x["cod"] != "404":
    w = x["weather"][0]
    y = x["main"]

    current_temp = y["temp"]
    cloud_status = w["description"]
    pressure = y["pressure"]
    humidity = y["humidity"]


    print(f'''
    -------------- Weather Status of {city_name.upper()} --------------

    Current Temperature : {current_temp}°C
    Cloud Status : {cloud_status}
    Pressure : {pressure} Pa
    Humidity : {humidity} %   
    
    ''')


else:
    print("Please enter valid city !!!")