import schweed


while True:
    text = input('schweed > ')
    result, error = schweed.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)
