for $x in doc("books.xml")/catalog/book
order by xs:double($x/price)
return $x/title
