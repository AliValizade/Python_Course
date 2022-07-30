from pyfiglet import Figlet

def show_menu():
    print('🈯🈯🈯🈯 MENU🈯🈯🈯🈯')
    print('1- Add Product')
    print('2- Edit Product')
    print('3- Delet Product')
    print('4- Search')
    print('5- Show Product List')
    print('6- Buy')
    print('7- Exit \n🈯🈯🈯🈯 END MENU🈯🈯🈯🈯')
def load():
    print('Loading.....')
    myfile = open('D:\EBook\Learning Computer\Python Edu\Python_Course\Assignment 6\My_Store\database.txt', 'r')
    data = myfile.read()
    product_list = data.split('\n')
    for i in range(len(product_list)):
        product_info = product_list[i].split(',')
        product_dict = {}
        product_dict['id'] = product_info[0]
        product_dict['name'] = product_info[1]
        product_dict['price'] = product_info[2]
        product_dict['count'] = product_info[3]
        Products.append(product_dict)
    print('Welcome to my store✅')
def add_product():
    while True:
        add_product = input('Plz enter the name of the product to Add: ➕ ')
        for item in Products:
            if item['name'] != add_product:
               Products.append({'id': input('Product ID: '), 'name': add_product , 'price': input('Price of Product: '), 'count': input('The count of Product: ')})
               print(add_product, 'Added to Store. ✅')
               break
        add_new = input('Do you want to add new product? (Y/N) ')
        if add_new.lower() == 'n':
            break
    show_menu()
def edit_product():
    name = input('Plz enter the name of the product to edit:🔁').lower()
    for i in range(len(Products)):
        if name == Products[i]['name']:
            Products[i]['name'] = input('Plz enter new name: ')
            Products[i]['price'] = input('Plz enter new price: ')
            Products[i]['count'] = input('Plz enter new count: ')
            break
    else:
        print('The desired product is not available in the store!⛔ Please create it.')
    show_menu()               
def delet_product():
    item_for_delet = input('Plz enter the name of the product to delet:➖ ').lower()
    for item in Products:
        if item['name'] == item_for_delet:
            Products.remove(item)
            print(item_for_delet, 'Removed!✅')
            break
    else:
        print('Sorry, item not found!')
def search_product():
    search_item = input('Plz enter the name of the product to search:🔍 ').lower()
    for item in Products:
        if item['name'] == search_item:
            print('search_item: ', str(item))
            break
    else:
        print('Sorry, item not found!')
    show_menu()
def show_list():
    for i in range(len(Products)):
        print(Products[i])
    show_menu()
def buy_product():
    invoice = []
    sum = 0
    while True:
        product_to_buy = input('Plz enter the name of the product to buy: 🛒 ')
        for item in Products:
            if item['name'] == product_to_buy:
                count_to_buy = int(input('Plz enter the count of the product to buy:🔢 '))
                invoice.append({'name': product_to_buy, 'count': count_to_buy, 'price': int(item['price']) * count_to_buy})
                item['count'] = int(item['count']) - count_to_buy
                break
        if input('Do you want to buy more product? (Y/N) ').lower() == 'n':
            break
    print('__________________________________\n✅🛒🛒🛒 Buy Invoice 🛒🛒🛒✅\n')
    for item in invoice:
        print(item)
        sum += int(item['price'])
    print('__________________________________\nTotal amount = ', sum, '\n')
    show_menu()
def save_and_exit():
    update_myfile = open('D:\EBook\Learning Computer\Python Edu\Python_Course\Assignment 6\My_Store\database.txt', 'w')
    for item in Products:
        update_myfile.write(item['id'] + ',' + item['name'] + ',' + str(item['price']) + ',' + str(item['count']))
        if item != Products[-1]:
            update_myfile.write('\n')
    update_myfile.close()
    print('Products List Updated.✅🙏')
    exit()

Products = []
load()

f = Figlet(font='slant')
print(f.renderText('Titech Co.'))

show_menu()
while True:
    menu_item = int(input('Plz enter number of the menu: '))
    if menu_item == 1:
        add_product()
    elif menu_item == 2:
        edit_product()
    elif menu_item == 3:
        delet_product()
    elif menu_item == 4:
        search_product()
    elif menu_item == 5:
        show_list()
    elif menu_item == 6:
        buy_product()
    elif menu_item == 7:
        save_and_exit()