import pandas as pd
from lxml import etree
import os

os.chdir("/Users/ShuWen/abc/Coding/Python/435/HW1")



root = etree.Element('foodservices')
data = pd.read_csv("FoodServiceData.csv")
data = data.fillna("")
colname = data.columns.values.tolist()
data = data.values.tolist()
for row in data:
    dat = etree.SubElement(root,"foodservice")
    for col in range(len(colname)):
        node = etree.SubElement(dat, colname[col]).text = str(row[col])

tree_out = (etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="UTF-8"))
with open('FoodServiceData.xml', 'wb') as f:
    f.write(tree_out)
