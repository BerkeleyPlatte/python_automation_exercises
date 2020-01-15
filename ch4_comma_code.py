spam = ['apples', 'bananas', 'tofu', 'cats']
test = []

def comma_code(words):
    rev_words = words[::-1]
    comma_words = []
    for each in rev_words:
        if rev_words.index(each) == 0:
            comma_words.append('and ' + each)
        else:
            comma_words.append(each + ',')
    answer = comma_words[::-1]
    print(' '.join(answer))


comma_code(spam) 
