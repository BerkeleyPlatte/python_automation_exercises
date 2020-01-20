import time, random

then = time.time()

print('name please')
name = input()
print(f'hello {name}')

now = time.time()

print('it took ', now - then, ' seconds')