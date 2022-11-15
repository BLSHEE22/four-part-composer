import random
import math
import sys

# GLOBAL list of melodies
mels = []

melRests = []
melHolds = []
melPassTones = []
fullMel = ""
bass = ""
tenor = ""
alto = ""
majScales = {0:{0:"c",1:"des",2:"d",3:"ees",4:"e",5:"f",6:"fis",7:"g",8:"aes",9:"a",10:"bes",11:"b"},
                1:{0:"c",1:"des",2:"d",3:"ees",4:"e",5:"f",6:"ges",7:"g",8:"aes",9:"a",10:"bes",11:"b"},
                2:{0:"c",1:"cis",2:"d",3:"dis",4:"e",5:"f",6:"fis",7:"g",8:"gis",9:"a",10:"ais",11:"b"},
                3:{0:"c",1:"des",2:"d",3:"ees",4:"e",5:"f",6:"fis",7:"g",8:"aes",9:"a",10:"bes",11:"b"},
                4:{0:"c",1:"cis",2:"d",3:"dis",4:"e",5:"f",6:"fis",7:"g",8:"gis",9:"a",10:"ais",11:"b"},
                5:{0:"c",1:"des",2:"d",3:"ees",4:"e",5:"f",6:"ges",7:"g",8:"aes",9:"a",10:"bes",11:"b"},
                6:{0:"c",1:"cis",2:"d",3:"dis",4:"e",5:"eis",6:"fis",7:"g",8:"gis",9:"a",10:"ais",11:"b"},
                7:{0:"c",1:"cis",2:"d",3:"dis",4:"e",5:"f",6:"fis",7:"g",8:"gis",9:"a",10:"ais",11:"b"},
                8:{0:"c",1:"des",2:"d",3:"ees",4:"e",5:"f",6:"ges",7:"g",8:"aes",9:"a",10:"bes",11:"b"},
                9:{0:"c",1:"cis",2:"d",3:"dis",4:"e",5:"f",6:"fis",7:"g",8:"gis",9:"a",10:"ais",11:"b"},
                10:{0:"c",1:"des",2:"d",3:"ees",4:"e",5:"f",6:"ges",7:"g",8:"aes",9:"a",10:"bes",11:"b"},
                11:{0:"c",1:"cis",2:"d",3:"dis",4:"e",5:"f",6:"fis",7:"g",8:"gis",9:"a",10:"ais",11:"b"},} 

