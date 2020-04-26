from lxml import etree
import pandas as pd
import os

os.chdir("/Users/ShuWen/abc/Coding/Python/435/HW1")


data = etree.parse("FoodServiceData.xml")
root = data.getroot()

# for TypeDescription
x = []
for node in root.xpath('//TypeDescription'):
    x.append(node.text)
result_x = pd.value_counts(x)
result_x = result_x.sort_index()
for i in range(len(result_x)):
    print(result_x.index.values[i] + " " + str(result_x[i]))

# for Grade
y = []
for node in root.xpath('//Grade'):
    y.append(node.text)
result_y = pd.value_counts(y)
result_y = result_y.sort_index()
for i in range(len(result_y)):
    print(result_y.index.values[i] + " " + str(result_y[i]))
