import os

class DirectoryPrint:

    def __init__(self):
        self.sublevel = 0
        self.HORIZONTAL_LINE = chr(9474)
        self.VERTICAL_LINE = chr(9472)
        self.EDGE = chr(9492)
        self.T_LINE = chr(9500)

    def print_directory(self, path, indentation_level):
        counter = self.countFilesAndFolders(path)
        list = os.scandir(path)
        sortedList = sorted(list, key=lambda entry: entry.name.lower())
        nfiles = 0
        ndirectories = 0

        for entry in sortedList:
            counter -= 1
            if entry.is_dir():
                ndirectories += 1
                if indentation_level > self.sublevel:
                    self.printText(entry, self.sublevel, counter)
                    self.sublevel += 1
                    values = self.print_directory(entry, indentation_level)
                    nfiles += values[1]
                    ndirectories += values[0]

                else:

                    self.printText(entry, self.sublevel, counter)
            else:
                nfiles += 1
                self.printText(entry, self.sublevel, counter)
        self.sublevel -= 1
        return ndirectories, nfiles

    def printText(self, entry, level, counter):

        indent = " " * 3 * level
        entryText = self.VERTICAL_LINE + " " + entry.name

        if counter != 0:
            if level != 0:
                print(self.HORIZONTAL_LINE + indent + self.T_LINE + entryText)
            else:
                print(indent + self.T_LINE + entryText)
        else:
            if level != 0:
                print(self.HORIZONTAL_LINE + indent + self.EDGE + entryText)
            else:
                print(indent + self.EDGE + entryText)

    def countFilesAndFolders(self, path):
        list = os.scandir(path)
        counter = 0
        for entry in list:
            counter += 1
        return counter



path1 = DirectoryPrint()
print(path1.print_directory(".", 3))