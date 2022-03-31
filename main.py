import numpy as np


def main():
    tex_all, lb_all, voc, cat = read_train_data(r"data\r8-train-stemmed.txt")
    pw, p = learn_nb_text()
    suc = classify_nb_text(pw, p)
    print(suc)


def classify_nb_text(pw, p):
    pass


def learn_nb_text():
    pass


def read_train_data(file_name):
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


if __name__ == '__main__':
    main()
