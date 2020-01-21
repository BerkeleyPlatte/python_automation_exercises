import re

one = 'https://nakedbiblepodcast.com/wp-content/uploads/2017/08/NB-01-Transcript.pdf'
three_7 = 'https://nakedbiblepodcast.com/wp-content/uploads/2015/02/Transcript-37-Acts-2-v1-21.pdf'
six_8 = 'https://nakedbiblepodcast.com/wp-content/uploads/2017/02/Podcast-68-Interview.pdf'
one_28 = 'https://nakedbiblepodcast.com/wp-content/uploads/2016/12/Transcript-128.pdf'
one_40 = 'https://nakedbiblepodcast.com/wp-content/uploads/2017/02/NB-140Transcript.pdf'
two_39 = 'https://nakedbiblepodcast.com/wp-content/uploads/2018/11/Episode-239-transcript.pdf'


def episode(link):
    candidates = re.split('/', link)
    final_candidates = []
    for each in candidates:
        if each.endswith('pdf'):
            final_candidates = re.split('-', each)
            final_candidates.append(final_candidates)
    return re.findall(r'\d+', final_candidates[1])[0]


print(episode(two_39))
