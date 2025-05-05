import playlist

myPlaylist=playlist.Playlist()

print('--- LinkListify Playlist Manager ---')
print('1. Add song to End')
print('2. Add song to Beginning')
print('3. Remove song by title')
print('4. Remove last song')
print('5. Display playlist')
print('6. Count songs')
print('7. Find song by title')
print('8. Reverse Playlist')
print('9. Play current song')
print('10. Skip to next song')
print('11. Skip to previous song')
print('0. Exit')
print()

while True:
    user=input('Choose an option: ')
    match user:
        case '0':
            break
        case '1':
            myPlaylist.addSongAtEnd(input('Enter song title: '),input('Enter song artist: '))
            print('Song added')
            print()
        case '2':
            myPlaylist.addSongAtBeginning(input('Enter song title: '),input('Enter song artist: '))
            print('Song added')
            print()
        case '3':
            myPlaylist.removeSongByTitle(input('Enter song title: '))
            print('Song removed')
            print()
        case '4':
            myPlaylist.removeLastSong()
            print('Song removed')
            print()
        case '5':
            myPlaylist.display_playlist()
            print()
        case '6':
            myPlaylist.countSongs()
            print()
        case '7':
            output=myPlaylist.findSong(input('Enter song title: '))
            if output:
                print('Song found')
            else:
                print('Song not found')
            print()
        case '8':
            myPlaylist.reversePlaylist()
            print('playlist reversed')
            print()
        case '9':
            myPlaylist.playCurrent()
            print()
        case '10':
            myPlaylist.nextTrack()
            myPlaylist.playCurrent()
            print()
        case '11':
            myPlaylist.previousTrack()
            myPlaylist.playCurrent()
            print()
        case '22':
            myPlaylist.testReverse()    
        case _:
            print("Enter a number")
            print()