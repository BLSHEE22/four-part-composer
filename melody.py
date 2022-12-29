from datetime import date
from datetime import datetime
import random
import math
import sys

# GLOBAL list of melodies and rhythms
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
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
# add to meters once supported: {"3/8":"4.","6/8":"4.","9/8":"4.","12/8":"4."}
# meters = {"2/4":"4","3/4":"4","4/4":"4","5/4":"4","6/4":"4"}
meters = {"4/4":"4"}
#tempos = {"Adagio":(55,71),"Andante":(71,87),"Moderato":(87,110),"Allegro":(110,132),"Vivace":(132,168),"Presto":(168,200)}
tempos = {"Adagio":(55,71),"Andante":(71,87),"Moderato":(87,110),"Allegro":(110,132)}
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
minScales = {-1:{0:"c",1:"cis",2:"d",3:"ees",4:"e",5:"f",6:"fis",7:"g",8:"gis",9:"a",10:"bes",11:"b"},
                0:{0:"c",1:"des",2:"d",3:"ees",4:"e",5:"f",6:"ges",7:"g",8:"aes",9:"a",10:"bes",11:"b"},
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

    # print ACE header
    def printHeader():
        print(OKGREEN,end="")
        print("#"*218,end="")
        print(FAIL,end="")
        print("ALGORITHMIC COMPOSITION ENGINE",end="")
        print(OKGREEN,end="")
        print("#"*220,end="")
        print(ENDC)

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
        # performance techniques are given a chance to be notated after every quarter note or longer
        # leaps occur 40% of the time and are always followed by TWO OR MORE non-leaps in the opposite direction of the leap
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
            '''
            if connDist < -6:
                starter[0] = (temp[0]+12,temp[1]+12)
            elif connDist > 6:
                starter[0] = (temp[0]-12,temp[1]-12)
            '''
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
        inTech = 0
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
        # if prev is a rest, rescale the pitch
        if prev > 700:
            prev -= 800
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
                # choose ###RHYTHM### of next note
                if choosingRhythms:
                    rhythmVal = random.choice(rhythmVals)
                    if not spaceLeft%1 == 0:
                        syncoBeatCnt += rhythmVal
                    else:
                        syncoBeatCnt = 0
                    # allowed synco beats
                    if syncoBeatCnt > 2:
                        def findUpperOdd(val):
                            while True:
                                if math.ceil(val)%2 == 0:
                                    return math.ceil(val)
                                val += 1
                        # get to the nearest strong beat
                        #rhythmVal = findUpperOdd(length-spaceLeft) - (length-spaceLeft)
                        # get to the nearest quarter
                        rhythmVal = math.ceil(length-spaceLeft) - (length-spaceLeft)
                        #print("Decided rhythm value: " + str(rhythmVal))
                    # find a shorter rhythm if chosen rhythm is too big
                    while rhythmVal not in rhythmVals or rhythmVal > spaceLeft:
                        if rhythmVal == min(rhythmVals):
                            break
                        #print("SHORTENING RHYTHM VALUE BY " + str(min(rhythmVals)))
                        rhythmVal -= min(rhythmVals) 
                    rhythmValsPicked.append(rhythmVal)

                # choose ###PITCH### of next note
                newNote = 0
                # 0 is a rest, rests have a 1/16 chance of getting picked
                rest = random.randrange(0,16)
                add800 = False
                # 0 or 1 is a leap, leaps have a 4/10 chance of getting picked
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
                    if justLeaped[0] == 0 and motionType < 4: goLeap = True
                    # LEAP LOGIC
                    if goLeap:
                        # find legal leaps
                        legalLeaps = findLegalLeaps(prev-restOffset, scale, motionType%2, phraseRange)
                        newNote = random.choice(legalLeaps)
                        justLeaped = (2, motionType%2) # legalLeaps[1] instead of motionType
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

                # choose ###ARTICULATIONS### for next note
                doneWithTech = False
                techs = [12,13,14,15,16,17]
                availPool = [a for a in articChoices]
                if len(rhythmValsPicked) > 1:
                    if rhythmValsPicked[-2] > 1:
                        for j in range(3):
                            for i in range(9,18):
                                availPool.append(i)
                # don't choose any artics for rests
                if not rest == 0:
                    articChoice = random.choice(availPool)
                else:
                    articChoice = 0
                # while in slur mode
                if inSlur > 0:
                    if inSlur < 4:
                        if rest == 0:
                            artics[-1] = 19
                            articChoice = 0
                            inSlur = 0
                        elif spaceLeft < 4:
                            articChoice = 19
                            inSlur = 0
                        else:
                            articChoice = random.choice([0,0,18,19])
                            if articChoice == 19:
                                inSlur = 0
                            else:
                                inSlur += 1
                    else:
                        articChoice = 19
                        inSlur = 0
                    doneWithTech = True
                # while in non-vib mode
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
                        #print("AUTO STOP NONVIB")
                        articChoice = 20
                        inNonVib = 0
                    doneWithTech = True
                # while in pizz mode
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
                        #print("AUTO STOP PIZZ")
                        articChoice = 23
                        inPizz = 0
                    doneWithTech = True
                # while in tech mode
                elif not doneWithTech and inTech > 0:
                    if inTech < 8:
                        availPool = [a for a in articChoices]
                        if inTech > 5:
                            for _ in range(2):
                                availPool.append(24)
                        articChoice = random.choice(availPool)
                        if articChoice == 24:
                            inTech = 0
                        else:
                            inTech += 1
                    else:
                        #print("AUTO STOP TECH")
                        articChoice = 24
                        inTech = 0
                    doneWithTech = True
                # entering slur mode
                elif inSlur == 0 and articChoice == 9 and not rest == 0:
                    inSlur += 1
                # entering non-vib mode
                elif inNonVib == 0 and articChoice == 10 and not rest == 0:
                    inNonVib += 1
                # entering pizz. mode
                elif inPizz == 0 and articChoice == 11 and not rest == 0:
                    inPizz += 1
                # entering tech mode
                elif inTech == 0 and articChoice in techs and not rest == 0:
                    inTech += 1
                #print(str(inSlur) + " " + str(inNonVib) + " " + str(inPizz) + " " + str(inTech))
                #print()
                artics.append(articChoice)

                # choose ###DYNAMICS### for next note
                
                # update spaceLeft
                if choosingRhythms:
                    spaceLeft = length - sum(rhythmValsPicked)
                else:
                    spaceLeft -= 1
                prev = newNote
                i += 1
        # if ending B too far away from the start of A, bridge the gap
        if cad == "B":
            endB = melody[-1][1]
            startA = mels[0][-1][0][1]
            connDist = endB - startA
            if not connDist == 12 and not connDist == -12:
                if connDist < -6:
                    melody[-1] = (melody[-1][0]+12,melody[-1][1]+12)
                elif connDist > 6:
                    melody[-1] = (melody[-1][0]-12,melody[-1][1]-12)
        # if we tried a slur on the last note, remove it
        if artics[-1] == 9:
            artics[-1] = 0
        # if we ended in slur mode, end the slur
        if not inSlur == 0:
            artics[-1] = 19
        ogMel = [x for x in melody]
        melody = [((x[0]+offset)%12,x[1]+offset) for x in ogMel] 
        return melToLily(melody, scaleDict, dynams, artics, rhythmVals, rhythmValsPicked, cad, ogMel)

    # build the scale
    def buildScale(scaleType, log=False):
        #print("Building scale...")
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
        elif scaleType == "wt-0" or scaleType == "wt-1":
            scale = {0,2,4,6,8,10}
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
        #print(scale)
        #print("Built scale.")
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

        # randomly boost the frequency of all the vals 
        for i in range(0,len(vals)):
            pipCount = random.choice(pips)
            dieRoll = random.randrange(1, pipCount)
            for j in range(dieRoll):
                rhythmVals.append(vals[i])

        # for debugging purposes
        rhythmVals =  [0.25,0.25,0.5,0.5,0.5,0.5,0.75,1,1,1,1,1,1,1,1,1.5,2,2,2,3,4]
        if log:
            print()
            for x in vals:
                print("{0:5s}: ".format(str(x)) + str(rhythmVals.count(x)))
            print()
            print("Rhythm value map generated.\n")
        return rhythmVals

    # translate melNums to LilyPond code
    def melToLily(mel, sc, dynams, artics, rhythmVals, rhythmValsPicked, cad, ogMel=[]):
        #print(mel)
        lilyMelody = []
        i = 0
        m = 4.0
        qsUsed = 0
        totalUsed = 0
        qsBeforeTie = float(meter[:meter.index("/")])/float(int(meter[meter.index("/")+1:])/4)
        qsBeforeTie = 1
        while i < len(mel):
            semis = mel[i][1]
            # 0-8 artics, (9 openSlur, 18 port, 19 closeSlur), (10 non-vib, 20 vib), 
            # (11 pizz, 21 snap, 22 stopped, 23 arco)
            # think of something for 2, then boost staccato and tenuto along with accent
            # think of something for 4, write a different implementation for fermata
            # don't let staccato go onto long notes (2 or greater)
            articToLily = {0:"",1:"\\accent ",2:"\\tenuto ",3:"\\marcato ",4:"\\staccato ",
                         5:"\\staccatissimo ",6:"\\staccato ",7:"\\tenuto ", 8:"\\trill ",
                         9:"\\( ", 10:"^\\markup non-vib. ", 11:"^\\markup pizz. ", 
                         12:"^\\markup \"sul ponticello\" ", 13:"^\\markup \"sul tasto\" ", 
                         14:"\\staccato ^\\markup \"col legno\" ", 
                         15:"\\staccato ^\\markup \"au talon\" ", 16:"^\\markup \"sotto voce\" ",  
                         17:"^\\markup flautando ", 18:"\\portato ", 19:"\\) ", 20:"^\\markup vib. ",
                         21:"\\snappizzicato ", 22:"\\stopped ", 23:"^\\markup arco ", 24:"^\\markup naturale "}
            rhythmToLily = {0.25:"16",0.5:"8",0.75:"8.",1:"4",1.5:"4.",2:"2",3:"2.",4:"1",6:"1.",8:"\\breve"}
            s = ""
            qsUsed += rhythmValsPicked[i]
            totalUsed += rhythmValsPicked[i]
            def tieUp(s, val, firstPiece, artic, meterSize, noteLength, barPlace, barSize):
                #print("Writing tie piece of length " + str(val) + "...")
                #print(artic)
                persistArtics = ["\\)","\\(","\\portato"]
                lastArtic = artic
                if artic not in persistArtics:
                    lastArtic = ""
                # print(str(float(noteLength)) + " " + str(float(barPlace)) + " " + str(float(barSize)) + " " + str(float(meterSize)))
                # noteLength = 0.5, barSize = 4.25
                # startPiece = 0.25, middlePiece = 0, endPiece = 0.25
                startPiece = 0
                middlePiece = 0
                endPiece = 0
                # Find illegal rhythms and take the biggest bite we can off to the left leg. 
                # Also remove zeros.
                def split(p):
                    for x in p:
                        if x not in rhythmToLily and not x == 0:
                            temp = x
                            tempList = []
                            while temp not in rhythmToLily:
                                temp -= 0.25
                            tempList.append(temp)
                            tempList.append(x-temp)
                            p.remove(x)
                            for y in tempList:
                                p.append(y)
                    p = [x for x in p if not x == 0]
                    return p
                # See if we can merge any two consecutive rhythms to form one legal rhythm. 
                # Beware of crossing the barline with the merge attempt.
                def merge(p):
                    initLen = len(p)
                    tempList = []
                    for j in range(initLen-1):
                        if p[j] + p[j+1] in rhythmToLily:
                            preLeg = sum(p[:j-1])
                            if j == 0:
                                preLeg = 0
                            if j == 1:
                                preLeg = p[0]
                            if ((barSize - noteLength + preLeg) < m) and not ((barSize - noteLength + preLeg + p[j] + p[j+1]) > m):
                                temp = p[j] + p[j+1]
                                tempList.append((j, temp))
                    if tempList:
                        #print("MERGE COMPLETED")
                        p.insert(tempList[0][0], tempList[0][1])
                        del(p[tempList[0][0]+1])
                        del(p[tempList[0][0]+1])
                    return p

                # if trying to tie over bar
                if barSize > m:
                    if barSize % 1 == 0:
                        endPiece = barSize - m
                        startPiece = noteLength - endPiece
                        lilyMelody.append(s + rhythmToLily[startPiece] + "~" + artic)
                        lilyMelody.append(s + rhythmToLily[endPiece] + lastArtic)
                    else:
                        endPiece = barSize - m
                        startPiece = min(1 - (barSize % 1), noteLength - endPiece)
                        middlePiece = noteLength - (startPiece + endPiece)
                        pieces = [startPiece, middlePiece, endPiece]
                        # print("After chop: " + str(pieces))
                        pieces = split(pieces)
                        # print("After split: " + str(pieces))
                        pieces = merge(pieces)
                        # print("After merge: " + str(pieces))
                        lilyMelody.append(s + rhythmToLily[pieces[0]] + "~" + artic)
                        for k in range(1, len(pieces)-1):
                            lilyMelody.append(s + rhythmToLily[pieces[k]] + "~" + lastArtic)
                        lilyMelody.append(s + rhythmToLily[pieces[-1]] + lastArtic)
                    return
                # if we can cancel the tie, do it
                elif (float(noteLength) == 2.0 and not float(barPlace) > 4.0 and float(barPlace) % 1 == 0.0 and 
                    not float(barSize) > 4.0) or (float(noteLength) == 3.0 and not float(barPlace) > 4.0 and 
                    float(barPlace) % 1 == 0.0 and not float(barSize) > 4.0) or (float(noteLength) == 4.0 and 
                    not float(barPlace) > 4.0 and float(barPlace) % 1 == 0.0 and not float(barSize) > 4.0):
                    # print("Cancelling tie due to measure-starting/measure-non-exceeding note.")
                    lilyMelody.append(s + rhythmToLily[noteLength] + artic)
                    return
                # if piece is bigger than our chop limit
                elif val > meterSize:
                    fillLength = val
                    pieceLength = fillLength
                    pieceDone = 0
                    while not pieceLength == 0:
                        end = ""
                        while pieceLength > meterSize:
                            pieceLength -= 0.25      
                            end = "~"
                        lilyMelody.append(s + rhythmToLily[pieceLength] + end + artic)
                        pieceDone += pieceLength
                        pieceLength = fillLength - pieceDone
                # if piece is a valid rhythm
                else:
                    lilyMelody.append(s + rhythmToLily[val] + firstPiece + artic)
                # if a non-final piece
                if firstPiece == "~":
                    tieUp(s, rhythmValsPicked[i]-val, "", "",meterSize,noteLength,barPlace,barSize)
                else:
                    return
            #print(str(i) + ": " + str(rhythmValsPicked[i]) + " | qsUsed: " + str(qsUsed) + " | totalUsed: " + str(totalUsed))
            if semis > 700:
                if qsUsed > qsBeforeTie:
                    #print("REST OVER THE BAR!!!")
                    qsUsed -= rhythmValsPicked[i]
                    qsLeft = qsBeforeTie-qsUsed
                    #print("qsLeft: " + str(qsLeft))
                    #print("qsExtra: " + str(rhythmValsPicked[i]-qsLeft))
                    #if rhythmValsPicked[i] == 3.0:
                        #qsLeft = totalUsed - rhythmValsPicked[i]
                    tieUp("r",qsLeft,"~","",qsBeforeTie,rhythmValsPicked[i],qsUsed+rhythmValsPicked[i],totalUsed)
                    qsUsed += rhythmValsPicked[i]
                else:
                    lilyMelody.append("r" + rhythmToLily[rhythmValsPicked[i]])
                if qsUsed > qsBeforeTie or qsUsed == qsBeforeTie:
                    qsUsed = qsUsed%qsBeforeTie
                    totalUsed = totalUsed%4
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
            if qsUsed > qsBeforeTie: # and not ((totalUsed-rhythmValsPicked[i])%meterSub == 0):
                #print("NOTE OVER THE BAR!!!")
                qsUsed -= rhythmValsPicked[i]
                qsLeft = qsBeforeTie-qsUsed
                #print("qsLeft: " + str(qsLeft))
                #print("qExtra: " + str(rhythmValsPicked[i]-qsLeft))
                # as long as this note ends on a downbeat and doesn't cross a barline, don't tie
                #if rhythmValsPicked[i] == 3.0:
                   #qsLeft = totalUsed - rhythmValsPicked[i]
                tieUp(sc[mel[i][0]%12] + s, qsLeft, "~", articToLily[artics[i]],qsBeforeTie,rhythmValsPicked[i],qsUsed+rhythmValsPicked[i],totalUsed)
                qsUsed += rhythmValsPicked[i]
            else:
                s += rhythmToLily[rhythmValsPicked[i]]
                s += articToLily[artics[i]]
                lilyMelody.append(sc[mel[i][0]%12] + s)
            if qsUsed > qsBeforeTie or qsUsed == qsBeforeTie:
                qsUsed = qsUsed%qsBeforeTie
                totalUsed = totalUsed%m
            i += 1
            #print(lilyMelody)

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
        # NO FERMATAS FOR REICH!!!
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
        print("Phase A Length: " + "{0:3s}".format(str(aLength))  + str(mels[0][5]))
        print("Phase B Length: " + "{0:3s}".format(str(bLength))  + str(mels[0][5][:-1]))
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
            inpStr += "\n- " + "{0:18s}".format(x) + " (" + str(viableScales[x]) + ")" 
        inpStr += "\n- random choice      (8)"
        inpStr += "\n- random build       (9)\n\n"
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
        # print("Tonal center of " + majScales[0][offset] + " chosen.")
        return sc

    # write the lilyPond code to output file
    def printFile(scaleStart, scaleName, scaleSigStart, scaleSigQual, mode, time, tempo, m, a, t, b):
        scaleStartTrans = {"c":"C","cis":"C#","des":"D-Flat","d":"D","dis":"D#","ees":"E-Flat","e":"E",
                           "fes":"F-Flat","f":"F","fis":"F#","ges":"G-Flat","g":"G","gis":"G#",
                           "aes":"A-Flat","a":"A","ais":"A#","bes":"B-Flat","b":"B","ces":"C-Flat"}
        scaleNameTrans = {"major":"Major","major pentatonic":"Major Pentatonic","minor":"Minor","minor pentatonic":"Minor Pentatonic",
                          "harmonic minor":"Harmonic Minor","chromatic":"Chromatic","wt-0":"Whole-Tone","wt-1":"Whole-Tone","":"Custom Scale"}
        if mode == "solo" or mode == "freeform":
            # instead of using scaleStart as title, use moodAnalyzer!
            #code = "\\header {\n  title = \"" + scaleStartTrans[scaleStart] + " " + scaleQual.capitalize() + " " + mode.capitalize() + " \"\n}\n\n"
            code = "\\header {\n  title = \"" + scaleStartTrans[scaleStart] + " " + scaleNameTrans[scaleName] + " " + mode.capitalize() + " \"\n}\n\n"
            code += "\\score {\n"
            code += "\\" + "new Staff { \set Staff.midiInstrument = \"violin\" \clef \"treble\" \\key " + scaleSigStart + " \\" + scaleSigQual + " "
            code += "\\time " + time[0] + " \\tempo " + tempo[0] + " " + time[1] + " = " + tempo[1] + " " + m + "}\n"
            #code += "\\midi{}\n"
            code += "}\n"
            code += "\\version \"2.22.2\""
            f = open("melody.ly", "w")
            f.write(code)
            f.close()
        elif mode == "reich":
            code = "\\header {\n  title = \"" + scaleStartTrans[scaleStart] + " " + scaleNameTrans[scaleName] + " " + mode.capitalize() + " \"\n}\n\n"
            code += "\\score {\n"
            code += "\\new PianoStaff <<"
            code += "\\" + "new Staff { \set Staff.midiInstrument = \"violin\" \clef \"treble\" \\key " + scaleSigStart + " \\" + scaleSigQual + " "
            code += "\\time " + time[0] + "\\tempo " + tempo[0] + " " + time[1] + " = " + tempo[1] + " " + m + "}\n"
            code += "\\" + "new Staff { \set Staff.midiInstrument = \"cello\" \clef \"bass\" \\key " + scaleSigStart + " \\" + scaleSigQual + " "
            code += "\\time " + time[0] + "\\tempo " + tempo[0] + " " + time[1] + " = " + tempo[1] + " " + t + "}\n"
            code += ">>\n"
            #code += "\\midi{}\n"
            code += "}\n"
            code += "\\version \"2.22.2\""
            f = open("melody.ly", "w")
            f.write(code)
            f.close()
        else:
            code = "\\header {\n  title = \"" + scaleStartTrans[scaleStart] + " " + scaleNameTrans[scaleName] + " " + mode.capitalize() + " \"\n}\n\n"
            code += "\\score {\n"
            code += "\\new PianoStaff <<"
            code += "\\" + "new Staff { \set Staff.midiInstrument = \"violin\" \clef \"treble\" \\key " + scaleSigStart + " \\" + scaleSigQual + " "
            code += "\\time " + time[0] + "\\tempo " + tempo[0] + " " + time[1] + " = " + tempo[1] + " " + m + "}\n"
            code += "\\" + "new Staff { \set Staff.midiInstrument = \"viola\" \clef \"treble\" \\key " + scaleSigStart + " \\" + scaleSigQual + " "
            code += "\\time " + time[0] + "\\tempo " + tempo[0] + " " + time[1] + " = " + tempo[1] + " " + a + "}\n"
            code += "\\" + "new Staff { \set Staff.midiInstrument = \"cello\" \clef \"bass\" \\key " + scaleSigStart + " \\" + scaleSigQual + " "
            code += "\\time " + time[0] + "\\tempo " + tempo[0] + " " + time[1] + " = " + tempo[1] + " " + t + "}\n"
            code += "\\" + "new Staff { \set Staff.midiInstrument = \"contrabass\" \clef \"bass\" \\key " + scaleSigStart + " \\" + scaleSigQual + " "
            code += "\\time " + time[0] + "\\tempo " + tempo[0] + " " + time[1] + " = " + tempo[1] + " " + b + "}\n"
            code += ">>\n"
            code += "\\midi{}\n"
            code += "}\n"
            code += "\\version \"2.22.2\""
            f = open("melody.ly", "w")
            f.write(code)
            f.close()

    # MAIN
    printHeader()
    print("\nWelcome to ACE.\n")
    offset = random.randrange(0,12)
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
    elif scaleType == "wt-0":
        while offset not in [0,2,4,6,8,10]:
            offset = random.choice([0,2,4,6,8,10])
    elif scaleType == "wt-1":
        while offset not in [1,3,5,7,9,11]:
            offset = random.choice([1,3,5,7,9,11])
    print("Tonal center of " + majScales[0][offset] + " chosen.")
    print()
    if modeChoice == 'solo':
        print("A solo melody will be generated.\n")
        solo(offset, scaleChart, scaleType, meter)
    elif modeChoice == "freeform":
        print("A freeform melody will be generated.\n")
        freeform(offset, scaleType, random.randrange(32,256), meter)
    elif modeChoice == "reich":
        print("Reich fan huh? Hopefully this will change your mind.\nA two-part phasing piece will be generated.\n")
        reich(majScales, scaleType, offset, meter)
    elif modeChoice == "fugue":
        print("THIS FEATURE IS A WORK IN PROGRESS. BE READY TO COVER YOUR EARS.")
        fugue(majScales, scaleType, offset, meter)

    # ANALYSIS
    # Give points for: variety of pitches, pitches stressing intended center (key-defining pitches), arcing contour, wide dynamics, good voice leading
    # Take away points for: lack of variety of pitches, pitches stressing NON-intended center, flat contour, narrow dynamics, 
    # --------------------: too large distances between consecutive notes
    pitchAnalysis = sorted([x[0] for x in mels[-1][-1] if not int(x[1]) > 700])
    def count_elements(seq) -> dict:
        hist = {}
        for i in seq:
            hist[i] = hist.get(i, 0) + 1
        return hist
    def ascii_histogram(seq) -> None:
        counted = count_elements(seq)
        for k in sorted(counted):
            print('{0:5d} {1}'.format(k, '+' * counted[k]))
    print("Analyzing solo...")
    ascii_histogram(pitchAnalysis)
    print("Solo passed tests. Proceeding to export stage.\n")

    # EXPORT LOGIC
    print("Exporting song to .ly...")
    # set scale values back to their abstract value
    scaleStart = majScales[0][offset]
    scaleSigStart = majScales[0][0]
    scaleSigQual = "major"
    if scaleType == "minor" or scaleType == "minor pentatonic" or scaleType == "harmonic minor":
        scaleStart = minScales[-1][offset]
        scaleSigStart = minScales[-1][offset]
        scaleSigQual = "minor"
    elif scaleType == "major" or scaleType == "major pentatonic":
        scaleSigStart = majScales[0][offset]
    printFile(scaleStart, scaleType, scaleSigStart, scaleSigQual, modeChoice, (meter, bpmFormat), (tempoMark, bpm), fullMel, alto, tenor, bass)
    print("Done.\n")

if __name__ == "__main__":
    main()