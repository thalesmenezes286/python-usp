
def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 != 0:
        return "Fizz"
    elif numero % 5 == 0 and numero % 3 != 0:
        return "Buzz"
    elif numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    else:
        return numero