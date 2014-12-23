
dictionary = ["apple","lenovo","hp","compaq","vaio","dell","toshiba","panasonic"]

def edit_distance(s,t):
    dist = 0
    a = list(s)
    b = list(t)
    while len(a) != len(b):
        if len(a) > len(b):
            if a[0] == b[0]:
                del a[-1]
                dist += 1
            else:
                del a[0]
                dist += 1
        elif a[0] == b[0]:
            del b[-1]
            dist += 1
        else:
            del b[0]
            dist += 1
    for i in range(len(a)):
        if a[i] != b[i]:
            a[i] = b[i]
            dist += 1
    return dist


x=raw_input("Enter an incorrect word: ")



count=min(edit_distance(x,dictionary[i]) for i in range(8))

for i in range(8):
    if(edit_distance(x,dictionary[i])==count):
       print dictionary[i]
       break

       

  

    
