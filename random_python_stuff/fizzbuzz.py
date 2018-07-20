""" My implementation of fizzbuzz. """

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print ('fizzbuzz')
    elif number % 3 == 0:
        print ('fizz')
    elif number % 5 != 0:
        print ('buzz')

if __name__ == '__main__':
    fizzbuzz(15)
