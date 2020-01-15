def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return int(number // 2)
    else:
        print(3 * number + 1)
        return int(3 * number + 1)


print('type a number')
try:
    num = input()
    while num != 1:
        num = collatz(int(num))
except ValueError:
    print("don't be that guy, just type a number")
    num = input()
    while num != 1:
        num = collatz(int(num))
