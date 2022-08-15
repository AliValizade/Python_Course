from media import Media

class Clip(Media):
    def __init__(self, id, n, dir, imdb, url, dur, c):
        Media.__init__(self, id, n, dir, imdb, url, dur, c)
    
    def show_info(self):
        print('======= ✅ Clip =======')
        Media.show_info(self)