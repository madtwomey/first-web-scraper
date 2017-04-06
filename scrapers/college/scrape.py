import csv
import requests
from BeautifulSoup import BeautifulSoup

years = ['2015-2016', '2014-2015', '2013-2014', '2012-2013', '2011-2012', '2010-2011']
list_of_rows = []

for year in years: 
	response = requests.get("https://columbian.gwu.edu/" + year)
	html = response.content

	soup = BeautifulSoup(html)
	table = soup.find('table')

	for row in table.findAll('tr')[1:-1]:
		list_of_cells = []
		list_of_cells.append(year)
		for cell in row.findAll('td'):
			list_of_cells.append(cell.text.encode('utf-8'))
		list_of_rows.append(list_of_cells)

outfile = open("faculty.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Department", "Faculty", "Sponsor", "Title"])
writer.writerows(list_of_rows)