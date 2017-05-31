from selenium import webdriver
from bs4 import BeautifulSoup as bs
import collections

url='http://gsd-auth-callinfo.s3-website.us-east-2.amazonaws.com/'

class ComplaintsScrapper:
    def __init__(self):
        pass

    def all_complaints(self):
        driver = webdriver.Chrome()
        driver.get(url)
        html = driver.page_source
        driver.close()
        soup = bs(html, 'lxml')

        numbers = []
        numberTag = soup.find_all('h4', class_='oos_previewHeader')
        for number in numberTag:
            numbers.append(number.text)

        codes = []
        codeTag = soup.find_all('a')
        for code in codeTag:
            if "area code" in code.text:
                k = code.text.strip(" area code")
                codes.append(k.strip("()"))

        comments = []
        commentTag = soup.find_all('span', class_='postCount')
        for comment in commentTag:
            comments.append(comment.text)

        commentTexts = []
        commentTextTag = soup.find_all('div', class_='oos_previewBody')
        for tag in commentTextTag:
            commentTexts.append(tag.text)

        complaints = []
        for i in range(0, len(numbers)):
            dict = collections.OrderedDict()
            dict['area code'] = int(codes[i])
            dict['number'] = numbers[i]
            dict['number of comments'] = int(comments[i])
            dict['the comment '] = commentTexts[i]
            complaints.append(dict)
        return complaints


