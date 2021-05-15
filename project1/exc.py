import pandas as pd

file = "C:\\Users\\ebbin\\Desktop\\company.xls"

fg = pd.read_excel(file)

ebbin = fg['Name'].where(df['item'] == 'ebbin')
