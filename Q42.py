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

def hash_spam(string):
    check=count_hashtag(string)
    if check>4:
        print("This tweet willbe considered as a spam!")
    else:
        print(check)

count_hashtag("this #is #a #test# to see #if the function works")
