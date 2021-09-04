fruits = ['orange', 'grape', 'apple']
add_item = 'mango'

def add_fruits(fruits, add_item):
    print('Current:',fruits)
    print('Add item:', add_item)
    fruits.append(add_item)
    print('After add item: ',fruits)

add_fruits(fruits,add_item)