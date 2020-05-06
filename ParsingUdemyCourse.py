from bs4 import BeautifulSoup
import urllib

url = "https://www.udemy.com/course/learn-flutter-dart-to-build-ios-android-apps/"
html_doc = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html_doc, 'html.parser')

cont_with_prewiew = soup.find_all('div',"lecture-container lecture-container--preview")
cont_with_title = [x.find('div','title').find('a').get_text() for x in cont_with_prewiew]
cont_with_time = [x.find('span','content-summary').get_text()  for x in cont_with_prewiew]

result = [(x,y) for x,y in zip(cont_with_title,cont_with_time)]
result.sort(key=lambda i: i[1])
result = ''.join([x[0] for x in result])
f = open('UdemyCourse.txt', 'w')
f.write(result)
f.close()
