from bs4 import BeautifulSoup

"""
+ soup = BeautifulSoup(html_string, "html.parser") - parse HTML

+ Once parsed, there are several ways to navigate
    * by tag name
        _ using find() - return a matching tag
        _ using find_all - return a list of matching tags

    * by CSS selectors
        _ select by id: #foo
        _ select by class: .bar
        _ select children: div > p
        _ select descendents: div p
        _ select if element have an attribute: soup.select("[attribute]")
    IT ALWAYS GIVE THE LIST BACK (return a list [])

    * accessing data in elements
        _ get_text: access the inner text in an element
        _ name: tag name
        _ attrs: dictionary of attributes

    * navigating (having a tag and finding elements relative to that tag or element)
        - via tags
            _ parent / parents
            _ contents
            _ next_sibling / next_siblings (may be not an element)
            _ previous_sibling / previous_siblings (may be not an element)
        - via searching
            _ find_parent / find_parents 
            _ find_next_sibling / find_next_siblings (an element)
            _ find_previous_sibling / find_previous_siblings (an element)
"""

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes" class="header h3">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""
#=======FIND()============
soup = BeautifulSoup(html, "html.parser")
# print(soup)
# print(type(soup))
# print(soup.body.div)
d = soup.find('div') #find the first one
l = soup.find_all('li') #find all 
# t = soup.find(id = 'first')
# t = soup.find(class_ = 'special')
t = soup.find(attrs={"data-example": "yes"})
# print(t)

#======SELECT()===========
# test = soup.select("#first")
# test = soup.select(".special")
test = soup.select("[data-example]")
# print(test)

#======Accessing Data======
# print(t.get_text())
# print(d.name) #div
for k in test: 
    print(k.attrs) # {'data-example': 'yes', 'class': ['header', 'h3']}


