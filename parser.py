import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def parse(html):
	soup = BeautifulSoup(html)
	table = soup.find('table', class_='als-sortable-table')

	country_code = {}
	code_country = {}
	for row in table.find_all('tr')[1:]:
		col = row.find_all('td')

		if '\xa0' in col[0].text.lower():
			country = col[0].text.lower().replace('\xa0', ' ')
		else:
			country = col[0].text.lower()

		country_code[country] = col[3].text
		code_country[col[3].text] = country



def main():
	parse(get_html('https://www.artlebedev.ru/country-list/'))


if __name__ == '__main__':
	main()
