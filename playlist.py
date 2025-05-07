import song
import csv
import os
import random

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

        if self.isEmpty():
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
        '''Searches for specific song by title and removes it from the linked list'''
        if self.isEmpty():
            print("No songs in playlist")
            return
        
        current=self.head
        while current:
            if current.title==title and current.prev and current.next: # Removing middle node
                prev=current.prev
                next=current.next
                prev.next=next
                next.prev=prev
                print('Song removed')
                return
            elif current.title==title and current.prev and not current.next: # No next node
                self.removeLastSong()
                return
            elif current.title==title and not current.prev and current.next: # No prev node
                self.head=self.head.next
                self.head.prev=None
                print('Song removed')
                return
            elif self.head==self.tail: # head is same as tail
                self.removeLastSong()
                return
            current=current.next
        print(f'Song "{title}" not found')

    def removeLastSong(self):
        '''Reassigns and modifies tail pointer to remove last value from linked list'''
        if self.tail is None and self.head is None:
            print("Playlist is empty")
            return
        elif self.tail is None and self.head is not None:
            self.head=None
            print('Song removed')
            return
        elif self.head==self.tail:
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
        while current:
            print(current)
            current=current.next

    def countSongs(self):
        '''Iterates through linked list and counts number of nodes'''
        counter=0
        if self.isEmpty():
            print(f'Number of songs: {counter}')
            return
        
        current=self.head
        while current:
            counter+=1
            current=current.next

        print(f'Number of songs: {counter}')

    def findSong(self,title):
        '''Searches through linked list for specific title'''
        current=self.head
        while current:
            if current.title==title:
                return current
            current=current.next
        return False

    def reversePlaylist(self):
        '''Reverses playlist in place'''
        if self.isEmpty():
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
        print('playlist reversed')

    '''------------------------ Advanced Features ------------------------'''

    ''' Play Mode '''
    def playCurrent(self):
        '''Prints details for current song playing'''
        if self.isEmpty():
            print('Playlist is empty')
            return

        if self.currentSong is None:
            self.currentSong=self.head
        print(self.currentSong)
    
    def nextTrack(self):
        '''Advances current track and wraps around when at end of playlist'''
        if self.isEmpty():
            print('Playlist is empty')
            return
        
        if self.currentSong is None:
            self.currentSong=self.head
        
        if self.tail.artist==self.currentSong.artist and self.tail.title==self.currentSong.title:
            self.currentSong=self.head
        else:
            self.currentSong=self.currentSong.next
    
    def previousTrack(self):
        '''decrements track and wraps around when at the beginning'''
        if self.isEmpty():
            print('Playlist is empty')
            return
        
        if self.currentSong is None:
            self.currentSong=self.head

        if self.head.artist==self.currentSong.artist and self.head.title==self.currentSong.title:
            self.currentSong=self.tail
        else:
            self.currentSong=self.currentSong.prev

    ''' Playlist Saving '''

    def saveToFile(self,filename):
        '''Writes all playlist songs data to a csv file'''
        if self.isEmpty():
            print('Playlist is empty')
            return
        
        filename=filename+'.csv'
        with open(filename, mode='w',newline='',encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Artist', 'Duration'])
            current=self.head
            while current:
                writer.writerow([current.title,current.artist,current.duration])
                current=current.next

    def loadFromFile(self,filename):
        '''Reads all playlist song data from file'''
        filename=filename+'.csv'
        self.clearCurrentPlaylist()
        try:
            with open(filename,mode='r',encoding='utf-8') as file:
                reader=csv.DictReader(file)
                for row in reader:
                    self.addSongAtEnd(row['Title'],row['Artist'],int(row['Duration']))
            print('Playlist loaded')
        except:
            print(f'File {filename[:-4]} not found')

    ''' Extra for playlist file management'''

    def deletePlaylist(self,filename):
        '''Erases playlist csv file from storage'''
        filename=filename+'.csv'
        try:
            os.remove(filename)
            print(f'Playlist {filename[:-4]} deleted')
        except:
            print(f"Playlist {filename[:-4]} does not exist")

    ''' Extra for testing and QOL'''
    
    def clearCurrentPlaylist(self):
        '''Empties playlist of song data'''
        if self.isEmpty():
            print('Playlist is empty, no songs cleared')
            return
        
        self.head=None
        self.tail=None
        self.currentSong=None
        print('Cleared playlist')