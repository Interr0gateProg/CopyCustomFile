import os

class Visitor():
    def __init__(self, fromDir):
        self.dir = fromDir
    def run(self):
        for (thisDir, dirsHere, filesHere) in os.walk(self.dir):
            self.visitdir(thisDir)
            for file in filesHere:
                pfile = os.path.join(thisDir, file)
                self.visitfile(pfile)
    def visitdir(self):
        pass
    def visitfile(self):
        pass



class CopyCustomFile(Visitor):
    def __init__(self, fromDir, toDir, endswith):
        Visitor.__init__(self, fromDir)
        self.toDir = toDir
        self.endswith = endswith
        self.fromDirLen = len(fromDir) + 1
        self.chunk = 1024 * 1000
    def visitdir(self, dirpath):
        pathdir = os.path.join(self.toDir, dirpath[self.fromDirLen:])
        try:
            os.mkdir(pathdir)
        except FileExistsError:
            print('File alive')
    def visitfile(self, dirfile):
        filedir = os.path.join(self.toDir, dirfile[self.fromDirLen:])
        if filedir.endswith(self.endswith):
            self.copyfile(dirfile, filedir)
    def copyfile(self, fromDir, toDir):
        with open(fromDir, 'rb') as F:
            with open(toDir, 'wb') as T:
                while True:
                    readchunk = F.read(self.chunk)
                    if not readchunk: break
                    T.write(readchunk)

if __name__ == '__main__':
    C = CopyCustomFile('C:/Users/SKY4/PycharmProjects', 'C:/Users/SKY4/Heheboi', '.py')
    C.run()