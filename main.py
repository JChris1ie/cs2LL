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
print('12. Save current playlist')
print('13. Load playlist by name')
print('14. Delete playlist from storage')
print('15. Clear current playlist')
print('0. Exit')
print()

while True:
    user=input('Choose an option: ')
    match user: # case switch used for all input cases
        case '0':
            print("Thank you for using this program.")
            print()
            break
        case '1':
            myPlaylist.addSongAtEnd(input('Enter song title: '),input('Enter song artist: '),input('Enter length in seconds: '))
            print('Song added')
            print()
        case '2':
            myPlaylist.addSongAtBeginning(input('Enter song title: '),input('Enter song artist: '),input('Enter length in seconds: '))
            print('Song added')
            print()
        case '3':
            myPlaylist.removeSongByTitle(input('Enter song title to remove: '))
            print()
        case '4':
            myPlaylist.removeLastSong()
            print()
        case '5':
            myPlaylist.display_playlist()
            print()
        case '6':
            myPlaylist.countSongs()
            print()
        case '7':
            output=myPlaylist.findSong(input('Enter song title to find: '))
            if output:
                print(f'Song found: {output}')
            else:
                print('Song not found')
            print()
        case '8':
            myPlaylist.reversePlaylist()
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
        case '12':
            myPlaylist.saveToFile(input('Enter playlist name to save as: '))
            print('Playlist saved')
            print()
        case '13':
            myPlaylist.loadFromFile(input('Enter playlist name to load: '))
            print()
        case '14':
            myPlaylist.deletePlaylist(input('Enter playlist name to delete: '))
            print()
        case '15':
            myPlaylist.clearCurrentPlaylist()
            print()
        case _: # catchall case for anything that is not a case
            print("ERROR: please enter a number")
            print()