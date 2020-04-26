for $x in distinct-values(doc("books.xml")//author)
return <result>{$x}{","}{count(doc("books.xml")//book[contains(author,$x)])}</result>

