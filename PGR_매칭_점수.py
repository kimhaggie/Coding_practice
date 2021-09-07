import re

def get_url(page):
    index=-1
    while True:
        index = page.find('<meta', index + 1)
        if index == -1:
            break
        for x in page[index:].split('>')[0].split('\"'):
            if 'https://'in x:
                return x

def get_body(page):
    index=-1
    while True:
        index = page.find('<body>', index + 1)
        if index == -1:
            break
        return page[index+7:].split('</body>')[0][:-1]

def match_score(body, target):
    visit = [False for _ in range(len(body))]
    print(body.split('\n'))
    index=-1
    while True:
        index = body.find('<a href', index + 1)
        if index == -1:
            break
        print(body[index:].split('>')[0])
        # for x in :
        #     print(x)

def solution(word, pages):
    answer = 0
    print(get_url(pages[0]))
    print(get_url(pages[1]))
    print(get_url(pages[2]))
    body = []
    for page in pages:
        body.append(get_body(page))
    # print(body)
    match_score(body[0],word)
    # print(pages[0])
    # print(pages[1])
    # print(pages[2])
    return answer

word = 'blind'
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
print(solution(word,pages))