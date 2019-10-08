from selenium import webdriver
import bs4 as bs

driver = webdriver.Chrome()

url = 'http://espn.com/college-football/rankings'
driver.get(url)
soup = bs.BeautifulSoup(driver.page_source, "lxml")
table = soup.find('tbody')
rows = table.find_all('tr')

links = []
for row in rows:
    links.append(url+row.find('a').get('href'))

# https://www.espn.com/college-football/team/_/id/228/clemson-tigers
# https://www.espn.com/college-football/team/roster/_/id/228

heights = []
weights = []

for link in links:
    base = 'https://www.espn.com/college-football/team/roster/_/'
    base += link.split('/')[-3] + '/' + link.split('/')[-2]
    driver.get(base)
    soup = bs.BeautifulSoup(driver.page_source, "lxml")
    table = soup.find('tbody')
    for td in soup.find_all('td'):
        s = td.text
        if "'" in s and '"' in s:
            s = s.replace("'", '').replace('"', '')
            print(s)
            height = (int(s.split(' ')[0]) * 12) + int(s.split(' ')[1])
            heights.append(height)

        elif 'lbs' in s:
            weight = int(s.split(' ')[0])
            weights.append(weight)

print(sum(heights)/len(heights))
print(sum(weights)/len(weights))
    
    
