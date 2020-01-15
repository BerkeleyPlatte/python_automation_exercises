import random


def coin_flip_streaks():
    count = 0
    h_or_t = []
    for n in range(10000):
        outcome = random.randint(0, 1)
        if outcome == 0:
            h_or_t.append('h')
        else:
            h_or_t.append('t')
    for i in range(len(h_or_t) - 5):
        if h_or_t[i] == h_or_t[i + 1]:
            if h_or_t[i + 1] == h_or_t[i + 2]:
                if h_or_t[i + 2] == h_or_t[i + 3]:
                    if h_or_t[i + 3] == h_or_t[i + 4]:
                        if h_or_t[i + 4] == h_or_t[i + 5]:
                            count += 1
    print('chance of streak: %s%%' % (count / 100))
    
coin_flip_streaks()
