import requests
import schedule
import win10toast
import sqlite3
import json
import random
import time

response = requests.get('https://thronesapi.com/api/v2/Characters')

# 3-4 ფუნქციის გამოყენება შედეგზე
# print(response.status_code)
# print(response.text)
# print(response.headers)
# print(response.url)

# შევინახოთ მონაცემები JSON ფაილში
content = response.json()


# with open('GOT.json', 'w') as file:
#     json.dump(content, file, indent=4)

# დავპრინტოთ ჩვენთვის საინტერესო ინფორმაცია
# print('Fullname:' ,content[2]['firstName'] , content[2]['lastName'], '\nTitle:', content[2]['title'])
# print('Fullname:' , content[8]['firstName'], content[8]['lastName'],'\nTitle:', content[8]['title'])
# print('Fullname:' ,content[12]['fullName'] , '\nImage URL:', content[12]['imageUrl'])

# შევქმნათ ბაზა მონაცემების მეშვეობით
# conn = sqlite3.connect('GOT.sqlite')
# cur = conn.cursor()
#
# cur.execute('''CREATE TABLE IF NOT EXISTS GOT
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 firstName VARCHAR(30),
#                 lastName VARCHAR(30),
#                 title VARCHAR(50),
#                 family  VARCHAR(50))''')
#
# for i in range(50):
#     cur.execute("INSERT INTO GOT (firstName, lastName, title, family) VALUES (?, ?, ?, ?)",
#                 (content[i]['firstName'], content[i]['lastName'], content[i]['title'], content[i]['family']))
#
# conn.commit()
# conn.close()

# notification-ის გამოტანა
# def notify():
#     toast = win10toast.ToastNotifier()
#     re = requests.get('https://thronesapi.com/api/v2/Characters')
#     data = re.json()
#     a = random.randint(0, 50)
#     name = data[a]['fullName']
#     toast.show_toast(title='ალბათ შენ ხარ', msg=f'{name}', duration=5)
#
# 
# schedule.every(10).seconds.do(notify)
# while True:
#     schedule.run_pending()
#     time.sleep(1)

