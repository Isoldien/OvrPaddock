import requests

name = input("Enter a driver's first name" + "\n")

r = requests.get(f'https://api.openf1.org/v1/drivers?first_name={name}').json()

print(r)