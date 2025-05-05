import playlist

myPlaylist=playlist.Playlist()

myPlaylist.addSongAtEnd('Time','Pink Floyd')
myPlaylist.addSongAtEnd('Money','Pink Floyd')
myPlaylist.addSongAtBeginning('Limelight','Rush')
myPlaylist.display_playlist()

print()
myPlaylist.reversePlaylist()
myPlaylist.countSongs()
myPlaylist.display_playlist()