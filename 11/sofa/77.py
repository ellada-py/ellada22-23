print('     1   2   3   4   5   6   7   8   9  10')
for i in range(1,11):
    if i%10:
        print(' '+str(i), end='')
    else:
        print(str(i), end='')
    for j in range(1,11):
        if j%10:
            if i*j>9:
                print('  '+str(i*j), end='')
            else:
                print('   '+str(i*j), end='')
        else:
            if i*j<100:
                print('  '+str(j*i))
            else:
                print(' '+str(j*i))