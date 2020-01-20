import re

one = 'https://nakedbiblepodcast.com/wp-content/uploads/2017/08/NB-01-Transcript.pdf'
two = 'https://nakedbiblepodcast.com/wp-content/uploads/2015/02/Transcript-37-Acts-2-v1-21.pdf'
three = 'https://nakedbiblepodcast.com/wp-content/uploads/2016/12/Transcript-128.pdf'
four = 'https://nakedbiblepodcast.com/wp-content/uploads/2017/02/NB-140Transcript.pdf'

def episode(link):
    candidates = re.split('/', link)
    final_candidates = []
    for each in candidates:
        if 'Transcript' in each:
            final_candidates = re.split('-', each)
            final_candidates.append(final_candidates)
    return re.findall(r'\d+', final_candidates[1])[0]


print(episode(four))
