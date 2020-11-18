# Project Name:         a simple program that scrapes the text from a website and saves it into a text file.
# Author:               Sandro Aguilar
# Date:                 November 18, 2020

import bs4
import urllib.request

def main():
  link = "https://thefraternityadvisor.com/300-situations-sorority-and-fraternity-presidents-must-overcome/"
  webpage = str(urllib.request.urlopen(link).read())
  soup = bs4.BeautifulSoup(webpage)

  print(soup.get_text())

  # create a file, write to it, and save it
  f = open("web-text.txt", "w+");
  f.write(soup.get_text());
  f.close();

if __name__ == "__main__":
  main()