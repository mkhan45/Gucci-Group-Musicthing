from input import read_from_mp3_folder

path = input("What is the path of the folder?\n")
database = read_from_mp3_folder(path)

filename = input("What should the file be called?\n")
pickle.dump(dictionary, filename)
