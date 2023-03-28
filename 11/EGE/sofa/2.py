for x in range (2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f= (not(not w or not(not x or y))) and (x or((not y)==z))
                print(x,y,z,w, end='  ')
                print(f)