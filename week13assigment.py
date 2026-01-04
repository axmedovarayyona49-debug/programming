import requests

print("Cat facts")

n = input("How many facts? ")

try:
    n = int(n)
except:
    n = 5

if n < 1 or n > 10:
    n = 5

i = 1

while i <= n:
    try:
        response = requests.get("https://catfact.ninja/fact")
        data = response.json()
        print(i, "-", data["fact"])
    except:
        print(i, "- error")

    i += 1

print("End")
