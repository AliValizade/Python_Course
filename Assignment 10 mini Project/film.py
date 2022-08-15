from media import Media

class Film(Media):
    def __init__(self, id, n, dir, imdb, url, dur, c):
        Media.__init__(self, id, n, dir, imdb, url, dur, c)
        
    def show_info(self):
        print('======= ✅ Film =======')
        Media.show_info(self)
        