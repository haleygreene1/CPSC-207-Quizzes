def count_hashtag(string):
    total= 0
    index=0
    while index < len (string):
        if string[index:index+ 1] == "#":
            total += 1
            index += 1
        else:
            index += 1
    return total

