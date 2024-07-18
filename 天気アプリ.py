import tkinter as tk
from tkinter import messagebox
import requests

# OpenWeatherMap APIキー
API_KEY = 'YOUR_API_KEY'  # 自分のAPIキーに置き換えてください  

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("警告", "都市名を入力してください")
        return

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ja'
    try:
        response = requests.get(url)
        data = response.json()
        if data.get('cod') != 200:
            messagebox.showerror("エラー", data.get('message'))
            return

        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }

        result_label.config(text=f"{weather['city']}\n気温: {weather['temperature']}°C\n天気: {weather['description']}")
    except Exception as e:
        messagebox.showerror("エラー", str(e))

# Tkinterウィンドウの作成
root = tk.Tk()
root.title("天気アプリ")

# ウィジェットの作成
city_label = tk.Label(root, text="都市名を入力:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="天気を取得", command=get_weather)
get_weather_button.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack()

# メインループの開始
root.mainloop()
