from media import Media

class Documantary(Media):
    def __init__(self, id, n, dir, imdb, url, dur, c):
        Media.__init__(self, id, n, dir, imdb, url, dur, c)

    def show_info(self):
        print('======= ✅ Documentory =======')
        Media.show_info(self)
