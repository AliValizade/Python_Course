from media import Media

class Series(Media):
    def __init__(self, id, n, dir, imdb, url, dur, c, p):
        Media.__init__(self, id, n, dir, imdb, url, dur, c)
        self.part = p

    def show_info(self):
        print('======= ✅ Series =======')
        Media.show_info(self)
        print('▶ Part of Series:', self.part)