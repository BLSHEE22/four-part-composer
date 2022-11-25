from datetime import date
from datetime import datetime
import random
import math
import sys

# GLOBAL list of melodies and rhythms
mels = []
rhythms = []
scales = []
bMels = []
melRests = []
melHolds = []
melPassTones = []
melRange = [i for i in range(-5,32)]
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
minScales = {0:{0:"c",1:"cis",2:"d",3:"ees",4:"e",5:"f",6:"fis",7:"g",8:"gis",9:"a",10:"bes",11:"b"},
                1:{0:"bis",1:"cis",2:"d",3:"dis",4:"e",5:"eis",6:"fis",7:"g",8:"gis",9:"a",10:"ais",11:"b"},
                2:{0:"c",1:"cis",2:"d",3:"ees",4:"e",5:"f",6:"ges",7:"g",8:"aes",9:"a",10:"bes",11:"b"},
                3:{0:"c",1:"des",2:"d",3:"ees",4:"e",5:"f",6:"ges",7:"g",8:"aes",9:"a",10:"bes",11:"b"},
                4:{0:"c",1:"cis",2:"d",3:"dis",4:"e",5:"f",6:"fis",7:"g",8:"gis",9:"a",10:"ais",11:"b"},
                5:{0:"c",1:"des",2:"d",3:"ees",4:"e",5:"f",6:"ges",7:"g",8:"aes",9:"a",10:"bes",11:"b"},
                6:{0:"c",1:"cis",2:"d",3:"dis",4:"e",5:"eis",6:"fis",7:"g",8:"gis",9:"a",10:"ais",11:"b"},
                7:{0:"c",1:"des",2:"d",3:"ees",4:"e",5:"f",6:"fis",7:"g",8:"aes",9:"a",10:"bes",11:"b"},
                8:{0:"c",1:"cis",2:"d",3:"dis",4:"e",5:"f",6:"fis",7:"g",8:"gis",9:"a",10:"ais",11:"b"},
                9:{0:"c",1:"cis",2:"d",3:"dis",4:"e",5:"f",6:"fis",7:"g",8:"gis",9:"a",10:"ais",11:"b"},
                10:{0:"c",1:"des",2:"d",3:"ees",4:"e",5:"f",6:"ges",7:"g",8:"aes",9:"a",10:"bes",11:"b"},
                11:{0:"c",1:"cis",2:"d",3:"dis",4:"e",5:"f",6:"fis",7:"g",8:"gis",9:"a",10:"ais",11:"b"},} 


