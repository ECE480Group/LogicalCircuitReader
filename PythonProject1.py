def main():
    while True:
        try:
            filename = input("Enter a filename: ").strip()
            infile = open(filename, "r") # Open the file
            break
        except IOError:
            print("File " + filename + " does not exist. Try again")

    infile.

    #no you SUCKA

    infile.close() # Close file
