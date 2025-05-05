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
print('0. Exit')

while True:
    user=input('Choose an option: ')
    match user:
        case '0':
            break
        case '1':
            myPlaylist.addSongAtEnd(input('Enter song title: '),input('Enter song artist: '))
        case '2':
            myPlaylist.addSongAtBeginning(input('Enter song title: '),input('Enter song artist: '))
        case '3':
            myPlaylist.removeSongByTitle(input('Enter song title: '))
        case '4':
            myPlaylist.removeLastSong()
        case '5':
            myPlaylist.display_playlist()
        case '6':
            myPlaylist.countSongs()
        case '7':
            output=myPlaylist.findSong(input('Enter song title: '))
            if output:
                print('Song found')
            else:
                print('Song not found')
        case '8':
            myPlaylist.reversePlaylist()