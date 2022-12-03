from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
driver = webdriver.Chrome()

driver.get("https://iotvega.com/product")

webNames = driver.find_elements(By.CLASS_NAME, "product-name")
webPrices = driver.find_elements(By.CLASS_NAME, "price_item")

names = list()
prices = list()
data = dict()

for e in webNames:
    names.append(e.text)
for e in webPrices:
    prices.append(e.text)

data.update(Name=names, Price=prices)

df = pd.DataFrame(data)
writer = pd.ExcelWriter('products.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='sheet1')

driver.quit()
writer.save()

