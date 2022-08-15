import pytube
from actor import Actor

class Media:
    def __init__(self, id, n, dir, imdb, url, dur, c):
        self.ID = id
        self.name = n
        self.director = dir
        self.IMDB_Score = imdb
        self.url = url
        self.duration = dur
        self.casts = c

    def show_info(self):
        print('⏹▶ ID:', self.ID, '▶ Name:', self.name, '▶ Director:', self.director, '▶ IMDB Score:', self.IMDB_Score, '▶ URL:', self.url, '▶ Duration:', self.duration, '▶ Casts:', self.casts)

    def download(self):
        link= self.url
        first_stream = pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./', filename= 'm01.mp4')
        print("Media Downloaded successfully!")

    
