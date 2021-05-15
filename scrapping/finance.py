from bs4 import BeautifulSoup
import requests
import openpyxl

page = requests.get('https://www.marketwatch.com/investing/stock/prsm/financials?countrycode=uk&mod=mw_quote_tab')

soup = BeautifulSoup(page.content, 'html.parser')





table = soup.find(class_='element element--table table--fixed financials')



flow = table.find(class_='table__header')

items = flow.find_all(class_='overflow__heading')

#print(items[0].find(class_='cell__content').get_text())
#print(items[1].find(class_='cell__content').get_text())
#print(items[2].find(class_='cell__content').get_text())
#print(items[3].find(class_='cell__content').get_text())
#print(items[4].find(class_='cell__content').get_text())
#print(items[5].find(class_='cell__content').get_text())

table_data = [items.find(class_='cell__content').get_text() for items in items]

print(table_data)

final = []

final.append(table_data)



body = table.find(class_="table__body row-hover")
body_rows = body.find_all(class_='table__row')


for body_row in body_rows:
    body_flow = body_row.find_all(class_='overflow__cell')
    table_body = [body_flow.find(class_='cell__content').get_text() for body_flow in body_flow]
    final.append(table_body)



print(final)



wb = openpyxl.load_workbook("C:\\Users\\ebbin\\Desktop\\finance.xlsx")

sh = wb["Sheet1"]

k = 1
m = 1

for i in final:

    print(i)

    for j in i:
        print(j)
        sh.cell(row=k,column=m).value = j
        m += 1

    k += 1
    m = 1

wb.save("C:\\Users\\ebbin\\Desktop\\finance.xlsx")




















