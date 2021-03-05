from random import randint

def play() :
    random_int = randint(0,100)

    while True :
        user_guess = int(input("猜數字0-100"))

        if user_guess == random_int :
            print(f"猜對了")
            break
        if user_guess > random_int :
            print(f"小一點")
            continue
        if user_guess < random_int :
            print(f"大一點")
            continue

if __name__ == '__main__':
    play()
