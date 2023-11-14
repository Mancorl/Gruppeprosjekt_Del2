def finn_differanse(liste):
    diff = list()
    for i in range(len(liste[:-1])):
        diff.append(liste[i+1] - liste[i])
    return diff
