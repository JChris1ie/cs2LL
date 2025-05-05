import song

class Playlist:
    def __init__(self):
        self.head=None
        self.tail=None

        self.currentSong=None # Advanced feature variable
    
    def isEmpty(self):
        return self.head is None
    
    def addSongAtEnd(self,title,artist):
        newSong=song.Song(title,artist)

        if self.head is None:
            self.head=newSong
            return
        
        current=self.head
        while current.next:
            current=current.next
        current.next=newSong
        newSong.prev=current
        self.tail=newSong

    def addSongAtBeginning(self,title,artist):
        newSong=song.Song(title,artist)

        if self.head is None:
            self.head=newSong
            return
        elif self.head is not None and self.tail is None:
            nextSong=self.head
            self.head=newSong
            newSong.next=nextSong
            nextSong.prev=self.head
            self.tail=nextSong
            return
        
        nextSong=self.head
        self.head=newSong
        newSong.next=nextSong
        nextSong.prev=self.head

    def removeSongByTitle(self,title):
        if self.head is None:
            print("No songs in playlist")
            return
        
        current=self.head
        while current:
            if current.title==title:
                prev=current.prev
                next=current.next
                prev.next=next
                next.prev=prev
            current=current.next

    def removeLastSong(self):
        if self.tail is None and self.head is None:
            print("Playlist is empty")
        elif self.tail is None and self.head is not None:
            self.head=None
                    
        self.tail=self.tail.prev
        self.tail.next=None

    def display_playlist(self):
        if self.head is None:
            print('Playlist is empty')
            return
        
        print("--- Current Playlist ---")
        current=self.head
        while current:
            print(current)
            current=current.next

    def countSongs(self):
        counter=0
        if self.head is None:
            print(f'Number of songs: {counter}')
            return
        
        current=self.head
        while current:
            counter+=1
            current=current.next

        print(f'Number of songs: {counter}')

    def findSong(self,title): # main should handle output
        current=self.head
        while current:
            if current.title==title:
                return True
            current=current.next
        return False

    def reversePlaylist(self):
        if self.head is None:
            print('Playlist is empty')
            return
        
        prev=None
        current=self.head
        while current:
            next_node=current.next
            current.prev=current.next
            current.next=prev
            prev=current
            current=next_node
        
        tail=self.tail
        self.tail=self.head
        self.head=tail

    '''------------------------ Advanced Features ------------------------'''

    def playCurrent(self):
        if self.currentSong is None:
            self.currentSong=self.head
        print(self.currentSong)
    
    def nextTrack(self):
        if self.currentSong is None:
            self.currentSong=self.head
        
        if self.tail.artist==self.currentSong.artist and self.tail.title==self.currentSong.title:
            self.currentSong=self.head
        else:
            self.currentSong=self.currentSong.next
    
    def previousTrack(self):
        if self.currentSong is None:
            self.currentSong=self.head

        if self.head.artist==self.currentSong.artist and self.head.title==self.currentSong.title:
            self.currentSong=self.tail
        else:
            self.currentSong=self.currentSong.prev