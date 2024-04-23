import requests
from bs4 import BeautifulSoup


def main():
    url = "https://www.imdb.com/chart/top"
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=header)
    html = response.text
    # 教學1, 全印
    # print(html)
    soup = BeautifulSoup(html)
    # print(soup)
    # 教學2, 印目標
    # tags = soup.find_all('span', {'class': 'sc-43986a27-8 jHYIIK cli-title-metadata-item'})
    # print(tags)
    # 教學3, 印div 縮排下的東西
    tags = soup.find_all('div', {'class': 'sc-43986a27-7 dBkaPT cli-title-metadata'})
    # print(tags)
    d = {}
    for tag in tags:
        target = tag.text
        print(target)
        year = target[:4]
        if year not in d:
            d[year] = 1
        else:
            d[year] += 1
    for year, count in sorted(d.items(), key=lambda t: t[1]):
        print(year, '->', count)


if __name__ == '__main__':
    main()
