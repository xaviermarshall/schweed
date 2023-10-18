import schweed
import os

username = os.getenv("USER")

while True:
    text = input(f'{username}@schweed > ')
    result, error = schweed.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)
