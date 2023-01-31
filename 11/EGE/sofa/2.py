for x in range (2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f= x and ((not y) or z) and (y or ((not z)==w))
                print(x,y,z,w, end='  ')
                print(f)