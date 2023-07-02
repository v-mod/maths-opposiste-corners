# X is width
# Y is height

startrootnum=1
linenum=0
x=input('x: ')
y=input('y: ')
endrootnum=10-(x-1)
while True:
    for l in range(int(str(linenum)+str(startrootnum)),int(str(linenum)+str(endrootnum))):
        topleft=rootnum
        topright=rootnum+(x-1)
        botleft=rootnum+10*(y-1)
        botright=rootnum+(x-1)+(10*(y-1))
        bckdg=topleft*botright
        fwddg=topright*botleft
        dif=bckdg-fwddg
        print('Constructed Rectangle: ')
        print(str(topleft)+'    '+str(topright))
        print(str(botleft)+'    '+str(botright))
        print(str(bckdg)+' - '+str(fwddg)+' = '+str(dif))
        rootnum=rootnum+1
    linenum=linenum+1