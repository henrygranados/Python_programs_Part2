def main():
    
    artistsList = load_artists("artists.txt")
    print (len(artistsList))
    artistName = input('What is the name of the artist? ')
    print (artist_count(artistName , artistsList))

#This fuction loads the artists.txt file and stores name of artists in a list
def load_artists(filename):
    
    with open(filename) as f:
        myList = f.read().splitlines()
    return myList

#This function checks how many times an artist shows in artists.txt file
def artist_count(artistName , artistsList):
    return int(artistsList.count(artistName))
    
main()