def main():

    # write a counterpoint line
    def counterpoint(mel):
        print(mel[0])
        return

    # make melody
    def makeMel(offset, scaleDict, scaleType, starter, prev, length, cad, dynams, artics, rhythmVals, rhythmValsPicked, new):
        # this function is turning into makePhrase
        # IMPLEMENT 'BUILD FROM BOTH SIDES'
        # IMPEMENT 'HIGH POINT'
        # IMPLEMENT 'END ON DOMINANT FUNCTIONING NOTE'
        # IMPLEMENT 'SCALE FUNCTION ANALYZER'

        # ACE MELODY RULES:
        # pitches must exist within phraseRange
        # motion is 50/50 up or down, never move by 0 (maybe should allow stationary move, 46/46/8 splits?)
        # rests are picked 1/16 of the time, marked by pitch '800-offset'
        # articulations are assigned 1/4 of the time, there are 7 possible choices
        # leaps occur 20% of the time and are always followed by TWO OR MORE non-leaps in the opposite direction of the leap
        # leaps are no bigger than an octave

        # create melody list and build scale
        melody = []
        # if first time writing A, write scale
        if "Scale" in cad:
            scale = buildScale(scaleType)
        # if restating A, connect the two statements
        if not new and (cad == "A" or cad == "Aend" or cad == "fugueA"):
            scale = scales[0]
            temp = starter[0]
            connDist = temp[1]-prev
            if connDist < -6:
                starter[0] = (temp[0]+12,temp[1]+12)
            elif connDist > 6:
                starter[0] = (temp[0]-12,temp[1]-12)
        else:
            scale = scales[0]

        prevRest = False
        goLeap = False
        justLeaped = (0, 0)
        choosingRhythms = True
        syncoBeatCnt = 0
        inSlur = 0
        inNonVib = 0
        inPizz = 0
        articChoices = [a for a in range(9)]
        dynamChoices = [d for d in range(5)]
        dynamTrans = [t for t in range(3)]
        # boost accents
        for j in range(random.randrange(1,5)):
            articChoices.append(1)
        # load in lots of the default option
        for k in range(random.randrange(10,13)):
            articChoices.append(0)

        # create instrumental range of notes
        phraseRange = [x-offset for x in melRange]

        # preload starter information 
        if starter:
            for x in starter:
                melody.append(x)
            prev = melody[0][1]
        # if no preloaded artics, preload non-artic for first beat
        if not artics:
            artics.append(random.choice(articChoices))
        # if starter and no rhythm value picked, choose one
        if starter:
            if not rhythmValsPicked:
                rhythmValsPicked.append(random.choice(rhythmVals))

        # intialize note count and total beats used count
        i = 1
        spaceLeft = length - sum(rhythmValsPicked) 
        if not choosingRhythms:
            spaceLeft = len(rhythmValsPicked)-1

        # if writing new melody
        if new:
            while spaceLeft > 0:
                # choose rhythm of next note
                if choosingRhythms:
                    rhythmVal = random.choice(rhythmVals)
                    if not spaceLeft%1 == 0:
                        syncoBeatCnt += 1
                    else:
                        syncoBeatCnt = 0
                    if syncoBeatCnt > 0:
                        def findUpperOdd(val):
                            while True:
                                if math.ceil(val)%2 == 0:
                                    return math.ceil(val)
                                val += 1
                        # get to the nearest strong beat
                        #print("Space used: " + str(length-spaceLeft))
                        #rhythmVal = findUpperOdd(length-spaceLeft) - (length-spaceLeft)
                        #rhythmVal = math.ceil(spaceLeft) - spaceLeft
                        # get to the nearest quarter
                        rhythmVal = math.ceil(length-spaceLeft) - (length-spaceLeft)
                        #print("Decided rhythm value: " + str(rhythmVal))
                    # find a shorter rhythm if chosen rhythm is too big
                    #print(rhythmVals)
                    while rhythmVal not in rhythmVals or rhythmVal > spaceLeft:
                        if rhythmVal == min(rhythmVals):
                            break
                        #print("SHORTENING RHYTHM VALUE BY " + str(min(rhythmVals)))
                        rhythmVal -= min(rhythmVals) 
                    rhythmValsPicked.append(rhythmVal)

                # choose pitch of next note
                newNote = 0
                # 0 is a rest, rests have a 1/16 chance of getting picked
                rest = random.randrange(0,16)
                add800 = False
                # 0 or 1 is a leap, leaps have a 1/5 chance of getting picked
                # mod2==0 is up, mod2==1 is down.
                motionType = random.randrange(0, 10)
                # if rest picked, move on
                if rest == 0 and not prevRest:
                    #print(str(i) + ": Rest Picked!")
                    newNote = prev+800
                    prevRest = True
                else:
                    restOffset = 0
                    if prevRest:
                        restOffset = 800
                    if justLeaped[0] == 0 and motionType < 2: goLeap = True
                    # LEAP LOGIC
                    if goLeap:
                        # find legal leaps
                        legalLeaps = findLegalLeaps(prev-restOffset, scale, motionType, phraseRange)
                        newNote = random.choice(legalLeaps)
                        justLeaped = (2, motionType) # legalLeaps[1] instead of motionType
                        goLeap = False
                    # POST-LEAP BALANCE LOGIC
                    elif justLeaped[0] > 0:
                        prevVal = justLeaped[0]
                        # direction overrides to opposite of the previous leap
                        oppFromLeap = 1
                        if justLeaped[1] == 1:
                            oppFromLeap = 0
                        legalSteps = findLegalSteps(prev-restOffset, scale, oppFromLeap, phraseRange)
                        newNote = random.choice(legalSteps)
                        lastDir = justLeaped[1]
                        justLeaped = (prevVal-1, lastDir)
                    # STEP LOGIC
                    else:
                        # find legal steps
                        legalSteps = findLegalSteps(prev-restOffset, scale, motionType%2, phraseRange)
                        newNote = random.choice(legalSteps)
                    prevRest = False
                melody.append((newNote%12, newNote))    

                # choose artics for next note
                doneWithTech = False
                availPool = [a for a in articChoices]
                if len(rhythmValsPicked) > 1:
                    if rhythmValsPicked[-2] > 1:
                        for j in range(2):
                            for i in range(9,18):
                                #availPool.append(i)
                                availPool.append(9)
                articChoice = random.choice(availPool)
                if inSlur > 0:
                    # 3 for now, move up to 6
                    if inSlur < 3:
                        articChoice = random.choice([0,0,18,19])
                        if articChoice == 19:
                            print("STOPPING SLUR")
                            inSlur = 0
                        else:
                            inSlur += 1
                    else:
                        print("AUTO STOP SLUR")
                        articChoice = 19
                        inSlur = 0
                    doneWithTech = True
                elif not doneWithTech and inNonVib > 0:
                    if inNonVib < 3:
                        if 10 in availPool:
                            availPool.remove(10)
                        availPool.append(20)
                        articChoice = random.choice(availPool)
                        if articChoice == 20:
                            inNonVib = 0
                        else:
                            inNonVib += 1
                    else:
                        print("AUTO STOP NONVIB")
                        articChoice = 20
                        inNonVib = 0
                    doneWithTech = True
                elif not doneWithTech and inPizz > 0:
                    if inPizz < 3:
                        if 11 in availPool:
                            availPool.remove(11)
                        availPool.append(21)
                        availPool.append(22)
                        availPool.append(23)
                        articChoice = random.choice(availPool)
                        if articChoice == 23:
                            inPizz = 0
                        else:
                            inPizz += 1
                    else:
                        print("AUTO STOP PIZZ")
                        articChoice = 23
                        inPizz = 0
                    doneWithTech = True
                elif inSlur == 0 and articChoice == 9:
                    print("Enetering SLUR mode.")
                    inSlur += 1
                elif inNonVib == 0 and articChoice == 10:
                    print("Entering NOVIB mode.")
                    inNonVib += 1
                elif inPizz == 0 and articChoice == 11:
                    print("Entering PIZZ mode.")
                    inPizz += 1
                print(str(inSlur) + " " + str(inNonVib) + " " + str(inPizz))
                print()
                artics.append(articChoice)
                
                # update spaceLeft
                if choosingRhythms:
                    spaceLeft = length - sum(rhythmValsPicked)
                else:
                    spaceLeft -= 1
                prev = newNote
                i += 1
        
        ogMel = [x for x in melody]
        melody = [((x[0]+offset)%12,x[1]+offset) for x in ogMel] 
        return melToLily(melody, scaleDict, dynams, artics, rhythmVals, rhythmValsPicked, cad, ogMel)

    # build the scale
    def buildScale(scaleType, log=False):
        print("Building scale...")
        # add WT-0, WT-1, OT-0, OT-1, OT-2
        # make random actually choose a random scale
        # change current random form to 'build' form
        if scaleType == "major":
            scale = {0,2,4,5,7,9,11}
        elif scaleType == "major pentatonic":
            scale = {0,2,4,7,9}
        elif scaleType == "minor":
            scale = {0,2,3,5,7,8,10}
        elif scaleType == "minor pentatonic":
            scale = {0,3,5,7,10}
        elif scaleType == "harmonic minor":
            scale = {0,2,3,5,7,8,11}
        elif scaleType == "chromatic":
            scale = {0,1,2,3,4,5,6,7,8,9,10,11}
        elif scaleType == "wt-0":
            scale = {0,2,4,6,8,10}
        elif scaleType == "wt-1":
            scale = {1,3,5,7,9,11}
        else:
            scale = {0}
            ct = 0
            curr = 0
            while ct < 5:
                i = random.randrange(1,5)
                curr += i
                if curr >= 12: 
                    scale.add(curr-12) 
                else: 
                    scale.add(curr)
                ct += 1
                if not ct == 5:
                    print(scale)
        print(scale)
        print("Built scale.")
        scales.append(scale)
        return scale
    
    # find LEAPS in the scale that are no more than a tenth away from a starting note
    def findLegalLeaps(note, scale, direction, bounds):
        # if failing in one direction, TRY THE OTHER and adjust data if success.
        legalLeaps = []
        leapStart = 5
        leapEnd = 13
        leapInc = 1
        if direction == 1:
            leapStart = -5
            leapEnd = -13
            leapInc = -1
        dist = leapStart
        while not dist == leapEnd:
            possLeap = note + dist
            if possLeap%12 in scale:
                if possLeap in bounds:
                    #print("LEAP ADDED")
                    legalLeaps.append(possLeap)
            dist += leapInc
        if not legalLeaps:
            #print("No legal leaps found.")
            # Try other direction!
            return [note]
        #print("Legal leaps found.")
        return legalLeaps

    # find STEPS in the scale from a starting note
    def findLegalSteps(note, scale, direction, bounds):
        #print("Finding legal steps...")
        #print("Note: " + str(note%12))
        #print("Scale: " + str(scale))
        #print("Direction: " + str(direction))
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
            #print("Trying PossStep " + str(possStep) + "...")
            #print("Legal Notes: " + str(legalNotes))
            if possStep%12 in scale:
                if possStep in bounds:
                    #print("PossStep added for note " + str(note%12) + ": " + str(possStep))
                    legalSteps.append(possStep)
            dist += stepInc
        if not legalSteps:
            #print("No legal steps found. Repeating note.")
            # Try other direction!!
            return [note]
        #print("Legal steps found.")
        return legalSteps

    # generate the available rhythmic value choices for a melody
    def genRhythmVals(log=False):
        if log:
            print("Generating rhythm value map...")        
        rhythmVals = []
        vals = [0.25,0.5,0.75,1,1.5,2,3,4]
        pips = [10,100,1000]

        # randomly boost the frequency of any of the first three vals 
        for i in range(0,len(vals)):
            pipCount = random.choice(pips)
            dieRoll = random.randrange(1, pipCount)
            for j in range(dieRoll):
                rhythmVals.append(vals[i])

        if log:
            print(rhythmVals)
            print("Rhythm value map generated.\n")
        # for debugging purposes
        return [0.25,0.25,0.5,0.5,0.5,0.5,0.75,1,1,1,1,1,1,1,1,1.5,2,2,2,3,4]
        #return rhythmVals

    # translate melNums to LilyPond code
    def melToLily(mel, sc, dynams, artics, rhythmVals, rhythmValsPicked, cad, ogMel=[]):
        global meter
        lilyMelody = []
        i = 0
        while i < len(mel):
            semis = mel[i][1]
            # 0-8 artics, (9 openSlur, 18 port, 19 closeSlur), (10 non-vib, 20 vib), 
            # (11 pizz, 21 snap, 22 stopped, 23 arco)
            articLily = {0:"",1:"\\accent ",2:"\\espressivo ",3:"\\marcato ",4:"\\fermata ",
                         5:"\\staccatissimo ",6:"\\staccato ",7:"\\tenuto ", 8:"\\trill ",
                         9:"\\( ", 10:"^\\markup non-vib. ", 11:"^\\markup pizz. ", 
                         12:"^\\markup \"sul ponticello\" ", 13:"^\\markup \"sul tasto\" ", 
                         14:"\\staccato ^\\markup \"col legno\" ", 
                         15:"\\staccato ^\\markup \"au talon\" ", 16:"^\\markup \"sotto voce\" ",  
                         17:"^\\markup flautando ", 18:"\\portato ", 19:"\\) ", 20:"^\\markup vib. ",
                         21:"\\snappizzicato ", 22:"\\stopped ", 23:"^\\markup arco "}
            rhythmToLily = {0.25:"16",0.5:"8",0.75:"8.",1:"4",1.5:"4.",2:"2",3:"2.",4:"1",6:"1.",8:"\\breve"}
            s = ""
            if semis > 700:
                lilyMelody.append("r" + rhythmToLily[rhythmValsPicked[i]])
                i += 1
                continue
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
            s += rhythmToLily[rhythmValsPicked[i]]
            s += articLily[artics[i]]
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

        return [retStr, [x[1] for x in mel], dynams, artics, rhythmVals, rhythmValsPicked, ogMel]

    # use makeMel to write a melodic phrase
    def makeSection(scaleDict, scaleType, offset, aLength, bLength, newMel, cad, eat=2):
        global fullMel
        global bass
        global tenor
        global alto

        # writing motif
        if newMel:
            # generate rhythm profile
            rhythmVals = genRhythmVals()
            # for solo writing
            if cad == "A":
                mel = makeMel(offset, scaleDict[offset%12], scaleType, [(0,0)], 0, aLength, cad+"Scale", [], [], rhythmVals, [], True)
                mels.append(mel)
                fullMel += mel[0]
            if cad == "B":                      
                mel = makeMel(offset, scaleDict[offset%12], scaleType, [], mels[0][-1][-1][1], aLength, cad, [], [], rhythmVals, [], True)
                bMels.append(mel)
                fullMel += mel[0]
            if cad == "endSolo":
                endMel = makeMel(offset, scaleDict[offset%12], scaleType, [], mels[0][-1][-1][1], 1, cad, [0], [0], [4], [], True)
                fullMel += endMel[0]   
            # for two-part phasing
            if cad == "phaseA":
                mel = makeMel(offset, scaleDict[offset%12], scaleType, [(0,0)], [], aLength, cad+"Scale", [], [], rhythmVals, [], True)
                mels.append(mel)
            if cad == "phaseB":
                bTrans = [(x[0],x[1]-24) for x in mels[0][-1][:-1]]
                b = makeMel(offset, scaleDict[offset%12], scaleType, bTrans, [], bLength, cad, mels[0][2][:-1], mels[0][3][:-1], mels[0][4], mels[0][5][:-1], False)
                bMels.append(b)
                tenor += b[0] 
            # for fugue
            if cad == "fugueA":
                mel = makeMel(offset+12, scaleDict[(offset+12)%12], scaleType, [(0,0)], [], aLength, cad+"Scale", [], [], rhythmVals, [], True)
                mels.append(mel)
                fullMel += mel[0]
                # create buffer for part entrances
                a = makeMel(offset, scaleDict[offset%12], scaleType, [(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800)], [], 9, cad, [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [2], [2,2,2,2,2,2,2,2,2], True)
                t = makeMel(offset, scaleDict[offset%12], scaleType, [(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800)], [], 14, cad, [0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0], [2], [2,2,2,2,2,2,2,2,2,2,2,2,2,2], True)
                b = makeMel(offset, scaleDict[offset%12], scaleType, [(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800),(0,800)], [], 21, cad, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [2], [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2], True)
                alto += a[0]
                tenor += t[0]
                bass += b[0]
            if cad == "fugueB":
                mel = makeMel(offset+12, scaleDict[(offset+12)%12], scaleType, [(0,0)], [], bLength, cad, [], [], rhythmVals, [], True)
                mels.append(mel)
                a = makeMel(offset, scaleDict[(offset)%12], scaleType, mels[-1][-1], [], aLength, cad, mels[-1][2], mels[-1][3], mels[-1][4], mels[-1][5], False)
                t = makeMel(offset-12, scaleDict[(offset-12)%12], scaleType, mels[-1][-1], [], aLength, cad, mels[-1][2], mels[-1][3], mels[-1][4], mels[-1][5], False)
                b = makeMel(offset-24, scaleDict[(offset-24)%12], scaleType, mels[-1][-1], [], aLength, cad, mels[-1][2], mels[-1][3], mels[-1][4], mels[-1][5], False)
                fullMel += mel[0]
                alto += a[0]
                tenor += t[0]
                bass += b[0]
            if cad == "fugueEnd":
                endMel = makeMel(offset, scaleDict[offset%12], scaleType, [(0,0)], [], 1, cad, [0], [0], [4], [], True)
                endMelA = makeMel(offset, scaleDict[offset%12], scaleType, [(-12,-12)], [], 1, cad, [0], [0], [4], [], True)
                endMelT = makeMel(offset, scaleDict[offset%12], scaleType, [(-12,-12)], [], 1, cad, [0], [0], [4], [], True)
                endMelB = makeMel(offset, scaleDict[offset%12], scaleType, [(-24,-24)], [], 1, cad, [0], [0], [4], [], True)
                fullMel += endMel[0]
                alto += endMelA[0]
                tenor += endMelT[0]
                bass += endMelB[0]
        
        # repeating motif
        else:
            # for solo
            if cad == "A":
                mel = makeMel(offset, scaleDict[offset%12], scaleType, mels[0][-1], mels[0][-1][-1][1], aLength, cad, mels[0][2], mels[0][3], mels[0][4], mels[0][5], False)
                fullMel += mel[0]
            if cad == "Aend":
                # finalize with the exact melody
                mel = makeMel(offset, scaleDict[offset%12], scaleType, mels[0][-1], bMels[0][-1][-1][1], aLength-2, cad, mels[0][2], mels[0][3], mels[0][4], mels[0][5], False)
                # eat some beats and rewrite a more finishing tail
                #mel = makeMel(offset, scaleDict[offset%12], scaleType, mels[0][-1][:-2], aLength-2, cad, mels[0][2][:-2], mels[0][3][:-2], mels[0][4][:-2], mels[0][5][:-2], False)
                fullMel += mel[0]
            if cad == "B":
                mel = makeMel(offset, scaleDict[offset%12], scaleType, bMels[0][-1], [], bLength, cad, bMels[0][2], bMels[0][3], bMels[0][4], bMels[0][5], False)
                fullMel += mel[0]
            # for two-part phasing
            if cad == "phaseA":
                mel = makeMel(offset, scaleDict[offset%12], scaleType, mels[0][-1], [], aLength, cad, mels[0][2], mels[0][3], mels[0][4], mels[0][5], False)
                fullMel += mel[0]
            if cad == "phaseB":
                b = makeMel(offset, scaleDict[offset%12], scaleType, bMels[0][-1], [], bLength, cad, bMels[0][2], bMels[0][3], bMels[0][4], bMels[0][5], False)
                tenor += b[0]
            if cad == "fullPhaseB":
                mel = makeMel(offset, scaleDict[offset%12], scaleType, [(x[0],x[1]-24) for x in mels[0][-1]], [], aLength, cad, mels[0][2], mels[0][3], mels[0][4], mels[0][5], False)
                tenor += mel[0]
            # for fugue
            if cad == "fugueA":
                mel = makeMel(offset+12, scaleDict[(offset+12)%12], scaleType, mels[0][-1], mels[0][-1][-1][1], aLength, cad, mels[0][2], mels[0][3], mels[0][4], mels[0][5], False)
                a = makeMel(offset, scaleDict[(offset)%12], scaleType, mels[0][-1], mels[0][-1][-1][1], aLength, cad, mels[0][2], mels[0][3], mels[0][4], mels[0][5], False)
                t = makeMel(offset-12, scaleDict[(offset-12)%12], scaleType, mels[0][-1], mels[0][-1][-1][1], aLength, cad, mels[0][2], mels[0][3], mels[0][4], mels[0][5], False)
                b = makeMel(offset-24, scaleDict[(offset-24)%12], scaleType, mels[0][-1], mels[0][-1][-1][1], aLength, cad, mels[0][2], mels[0][3], mels[0][4], mels[0][5], False)
                fullMel += mel[0]
                alto += a[0]
                tenor += t[0]
                bass += b[0]
            if cad == "fugueB":
                mel = makeMel(offset+12, scaleDict[(offset+12)%12], scaleType, mels[-1][-1], mels[0][-1][-1][1], aLength, cad, mels[-1][2], mels[-1][3], mels[-1][4], mels[-1][5], False)
                a = makeMel(offset, scaleDict[(offset)%12], scaleType, mels[-1][-1], mels[0][-1][-1][1], aLength, cad, mels[-1][2], mels[-1][3], mels[-1][4], mels[-1][5], False)
                t = makeMel(offset-12, scaleDict[(offset-12)%12], scaleType, mels[-1][-1], mels[0][-1][-1][1], aLength, cad, mels[-1][2], mels[-1][3], mels[-1][4], mels[-1][5], False)
                b = makeMel(offset-24, scaleDict[(offset-24)%12], scaleType, mels[-1][-1], mels[0][-1][-1][1], aLength, cad, mels[-1][2], mels[-1][3], mels[-1][4], mels[-1][5], False)
                fullMel += mel[0]
                alto += a[0]
                tenor += t[0]
                bass += b[0]
    
    # composes an AABA tune
    def solo(key, scaleDict, scaleType, meter):
        # USE RHYTHMIC MOTIF LOGIC HERE
        # -   generate random beat length x for rhythmic motif and store the first x beats as the motif
        # IMPLEMENT CONTOUR SHAPER THAT WRITES A MELODY FROM BOTH ENDS
        # - melody has the option of finishing back at the starting note or at the dominant of the starting note
        # Pattern: Length can be any multiple (between 1-4 for now) of the doubled numerator.
        #length = int(meter[0])*2*random.randrange(4,8)
        length = 16

        #for i in range(random.choice([2,4,6,8])):
        print("Writing A section with length " + str(length) + "...")
        makeSection(scaleDict, scaleType, key, length, length, True, "A")
        print("Restating A section...")
        makeSection(scaleDict, scaleType, key, length, length, False, "A")
        print("Writing B section with length " + str(length) + "...")
        makeSection(scaleDict, scaleType, key, length, length, True, "B")
        print("Concluding with A section...")
        makeSection(scaleDict, scaleType, key, length, length, False, "Aend")
        print("Ending solo...")
        makeSection(scaleDict, scaleType, key, 1, 1, True, "endSolo")

    # composes a freeform tune
    def freeform(key, scaleType, beats, meter):
        # SET A PRECLIM, RETPRE, CLIMAX (required), RETPRE2, AND POSTCLIM.
        # BUILD MELODY FROM BOTH ENDS!!!!
        makeSection(majScales, scaleType, key, beats, beats, True, "A")

    # composes a two-part phasing piece
    def reich(majScales, scaleAsk, offset, meter):
        aLength = random.choice([4,5,6,7,8,9,11,13,15,17])
        makeSection(majScales, scaleAsk, offset, aLength, 0, True, "phaseA")
        lengthDiff = mels[0][5][-1]
        bLength = aLength - lengthDiff
        aAdj = 1
        while not bLength%1.0==0:
            #print("Adjusting bLength: " + str(bLength))
            bLength *= 2
            aAdj *= 2
        aLength = aAdj*aLength
        bLength = int(bLength)
        print("Phase A Length: " + str(aLength))
        print("Phase B Length: " + str(bLength))
        print(mels[0][5])
        print(mels[0][5][:-1])
        makeSection(majScales, scaleAsk, offset, aLength, bLength, True, "phaseB")
        for _ in range(bLength):
            makeSection(majScales, scaleAsk, offset, aLength, bLength, False, "phaseA")
        for _ in range(aLength-1):
            makeSection(majScales, scaleAsk, offset, aLength, bLength, False, "phaseB")
        for _ in range(2):
            makeSection(majScales, scaleAsk, offset, aLength, bLength, False, "phaseA")
            makeSection(majScales, scaleAsk, offset, aLength, bLength, False, "fullPhaseB")

    # composes a fugue (WORK IN PROGRESS)
    def fugue(majScales, scaleAsk, offset, meter):
        aLength = random.choice([12,16,32,64])
        bLength = random.choice([12,16,32,64])
        print("Subject Length: " + str(aLength))
        #print("A")
        makeSection(majScales, scaleAsk, offset, aLength, aLength, True, "fugueA")
        #print("ReA")
        makeSection(majScales, scaleAsk, offset, aLength, aLength, False, "fugueA")
        #print("B")
        makeSection(majScales, scaleAsk, offset, bLength, bLength, True, "fugueB")
        #makeSection(majScales, scaleAsk, offset, bLength, bLength, False, "fugueB")
        #print("ReA")
        makeSection(majScales, scaleAsk, offset, aLength, aLength, False, "fugueA")
        #print("End")
        makeSection(majScales, scaleAsk, offset, 1, 1, True, "fugueEnd")
        
    # ask the user what scale they want to use
    def scaleAsk():
        sc = ""
        viableScales = {"major":0,"major pentatonic":1,"minor":2,"minor pentatonic":3,"harmonic minor":4,"chromatic":5,"wt-0":6,"wt-1":7}
        inpStr = "What kind of scale would you like to use for your piece? Enter the corresponding number.\n"
        for x in viableScales.keys():
            inpStr += "\n- " + x + " (" + str(viableScales[x]) + ")" 
        inpStr += "\n- random choice (8)"
        inpStr += "\n- random build (9)\n\n"
        ans = input(inpStr)
        print()
        if ans == "8":
            ans = str(random.choice(list(viableScales.values())))
        if ans not in [str(x) for x in viableScales.values()]:
            print("Your melody will use a randomly built scale.")
        else:
            for y in viableScales.keys():
                if str(viableScales[y]) == ans:
                    sc = y
                    break
            print("Your melody will use the " + sc + " scale.")            
        print("Tonal center of " + majScales[0][offset] + " chosen.")
        return sc

    # write the lilyPond code to output file
    def printFile(scaleStart, scaleQual, mode, time, tempo, m, a, t, b):
        scaleStartTrans = {"c":"C","cis":"C#","des":"D-Flat","d":"D","dis":"D#","ees":"E-Flat","e":"E",
                           "fes":"F-Flat","f":"F","fis":"F#","ges":"G-Flat","g":"G","gis":"G#",
                           "aes":"A-Flat","a":"A","ais":"A#","bes":"B-Flat","b":"B","ces":"C-Flat"}
        if mode == "solo" or mode == "freeform":
            # instead of using scaleStart as title, use moodAnalyzer!
            code = "\\header {\n  title = \"" + scaleStartTrans[scaleStart] + " " + scaleQual.capitalize() + " " + mode.capitalize() + " \"\n}\n\n"
            code += "\\score {\n"
            code += "\\" + "new Staff { \set Staff.midiInstrument = \"violin\" \clef \"treble\" \\key " + scaleStart + " \\" + scaleQual + " "
            code += "\\time " + time[0] + " \\tempo " + tempo[0] + " " + time[1] + " = " + tempo[1] + " " + m + "}\n"
            #code += "\\midi{}\n"
            code += "}\n"
            code += "\\version \"2.22.2\""
            f = open("ConvertMe.ly", "w")
            f.write(code)
            f.close()
        elif mode == "reich":
            code = "\\header {\n  title = \"" + scaleStartTrans[scaleStart] + " " + scaleQual.capitalize() + " " + mode.capitalize() + " \"\n}\n\n"
            code += "\\score {\n"
            code += "\\new PianoStaff <<"
            code += "\\" + "new Staff { \set Staff.midiInstrument = \"violin\" \clef \"treble\" \\key " + scaleStart + " \\" + scaleQual + " "
            code += "\\time " + time[0] + "\\tempo " + tempo[0] + " " + time[1] + " = " + tempo[1] + " " + m + "}\n"
            code += "\\" + "new Staff { \set Staff.midiInstrument = \"cello\" \clef \"bass\" \\key " + scaleStart + " \\" + scaleQual + " "
            code += "\\time " + time[0] + "\\tempo " + tempo[0] + " " + time[1] + " = " + tempo[1] + " " + t + "}\n"
            code += ">>\n"
            #code += "\\midi{}\n"
            code += "}\n"
            code += "\\version \"2.22.2\""
            f = open("ConvertMe.ly", "w")
            f.write(code)
            f.close()
        else:
            code = "\\header {\n  title = \"" + scaleStartTrans[scaleStart] + " " + scaleQual.capitalize() + " " + mode.capitalize() + " \"\n}\n\n"
            code += "\\score {\n"
            code += "\\new PianoStaff <<"
            code += "\\" + "new Staff { \set Staff.midiInstrument = \"violin\" \clef \"treble\" \\key " + scaleStart + " \\" + scaleQual + " "
            code += "\\time " + time[0] + "\\tempo " + tempo[0] + " " + time[1] + " = " + tempo[1] + " " + m + "}\n"
            code += "\\" + "new Staff { \set Staff.midiInstrument = \"viola\" \clef \"treble\" \\key " + scaleStart + " \\" + scaleQual + " "
            code += "\\time " + time[0] + "\\tempo " + tempo[0] + " " + time[1] + " = " + tempo[1] + " " + a + "}\n"
            code += "\\" + "new Staff { \set Staff.midiInstrument = \"cello\" \clef \"bass\" \\key " + scaleStart + " \\" + scaleQual + " "
            code += "\\time " + time[0] + "\\tempo " + tempo[0] + " " + time[1] + " = " + tempo[1] + " " + t + "}\n"
            code += "\\" + "new Staff { \set Staff.midiInstrument = \"contrabass\" \clef \"bass\" \\key " + scaleStart + " \\" + scaleQual + " "
            code += "\\time " + time[0] + "\\tempo " + tempo[0] + " " + time[1] + " = " + tempo[1] + " " + b + "}\n"
            code += ">>\n"
            code += "\\midi{}\n"
            code += "}\n"
            code += "\\version \"2.22.2\""
            f = open("ConvertMe.ly", "w")
            f.write(code)
            f.close()

    # MAIN
    print("\nWelcome to ACE.\n")
    offset = random.randrange(0,12)
    # add to meters once supported: {"3/8":"4.","6/8":"4.","9/8":"4.","12/8":"4."}
    # meters = {"2/4":"4","3/4":"4","4/4":"4","5/4":"4","6/4":"4"}
    meters = {"4/4":"4"}
    #tempos = {"Adagio":(55,71),"Andante":(71,87),"Moderato":(87,110),"Allegro":(110,132),"Vivace":(132,168),"Presto":(168,200)}
    tempos = {"Adagio":(55,71),"Andante":(71,87),"Moderato":(87,110),"Allegro":(110,132)}
    meter = random.choice(list(meters.keys()))
    bpmFormat = meters[meter]
    tempoMark = random.choice(list(tempos.keys()))
    bpm = str(random.randrange(tempos[tempoMark][0],tempos[tempoMark][1]))
    #fileName = sys.argv[1]

    # MODE LOGIC
    # possibly setup 'serial' as scale choice rather than mode choice?
    # make 'raga' mode -> need drone
    # make 'mirror' mode -> part of build from both ends
    viableModes = ["solo","freeform","reich","fugue"]
    modeChoice = input("Choose your mode by entering its keyword.\n\n- AABA Solo (solo)\n- Freeform Solo (freeform)\n- Phasing Piece (reich)\n- Fugue (fugue)\n\n")
    if modeChoice not in viableModes:
        modeChoice = "freeform"
    print("\nYou have chosen " + modeChoice + " mode.\n")
    # ask what scale the user wants to use
    scaleType = scaleAsk()
    scaleChart = majScales
    if scaleType == "minor" or scaleType == "minor pentatonic" or scaleType == "harmonic minor":
        scaleChart = minScales
    print()
    if modeChoice == 'solo':
        print("A solo melody will be generated.\n")
        solo(offset, scaleChart, scaleType, meter)
    elif modeChoice == "freeform":
        print("A freeform melody will be generated.\n")
        freeform(offset, scaleType, random.randrange(32,256), meter)
    elif modeChoice == "reich":
        print("Reich fan huh? Well - hopefully this will change your mind.\nA two-part phasing piece will be generated.\n")
        reich(majScales, scaleType, offset, meter)
    elif modeChoice == "fugue":
        print("THIS FEATURE IS A WORK IN PROGRESS. BE READY TO COVER YOUR EARS.")
        fugue(majScales, scaleType, offset, meter)

    # EXPORT LOGIC
    print("Exporting song to .ly...")
    # set scale values back to their abstract value
    scaleStart = majScales[0][0]
    if scaleType == "minor" or scaleType == "minor pentatonic" or scaleType == "harmonic minor":
        scaleStart = minScales[0][offset]
        scaleType = "minor"
    elif scaleType == "major" or scaleType == "major pentatonic":
        scaleStart = majScales[0][offset]
        scaleType = "major"
    else:
        scaleType = "major"
    printFile(scaleStart, scaleType, modeChoice, (meter, bpmFormat), (tempoMark, bpm), fullMel, alto, tenor, bass)
    print("Done.\n")

if __name__ == "__main__":
    main()