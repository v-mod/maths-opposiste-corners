rootnum=1
linenum=0
endrootnum=8
while True:
    for x in range(int(str(linenum)+str(rootnum)),int(str(linenum)+str(endrootnum))):
        print(int(str(linenum)+str(rootnum)))
        print(int(str(linenum)+str(endrootnum)))
        topleft=rootnum
        topright=rootnum+2
        botleft=rootnum+10
        botright=rootnum+12
        bckdg=topleft*botright
        fwddg=topright*botleft
        if bckdg > fwddg:
            dif=bckdg-fwddg
        elif bckdg < fwddg:
            dif=fwddg-bckdg
        print('Constructed Rectangle: ')
        print(str(topleft)+'    '+str(topright))
        print(str(botleft)+'    '+str(botright))
        print(str(bckdg)+' - '+str(fwddg)+' = '+str(dif))
        rootnum=rootnum+1
    linenum=linenum+1