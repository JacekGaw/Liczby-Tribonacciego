n = input()
var = {}

def var_spr(var):
    if(var == 0):
        print(f"{var}\tTAK")
    elif(var == 1)
        print(f"{var}\tTAK")
    elif(var == 2)

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

