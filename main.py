# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import array as arr
from array import array

import switch as switch


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def readTrainData(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    texAll = []
    lbAll = []
    voc = []
    for line in lines:
        splitted = line.split('\t')
        lbAll.append(splitted[0])
        texAll.append(splitted[1].split())
        words = splitted[1].split()
        for w in words:
            voc.append(w)
    voc = set(voc)
    cat = set(lbAll)
    return texAll, lbAll, voc, cat


# Press the green button in the gutter to run the script.
class Myclass:
    name = ''
    number = 0
    def __init__(self,name,number):
        self.name = name
        self.number = number


class Word:
    name = ''
    total_number = 0
    ship = 0
    money_fx = 0
    acq = 0
    crude = 0
    earn = 0
    grain = 0
    trade = 0
    interest = 0

    def __init__(self, name, total_number):
        self.name = name
        self.total_number = total_number


def find_word_index(name):
    j = 0
    for v in myvoc:
        if v.name == name:
            return j
        j += 1


if __name__ == '__main__':
    texAll1, lbAll1, voc1, cat1 = readTrainData('r8-train-stemmed.txt')
    myclasses = []
    myvoc = []
    for cat in cat1:
        myclasses.append(Myclass(cat, 0))
        print(cat)
    for x in voc1:
        myvoc.append(Word(x, 0))
    i = 0
    for text in texAll1:
        class_name = lbAll1[i]
        print(class_name + " " + str(i))
        for word in text:
            index = find_word_index(word)
            word_class = myvoc[index]
            word_class.total_number += 1
            if class_name == 'ship':
                word_class.ship += 1
            if class_name == 'money-fx':
                word_class.money_fx += 1
            if class_name == 'acq':
                word_class.acq += 1
            if class_name == 'crude':
                word_class.crude += 1
            if class_name == 'earn':
                word_class.money_fx += 1
            if class_name == 'grain':
                word_class.money_fx += 1
            if class_name == 'trade':
                word_class.money_fx += 1
            if class_name == 'interest':
                word_class.money_fx += 1
        i += 1



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
