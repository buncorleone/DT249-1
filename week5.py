"""ABC notation is a shorthand form of musical notation. In basic form it uses the letters A through G to represent the
given notes, with other elements used to place added value on these - sharp, flat, the length of the note, key,
ornamentation. Later, with computers becoming a major means of communication, others saw the possibilities of using
this form of notation as an ASCII code that could facilitate the sharing of music online, also adding a new and simple
language for software developers. In this later form it remains a language for notating music using the ASCII character
set.

Write a program to read the attached file and print the Id, title (one only), time and key signatures line by line.

    Each tune consists of headers + notation. The headers start with a character followed by a : (colon)
    The notation follows the headers.
    Each tune begins with the X: - This is also the index field.
    Titles begin with T:
    A tune can have multiple titles, but we are only interested in the first one. If there are more, we just ignore the
    rest
    The time signature is stored in the M: line
    The key signature is stored in he K: line
    You can ignore the notation, we are just interested in the headers

Below is an example of the sort of output the program should produce:

195 ... Road to Lisdoonvarna, The ... Time sig: C| ... Key sig: D ...
196 ... Jenny's Wedding ... Time sig: C| ... Key sig: D ...
197 ... Dark Girl in Blue, The ... Time sig: C| ... Key sig: D ...
198 ... Knotted Cord, The ... Time sig: C| ... Key sig: Ador ...
199 ... Lucy's Tune ... Time sig: C| ... Key sig: Em ...
200 ... Banks of the Liffey, The ... Time sig: C| ... Key sig: G ...
-------------------------------
There are 100 tunes in the file
-------------------------------

For the really ambitious: See if you can get your computer to play a tune from the file."""


# Open the file Music.abc as the string variable raw_data
# Initialise each of the variables, including temp_title which is used to skip the additional titles

with open("Music.abc", "r") as raw_data:
    song_index = int()
    title = ""
    temp_title = ""
    key_sig = ""
    time_sig = ""
    song_line = ""
    # Read each line in the file and check for the characters which denote each piece of information we require
    # Store the information as a variable and add it to the song_line
    # Once we find a new song (by detecting the line contains X:), wipe out the temp_title variable
    for line in raw_data:
        if "X:" in line:
            temp_title = ""
            song_index = line[2:-1:]
            song_line += (song_index + "...")
        elif "T:" in line:
            # Check if T: already exists in our temp_title variable, meaning we have already captured the title for this
            # song. If found, continue out of the loop (skipping the else statement on line 58)
            if "T:" in temp_title:
                continue
            else:
                # If T: was not found in the temp_title, then capture it in temp_title as is and in title with the
                # correct formatting
                temp_title = line
                title = line[2:-1:]
                song_line += (title + "...")
        elif "M:" in line:
            key_sig = line[2:-1:]
            song_line += ("Key Sig: " + key_sig + "...")
        elif "K:" in line:
            time_sig = line[2::]
            song_line += ("Time Sig: " + time_sig)
    print(song_line)
