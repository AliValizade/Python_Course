from pyfiglet import Figlet
import qrcode

def show_menu():
    print('🈯🈯🈯🈯 MENU🈯🈯🈯🈯')
    print('1- Add Product')
    print('2- Edit Product')
    print('3- Delet Product')
    print('4- Search')
    print('5- Show Product List')
    print('6- Buy')
    print('7- Make QRCode of Product')
    print('8- Exit \n🈯🈯🈯🈯 END MENU🈯🈯🈯🈯')
def load():
    print('Loading.....')
    myfile = open('database.txt', 'r')
    data = myfile.read()
    product_list = data.split('\n')
    for i in range(len(product_list)):
        product_info = product_list[i].split(',')
        product_dict = {}
        product_dict['id'] = int(product_info[0])
        product_dict['name'] = product_info[1]
        product_dict['price'] = int(product_info[2])
        product_dict['count'] = int(product_info[3])
        Products.append(product_dict)
    print('Welcome to my store✅')
def add_product():
    while True:
        add_product = input('Plz enter the name of the product to Add: ➕ ').lower()
        for item in Products:
            if item['name'] != add_product:
               Products.append({'id': int(input('Product ID: ')), 'name': add_product , 'price': int(input('Price of Product: ')), 'count': int(input('The count of Product: '))})
               print(add_product, 'Added to Store. ✅')
               break
        add_new = input('Do you want to add new product? (Y/N) ')
        if add_new.lower() == 'n':
            break
    show_menu()
def edit_product():
    edit_id = int(input('Plz enter the id of the product to edit:🔁 '))
    for i in range(len(Products)):
        if edit_id == Products[i]['id']:
            print('1- Edit name: \n2- Edit price: \n3- Edit count: ')
            edit_menu = int(input('Plz select item for edit: '))
            if edit_menu == 1:
                Products[i]['name'] = input('Plz enter new name: ')
            elif edit_menu == 2:
                Products[i]['price'] = int(input('Plz enter new price: '))
            elif edit_menu == 2:
                Products[i]['count'] = int(input('Plz enter new count: '))
            break
    else:
        print('The desired product is not available in the store!⛔ Please create it.')
    show_menu()               
def delete_product():
    item_for_delete = int(input('Plz enter the id of the product to delet:➖ '))
    for item in Products:
        if item['id'] == item_for_delete:
            Products.remove(item)
            print(item_for_delete, 'Removed!✅')
            break
    else:
        print('Sorry, Product not found!')
def search_product():
    search_item = input('Plz enter the name of the product to search:🔍 ').lower()
    for item in Products:
        if item['name'] == search_item:
            print('search_item  => ', item)
            break
    else:
        print('Sorry, Product not found!')
    show_menu()
def show_list():
    for i in range(len(Products)):
        print(Products[i])
    show_menu()
def buy_product():
    invoice = []
    sum = 0
    while True:
        product_to_buy = int(input('Plz enter the id of the product to buy: 🛒 '))
        for item in Products:
            if item['id'] == product_to_buy:
                count_to_buy = int(input('Plz enter the count of the product to buy:🔢 '))
                if count_to_buy <= item['count']:
                    invoice.append({'name': item['name'], 'count': count_to_buy, 'price': item['price'] * count_to_buy})
                    item['count'] = int(item['count']) - count_to_buy
                    print(item['name'], 'Added to your Invoice. ✅' )
                else:
                    print('ُSorry! Insufficient inventory. We have', str(item['count']), 'of', item['name'])
                break
        if input('Do you want to buy more product? (Y/N) ').lower() == 'n':
            break
    print('_____________________________\n✅🛒🛒🛒 Buy Invoice 🛒🛒🛒✅\n')
    for item in invoice:
        print(item)
        sum += int(item['price'])
    print('_________________________________________________\nTotal amount = ', sum, '\n')
    show_menu()
def product_qrcode():
    product_id = int(input('Plz enter the id of the product to make QRCode: '))
    for item in Products:
        if product_id == item['id']:
            product_QRCode = qrcode.make(item)
            product_QRCode.save('qrcode.png')
    show_menu()          
def save_and_exit():
    update_myfile = open('database.txt', 'w')
    for item in Products:
        update_myfile.write(str(item['id']) + ',' + item['name'] + ',' + str(item['price']) + ',' + str(item['count']))
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
        delete_product()
    elif menu_item == 4:
        search_product()
    elif menu_item == 5:
        show_list()
    elif menu_item == 6:
        buy_product()
    elif menu_item == 7:
        product_qrcode()    
    elif menu_item == 8:
        save_and_exit()