import bs4
import urllib.request

link = "https://thefraternityadvisor.com/300-situations-sorority-and-fraternity-presidents-must-overcome/"
webpage=str(urllib.request.urlopen(link).read())
soup = bs4.BeautifulSoup(webpage)

print(soup.get_text())

# create a file
f = open("web-text.txt", "w+");
