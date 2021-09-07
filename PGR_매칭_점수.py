import re

def solution(word, pages):
    word = word.lower()
    url_to_idx = dict()
    page_info = []
    for idx, page in enumerate(pages):
        cur = []
        p = re.compile(r"<meta property=\"og:url\" content=\"https://([\S]+)\"/>")
        url_to_idx[p.findall(page)[0]] = idx
        cur.append(p.findall(page)[0])

        p = re.compile(r"<a href=\"https://([\S]+)\"")
        cur.append(p.findall(page))
        low_page = page.lower()
        p = re.compile(r"[a-zA-Z]+")
        cur.append(p.findall(low_page).count(word))
        page_info.append(cur)

    link_score = [0 for _ in range(len(page_info))]
    base_score = []
    for idx, info in enumerate(page_info):
        out = info[1]
        base_score.append(info[2])
        for link in out:
            if not link in url_to_idx.keys():
                continue
            link_score[url_to_idx[link]] += info[2]/len(info[1])
    result = []
    for a,b in zip(base_score,link_score):
        result.append(a+b)
    max_idx = -1
    max_val = -1
    for idx,val in enumerate(result):
        if max_val<val:
            max_idx = idx
            max_val = val
    return max_idx

word = 'blind'
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]

word = 'Muzi'
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
print(solution(word,pages))