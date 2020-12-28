# Program runs in the morning, scrape data from url and
# sends me a text with chance to rain on that day.

import requests, bs4
import textMyself

# Scrape weather data from url.
url = 'https://weather.com/weather/today/l/e700fb76f5138a2fc1d9befac622f7674926122a837e00fce243fdebb49ce906'
res = requests.get(url)
res.raise_for_status()
# Finds if it is going to rain.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
allsite = soup.select('.CurrentConditions--precipValue--RBVJT')
rain = allsite[0].getText()
# Sends the SMS text.
textMyself.textmyself(rain)