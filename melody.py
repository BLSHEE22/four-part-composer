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

    #PTORHOLD
    #def makeMel(offset, scale, starter, length, cad, r, h, p):
    # keep melodies within a set registral range
    def makeMel(offset, scaleDict, scaleType, starter, length, cad, rests, rhythmVals, rhythmValsPicked, log):

        # create melody list and build scale
        melody = []
        if log:
            scale = buildScale(scaleType)
        goLeap = False
        justLeaped = (False, 0)
        lastDir = 2
        consecDir = 1
        #nonLeaps = [[[2,2,4],[-1,-1,-3]],[[1],[-3]],[[2,2,3],[-2,-2,-3]],[[1],[-3]],[[1,3],[-2,-2,-4]],[[2,4],[-1,-1,-3]],[[1],[-4]],[[2,4],[-2,-2,-3]],[[2],[-1]],[[2,3],[-2,-2,-4]],[[1,2],[-3]],[[1,3],[-2,-2,-4]]] # legal nonLeaps from every scale degree
        #leaps = [[[5,7,9,11,12],[-5,-7,-8]],[[5,7,9,11,12],[-5,-7,-8]],[[5,7,9,10,12],[-5,-7,-9]],[[5,7,9,10,12],[-5,-7,-9]],[[5,7,8,10,12],[-5,-7,-9]],[[7,9,11,12],[-5,-6,-8]],[[6],[-6]],[[5,7,9,10,12],[-5,-7,-8]],[[5,7,9,10,12],[-5,-7,-8]],[[5,7,8,10,12],[-5,-7,-9]],[[5,7,8,10,12],[-5,-7,-9]],[[6,8,10,12],[-6,-7,-9]]] # legal leaps from every scale degree
        # dom = [2,7,11]
        # preDom = [0,2,5,9]

        # starter = maj[random.randrange(0, len(maj)-1)]
        for x in starter:
            melody.append(x)
    
        #print("Melody pre-offset: " + str(melody))
        # melody.append((starter, starter))
        if not rests:
            rests.append(False)
        if not rhythmValsPicked:
            rhythmValsPicked.append(random.choice(rhythmVals))

        # 50/50 up or down, never move by 0
        # leaps occur 30% of the time and are always following by a non-leap in the opposite direction of the leap
        i = 1
        spaceLeft = length - sum(rhythmValsPicked) 

        if not log:
            print("Melodic motif repeated.")
        else:
            while spaceLeft > 0:
                # placeholder
                newNote = 0

                # if 0, set restApp to True
                rest = random.randrange(0,6)
                # 0 is up, 1 is down
                uOrD = random.randrange(0,2)
                # if 0 or 1, leap!
                l = random.randrange(0, 8)

                # PRINT EXISTING MELODY 
                print()
                #print("Current melody:")
                #print("Pitches: " + str([x[1] for x in melody]))
                #print("Rhythms: " + str(rhythmValsPicked))
                #print("Creating new note...")
                #print("Note created.")

                # LOGIC FOR DECIDING THE RHYTHM
                print("Choosing rhythm...")
                rhythmVal = random.choice(rhythmVals)
                #print("Rhythm Value Map: " + str(rhythmVals))
                while rhythmVal not in rhythmVals or rhythmVal > spaceLeft:
                    if rhythmVal == 0.5:
                        break
                    #print("Rhythm of value " + str(rhythmVal) + " chosen.")
                    #print("RHYTHM TOO LONG, SHORTENING BY AN EIGTH NOTE...")
                    rhythmVal -= 0.5

                print("Rhythm of value " + str(rhythmVal) + " chosen.")

                # This logic is basically ignored.            
                #if spaceLeft < 2.5:
                    #penOrUlt = True
                penOrUlt = False
                restApp = False
                
                # Used to land cadences on strong beats, not used here.
                emerg8 = False

                print("Deciding motion...")
                if not penOrUlt:
                    if rest == 0:
                        restApp = True
                    if not justLeaped[0] and l < 2: goLeap = True
                    # LEAP LOGIC
                    if goLeap:
                        if uOrD == 0:
                            print("Upward leap chosen.")
                        else:
                            print("Downward leap chosen.")
                        # find legal leaps
                        legalLeaps = findLegalLeaps(melody[i-1][1], scale, uOrD)
                        print("Legal Leaps: " + str(legalLeaps))
                        # pick a random leap in legalLeaps
                        newNote = random.choice(legalLeaps)
                        print(str(newNote) + " chosen.")

                        #leap = leaps[maj.index(melody[i-1][0]%12)][uOrD][random.randrange(0,len(leaps[maj.index(melody[i-1][0]%12)][uOrD]))]
                        #newNote = melody[i-1][1] + leap
                        justLeaped = (True, uOrD)
                        goLeap = False
                    # POST-LEAP BALANCE LOGIC
                    elif justLeaped[0]:
                        print("Post-leap balance required.")
                        # direction overrides to opposite of the previous leap
                        oppFromLeap = 1
                        if justLeaped[1] == 1:
                            oppFromLeap = 0
                        # find legal steps
                        legalSteps = findLegalSteps(melody[i-1][1], scale, oppFromLeap)
                        print("Legal Steps: " + str(legalSteps))

                        # pick a random step in legalSteps
                        newNote = random.choice(legalSteps)
                        print(str(newNote) + " chosen.")

                        #fillIn = nonLeaps[maj.index(melody[i-1][0]%12)][oppFromLeap][random.randrange(0, len(nonLeaps[maj.index(melody[i-1][0]%12)][oppFromLeap]))]
                        #newNote = melody[i-1][1] + fillIn
                        justLeaped = (False, 0)
                    # STEP LOGIC
                    else:
                        if uOrD == 0:
                            print("Upward step chosen.")
                        else:
                            print("Downward step chosen.")
                        # find legal steps
                        legalSteps = findLegalSteps(melody[i-1][1], scale, uOrD)
                        print("Legal Steps: " + str(legalSteps))

                        # pick a random step in legalSteps
                        newNote = random.choice(legalSteps)
                        print(str(newNote) + " chosen.")
                        #nonLeap = nonLeaps[maj.index(melody[i-1][0]%12)][uOrD][random.randrange(0, len(nonLeaps[maj.index(melody[i-1][0]%12)][uOrD]))]
                        #newNote = melody[i-1][1] + nonLeap

                # REGISTER CONTROL LOGIC (temporarily disabled)
                # if note extends beyond lower bound, bring up an octave
                #if melody[-1][1] - newNote > 6:
                    #newNote += 12
                # if note extends beyond upper bound, bring down an octave
                #if newNote - melody[-1][1] > 6:
                    #newNote -= 12
                # emerg8 is always false, so this always executes.
                if not emerg8:
                    melody.append((newNote%12, newNote))
                    rhythmValsPicked.append(rhythmVal)
                    rests.append(restApp)
                else:
                    i -= 1
                    length -= 0.5
                
                # update spaceLeft
                spaceLeft = length - sum(rhythmValsPicked)
                print("New melody: " + str([x[1] for x in melody]))
                print("            " + str(rhythmValsPicked))
                print("Total beats used: " + str(sum(rhythmValsPicked)))
                print("Space left: " + str(spaceLeft))
                #print()
                i += 1
        
        ogMel = [x for x in melody]
        melody = [((x[0]+offset)%12,x[1]+offset) for x in ogMel] 
        return melToLily(melody, scaleDict, rests, rhythmVals, rhythmValsPicked, cad, ogMel)

    # build the scale
    def buildScale(scaleType):
        print("Building scale...")
        if scaleType == "major":
            scale = {0,2,4,5,7,9,11}
        elif scaleType == "minor":
            scale = {0,2,3,5,7,8,10}
        elif scaleType == "chromatic":
            scale = {0,1,2,3,4,5,6,7,8,9,10,11}
        else:
            scale = {0}
            curr = 0
            while curr < 12:
                i = random.randrange(1,4)
                curr += i
                if curr >= 12: 
                    scale.add(curr-12) 
                else: 
                    scale.add(curr)
        print(scale)
        print("Built scale.")
        return scale
    
    # find LEAPS in the scale that are no more than a tenth away from a starting note
    def findLegalLeaps(note, scale, direction):
        #print("Finding legal leaps...")
        legalLeaps = []
        leapStart = 5
        leapEnd = 16
        leapInc = 1
        defOctLeap = 12
        if direction == 1:
            leapStart = -5
            leapEnd = -16
            leapInc = -1
            defOctLeap = -12
        dist = leapStart
        while not dist == leapEnd:
            possLeap = note + dist
            if possLeap in scale or possLeap%12 in scale:
                legalLeaps.append(possLeap)
            dist += leapInc
        if not legalLeaps:
            #print("No legal leaps found. Returning an octave leap.")
            return [note+defOctLeap]
        #print("Legal leaps found.")
        return legalLeaps

    # find STEPS in the scale from a starting note
    def findLegalSteps(note, scale, direction):
        #print("Finding legal steps...")
        legalSteps = []
        stepStart = 1
        stepEnd = 4
        stepInc = 1
        if direction == 1:
            stepStart = -1
            stepEnd = -4
            stepInc = -1
        dist = stepStart
        while not dist == stepEnd:
            possStep = note + dist
            if possStep in scale or possStep%12 in scale:
                legalSteps.append(possStep)
            dist += stepInc
        if not legalSteps:
            #print("No legal steps found. Repeating note.")
            return [note]
        #print("Legal steps found.")
        return legalSteps

    # generate the available rhythmic value choices for a melody
    def genRhythmVals():
        print("Generating rhythm value map...")        
        rhythmVals = []
        vals = [0.5,1,1.5,2,3,4] #implement 0.25, 6, and 8
        pips = [10,100,1000]

        # randomly boost the frequency of any of the first four vals 
        for i in range(2):
            pipCount = random.choice(pips)
            dieRoll = random.randrange(1, pipCount)
            for j in range(dieRoll):
                rhythmVals.append(vals[i])

        # tack on the last four (soon to be six) vals (we don't want to see too many of these)
        rhythmVals.append(vals[2])
        rhythmVals.append(vals[3])
        rhythmVals.append(vals[4])
        rhythmVals.append(vals[5])
        #rhythmVals.append(vals[6])
        #rhythmVals.append(vals[7])
        print(rhythmVals)
        print("Rhythm value map generated.")
        return rhythmVals

    # translate melNums to LilyPond code
    def melToLily(mel, sc, rests, rhythmVals, rhythmValsPicked, cad, ogMel=[]):
        #print("MelToLily: " + str(mel))
        #print("OgMel: " + str(ogMel))
        #print(r)
        #print(h)
        #print(p)
        #print(mel)
        #print("RHYTHMVALSPICKED: " + str(rhythmValsPicked))
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
            rhythmToLily = {0.25:"16",0.5:"8",1:"4",1.5:"4.",2:"2",3:"2.",4:"1"}
            if not rests[i]:
                s += rhythmToLily[rhythmValsPicked[i]]
            else:
                lilyMelody.append("r" + rhythmToLily[rhythmValsPicked[i]])
                i += 1
                continue
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

        return [retStr, [x[1] for x in mel], rests, rhythmVals, rhythmValsPicked, ogMel]

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

        return chordsChosen

        # return makeMel(offset-regOffset, scale, starter)

    # put the melody and harmony together
    def makePhrase(scaleDict, scaleType, offset, length, newMel, cad="authentic", eat=2):
        global fullMel
        global bass
        global tenor
        global alto

        # creating new melody
        if newMel:

            rhythmVals = genRhythmVals()
            mel = makeMel(offset, scaleDict[offset%12], scaleType, [(0,0)], length, cad, [], rhythmVals, [], True)
       
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
        
        # creation variation on old melody
        else:

            # Use rhythms of old melody but create new pitches!
            #print("Old melody: " + str(mels))
            #mel = makeMel(offset, scaleDict[offset%12], [(0,0)], length, cad, [], [999], [])
            
            # For restating the exact melody:
            c = sum(mels[0][4])
            if cad == "end1":
                length = 13-c
            else:
                length = 16-c
            mel = makeMel(offset, scaleDict[offset%12], scaleType, mels[0][-1], length, cad, mels[0][2], mels[0][3], mels[0][4], False)
            if cad == "end1":
                mels.append(mel)

        fullMel += mel[0]

    # write the lilyPond code to output file
    def printSong(scaleDict, m, a, t, b):
        code = "\\header{\n  title = \"Computery's Masterpiece\"\n}\n\n"
        code += "\\score {\n"
        code += "\\new PianoStaff <<\n"
        code += "\\" + "new Staff { \set Staff.midiInstrument = \"violin\" \clef \"treble\" \\key " + scaleDict + " \\major " + m + "}\n"
        #code += "\\" + "new Staff { \set Staff.midiInstrument = \"viola\" \clef \"treble\" \\key " + scale + " \\major " + a + "}\n"
        #code += "\\" + "new Staff { \set Staff.midiInstrument = \"cello\" \clef \"bass\" \\key " + scale + " \\major " + t + "}\n"
        #code += "\\" + "new Staff { \set Staff.midiInstrument = \"contrabass\" \clef \"bass\" \\key " + scale + "\\major " + b + "}\n"
        code += ">>\n"
        code += "\\midi{}\n"
        code += "}\n"
        code += "\\version \"2.22.2\""
        f = open("ConvertMe.ly", "w")
        f.write(code)
        f.close()
    
    # composes an AABA tune
    def AABA(key, scaleType):
        print("Generating A section...")
        makePhrase(majScales, scaleType, key, 16, True, "half")
        print("\nRestating A section...")
        makePhrase(majScales, scaleType, key, 16, False, "authentic")
        print("\nGenerating B section...") #keep rhythmvals the same perhaps?
        makePhrase(majScales, scaleType, key, 16, True, "retran")
        print("\nRestating A section...")
        makePhrase(majScales, scaleType, key, 16, False, "end1",6)

    # composes a freeform tune
    def freeform(key, beats):
        makePhrase(majScales, key, beats, True, "authentic")

    # composes a tune that writes and employs a rhythmic motif
    def rhythmicMotif(key):
        makePhrase(majScales, key, 8, True, "authentic")
        makePhrase(majScales, key, 8, False, "authentic")

    # MAIN
    offset = random.randrange(0,12)
    #fileName = sys.argv[1]
    #offset = 11
    scaleAsk = input("What kind of scale would you like to use for your melody?\n- major\n- minor\n- chromatic\n- random\n")
    print()
    if scaleAsk == 'major' or scaleAsk == 'minor' or scaleAsk == 'chromatic':
        print("Writing melody using " + scaleAsk + " scale...")
    else:
        print("Writing melody using randomly built scale...")
    print("Tonal center of " + majScales[0][offset] + " chosen.")
    AABA(offset, scaleAsk)
    #freeform(offset, 64)
    #rhythmicMotif(offset)
    #print(offset)
    #print()
    #makePhrase(majScales, offset, 1, True, "end2")
    printSong(majScales[0][offset], fullMel, alto, tenor, bass)

if __name__ == "__main__":
    main()