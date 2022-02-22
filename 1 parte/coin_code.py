import requests
from bs4 import BeautifulSoup

url = "https://www.iban.com/currency-codes"

def get_coin_code():
	all_countries = []

	#request + soup
	request = requests.get(url)
	html_content = request.text
	soup = BeautifulSoup(html_content, 'html.parser')

	table = soup.find("table")
	lines = table.find_all("tr")[1:]

	for line in lines:
		items = line.find_all("td")
		name = items[0].text
		coin_name = items[1].text
		coin_code = items[2].text

		if coin_name != "No universal currency":
			country = {
				'country': name,
				'code': coin_code
			}
			all_countries.append(country)

	for index, country in enumerate(all_countries):
		print(f"#{index} {country['country']}")

	return all_countries