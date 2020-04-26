from lxml import etree, html
import pandas as pd
import os

os.chdir("/Users/ShuWen/abc/Coding/Python/435/HW1")


data = html.parse("book.html")
root = data.getroot()

# Get the book name
book_name = []
book_name_tree = root.xpath('//div[@class="AllEditionsItem-tileTitle"]/a')

for node in book_name_tree:
    book_name.append(node.text)

# Get the author's name
book_author = []
book_author_tree = root.xpath('//div[@class="SearchResultListItem-bottomSpacing SearchResultListItem-subheading"]')

for node in book_author_tree:
    # print(len(node))
    if len(node) != 0:
        book_author.append(node.getchildren()[0].text)
    else:
        book_author.append("NAN")

# Get the price, format and condition
book_price = []
book_format = []
book_condition = []
book_datapoint_tree = root.xpath('//div[@class="SearchResultTileItem-dataPoints"]')

for node in book_datapoint_tree:
    # print(len(node))
    if len(node) == 1:
        book_price.append("NAN")
        book_format.append("NAN")
        book_condition.append("NAN")
    else:
        book_price.append(node.getchildren()[0].getchildren()[0].getchildren()[1].text)
        book_format.append(node.getchildren()[1].getchildren()[0].getchildren()[0].text_content())
        book_condition.append(node.getchildren()[1].getchildren()[1].getchildren()[1].text)

#Concat data into a dataframe
book_name_df=pd.DataFrame(book_name)
book_price_df=pd.DataFrame(book_price)
book_condition_df=pd.DataFrame(book_condition)
book_format_df=pd.DataFrame(book_format)
book_author_df=pd.DataFrame(book_author)
book_df=pd.concat([book_name_df,book_author_df,book_price_df,book_format_df,book_condition_df],axis=1)
book_df.columns=["Name","Author","Price","Format","Condition"]

#output XML
colname = book_df.columns.values.tolist()
data = book_df.values.tolist()
root_out=etree.Element('books')
for row in data:
    dat = etree.SubElement(root_out,"book")
    for col in range(len(colname)):
        node = etree.SubElement(dat, colname[col]).text = str(row[col])
tree_out = (etree.tostring(root_out, pretty_print=True, xml_declaration=True, encoding="UTF-8"))
with open('book.xml', 'wb') as f:
    f.write(tree_out)