def urls():
    the_urls = []
    print('the number, please:')
    latest = int(input()) + 1
    for i in range(1, latest):
        url = f'https://nakedbiblepodcast.com/page/{i}/'
        the_urls.append(url)
    return the_urls

print(urls())