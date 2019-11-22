def search_for_string(alist, string):
    newlist = []
    for i in range(len(alist)):
        if alist[i] == string:
            newlist.append(i)
    return newlist