def main():

    # keep melodies within a set registral range
    def makeMel(offset, scale, starter, length, cad, r, h, p):
        # def makeMel(offset, scale, starter, length, cad, r, rhythmVals):

        # create option to HOLD TONE or ADD PASSING TONES

        # [('b', 11), ('a', 9), ('e', 16), ('d', 14), ('c', 12), ('e', 16), ('b', 11), 
        # ('a', 9), ('a', 21), ('g', 19), ('e', 16), ('d', 14), ('c', 12), ('a', 9), ('f', 5), ('g', -5), ('a', -3)]

        melody = []
        rests = r
        holds = h
        passTones = p
        # numToLetter = {0:"c",1:"cis",2:"d",3:"dis",4:"e",5:"f",6:"fis",7:"g",8:"gis",9:"a",10:"ais",11:"b"}
        #maj = [0,2,4,5,7,9,11,12]
        maj = [0,1,2,3,4,5,6,7,8,9,10,11,12]
        goLeap = False
        justLeaped = (False, 0)
        lastDir = 2
        consecDir = 1
        nonLeaps = [[[2,2,4],[-1,-1,-3]],[[1],[-3]],[[2,2,3],[-2,-2,-3]],[[1],[-3]],[[1,3],[-2,-2,-4]],[[2,4],[-1,-1,-3]],[[1],[-4]],[[2,4],[-2,-2,-3]],[[2],[-1]],[[2,3],[-2,-2,-4]],[[1,2],[-3]],[[1,3],[-2,-2,-4]]] # legal nonLeaps from every scale degree
        leaps = [[[5,7,9,11,12],[-5,-7,-8]],[[5,7,9,11,12],[-5,-7,-8]],[[5,7,9,10,12],[-5,-7,-9]],[[5,7,9,10,12],[-5,-7,-9]],[[5,7,8,10,12],[-5,-7,-9]],[[7,9,11,12],[-5,-6,-8]],[[6],[-6]],[[5,7,9,10,12],[-5,-7,-8]],[[5,7,9,10,12],[-5,-7,-8]],[[5,7,8,10,12],[-5,-7,-9]],[[5,7,8,10,12],[-5,-7,-9]],[[6,8,10,12],[-6,-7,-9]]] # legal leaps from every scale degree
        dom = [2,7,11]
        preDom = [0,2,5,9]

        # starter = maj[random.randrange(0, len(maj)-1)]
        for x in starter:
            melody.append(x)
    
        #print("Melody pre-offset: " + str(melody))
        # melody.append((starter, starter))
        if not rests:
            rests.append(False)
        if not holds:
            holds.append(False)
        if not passTones:
            passTones.append(False)

        # print(melody)
        '''
        if cad == "end1":
            for i in range(10):
                print()
            #print("*********")
            #print()
        '''

        # 50/50 up or down, never move by 0
        # leaps occur 30% of the time and are always following by a non-leap in the opposite direction of the leap
        i = 1
        while i < length:
            # 0 up, 1 down
            newNote = 0

            # if 0, set restApp to True
            rest = random.randrange(0,5)
            uOrD = random.randrange(0,2)
            #print("consecDir: " + str(consecDir))
            #print("lastDir: " + str(lastDir))
            #print("uOrD: " + str(uOrD))
            #print()
            if uOrD == lastDir:
                consecDir += 1
            else:
                consecDir = 1
            if consecDir > 5:
                #print("TOO MANY CONSECUTIVE SAME-DIRECTION MOVES")
                if uOrD == 0:
                    uOrD = 1
                else:
                    uOrD = 0
            lastDir = uOrD
            #print("consecDir: " + str(consecDir))
            #print("lastDir: " + str(lastDir))
            #print("uOrD: " + str(uOrD))
            #print()

            # if 0 or 1, leap!
            l = random.randrange(0, 11)

            # this will become outmoted
            ptOrHold = random.randrange(0,5) 

            # RHYTHMVAL METHOD
            #rhythmVal = rhythmVals[random.randrange(0,len(rhythmVals))]
            #print("rhythmVals: " + str(rhythmVals))
            #print("rhythmVal: " + str(rhythmVal))

            # outmoted
            #ptOrHold = random.randrange(4,10)
            #ptOrHold = 1
            #ptOrHold = 4

            penOrUlt = False
            restApp = False
            holdApp = False
            passApp = False
            emerg8 = False
            #print("melody: " + str([x[1] for x in melody]))
            #print(holds)
            #print(passTones)
            #print("i: {0:4s} length: {1:4s} {2:10s}> ".format(str(i),str(length),cad),end="")
            if cad == "half":
                if i == length-2:
                    # if rhythmVal == 2:
                    if ptOrHold == 4:
                        toDom = melody[i-1][0]%12-dom[random.randrange(0, len(dom))]
                        newNote = melody[i-1][1] - toDom
                        length -= 1
                        holdApp = True
                        # DOMINANT
                        newNote = 7
                    else:
                        toPreDom = melody[i-1][0]%12-preDom[random.randrange(0, len(preDom))]
                        newNote = melody[i-1][1] - toPreDom
                        # PREDOMINANT
                        if newNote > 9:
                            newNote = 9
                        if newNote < 2:
                            newNote = 2
                    penOrUlt = True
                    #print("newNote: " + str(newNote))
                    #print("offset: " + str(offset))

                elif i == length-1:
                    toFive = melody[i-1][0]%12-7
                    newNote = melody[i-1][1] - toFive
                    penOrUlt = True
                    #print("newNote: " + str(newNote))
                    #print("offset: " + str(offset))

                    # DOMINANT
                    newNote = 7
                
                # CLOSEST REGISTER
                if melody[-1][1] - newNote > 6:
                    newNote += 12
                if newNote - melody[-1][1] > 6:
                    newNote -= 12
                    
            elif cad == "authentic":
                if length % 1 != 0:
                    #print("APPEND EMERGENCY EIGHTH NOTE")
                    pUorD = random.randrange(0,2)
                    #print(pUorD)
                    nonLeap = nonLeaps[maj.index(melody[i-1][0]%12)][pUorD][random.randrange(0, len(nonLeaps[maj.index(melody[i-1][0]%12)][pUorD]))]
                    #print("NonLeap: " + str(nonLeap))    
                    newNote = melody[i-1][1] + nonLeap
                    passTones.append(True)
                    rests.append(False)
                    holds.append(False)
                    passApp = True
                    #print("PASSING TONE ADDED")
                    #print("Two eighth notes")

                    # CLOSEST REGISTER
                    if melody[-1][1] - newNote > 6:
                        newNote += 12
                    if newNote - melody[-1][1] > 6:
                        newNote -= 12

                    melody.append((newNote%12, newNote))
                    # DON'T INCREMENT
                    #i += 1
                    emerg8 = True
                    penOrUlt = True
                elif i == length-3:
                    toPreDom = melody[i-1][0]%12-preDom[random.randrange(0, len(preDom))]
                    newNote = melody[i-1][1] - toPreDom
                    penOrUlt = True
                    #print("newNote: " + str(newNote))
                    #print("offset: " + str(offset))

                    # PREDOMINANT
                    newNote = preDom[random.randrange(1, len(preDom))]
                elif i == length-2:
                    toLT = melody[i-1][0]%12-11
                    newNote = melody[i-1][1] - toLT                        
                    penOrUlt = True
                    #print("newNote: " + str(newNote))
                    #print("offset: " + str(offset))

                    # LEADING TONE
                    newNote = 11
                elif i == length-1:
                    toTon = melody[i-1][0]%12
                    newNote = melody[i-1][1] - toTon
                    penOrUlt = True
                    #print("newNote: " + str(newNote))
                    #print("offset: " + str(offset))

                    # TONIC
                    newNote = 12
                #print(melody[-1][1])
                #print(newNote)
                # CLOSEST REGISTER
                if melody[-1][1] - newNote > 6:
                    newNote += 12
                if newNote - melody[-1][1] > 6:
                    newNote -= 12

            elif cad == "retran": 
                if i == length-2:
                    # if rhythmVal == 2:
                    if ptOrHold == 4:
                        length -= 1
                        holdApp = True
                        #"Hold chosen!")

                        # TONIC (in V)
                        newNote = 0

                    else:

                        # PITCH IN DOMINANT TRIAD (in V)
                        retDom = [-5,-1,2,7]
                        newNote = retDom[random.randrange(0, len(retDom))]

                    #newNote = melody[i-1][1] - toTon
                    penOrUlt = True
                    #print("newNote: " + str(newNote))
                    #print("offset: " + str(offset))

                elif i == length-1:
                    toTon = melody[i-1][0]%12
                    newNote = melody[i-1][1] - toTon
                    penOrUlt = True
                    #print("newNote: " + str(newNote))
                    #print("offset: " + str(offset))

                    # TONIC (in V)
                    newNote = 0
                
                # CLOSEST REGISTER
                if melody[-1][1] - newNote > 6:
                    newNote += 12
                if newNote - melody[-1][1] > 6:
                    newNote -= 12

            elif cad == "end1":
                if length % 1 != 0:
                    #print("APPEND EMERGENCY EIGHTH NOTE")
                    pUorD = random.randrange(0,2)
                    #print(pUorD)
                    nonLeap = nonLeaps[maj.index(melody[i-1][0]%12)][pUorD][random.randrange(0, len(nonLeaps[maj.index(melody[i-1][0]%12)][pUorD]))]
                    #print("NonLeap: " + str(nonLeap))    
                    newNote = melody[i-1][1] + nonLeap
                    passTones.append(True)
                    rests.append(False)
                    holds.append(False)
                    passApp = True
                    #print("PASSING TONE ADDED")
                    #print("Two eighth notes")
                    melody.append((newNote%12, newNote))
                    # DON'T INCREMENT
                    #i += 1
                    emerg8 = True
                    penOrUlt = True                
                    
                elif i == length-4:
                    pDom = [-3,0,2,5]
                    # if rhythmVal == 0.5:
                    if ptOrHold == 0:
                        newNote = pDom[random.randrange(0, len(pDom))]
                        passTones.append(True)
                        rests.append(False)
                        holds.append(False)
                        passApp = True
                        #print("PASSING TONE ADDED")
                        #print("Two eighth notes")
                        melody.append((newNote%12, newNote))
                        i += 1
                        length += 1
                        pUorD = random.randrange(0,2)
                        #print(pUorD)
                        nonLeap = nonLeaps[maj.index(melody[i-1][0]%12)][pUorD][random.randrange(0, len(nonLeaps[maj.index(melody[i-1][0]%12)][pUorD]))]
                        #print("NonLeap: " + str(nonLeap))    
                        newNote = melody[i-1][1] + nonLeap
                    # elif rhythmVal == 2:
                    elif ptOrHold == 4:
                        #print("Hold chosen!")
                        toPreDom = melody[i-1][0]%12-preDom[random.randrange(0, len(preDom))]
                        newNote = melody[i-1][1] - toPreDom

                        # DOMINANT
                        newNote = -1
                        length -= 1
                        holdApp = True
                    else:
                        toPreDom = melody[i-1][0]%12-preDom[random.randrange(0, len(preDom))]
                        newNote = melody[i-1][1] - toPreDom
                        #print("Quarter note")

                        # PREDOMINANT
                        newNote = pDom[random.randrange(0, len(pDom))]

                    #print("newNote: " + str(newNote))
                    #print("offset: " + str(offset))
                    penOrUlt = True
                elif i == length-3:
                    pDom = [-3,0,2,5]
                    # if rhythmVal == 0.5:
                    if ptOrHold == 0:
                        newNote = pDom[random.randrange(0, len(pDom))]
                        passTones.append(True)
                        rests.append(False)
                        holds.append(False)
                        passApp = True
                        #print("PASSING TONE ADDED")
                        #print("Two eighth notes")
                        melody.append((newNote%12, newNote))
                        i += 1
                        length += 1
                        pUorD = random.randrange(0,2)
                        #print(pUorD)
                        nonLeap = nonLeaps[maj.index(melody[i-1][0]%12)][pUorD][random.randrange(0, len(nonLeaps[maj.index(melody[i-1][0]%12)][pUorD]))]
                        #print("NonLeap: " + str(nonLeap))    
                        newNote = melody[i-1][1] + nonLeap

                    # elif rhythmVal == 2:
                    elif ptOrHold == 4:
                        #"Hold chosen!")
                        toPreDom = melody[i-1][0]%12-preDom[random.randrange(0, len(preDom))]
                        newNote = melody[i-1][1] - toPreDom

                        # DOMINANT
                        newNote = -1
                        length -= 1
                        holdApp = True
                    else:
                        toPreDom = melody[i-1][0]%12-preDom[random.randrange(0, len(preDom))]
                        newNote = melody[i-1][1] - toPreDom
                        #print("Quarter note")

                        # PREDOMINANT
                        newNote = pDom[random.randrange(0, len(pDom))]

                    #print("newNote: " + str(newNote))
                    #print("offset: " + str(offset))
                    penOrUlt = True
                elif i == length-2:
                    pDom = [-3,0,2,5]
                    # if rhythmVal == 0.5:
                    if ptOrHold == 0:
                        newNote = pDom[random.randrange(0, len(pDom))]
                        passTones.append(True)
                        rests.append(False)
                        holds.append(False)
                        passApp = True
                        #print("PASSING TONE ADDED")
                        #print("Two eighth notes")
                        melody.append((newNote%12, newNote))
                        i += 1
                        length += 1
                        pUorD = random.randrange(0,2)
                        #print(pUorD)
                        nonLeap = nonLeaps[maj.index(melody[i-1][0]%12)][pUorD][random.randrange(0, len(nonLeaps[maj.index(melody[i-1][0]%12)][pUorD]))]
                        #print("NonLeap: " + str(nonLeap))    
                        newNote = melody[i-1][1] + nonLeap

                    # elif rhythmVal == 2:
                    elif ptOrHold == 4:
                        #"Hold chosen!")
                        toDom = melody[i-1][0]%12-dom[random.randrange(0, len(dom))]
                        newNote = melody[i-1][1] - toDom

                        # DOMINANT
                        newNote = -1
                        length -= 1
                        holdApp = True
                    else:
                        toPreDom = melody[i-1][0]%12-preDom[random.randrange(0, len(preDom))]
                        newNote = melody[i-1][1] - toPreDom
                        #print("Quarter note")

                        # PREDOMINANT
                        newNote = pDom[random.randrange(0, len(pDom))]

                    #print("newNote: " + str(newNote))
                    #print("offset: " + str(offset))
                    penOrUlt = True

                elif i == length-1:
                    toLT = melody[i-1][0]%12-11
                    newNote = melody[i-1][1] - toLT
                    #print("Quarter note")
                    penOrUlt = True
                    #print("newNote: " + str(newNote))
                    #print("offset: " + str(offset))

                    # LEADING TONE
                    newNote = -1 

                # CLOSEST REGISTER
                if melody[-1][1] - newNote > 6:
                    newNote += 12
                if newNote - melody[-1][1] > 6:
                    newNote -= 12

            # no holds allowed on the last or fourth-to-last note of the phrase
            # Fixed!!!
            #if i == length-1 or i == length-4:
                #ptOrHold = 1

            # print out rhythmic value
            '''
            if ptOrHold == 0:
                print("Two eighth notes")
            elif ptOrHold == 4:
                print("Hold chosen!")
            elif not holdApp:
                print("Quarter note")
            '''

            # avoid unnecessary massive register shifts
            '''
            if i != length-2 and i != length-1:
                print("old note: " + str(melody[i-1][1]))
                print("new note: " + str(newNote))
                if melody[i-1][1] - newNote < -7:
                    newNote -= 12
                if melody[i-1][1] - newNote > 7:
                    newNote += 12
                print("CHANGING...")
                print("old note: " + str(melody[i-1][1]))
                print("new note: " + str(newNote))
            ''' 

            # print("Prev note: " + str(melody[i-1]))

            if True:
                if not penOrUlt:
                    #if rest == 0:
                        #restApp = True

                    #if rest == 0:
                        #print("REST CHOSEN")
                        #restApp = True 
                        # below three lines make all rests into holds
                        #length -= 1
                        #holdApp = True
                        #print("HOLD CHOSEN")
                    if not justLeaped[0] and l < 2: goLeap = True
                    if goLeap:
                        # if trying to leap down while too low, reverse direction
                        #print("Melody currently: " + str(melody[i-1][1]+offset))
                        #print("Direction trying to leap: " + str(uOrD))
                        if melody[i-1][1]+offset < 3 and uOrD == 1:
                            #print("NOT FINE")
                            uOrD = 0
                        # and vice versa
                        if melody[i-1][1]+offset > 11 and uOrD == 0:
                            #print("NOT FINE")
                            uOrD = 1
                        leap = leaps[maj.index(melody[i-1][0]%12)][uOrD][random.randrange(0,len(leaps[maj.index(melody[i-1][0]%12)][uOrD]))]
                        newNote = melody[i-1][1] + leap
                        #print("Leap: " + str(leap))
                        justLeaped = (True, uOrD)
                        goLeap = False
                    elif justLeaped[0]:
                        oppFromLeap = 1
                        if justLeaped[1] == 1:
                            oppFromLeap = 0
                        #print(oppFromLeap)
                        #temp1 = nonLeaps[maj.index(melody[i-1][0]%12)][oppFromLeap]
                        # randNum = random.randrange(0, len(nonLeaps[maj.index(melody[i-1][0]%12)][oppFromLeap]))
                        # print(temp1)
                        # print(randNum)
                        fillIn = nonLeaps[maj.index(melody[i-1][0]%12)][oppFromLeap][random.randrange(0, len(nonLeaps[maj.index(melody[i-1][0]%12)][oppFromLeap]))]
                        newNote = melody[i-1][1] + fillIn
                        #print("Fill-In: " + str(fillIn))
                        justLeaped = (False, 0)
                    else:
                        nonLeap = nonLeaps[maj.index(melody[i-1][0]%12)][uOrD][random.randrange(0, len(nonLeaps[maj.index(melody[i-1][0]%12)][uOrD]))]
                        #print("NonLeap: " + str(nonLeap))
                        newNote = melody[i-1][1] + nonLeap
                    # if rhythmVal == 0.5:
                    if ptOrHold == 0 and not restApp:
                        passTones.append(True)
                        rests.append(False)
                        holds.append(False)
                        passApp = True
                        #print("PASSING TONE ADDED")
                        melody.append((newNote%12, newNote))
                        i += 1
                        length += 1
                        pUorD = random.randrange(0,2)
                        #print(pUorD)
                        nonLeap = nonLeaps[maj.index(melody[i-1][0]%12)][pUorD][random.randrange(0, len(nonLeaps[maj.index(melody[i-1][0]%12)][pUorD]))]
                        #print("NonLeap: " + str(nonLeap))    
                        newNote = melody[i-1][1] + nonLeap
                    # elif rhythmVal == 2:
                    elif ptOrHold == 4 and not restApp:
                        length -= 1
                        holdApp = True
                        #print("HOLD CHOSEN")
                if not emerg8:
                    melody.append((newNote%12, newNote))
                    rests.append(restApp)
                    holds.append(holdApp)
                    passTones.append(passApp)
                    #rhythmValsPicked.append(rhythmVal)
                    #rests.append(restApp)
                else:
                    i -= 1
                    length -= 0.5
                # print("Rests: " + str(rests))
                #"AFTER")
                #print(" melody: "  + str([x[1] for x in melody]))
                #print(holds)
                #print(passTones)
                #print()
                i += 1

        # print(melody)
        #print(rests)
        #print(holds)
        #print(passTones)
        
        ogMel = [x for x in melody]
        # melody bounds keeper
        #bounds = (18,-11)
        '''
        for i in range(len(ogMel)):
            if i > len(ogMel)-4:
                bounds = (9,-5)
            print("Is " + str(ogMel[i][1]) + " greater than " + str(bounds[0]) + "?")
            if ogMel[i][1] > bounds[0]:
                ogMel[i] = (ogMel[i][0], ogMel[i][1]-12)
                print("YES, lowering to " + str(x) + ".")
            print("Is " + str(ogMel[i][1]) + " less than " + str(bounds[1]) + "?")
            if ogMel[i][1] < bounds[1]:
                ogMel[i] = (ogMel[i][0], ogMel[i][1]+12)
                print("YES, raising to " + str(ogMel[i]) + ".")
        #print("OgMel: " + str(ogMel))
        '''
        melody = [((x[0]+offset)%12,x[1]+offset) for x in ogMel] 
        #print("Melody + offset: " + str(melody))   
        return melToLily(melody, scale, rests, holds, passTones, cad, ogMel)
        # return melToLily(melody, scale, rests, rhythmValsPicked, cad, ogMel)

    # generate the available rhythmic value choices for a melody
    def genRhythmVals():
                
                rhythmVals = []
                vals = [0.5,1,1.5,2,3,4]

                for i in range(7):
                    dieRoll = random.randrange(1,4)
                    for j in range(dieRoll):
                        rhythmVals.append(vals[i])

                return rhythmVals

    # translate melNums to LilyPond code
    def melToLily(mel, sc, r, h, p, cad, ogMel=[]):
        # def melToLily(mel, sc, r, rhythms, cad, ogMel=[]):
        #print("MelToLily: " + str(mel))
        #print("OgMel: " + str(ogMel))
        #print(r)
        #print(h)
        #print(p)
        lilyMelody = []
        i = 0
        while i < len(mel):
            semis = mel[i][1]
            s = ""
            if semis < -12:
                while semis < -12:
                    s += ","
                    semis += 12
                semis = mel[i][1]
            while semis > -1:
                s += "'"
                semis -= 12
            if cad == "end2":
                s += "1"
                #print("MEL: " + str(mel))
                lilyMelody.append(sc[mel[i][0]%12] + s)
                i += 1
                continue
            # rhythmToLily = {0:"4",0.5:"8",1:"4",1.5:"4.",2:"2",3:"2.",4:"1"}
            # if not r[i]:
            #   s += rhythmToLily[rhythms[i]]
            # else:
            #   lilyMelody.append("r" + rhythmToLily[rhythms[i]])
            #   i += 1
            #   continue
            if p[i]:
                #print("RECOGNIZED PASSING TONE!")
                s += "8"
                lilyMelody.append(sc[mel[i][0]%12] + s)
                i += 1
                #lilyMelody.append(sc[mel[i+1][0]%12] + s)
                #i += 2
                continue
            elif r[i]:
                #print("RECOGNIZED REST SYMBOL!!!")
                lilyMelody.append("r4")
                i += 1
                continue
            elif h[i]:
                #print("RECOGNIZED HOLD SYMBOL!!!")
                s += "2"
                lilyMelody.append(sc[mel[i][0]%12] + s)
                i += 1
                continue
            else:
                s += "4"
            lilyMelody.append(sc[mel[i][0]%12] + s)
            i += 1
            # print("LilyMelody: " + str(lilyMelody))

        #print(mel)
        mel = [(sc[x[0]%12], x[1]) for x in mel]
        # print(mel)
        # print()
        retStr = ""
        for x in lilyMelody:
            retStr += x + " "
        # print('\n')

        return [retStr, [x[1] for x in mel], r, h, p, ogMel]
        # return [retStr, [x[1] for x in mel], r, rhythms, ogMel]

    # build chords based on mel and common harmonic progression fundamentals
    def makeHarm(mel, offset, cad):

        # mel[0] = retStr
        # mel[1] = nums
        # mel[2] = rests
        # mel[3] = holds
        # mel[4] = passTones

        # create option to HOLD TONE or ADD PASSING TONES

        def left():
            return 0.1
        
        #print("Mel to be made into harm: " + str(mel))

        abstrMel = [(x-offset)%12 for x in mel[1]]
        # print("*****************************************")
        # print(mel)
        #print(abstrMel)
        # print(offset)
        
        # build all diatonic chords (1, 3, 6, 8, and 10 are non-diatonic)
        chordLib = {0:[[2,5,9],[4,0,7],[4,4,9],[5,2,9],[5,5,9],[7,2,5],[7,5,9],[9,0,5],[9,4,9]],
                    1:[[3,9,6],[3,10,6],[4,1,8],[4,9,7],[5,1,8],[5,11,8],[7,4,10],[7,3,10],[9,6,3],[10,4,7]],
                    2:[[2,0,5],[2,5,9],[4,0,7],[4,-1,7],[5,2,9],[5,-1,7],[7,5,11],[7,5,12],[9,2,5]],
                    3:[[0,8,10],[0,9,6],[3,8,12],[5,0,8],[7,7,0],[7,10,1],[8,7,0],[8,8,11],[9,6,12],[9,5,12]],
                    4:[[0,4,9],[2,0,5],[4,-1,7],[5,0,9],[5,5,9],[7,0,7],[7,-1,4],[9,9,12],[9,5,12],[11,4,7]],
                    5:[[0,0,9],[2,0,9],[2,2,9],[5,0,9],[5,2,9],[5,5,9],[7,2,11],[9,5,12],[11,7,14]],
                    6:[[0,2,9],[0,9,3],[2,9,12],[3,9,0],[9,2,12],[9,3,0]],
                    7:[[2,-3,5],[2,0,5],[4,0,7],[5,0,9],[5,2,9],[7,0,4],[7,2,11],[7,5,11],[9,4,12],[9,5,12],[11,5,14],[11,7,14]],
                    8:[[0,3,8],[0,5,12],[0,12,5],[2,5,11],[3,0,8],[4,1,10],[5,2,11],[5,2,10],[10,2,4]],
                    9:[[0,0,5],[0,4,9],[2,0,5],[2,2,5],[4,2,7],[4,4,12],[5,2,11],[5,2,12],[5,5,12],[7,4,12],[7,5,11],[9,4,12],[11,5,14],[11,7,14]],
                    10:[[0,0,3],[0,4,7],[2,2,7],[2,10,5],[3,3,7],[3,3,6],[4,2,7],[5,2,7],[7,2,5],[7,2,7]],
                    11:[[2,-3,5],[2,2,7],[2,5,7],[4,2,7],[5,2,7],[5,2,8],[7,4,12],[7,5,14],[7,7,14],[9,4,12],[9,5,12],[9,5,14]]}
        
        # all legal predominant harmonies based on each melody note
        preDomLib = {0:[[2,2,5],[2,9,5],[5,2,9],[9,2,5]],
                     2:[[2,2,5],[2,9,5],[5,2,9],[9,2,5]],
                     4:[[7,7,12]],
                     5:[[2,0,9],[2,2,9],[9,2,9]],
                     7:[[4,0,7]],
                     9:[[2,0,5],[2,2,5],[5,2,9]],
                     10:[[7,2,7]],
                     11:[[5,2,9]]}

        # all legal dominant harmonies based on each melody note
        domLib = {0:[[7,4,7]],
                  2:[[7,5,11],[11,5,7],[5,11,7]],
                  4:[[7,5,11]],
                  5:[[7,2,11]],
                  7:[[7,5,11],[2,11,5],[11,5,14],[5,2,11]],
                  9:[[7,5,11]],
                  11:[[-5,7,5],[2,5,7],[7,5,14],[5,2,7]]}
        
        # root position tonic chord
        rootTon = [0,0,4]

        # root position I7 chord
        rootDom = [0,-2,4]

        # root position V7 chord for HC
        rootDom7HC = [7,2,5]

        # root position V7 chord
        rootDom7 = [-5,2,5]

        chordsChosen = [rootTon]
        
        i = 1
        melLength = len(abstrMel)
        while i < melLength:
            if cad == "half":
                if i == len(abstrMel)-2:
                    # if pass tone
                    if mel[4][i]:
                        chordsChosen.append(preDomLib[abstrMel[i+1]][random.randrange(0, len(preDomLib[abstrMel[i+1]]))])
                        i += 2
                        continue
                    # if hold tone
                    if mel[3][i]:
                        chordsChosen.append(preDomLib[abstrMel[i]][random.randrange(0, len(preDomLib[abstrMel[i]]))])
                        chordsChosen.append(rootDom7HC)
                        i += 1
                        continue
                    chordsChosen.append(preDomLib[abstrMel[i]][random.randrange(0, len(preDomLib[abstrMel[i]]))])
                    i += 1
                    continue
                elif i == len(abstrMel)-1:
                    # if pass tone
                    if mel[4][i]:
                        chordsChosen.append(domLib[abstrMel[i+1]][random.randrange(0, len(domLib[abstrMel[i+1]]))])
                        i += 2
                        continue
                    # if hold tone
                    if mel[3][i]:
                        chordsChosen.append(domLib[abstrMel[i]][random.randrange(0, len(domLib[abstrMel[i]]))])
                        chordsChosen.append(domLib[abstrMel[i]][random.randrange(0, len(domLib[abstrMel[i]]))])
                        i += 1
                        continue
                    chordsChosen.append(rootDom7HC)
                    i += 1
                    continue
            elif cad == "authentic":
                if i == len(abstrMel)-2:
                    # if pass tone
                    if mel[4][i]:
                        chordsChosen.append(domLib[abstrMel[i+1]][random.randrange(0, len(domLib[abstrMel[i+1]]))])
                        i += 2
                        continue
                    # if hold tone
                    if mel[3][i]:
                        chordsChosen.append(rootDom)
                        chordsChosen.append(rootTon)
                        i += 1
                        continue
                    chordsChosen.append(domLib[abstrMel[i]][0])
                    i += 1
                    continue
                elif i == len(abstrMel)-1:
                    # if pass tone
                    if mel[4][i]:
                        chordsChosen.append(chordLib[abstrMel[i+1]][0])
                        i += 2
                        continue
                    # if hold tone
                    if mel[3][i]:
                        chordsChosen.append(domLib[abstrMel[i]][random.randrange(0, len(domLib[abstrMel[i]]))])
                        chordsChosen.append(rootTon)
                        i += 1
                        continue
                    chordsChosen.append(rootTon)
                    i += 1
                    continue
            elif cad == "retran":
                if i == len(abstrMel)-3:
                    # if pass tone
                    if mel[4][i]:
                        chordsChosen.append(domLib[abstrMel[i+1]][random.randrange(0, len(domLib[abstrMel[i+1]]))])
                        i += 2
                        continue
                    # if hold tone
                    if mel[3][i]:
                        chordsChosen.append(domLib[abstrMel[i]][random.randrange(0, len(domLib[abstrMel[i]]))])
                        chordsChosen.append(domLib[abstrMel[i]][random.randrange(0, len(domLib[abstrMel[i]]))])
                        i += 1
                        continue
                    chordsChosen.append(domLib[abstrMel[i]][random.randrange(0, len(domLib[abstrMel[i]]))])
                    i += 1
                    continue
                elif i == len(abstrMel)-2:
                    # if pass tone
                    if mel[4][i]:
                        chordsChosen.append(domLib[abstrMel[i+1]][random.randrange(0, len(domLib[abstrMel[i+1]]))])
                        i += 2
                        continue
                    # if hold tone
                    if mel[3][i]:
                        chordsChosen.append(domLib[abstrMel[i]][random.randrange(0, len(domLib[abstrMel[i]]))])
                        chordsChosen.append(rootDom)
                        i += 1
                        continue
                    chordsChosen.append(domLib[abstrMel[i]][random.randrange(0, len(domLib[abstrMel[i]]))])
                    i += 1
                    continue
                elif i == len(abstrMel)-1:
                    # if pass tone
                    if mel[4][i]:
                        chordsChosen.append(rootDom)
                        i += 2
                        continue
                    # if hold tone
                    if mel[3][i]:
                        chordsChosen.append(domLib[abstrMel[i]][random.randrange(0, len(domLib[abstrMel[i]]))])
                        chordsChosen.append(rootDom)
                        i += 1
                        continue
                    chordsChosen.append(rootDom)
                    i += 1
                    continue
            elif cad == "end1":
                if i == len(abstrMel)-4:
                    # if pass tone
                    if mel[4][i]:
                        chordsChosen.append(preDomLib[abstrMel[i+1]][random.randrange(0, len(preDomLib[abstrMel[i+1]]))])
                        i += 2
                        continue
                    # if hold tone
                    if mel[3][i]:
                        chordsChosen.append(preDomLib[abstrMel[i]][random.randrange(0, len(preDomLib[abstrMel[i]]))])
                        chordsChosen.append(preDomLib[abstrMel[i]][random.randrange(0, len(preDomLib[abstrMel[i]]))])
                        i += 1
                        continue
                    chordsChosen.append(preDomLib[abstrMel[i]][random.randrange(0, len(preDomLib[abstrMel[i]]))])
                    i += 1
                    continue
                elif i == len(abstrMel)-3:
                    # if pass tone
                    if mel[4][i]:
                        chordsChosen.append(preDomLib[abstrMel[i+1]][random.randrange(0, len(preDomLib[abstrMel[i+1]]))])
                        i += 2
                        continue
                    # if hold tone
                    if mel[3][i]:
                        chordsChosen.append(preDomLib[abstrMel[i]][random.randrange(0, len(preDomLib[abstrMel[i]]))])
                        chordsChosen.append(preDomLib[abstrMel[i]][random.randrange(0, len(preDomLib[abstrMel[i]]))])
                        i += 1
                        continue
                    chordsChosen.append(preDomLib[abstrMel[i]][random.randrange(0, len(preDomLib[abstrMel[i]]))])
                    i += 1
                    continue
                elif i == len(abstrMel)-2:
                    # if pass tone
                    if mel[4][i]:
                        chordsChosen.append(preDomLib[abstrMel[i+1]][random.randrange(0, len(preDomLib[abstrMel[i+1]]))])
                        i += 2
                        continue
                    # if hold tone
                    if mel[3][i]:
                        chordsChosen.append(preDomLib[abstrMel[i]][random.randrange(0, len(preDomLib[abstrMel[i]]))])
                        chordsChosen.append(rootDom7)
                        i += 1
                        continue
                    chordsChosen.append(preDomLib[abstrMel[i]][random.randrange(0, len(preDomLib[abstrMel[i]]))])
                    i += 1
                    continue
                elif i == len(abstrMel)-1:
                    # if pass tone
                    if mel[4][i]:
                        chordsChosen.append(domLib[abstrMel[i]][random.randrange(0, len(domLib[abstrMel[i]]))])
                        i += 2
                        continue
                    # if hold tone
                    if mel[3][i]:
                        chordsChosen.append(domLib[abstrMel[i]][random.randrange(0, len(domLib[abstrMel[i]]))])
                        chordsChosen.append(rootDom7)
                        i += 1
                        continue
                    chordsChosen.append(rootDom7)
                    i += 1
                    continue
            
            # if passTone in mel
            if mel[4][i]:
                chordsChosen.append(chordLib[abstrMel[i+1]][random.randrange(0, len(chordLib[abstrMel[i+1]]))])
                i += 2
                continue
            # if hold in mel
            if mel[3][i]:
                chordsChosen.append(chordLib[abstrMel[i]][random.randrange(0, len(chordLib[abstrMel[i]]))])
                chordsChosen.append(chordLib[abstrMel[i]][random.randrange(0, len(chordLib[abstrMel[i]]))])
                i += 1
                continue
            chordsChosen.append(chordLib[abstrMel[i]][random.randrange(0, len(chordLib[abstrMel[i]]))])
            i += 1
        
        # print(abstrMel)
        # print(chordsChosen)
        '''
        for i in range(len(chordsChosen)):
            try:
                if chordsChosen[i][2]-12 > mel[1][i]:
                    t = chordsChosen[i][2]
                    chordsChosen[i][2] = mel[1][i]
                    mel[1][i] = t
                    if chordsChosen[i][1] > chordsChosen[i][2]:
                        u = chordsChosen[i][1]
                        chordsChosen[i][1] = chordsChosen[i][2]
                        chordsChosen[i][2] = u
                        if chordsChosen[i][0]-12 > chordsChosen[i][1]:
                            v = chordsChosen[i][0]
                            chordsChosen[i][0] = chordsChosen[i][1]
                            chordsChosen[i][1] = v
            except:
                #print("'i' was too big for one of the lists.")
                # random.shuffle(chordsChosen[i], left)
        '''
        # print(chordsChosen)
        # print()

        return chordsChosen

        # return makeMel(offset-regOffset, scale, starter)

    # put the melody and harmony together
    def makePhrase(scale, offset, length, newMel, cad="authentic", eat=2):
        global fullMel
        global bass
        global tenor
        global alto

        # generating new melody
        if newMel:
            
            mel = makeMel(offset, scale[offset%12], [(0,0)], length, cad, [], [], [])
            # rhythmVals = genRhythmVals()
            # mel = makeMel(offset, scale[offset%12], [(0,0)], length, cad, [], rhythmVals)
            #print("mel[-1]: " + str(mel[-1]))
            #mels.append(mel)
            #print("Check these: " + str(mels[0][-1]) + " " + str(mels[0][3]))
            if cad == "end2":
                # "Cad mel: " + str(mel))
                realNote = mels[-1][-1][-1][1]
                #print("offset: " + str(offset))
                
                # SET REGISTER OF FINAL NOTE TO MATCH CONTEXT
                while realNote > 10:
                    mel[0] = mel[0][:mel[0].index("1")] + "'" + mel[0][mel[0].index("1"):]
                    realNote -= 12
                realNote = mels[-1][-1][-1][1]
                #print("realNote: " + str(realNote))
                while realNote < -10:
                    mel[0] = mel[0][:mel[0].index("1")-mel[0].count("'")] + mel[0][mel[0].index("1"):]
                    realNote += 12
                # mels[0] += "1"
                
            mels.append(mel)
            #print(mels[-1])
        
        # restating old melody
        else:

            #c = sum(mel[-1])
            #if cad == "end1":
                #length = 13-c
            #else:
                #length = 16-c
            #mel = makeMel(offset, scale[offset%12], ogMel, length, cad, mels[0][2], r, rhythms)
            #if cad == "end1":
                #mels.append(mel)
            # ALL OF THE BELOW CODE (AT THIS INDENTATION) WILL BE REPLACED BY THE ABOVE...   

            i = 0
            newEat = eat
            newHolds = mels[0][3]
            while len(newHolds) > len(mels[0][-1]):
                #print("POPPED FROM HOLDS")
                newHolds.pop()

            newPassTones = mels[0][4]
            while len(newPassTones) > len(mels[0][-1]):
                #print("POPPED FROM PASS TONES")
                newPassTones.pop()

            while i < newEat:
                if newHolds[0-i]:
                    newEat -= 1
                elif newPassTones[0-i]:
                    newEat += 1
                i += 1
            #print("eat: " + str(eat))
            #print("newEat: " + str(newEat))
            #print()
            #print("Before: " + str(mels[0][-1]))
            #print(newHolds)
            ogMel = mels[0][-1][:0-newEat]
            newHolds = newHolds[:0-newEat]
            newPassTones = newPassTones[:0-newEat]
            #if len(ogMel) != len(mels[0][3]):
            #   print("HOLD ON A MINUTE PLAYA")
            #print("After: " + str(ogMel))
            #print(newHolds)
            #print("ogMel: " + str(ogMel))
            #print("Temp: " + str(temp))
            c = 0
            for i in range(len(newHolds)):
                if newHolds[i]:
                    c += 1
                elif newPassTones[i]:
                    c -= 0.5
                c += 1
                #print(str(mels[0][-1][i]) + " " + str(c))
            if cad == "end1":
                length = 13-c
            else:
                length = 16-c
            #length = 13-c
            
            #if not length % 1 == 0:
                #length -= 1.5

            mel = makeMel(offset, scale[offset%12], ogMel, length, cad, mels[0][2], newHolds, newPassTones)
            if cad == "end1":
                mels.append(mel)
            #mel = mels[0]
            #print("MOTIF MEL: " + str(mel))
        #print("Made mel: " + str(mel))

        #FORM HARMONIES
        harmonies = makeHarm(mel, offset, cad)
        altoLine = [x[2] for x in harmonies]
        tenorLine = [x[1] for x in harmonies]
        bassLine = [x[0] for x in harmonies]
        fullMel += mel[0]
        var = [False, False, False, False, False]
        restVar = []
        holdVar = []
        passVar = []

        if cad != "end2":
            for x in harmonies:
                restVar.append(random.choice(var))
                holdVar.append(random.choice(var))
                passVar.append(random.choice(var))
        else:
            for x in harmonies:
                restVar.append(False)
                holdVar.append(True)
                passVar.append(False)
        
        # line up the notes for each part
        def lineUp(ls, melMode=False):
            length = min(len(mels[0][3]),len(ls))
            for i in range(length):
                buff = 4*" "
                if melMode:
                    if mels[0][3][i]:
                        buff = 12*" "
                    elif mels[0][4][i]:
                        buff = ""
                        length += 1
                print("{0:3s} ".format(str(ls[i])),end=buff)
            print()

        print("\nStaff Representation:\n")
        lineUp([x-offset for x in mel[1]], True)
        lineUp(altoLine)
        lineUp(tenorLine)
        lineUp(bassLine)
        print()
        
        # instrumental range setup
        bassOff = 24
        tenAltOff = 12

        #not using this
        '''
        if cad == "retran":
            bassOff += 12
            tenAltOff += 12
        '''
        # FORM THE INDIVIDUAL HARMONIC LINES BEFORE SHIPPING THEM OUT TO BE TRANSLATED
        # Enforce four-part writing rules such as...
        # - parallel fifths
        # - leap to a fifth by similar motion
        # - leap to an octave by similar motion

        # add holds and passes where possible to spice up the line
        def spiceUp(ls):
            newMel = []
            holds = []
            passes = []
            rests = []
            # in the future, need the scale passed in to determine scalar passes!
            passPairs = [{0,4}, {2,5}, {7,9}, {9,12}]
            passInserts = [2,4,8,11]
            neighbors = {0:[2,-1],2:[2,-2],4:[1,-2],5:[2,-1],7:[2,-2],9:[2,-2],11:[1,-2]}
            i = 0
            while i < len(ls):
                passRoll = random.randrange(0,2)
                # if on last note of melody, return quarter
                if i == len(ls)-1:
                    rests.append(False)
                    holds.append(False)
                    passes.append(False)
                    newMel.append(ls[i])
                    i += 1
                    continue
                # check equivalence to next note of melody, 80% hold, 20% neighbor
                if ls[i] == ls[i+1]:
                    roll = random.randrange(0,9)
                    # hold
                    if roll > 1:
                        rests.append(False)
                        holds.append(True)
                        passes.append(False)
                        newMel.append(ls[i])
                        i += 1
                    # neighbor
                    else:
                        dirRoll = random.randrange(0,1)
                        neighborMove = neighbors[ls[i]%12][dirRoll]
                        rests.append(False)
                        rests.append(False)
                        holds.append(False)
                        holds.append(False)
                        passes.append(True)
                        passes.append(True)
                        newMel.append(ls[i])
                        newMel.append(ls[i] + neighborMove)
                # check if pairing in passPairs dict, accept 67% of time
                elif {ls[i], ls[i+1]} in passPairs and passRoll > 0:
                    rests.append(False)
                    rests.append(False)
                    holds.append(False)
                    holds.append(False)
                    passes.append(True)
                    passes.append(True)
                    newMel.append(ls[i])
                    newMel.append(passInserts[passPairs.index({ls[i], ls[i+1]})])
                # return quarter   
                else:
                    rests.append(False)
                    holds.append(False)
                    passes.append(False)
                    newMel.append(ls[i])
                i += 1
            return [newMel, rests, holds, passes]

        # prepare line for lilyMel translator
        def finalizeLine(line, off):
            lineInfo = spiceUp(line)
            newLine = lineInfo[0]        
            rests = lineInfo[1]
            holds = lineInfo[2]
            passes = lineInfo[3]
            if cad == "end2":
                holds = [True]
            finalLine = [(((x+offset-off)%12, x+offset-off)) for x in newLine]
            return [finalLine, rests, holds, passes]
        
        finalBassLine = finalizeLine(bassLine, bassOff)
        finalTenorLine = finalizeLine(tenorLine, tenAltOff)
        finalAltoLine = finalizeLine(altoLine, tenAltOff)

        bass += melToLily(finalBassLine[0], scale[offset%12], finalBassLine[1], finalBassLine[2], finalBassLine[3], cad)[0]
        tenor += melToLily(finalTenorLine[0], scale[offset%12], finalTenorLine[1], finalTenorLine[2], finalTenorLine[3], cad)[0]
        alto += melToLily(finalAltoLine[0], scale[offset%12], finalAltoLine[1], finalAltoLine[2], finalAltoLine[3], cad)[0]
        #print("Bass: " + str(bass))
        #print("Tenor: " + str(tenor))
        #print("Alto: " + str(alto))
        #print()

    # write the lilyPond code to output file
    def printSong(scale, m, a, t, b):
        code = "\\header{\n  title = \"Computery's Masterpiece\"\n}\n\n"
        code += "\\score {\n"
        code += "\\new PianoStaff <<\n"
        code += "\\" + "new Staff { \set Staff.midiInstrument = \"violin\" \clef \"treble\" \\key " + scale + " \\major " + m + "}\n"
        code += "\\" + "new Staff { \set Staff.midiInstrument = \"viola\" \clef \"treble\" \\key " + scale + " \\major " + a + "}\n"
        code += "\\" + "new Staff { \set Staff.midiInstrument = \"cello\" \clef \"bass\" \\key " + scale + " \\major " + t + "}\n"
        code += "\\" + "new Staff { \set Staff.midiInstrument = \"contrabass\" \clef \"bass\" \\key " + scale + "\\major " + b + "}\n"
        code += ">>\n"
        code += "\\midi{}\n"
        code += "}\n"
        code += "\\version \"2.22.2\""
        f = open("ConvertMe.ly", "w")
        f.write(code)
        f.close()
    
    # EAT HAS TO REPRESENT BEATS, NOT NOTES

    # for no holds or passes, 16->(3,3)->17->(3,6)

    # MAIN
    offset = random.randrange(0,12)
    #fileName = sys.argv[1]
    #offset = 11
    #print(offset)
    print("GENERATING A SECTION:")
    makePhrase(majScales, offset, 16, True, "half")
    print("RESTATING A SECTION:")
    makePhrase(majScales, offset, 3, False, "authentic", 3)
    print("GENERATING B SECTION:")
    makePhrase(majScales, offset+7, 17, True, "retran")
    print("RESTATING A SECTION:")
    makePhrase(majScales, offset, 3, False, "end1", 6)
    print("FINALIZING CADENCE:")
    makePhrase(majScales, offset, 1, True, "end2")
    printSong(majScales[0][offset], fullMel, alto, tenor, bass)

if __name__ == "__main__":
    main()