# cs2LL

# Prompt used for first LLM:
# How can i wrap around from the beginning of a doubly linked list to the end in python without assigning the head's previous pointer or tail's next pointer

# Helped me to come to the idea of checking each current track's title and artist against the tail or head pointer for wrapping around from the back or front. I was planning to turn the doubly linked list into a circular one just for the duration of the function and then change the continuation pointers of the head and tail back to "None," but not modifying those in the first place seems to be a little simpler.