for x in range (2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (y or (z==w)) and (((not z) or x)==w)==1:
                    print(x,y,z,w)