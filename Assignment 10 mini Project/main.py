import qrcode
from film import Film
from documentory import Documantary
from clip import Clip
from serial import Series
from actor import Actor
class Main:
    def __init__(self):
        print('Loading.....')
        myfile = open('database.txt', 'r')
        media_text = myfile.read().split('\n')
        self.media_list = []
        try:
            for i in range(len(media_text)):
                self.media_info = media_text[i].split(',')
                if self.media_info[0][0].lower() == 'f':
                    self.media_list.append(Film(self.media_info[0], self.media_info[1], self.media_info[2], self.media_info[3], self.media_info[4], int(self.media_info[5]), self.media_info[6]))
                elif self.media_info[0][0].lower() == 's':
                    self.media_list.append(Series(self.media_info[0], self.media_info[1], self.media_info[2], self.media_info[3], self.media_info[4], int(self.media_info[5]), self.media_info[6], self.media_info[7]))
                elif self.media_info[0][0].lower() == 'c':
                    self.media_list.append(Clip(self.media_info[0], self.media_info[1], self.media_info[2], self.media_info[3], self.media_info[4], int(self.media_info[5]), self.media_info[6]))
                elif self.media_info[0][0].lower() == 'd':
                    self.media_list.append(Documantary(self.media_info[0], self.media_info[1], self.media_info[2], self.media_info[3], self.media_info[4], int(self.media_info[5]), self.media_info[6]))
        except:
            print('Database is empty! ')
        print('Welcome to my studio✅')
        myfile.close()
        self.show_menu()
    def add_media(self):
        while True:
            input_id = input('Plz enter the media ID (id started with first letter of media type) )➕ : ')
            if input_id[0].lower() == 'f':
                self.media_list.append(Film(input_id, input('enter name of your media: '), input('enter director of your media: '), input('enter IDMB Score of your media: '), input('enter url of your media: '), int(input('enter duration of your media: ')), input('enter casts of your media: ')))
            elif input_id[0].lower() == 's':
                self.media_list.append(Series(input_id, input('enter name of your media: '), input('enter director of your media: '), input('enter IDMB Score of your media: '), input('enter url of your media: '), int(input('enter duration of your media: ')), input('enter casts of your media: '), input('enter part number of your media: ')))
            elif input_id[0].lower() == 'c':
                self.media_list.append(Clip(input_id, input('enter name of your media: '), input('enter director of your media: '), input('enter IDMB Score of your media: '), input('enter url of your media: '), int(input('enter duration of your media: ')), input('enter casts of your media: ')))
            elif input_id[0].lower() == 'd':
                self.media_list.append(Documantary(input_id, input('enter name of your media: '), input('enter director of your media: '), input('enter IDMB Score of your media: '), input('enter url of your media: '), int(input('enter duration of your media: ')), input('enter casts of your media: ')))
            else:
                print('Error! The ID must be a combination of the first letter of the type of media and numbers(such as f101, c1112, s2000 or d1222):')
            if input('Do you want to add another media? (Y/N) ').lower() == 'n':
                break
        self.show_menu()
    def edit_media(self):
        edit_id = input('Plz enter the media ID to edit 📝 : ')
        for media in self.media_list:
            if media.ID == edit_id:
                print('edit_menu','\n1- Edit name:','\n2- Edit Director:','\n3- Edit IMDB_Score:','\n4- Edit URL:','\n5- Edit Duration:','\n6- Edit Casts:')
                edit_choice = int(input('Plz choice item to edit: '))
                if edit_choice == 1:
                    media.name = input('Enter new name: ')
                elif edit_choice == 2:
                    media.director = input('Enter new director: ')
                elif edit_choice == 3:
                    media.IMDB_Score = input('Enter new IMDB_Score: ')
                elif edit_choice == 4:
                    media.url = input('Enter new URL: ')
                elif edit_choice == 5:
                    media.duration = int(input('Enter new duration: '))
                elif edit_choice == 6:
                    media.casts = input('Enter new casts: ')
                break
        else:
            print('Your media ID not exist! try again.')
        self.show_menu()
    def delete_media(self):
        delete_ID = input('Plz enter the media ID to delete ❌ :')
        for media in self.media_list:
            if media.ID == delete_ID:
                self.media_list.remove(media)
                break
        else:
            print('The media ID not found ‼')
        self.show_menu()
    def search_media(self):
        print('1- Search by media ID','\n2- Search with duration of media')
        search_type = int(input('Plz select type of search: 🍳  '))
        if search_type == 1:
            search_ID = input('Plz enter the media ID to search: 🍳  ')
            for media in self.media_list:
                if media.ID == search_ID:
                    media.show_info()
                    break
            else:
                print('The media ID not found ‼')
        elif search_type == 2:
            search_time1 = int(input('Enter first time (minute): '))
            search_time2 = int(input('Enter second time (minute): '))
            for media in self.media_list:
                if search_time2 > media.duration > search_time1:
                    media.show_info()
        self.show_menu()
    def show_media_list(self):
        print('📝 Database loaded. 📝')
        for item in self.media_list:
            item.show_info()
        self.show_menu()
    def download_media(self):
        download_ID = input('Plz enter the media ID to Download ⭕ :')
        for media in self.media_list:
            if media.ID == download_ID:
                media.download()
        else:
            print('The media ID not found ‼')
        self.show_menu()
    def media_qrcode(self):
        qrcode_ID = input('Plz enter the media ID to make QRCode 🔣 :')
        for media in self.media_list:
            if media.ID == qrcode_ID:
                media_qrcode = qrcode.make(media)
                media_qrcode.save('qrcode.png')
                break
        self.show_menu()
    def show_casts(self):
        media_artist = input('Plz enter the media ID to show casts 👩‍👩‍👧‍👧 :')
        for media in self.media_list:
            if media.ID == media_artist:
                artists = media.casts.split('-')
        print(media.name, 'Actors: ⏬')
        for artist in artists:
            Actor(artist).artists_list()
        self.show_menu()
    def save_media_list(self):
        update_myfile = open('database.txt', 'w')
        for media in self.media_list:
            if media.ID[0] == 'f':
                update_myfile.write(media.ID + ',' + media.name + ',' + media.director + ',' + media.IMDB_Score + ',' + media.url + ',' + media.duration + ',' + media.casts)
            elif media.ID[0] == 's':
                update_myfile.write(media.ID + ',' + media.name + ',' + media.director + ',' + media.IMDB_Score + ',' + media.url + ',' + media.duration + ',' + media.casts + ',' + media.part)
            elif media.ID[0] == 'c':
                update_myfile.write(media.ID + ',' + media.name + ',' + media.director + ',' + media.IMDB_Score + ',' + media.url + ',' + media.duration + ',' + media.casts)
            elif media.ID[0] == 'd':
                update_myfile.write(media.ID + ',' + media.name + ',' + media.director + ',' + media.IMDB_Score + ',' + media.url + ',' + media.duration + ',' + media.casts)
            if media != self.media_list[-1]:
                update_myfile.write('\n')
        update_myfile.close()
        print('Products List Updated.✅🙏')
        exit()
    def show_menu(self):
        print('======== MENU ========')
        print('1- Add Media')
        print('2- Edit Media')
        print('3- Delet Media')
        print('4- Search Media')
        print('5- Show Media List')
        print('6- Download Media')
        print('7- Make QRCode of Media')
        print('8- Show Casts')
        print('9- Exit \n====== END MENU ======')
        while True:
            self.menu_item = int(input('Plz choice menu number: '))
            if self.menu_item == 1:
                self.add_media()
            elif self.menu_item == 2:
                self.edit_media()
            elif self.menu_item == 3:
                self.delete_media()
            elif self.menu_item == 4:
                self.search_media()
            elif self.menu_item == 5:
                self.show_media_list()
            elif self.menu_item == 6:
                self.download_media()
            elif self.menu_item == 7:
                self.media_qrcode()
            elif self.menu_item == 8:
                self.show_casts()
            elif self.menu_item == 9:
                self.save_media_list()
Main()