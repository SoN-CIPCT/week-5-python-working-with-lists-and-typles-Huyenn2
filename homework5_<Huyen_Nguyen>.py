List Exercise:
>>> Vietnamese_foods = ["broken rice", "sandwich", "brisket noodle soup", "spring rolls", "egg rolls", "grilled pork noodle bowl salad"]
>>> print(Vietnamese_foods)
['broken rice', 'sandwich', 'brisket noodle soup', 'spring rolls', 'egg rolls', 'grilled pork noodle bowl salad']
>>> print(f'The first two items in the list are: {Vietnamese_foods[0:2]}')
The first two items in the list are: ['broken rice', 'sandwich']
>>> print(f'The middle two items in the list are: {Vietnamese_foods[2:4]}')
The middle two items in the list are: ['brisket noodle soup', 'spring rolls']
>>> res = Vietnamese_foods [::len(Vietnamese_foods)-1]
>>> print(f'The first and the last items in the list are:' + str(res))
The first and the last items in the list are:['broken rice', 'grilled pork noodle bowl salad']

Tuple Exercise:
>>> Menu = [(1,'strawberry'),(2,'grapes'),(3,'cherry'),(4,'kiwi'),(5,'pear')]
>>> for food in Menu:
...     print(food)
...     
(1, 'strawberry')
(2, 'grapes')
(3, 'cherry')
(4, 'kiwi')
(5, 'pear')
>>> Update_menu = [(1,'strawberry'),(2,'grapes'),(3,'cherry'),(4,'kiwi'),(5,'pear')]
>>> for food in Update_menu:
...     print(food)
...     
(1, 'strawberry')
(2, 'grapes')
(3, 'cherry')
(4, 'kiwi')
(5, 'pear')
>>> 
