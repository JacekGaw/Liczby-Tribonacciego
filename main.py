n = input()
var = {}
ciag = {}
ciag[0] = 0
ciag[1] = 1
ciag[2] = 2

def var_count(var):
    result = 0
    i = 3
    found = 0
    while result < var:
        result = ciag[i-1] + ciag[i-2] + ciag[i-3]
        ciag[i] = result
        i += 1
    for x in range(3, len(ciag)):
        if(var == ciag[x]):
            print(f"{var}\tTAK")
            found = 1
            break
        else:
            found = 0
    if(found == 0):
        print(f"{var}\tNIE")


def var_spr(var):
    if(var == 0):
        print(f"{var}\tTAK")
    elif(var == 1):
        print(f"{var}\tTAK")
    elif(var == 2):
        print(f"{var}\tTAK")
    else:
        var_count(var)

if(n.isdigit()):
    n = int(n)
    if(n < 0):
        print("BLAD")
    else:
        for i in range(0, n):
            var[i] = input()
        for i in range(0, n):
            if(var[i].isdigit()):
                var[i] = int(var[i])
                if(var[i] < 0):
                    print("BLAD")
                else:
                    var_spr(var[i])
            else:
                print("BLAD")
else:
    print("BLAD")