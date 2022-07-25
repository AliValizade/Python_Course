from pyfiglet import Figlet

def show_menu():
        print('1- Add Product')
        print('2- Edit Product')
        print('3- Delet Product')
        print('4- Search')
        print('5- Show Product List')
        print('6- Buy')
        print('7- Exit')
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
    myfile = open('D:\EBook\Learning Computer\Python Edu\Python_Course\Assignment 6\My_Store\database.txt', 'a')
    while True:
        myfile.write('\n')
        myfile.write(input('Plz enter produc id:'))
        myfile.write(',')
        myfile.write(input('Plz enter produc name:'))
        myfile.write(',')
        myfile.write(input('Plz enter price of produc:'))
        myfile.write(',')
        myfile.write(input('Plz enter count of the produc:'))
        myfile.close()
        add_new = input('Do you want to add new product? (Y/N) ')
        if add_new.lower() == 'n':
            break
    myfile.close()
def edit_product():
    pass
def delet_product():
    pass
def search_product():
    pass
def show_list():
    for i in range(len(Products)):
        print(Products[i])
def buy_product():
    pass

Products = []
load()

f = Figlet(font='slant')
print(f.renderText('Titech Co.'))

show_menu()
menu_item = int(input('Plz enter number of the menu: '))
if menu_item == 1:
    add_product()
elif menu_item == 2:
    pass
elif menu_item == 3:
    pass
elif menu_item == 4:
    pass
elif menu_item == 5:
    show_list()
elif menu_item == 6:
    pass
elif menu_item == 7:
    exit()


