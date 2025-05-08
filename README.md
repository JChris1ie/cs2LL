# CS2 LinkListify Final Project

Jeb Christie

This project was to simulate a basic music player using a doubly linked list. The features include adding/removing songs from a playlist, reversing the playlist, simulated playing and skipping through the playlist, and playlist save/load/deletion functionality.

To use this program, run the code and enter the number of the action that you want to do as prompted, and follow further prompts to add information as needed.

## Division of work
All coding was done by me!

## Advanced features
The advanced features implemented were play mode and playlist save and load features. 

### Play mode
#### Prompt for first LLM usage:
"How can i wrap around from the beginning of a doubly linked list to the end in python without assigning the head's previous pointer or tail's next pointer"

Helped me to come to the idea of checking each current track's title and artist against the tail or head pointer for wrapping around from the back or front. I was planning to turn the doubly linked list into a circular one just for the duration of the function and then change the continuation pointers of the head and tail back to "None," but not modifying those in the first place seems to be a little simpler.

### Playlist save and load
#### Prompt used for second LLM usage:
"how can i save a python linked list of song objects with title, artist,
duration attributes to a csv file and load those objects from the csv to a linked list again"

Helped me to use the csv module in python. Without using this prompt, I would have just put in each entry by writing the data in a file normally and just mimicing the csv format, but the csv module made that process easier with the csv reader and writer as well as the writerow and read functions. 

## Extras

Added playlist clear and deletion functions for QOL. Clear function clears current playlist, and deletion function deletes a playlist file from storage.