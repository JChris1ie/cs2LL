class Song:
    def __init__(self,title,artist,duration=0):
        self.title=title
        self.artist=artist
        self.next=None
        self.prev=None
        
        self.duration=duration # advanced feature variable

    def __str__(self):
        return (f'{self.title} by {self.artist}, {self.duration} seconds')