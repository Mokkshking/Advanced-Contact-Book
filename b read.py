
# read
import pickle

afile = open(r"addressbook.dat","rb")
while True:
    x=pickle.load(afile)
    print(x)


afile.close()



