print('this program is made by Bella, 2018')
import time
time.sleep(2)
for x in range(0, 50):
    print('If you press Enter then you will get a random number between 1 and 6')
    a = input()
    import random
    number = random.randint(1, 6)
    print(number)
