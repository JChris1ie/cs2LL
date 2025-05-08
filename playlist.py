import song
import csv
import os

class Playlist:

    def __init__(self):
        '''Initializes the playlist'''
        self.head=None
        self.tail=None

        self.currentSong=None # Advanced feature variable

        noDelete=['recommend.csv'] # Extra feature variable

    def isEmpty(self):
        '''Returns if list has values or not'''
        return self.head is None
    
    def addSongAtEnd(self,title,artist,duration):
        '''Adds a new song node to the end of current linked list'''
        newSong=song.Song(title,artist,duration)

        if self.isEmpty():
            self.head=newSong
            return
        
        current=self.head
        while current.next: # Traverse to end and reassign tail and pointers
            current=current.next
        current.next=newSong
        newSong.prev=current
        self.tail=newSong

    def addSongAtBeginning(self,title,artist,duration):
        '''Adds new song node to beginning of linked list'''
        newSong=song.Song(title,artist,duration)

        if self.isEmpty(): # check if empty
            self.head=newSong
            return
        elif self.head is not None and self.tail is None: # not empty case
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
        '''Searches for specific song by title and removes it from the linked list'''
        if self.isEmpty():
            print("No songs in playlist")
            return
        
        current=self.head
        while current:
            if current.title==title and current.prev and current.next: # Removing middle node case
                prev=current.prev
                next=current.next
                prev.next=next
                next.prev=prev
                print('Song removed')
                return
            elif current.title==title and current.prev and not current.next: # No next node case
                self.removeLastSong()
                return
            elif current.title==title and not current.prev and current.next: # No prev node case
                self.head=self.head.next
                self.head.prev=None
                print('Song removed')
                return
            elif self.head==self.tail: # head is same as tail case
                self.removeLastSong()
                return
            current=current.next
        print(f'Song "{title}" not found')

    def removeLastSong(self):
        '''Reassigns and modifies tail pointer to remove last value from linked list'''
        if self.tail is None and self.head is None:
            print("Playlist is empty")
            return
        elif self.tail is None and self.head is not None: # is head but no tail case
            self.head=None
            print('Song removed')
            return
        elif self.head==self.tail: # one song in playlist case
            self.head=None
            self.tail=None
            print('Song removed')
            return
                    
        self.tail=self.tail.prev
        self.tail.next=None
        print('Song removed')

    def display_playlist(self):
        '''Prints details for each song node'''
        if self.isEmpty():
            print('Playlist is empty')
            return
        
        print("--- Current Playlist ---")
        current=self.head 
        while current: # iterates through playlist
            print(current) # prints and advances
            current=current.next 

    def countSongs(self):
        '''Iterates through linked list and counts number of nodes'''
        counter=0
        if self.isEmpty(): # empty list case
            print(f'Number of songs: {counter}')
            return
        
        current=self.head
        while current: # list not empty case
            counter+=1
            current=current.next

        print(f'Number of songs: {counter}')

    def findSong(self,title):
        '''Searches through linked list for specific title'''
        current=self.head
        while current:
            if current.title==title: # just checks title
                return current
            current=current.next
        return False # user output handled in main.py

    def reversePlaylist(self):
        '''Reverses playlist in place'''
        if self.isEmpty():
            print('Playlist is empty')
            return
        
        prev=None 
        current=self.head
        while current:
            next_node=current.next # reassign pointers for navigation
            current.prev=current.next
            current.next=prev # reassign node pointers
            prev=current
            current=next_node # advance loop variable
        
        tail=self.tail # swap tail and head
        self.tail=self.head
        self.head=tail
        print('playlist reversed')

    '''------------------------ Advanced Features ------------------------'''

    ''' Play Mode '''
    def playCurrent(self):
        '''Prints details for current song playing'''
        if self.isEmpty():
            print('Playlist is empty')
            return

        if self.currentSong is None: # assigns current song as self.head if current song is none
            self.currentSong=self.head
            print('--- Now Playing ---')
        print(self.currentSong)
    
    def nextTrack(self):
        '''Advances current track and wraps around when at end of playlist'''
        if self.isEmpty():
            print('Playlist is empty')
            return
        
        if self.currentSong is None: # initialization if not already done
            self.currentSong=self.head
        
        if self.tail.artist==self.currentSong.artist and self.tail.title==self.currentSong.title: # wrap around case
            self.currentSong=self.head
        else: # normal advance case
            self.currentSong=self.currentSong.next
    
    def previousTrack(self):
        '''decrements track and wraps around when at the beginning'''
        if self.isEmpty():
            print('Playlist is empty')
            return
        
        if self.currentSong is None: # initialization if not already done
            self.currentSong=self.head

        if self.head.artist==self.currentSong.artist and self.head.title==self.currentSong.title: # wrap around from front case
            self.currentSong=self.tail
        else: # normal backtrack case
            self.currentSong=self.currentSong.prev

    ''' Playlist Saving '''

    def saveToFile(self,filename):
        '''Writes all playlist songs data to a csv file'''
        if self.isEmpty():
            print('Playlist is empty')
            return
        
        filename=filename+'.csv' # takes normal string and adds .csv to it 
        with open(filename, mode='w',newline='',encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Artist', 'Duration']) # first row with variable names
            current=self.head
            while current: # writes all song data to file
                writer.writerow([current.title,current.artist,current.duration])
                current=current.next

    def loadFromFile(self,filename):
        '''Reads all playlist song data from file'''
        filename=filename+'.csv'
        self.clearCurrentPlaylist() # clears current playlist before starting
        try: # tries to open and read file
            with open(filename,mode='r',encoding='utf-8') as file:
                reader=csv.DictReader(file)
                for row in reader: # reads data
                    self.addSongAtEnd(row['Title'],row['Artist'],int(row['Duration']))
            print('Playlist loaded')
        except: # gives user error if file not found
            print(f'File {filename[:-4]} not found')

    ''' Extra for playlist file management'''

    def deletePlaylist(self,filename):
        '''Erases playlist csv file from storage'''
        filename=filename+'.csv'
        try: # tries to remove file by name
            os.remove(filename)
            print(f'Playlist {filename[:-4]} deleted')
        except: # case if file not found
            print(f"Playlist {filename[:-4]} does not exist")

    ''' Extra for testing and QOL'''
    
    def clearCurrentPlaylist(self):
        '''Empties playlist of song data'''
        if self.isEmpty():
            print('Playlist is empty, no songs cleared')
            return
        
        self.head=None # clears pointers so nodes are inaccessible
        self.tail=None
        self.currentSong=None
        print('Cleared playlist')