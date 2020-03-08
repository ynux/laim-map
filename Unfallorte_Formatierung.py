import pyproj
P = pyproj.Proj(proj='utm', zone="32N", ellps='WGS84', preserve_units=True)
with open("init.txt","r") as init:
    for zeile in init:
        while zeile[-1]=="\r" or zeile[-1]=="\n":zeile=zeile[:-1]
        print(zeile)
        try:
            with open("Unfallorte"+zeile+"_LinRef.txt","r") as data_in:
                with open("Unfallorte"+zeile+"_LinRef.csv","w") as data_out:
                    line = data_in.readline()
                    n=1
                    for c in line[:-1]:
                        if c==";":n+=1
                        data_out.write(c)
                        continue
                    data_out.write(";lat;lon\n")
                    for line in data_in:
                        l=["",""]
                        n1=n
                        for c in line:
                            if c=="\n": continue
                            if c==";": n1-=1
                            elif n1<=2:
                                if c==",": c="."
                                l[2-n1]+=c
                            data_out.write(c)
                        l[0]=float(l[0])
                        l[1]=float(l[1])
                        l=list(P(l[0],l[1],inverse=True))
                        data_out.write(";"+str(l[0])+"E;"+str(l[1])+"N\n")
        except FileNotFoundError:
            print("Unfallorte"+zeile+"_LinRef.txt existiert nicht")
