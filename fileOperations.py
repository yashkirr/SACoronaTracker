"""
Author: Yashkir Ramsamy
Contact: me@yashkir.co.za
Date: 2020/07/13

Purpose: Managing File I/O
"""
import pickle

class File:
    def __init__(self,file):
        self.file = file
        f = open(self.file, "w")
        f.close()

    def writeToFile(self,object):
        f = open(self.file,'wb')
        pickle.dump(object,f)
        f.close()
        print("Saved hash")

    def readFromFile(self):
        f = open(self.file,'rb')
        object = pickle.load(f)
        f.close()
        return object