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
minScales = {0:{0:"c",1:"des",2:"d",3:"ees",4:"e",5:"f",6:"fis",7:"g",8:"gis",9:"a",10:"bes",11:"b"},
                1:{0:"c",1:"des",2:"d",3:"ees",4:"fes",5:"f",6:"ges",7:"g",8:"aes",9:"a",10:"bes",11:"b"},
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
    def makeMel(offset, scaleDict, scaleType, starter, length, cad, rests, rhythmVals, rhythmValsPicked, log):
        # this function is turning into make phrase, makePhrase is turning into makeSection!
        # IMPLEMENT 'BUILD FROM BOTH SIDES'
        # IMPEMENT 'HIGH POINT'
        # IMPLEMENT 'END ON DOMINANT FUNCTIONING NOTE'
        # IMPLEMENT 'SCALE FUNCTION ANALYZER'

        # create melody list and build scale
        melody = []
        # if first time writing A, write scale
        if log and not cad == "B":
            scale = buildScale(scaleType)
        else:
            scale = scales[0]
        goLeap = False
        justLeaped = (False, 0)
        choosingRhythms = True
        syncoBeatCnt = 0

        # create instrumental range of notes
        minBound = -24-offset
        maxBound = 24-offset
        #legalNotes = []
        #for c in range(minBound, maxBound):
            #legalNotes.append(c)

        # if cad == B and writing new melody
        if cad == "B" and log:
            # choose dominant functioning note to start on
            dom = 7
            if 7 not in scale:
                dom == random.choice(list(scale))
                while dom == 0:
                    dom == random.choice(list(scale))   
            starter = [(dom,dom)]
            #choosingRhythms = False

        # preload starter information 
        for x in starter:
            melody.append(x)
    
        # if no preloaded rests, preload non-rest for first beat
        if not rests:
            rests.append(False)
        # if no rhythm value picked, choose one
        if not rhythmValsPicked:
            rhythmValsPicked.append(random.choice(rhythmVals))
        # else if cad == B, disable choosingRhythms
                
        # log starting note info
        #print("Starting note: " + str(melody))    
        #print("Rhythm val for starting note: " + str(rhythmValsPicked))

        # ACE MELODY RULES:
        # 50/50 up or down, never move by 0 (maybe should allow the latter, 46/46/8 splits?)
        # rests are designated 1/1000 of the time (we are deprecating rest creation here)
        # leaps occur 50% of the time and are always followed by a non-leap in the opposite direction of the leap
        # leaps are no bigger than a 10th (15 semitones) and must not extend beyond legalNotes

        # intialize note count and total beats used count
        i = 1
        spaceLeft = length - sum(rhythmValsPicked) 
        if not choosingRhythms:
            spaceLeft = len(rhythmValsPicked)-1

        if log:
            while spaceLeft > 0:
                # placeholder
                newNote = 0

                # 0 is a rest, rests have a 1 in 30 chance of getting picked (rests are being deprecated here)
                rest = random.randrange(0,999999)
                # 0 or 1 is a leap, leaps have a 2/9 chance of getting picked
                # mod2==0 is up, mod2==1 is down.
                motionType = random.randrange(0, 9)

                # LOGIC FOR DECIDING THE RHYTHM
                if choosingRhythms:
                    #print("Choosing rhythm...")
                    rhythmVal = random.choice(rhythmVals)
                    #print("Rhythm Value Map: " + str(rhythmVals))
                    #print("Space left: " + str(spaceLeft))

                    # if immediately chosen rhythm put us on a syncopation, log the note
                    if not spaceLeft%1 == 0:
                        #print("We're in synco:")
                        syncoBeatCnt += 1
                    # if we're on downbeat, reset syncoBeatCnt
                    else:
                        #print("We're on downbeat:")
                        syncoBeatCnt = 0
                    #print("Beats on Synco: " + str(syncoBeatCnt))

                    # if syncopating for longer than four beats, get back on downbeat
                    if syncoBeatCnt > 0:
                        #print("We need to get onto a strong beat immediately!")
                        #print("Space left: " + str(spaceLeft))
                        def findUpperOdd(val):
                            while True:
                                if math.ceil(val)%2 == 1:
                                    return math.ceil(val)
                                val += 1
                        #rhythmVal = findUpperOdd(spaceLeft) - spaceLeft

                        # don't worry about strong vs. weak, just get to the quarter
                        rhythmVal = math.ceil(spaceLeft) - spaceLeft
                        #print(rhythmVal)

                    # find a shorter rhythm if chosen rhythm is too big
                    while rhythmVal not in rhythmVals or rhythmVal > spaceLeft:
                        if rhythmVal == min(rhythmVals):
                            break
                        #print("Rhythm of value " + str(rhythmVal) + " chosen.")
                        #print("RHYTHM TOO LONG, SHORTENING BY MINIMUM RHYTHM VALUE...")
                        rhythmVal -= min(rhythmVals) 

                    # REPORT RHYTHM CHOSEN
                    #print("Rhythm of value " + str(rhythmVal) + " chosen.")

                # LOGIC FOR DECIDING MOTION
                #print("Deciding motion...")
                restApp = False
                if rest == 0:
                    restApp = True
                if not justLeaped[0] and motionType < 2: goLeap = True
                # LEAP LOGIC
                if goLeap:
                    # find legal leaps
                    legalLeaps = findLegalLeaps(melody[i-1][1], scale, motionType)
                    #print("Legal Leaps: " + str(legalLeaps))
                    # pick a random leap in legalLeaps
                    newNote = random.choice(legalLeaps)
                    #print(str(newNote) + " chosen.")
                    # set leap flags to true
                    justLeaped = (True, motionType)
                    goLeap = False
                # POST-LEAP BALANCE LOGIC
                elif justLeaped[0]:
                    #print("Post-leap balance required.")
                    # direction overrides to opposite of the previous leap
                    oppFromLeap = 1
                    if justLeaped[1] == 1:
                        oppFromLeap = 0
                    # find legal steps
                    legalSteps = findLegalSteps(melody[i-1][1], scale, oppFromLeap)
                    #print("Legal Steps: " + str(legalSteps))
                    # pick a random step in legalSteps
                    newNote = random.choice(legalSteps)
                    #print(str(newNote) + " chosen.")
                    # set leap flags to false, leap has been officially balanced
                    justLeaped = (False, 0)
                # STEP LOGIC
                else:
                    # find legal steps
                    legalSteps = findLegalSteps(melody[i-1][1], scale, motionType%2)
                    #print("Legal Steps: " + str(legalSteps))

                    # pick a random step in legalSteps
                    newNote = random.choice(legalSteps)
                    #print(str(newNote) + " chosen.")
                    #print("Melody: " + str(melody))

                # add chosen data to melody
                melody.append((newNote%12, newNote))
                if choosingRhythms:
                    rhythmValsPicked.append(rhythmVal)
                    rests.append(restApp)
                
                # update spaceLeft
                if choosingRhythms:
                    spaceLeft = length - sum(rhythmValsPicked)
                else:
                    spaceLeft -= 1
                if spaceLeft == 0:
                    #print("Writing melody...")
                    realMel = [x[1] for x in melody]
                    #print("Finished melody: " + str([x[1] for x in melody]))
                    #print("Finished melody: ")
                    '''
                    for i in range(len(melody)):
                        if i == len(melody)-1:
                            print(str(realMel[i]),end="")
                            print(" (" + str(rhythmValsPicked[i]) + ")",end="")
                        else:
                            print(str(realMel[i]),end="")
                            print(" (" + str(rhythmValsPicked[i]) + "), ",end="")
                    print(".\n")
                    print("Length of section: " + str(sum(rhythmValsPicked)))
                    '''
                    #print("Space left: " + str(spaceLeft))
                    #print()
                i += 1
        
        ogMel = [x for x in melody]
        melody = [((x[0]+offset)%12,x[1]+offset) for x in ogMel] 
        return melToLily(melody, scaleDict, rests, rhythmVals, rhythmValsPicked, cad, ogMel)

    # build the scale
    def buildScale(scaleType, log=False):
        print("Building scale...")
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
        else:
            scale = {0}
            ct = 0
            curr = 0
            while ct < 6:
                i = random.randrange(1,5)
                curr += i
                if curr >= 12: 
                    scale.add(curr-12) 
                else: 
                    scale.add(curr)
                ct += 1
                if not ct == 6:
                    print(scale)
        print(scale)
        print("Built scale.")
        scales.append(scale)
        return scale
    
    # find LEAPS in the scale that are no more than a tenth away from a starting note
    def findLegalLeaps(note, scale, direction):
        # if failing in one direction, TRY THE OTHER and adjust data if success.
        legalLeaps = []
        leapStart = 5
        leapEnd = 12
        leapInc = 1
        defOctLeap = 12
        if direction == 1:
            leapStart = -5
            leapEnd = -12
            leapInc = -1
            defOctLeap = -12
        dist = leapStart
        while not dist == leapEnd:
            possLeap = note + dist
            if possLeap in scale or possLeap%12 in scale:
                #print("LEAP ADDED")
                legalLeaps.append(possLeap)
            dist += leapInc
        if not legalLeaps:
            #print("No legal leaps found. Carrying out default octave leap.")
            return [note+defOctLeap]
        #print("Legal leaps found.")
        return legalLeaps

    # find STEPS in the scale from a starting note
    def findLegalSteps(note, scale, direction):
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
            if possStep in scale or possStep%12 in scale:
                #print("PossStep added for note " + str(note%12) + ": " + str(possStep))
                legalSteps.append(possStep)
            dist += stepInc
        if not legalSteps:
            #print("No legal steps found. Repeating note.")
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
        return [0.25,0.25,0.5,0.5,0.5,0.5,0.75,1,1,1,1,1,1,1,1,2,2,2,3,4]
        #return rhythmVals

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
            rhythmToLily = {0.25:"16",0.5:"8",0.75:"8.",1:"4",1.5:"4.",2:"2",3:"2.",4:"1",6:"1.",8:"\\breve"}
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

    # use makeMel to write a melodic phrase
    def makePhrase(scaleDict, scaleType, offset, aLength, bLength, newMel, cad, eat=2):
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
                mel = makeMel(offset, scaleDict[offset%12], scaleType, [(0,0)], aLength, cad, [], rhythmVals, [], True)
                mels.append(mel)
                fullMel += mel[0]
            if cad == "B":                      
                # using A's rests and rhythms!
                mel = makeMel(offset, scaleDict[offset%12], scaleType, [(0,0)], aLength, cad, [], rhythmVals, [], True)
                # new rhythms
                #mel = makeMel(offset, scaleDict[offset%12], scaleType, [(7,7)], aLength, cad, [], rhythmVals, [], True)
                bMels.append(mel)
                fullMel += mel[0]
            if cad == "endSolo":
                endMel = makeMel(offset, scaleDict[offset%12], scaleType, [mels[0][-1][0]], 1, cad, [False], [4], [], True)
                fullMel += endMel[0]   
            # for two-part phasing
            if cad == "phaseA":
                mel = makeMel(offset, scaleDict[offset%12], scaleType, [(0,0)], aLength, cad, [], rhythmVals, [], True)
                mels.append(mel)
            if cad == "phaseB":
                b = makeMel(offset, scaleDict[offset%12], scaleType, [(-12,-12)], bLength, cad, [], rhythmVals, [], True)
                bMels.append(b)
            if cad == "endPhase":
                endMel = makeMel(offset, scaleDict[offset%12], scaleType, [(0,0)], 1, cad, [False], [4], [], True)
                endMelB = makeMel(offset, scaleDict[offset%12], scaleType, [(-12,-12)], 1, cad, [False], [4], [], True)
                fullMel += endMel[0]
                tenor += endMelB[0]  
            # for canon
            if cad == "roundA":
                mel = makeMel(offset, scaleDict[offset%12], scaleType, [(0,0)], aLength, cad, [], rhythmVals, [], True)
                mels.append(mel)
                fullMel += mel[0]
                #a = makeMel(offset, scaleDict[offset%12], scaleType, mels[0][-1], aLength, cad, [True]*len(mels[0][2]), mels[0][3], mels[0][4], False)
                #t = makeMel(offset, scaleDict[offset%12], scaleType, mels[0][-1], aLength, cad, [True]*len(mels[0][2]), mels[0][3], mels[0][4], False)
                #b = makeMel(offset, scaleDict[offset%12], scaleType, mels[0][-1], aLength, cad, [True]*len(mels[0][2]), mels[0][3], mels[0][4], False)
                #alto += a[0]
                #tenor += t[0]
                #bass += b[0]
                # create buffer for part entrances
                a = makeMel(offset, scaleDict[offset%12], scaleType, [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)], 9, cad, [True,True,True,True,True,True,True,True,True], [2], [2,2,2,2,2,2,2,2,2], True)
                t = makeMel(offset, scaleDict[offset%12], scaleType, [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)], 16, cad, [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True], [2], [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2], True)
                b = makeMel(offset, scaleDict[offset%12], scaleType, [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)], 21, cad, [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True], [2], [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2], True)
                alto += a[0]
                tenor += t[0]
                bass += b[0]
            if cad == "roundB":
                mel = makeMel(offset, scaleDict[offset%12], scaleType, [(0,0)], bLength, cad, [], rhythmVals, [], True)
                mels.append(mel)
                a = makeMel(offset-5, scaleDict[(offset-5)%12], scaleType, mels[-1][-1], aLength, cad, mels[-1][2], mels[-1][3], mels[-1][4], False)
                t = makeMel(offset-10, scaleDict[(offset-10)%12], scaleType, mels[-1][-1], aLength, cad, mels[-1][2], mels[-1][3], mels[-1][4], False)
                b = makeMel(offset-24, scaleDict[(offset-24)%12], scaleType, mels[-1][-1], aLength, cad, mels[-1][2], mels[-1][3], mels[-1][4], False)
                fullMel += mel[0]
                alto += a[0]
                tenor += t[0]
                bass += b[0]
            if cad == "roundEnd":
                endMel = makeMel(offset, scaleDict[offset%12], scaleType, [(0,0)], 1, cad, [False], [4], [], True)
                endMelA = makeMel(offset, scaleDict[offset%12], scaleType, [(-5,-5)], 1, cad, [False], [4], [], True)
                endMelT = makeMel(offset, scaleDict[offset%12], scaleType, [(-10,-10)], 1, cad, [False], [4], [], True)
                endMelB = makeMel(offset, scaleDict[offset%12], scaleType, [(-24,-24)], 1, cad, [False], [4], [], True)
                fullMel += endMel[0]
                alto += endMelA[0]
                tenor += endMelT[0]
                bass += endMelB[0]
        
        # repeating motif
        else:
            # for solo
            if cad == "A":
                mel = makeMel(offset, scaleDict[offset%12], scaleType, mels[0][-1], aLength, cad, mels[0][2], mels[0][3], mels[0][4], False)
                fullMel += mel[0]
            if cad == "Aend":
                # finalize with the exact melody
                mel = makeMel(offset, scaleDict[offset%12], scaleType, mels[0][-1], aLength-2, cad, mels[0][2], mels[0][3], mels[0][4], False)
                # eat some beats and rewrite a more finishing tail
                #mel = makeMel(offset, scaleDict[offset%12], scaleType, mels[0][-1][:-2], aLength-2, cad, mels[0][2][:-2], mels[0][3][:-2], mels[0][4][:-2], False)
                fullMel += mel[0]
            if cad == "B":
                mel = makeMel(offset, scaleDict[offset%12], scaleType, bMels[0][-1], bLength, cad, bMels[0][2], bMels[0][3], bMels[0][4], False)
                fullMel += mel[0]
            # for two-part phasing
            if cad == "phaseA":
                mel = makeMel(offset, scaleDict[offset%12], scaleType, mels[0][-1], aLength, cad, mels[0][2], mels[0][3], mels[0][4], False)
                fullMel += mel[0]
            if cad == "phaseB":
                b = makeMel(offset, scaleDict[offset%12], scaleType, bMels[0][-1], bLength, cad, bMels[0][2], bMels[0][3], bMels[0][4], False)
                tenor += b[0]
            # for canon
            if cad == "roundA":
                mel = makeMel(offset, scaleDict[offset%12], scaleType, mels[0][-1], aLength, cad, mels[0][2], mels[0][3], mels[0][4], False)
                a = makeMel(offset-5, scaleDict[(offset-5)%12], scaleType, mels[0][-1], aLength, cad, mels[0][2], mels[0][3], mels[0][4], False)
                t = makeMel(offset-10, scaleDict[(offset-10)%12], scaleType, mels[0][-1], aLength, cad, mels[0][2], mels[0][3], mels[0][4], False)
                b = makeMel(offset-24, scaleDict[(offset-24)%12], scaleType, mels[0][-1], aLength, cad, mels[0][2], mels[0][3], mels[0][4], False)
                fullMel += mel[0]
                alto += a[0]
                tenor += t[0]
                bass += b[0]
            if cad == "roundB":
                mel = makeMel(offset, scaleDict[offset%12], scaleType, mels[-1][-1], aLength, cad, mels[-1][2], mels[-1][3], mels[-1][4], False)
                a = makeMel(offset-5, scaleDict[(offset-5)%12], scaleType, mels[-1][-1], aLength, cad, mels[-1][2], mels[-1][3], mels[-1][4], False)
                t = makeMel(offset-10, scaleDict[(offset-10)%12], scaleType, mels[-1][-1], aLength, cad, mels[-1][2], mels[-1][3], mels[-1][4], False)
                b = makeMel(offset-24, scaleDict[(offset-24)%12], scaleType, mels[-1][-1], aLength, cad, mels[-1][2], mels[-1][3], mels[-1][4], False)
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

        # 3/8 -> 6,12,18,24,etc.
        # 6/8 -> 12
        # 9/8 -> 18
        # 12/8 -> 24
        # 2/4 -> 4
        # 3/4 -> 6
        # 4/4 -> 8
        # 5/4 -> 10
        # 6/4 -> 12

        # Pattern: Length can be any multiple (between 1-4 for now) of the doubled numerator.

        #length = int(meter[0])*2*random.randrange(4,8)
        length = 16

        #for i in range(random.choice([2,4,6,8])):
        print("Writing A section with length " + str(length) + "...")
        makePhrase(scaleDict, scaleType, key, length, length, True, "A")
        print("Restating A section...")
        makePhrase(scaleDict, scaleType, key, length, length, False, "A")
        print("Writing B section with length " + str(length) + "...")
        makePhrase(scaleDict, scaleType, key, length, length, True, "B")
        print("Concluding with A section with length " + str(length-2) + "...")
        makePhrase(scaleDict, scaleType, key, length, length, False, "Aend")
        print("Ending solo...")
        #makePhrase(scaleDict, scaleType, key, 1, 1, True, "endSolo")

    # composes a freeform tune
    def freeform(key, scaleType, beats):
        # SET A PRECLIM, RETPRE, CLIMAX (required), RETPRE2, AND POSTCLIM.
        # BUILD MELODY FROM BOTH ENDS!!!!
        makePhrase(majScales, scaleType, key, beats, beats, True, "A")

    # composes a phasing tune
    def reich(majScales, scaleAsk, offset):
        aLength = 1
        bLength = 1
        while aLength == bLength:
            aLength = random.choice([4,5,6,7,8,9,11,13,15])
            bLength = random.choice([5,6,7,8,9,11,13,15,17])
        makePhrase(majScales, scaleAsk, offset, aLength, bLength, True, "phaseA")
        makePhrase(majScales, scaleAsk, offset, aLength, bLength, True, "phaseB")
        aCt = 1
        bCt = 1
        for i in range(int(aLength*bLength)):
            if aCt <= bLength:
                makePhrase(majScales, scaleAsk, offset, aLength, bLength, False, "phaseA")
                aCt += 1
            if bCt <= aLength:
                makePhrase(majScales, scaleAsk, offset, aLength, bLength, False, "phaseB")
                bCt += 1
        makePhrase(majScales, scaleAsk, offset, aLength, bLength, True, "endPhase")

    # composes a canon
    def canon(majScales, scaleAsk, offset):
        aLength = random.choice([16,32,64])
        bLength = random.choice([16,32,64])
        makePhrase(majScales, scaleAsk, offset, aLength, aLength, True, "roundA")
        makePhrase(majScales, scaleAsk, offset, aLength, aLength, False, "roundA")
        makePhrase(majScales, scaleAsk, offset, bLength, bLength, True, "roundB")
        #makePhrase(majScales, scaleAsk, offset, bLength, bLength, False, "roundB")
        makePhrase(majScales, scaleAsk, offset, aLength, aLength, False, "roundA")
        makePhrase(majScales, scaleAsk, offset, 1, 1, True, "roundEnd")

    # composes a serialist piece
    def serial(majScales, scaleAsk, offset):
        aLength = random.choice([4,5,6,7,8,9,10,11,12,13,14,15,16])
        bLength = random.choice([4,5,6,7,8,9,10,11,12,13,14,15,16])
        print(aLength)
        print(bLength)
        makePhrase(majScales, scaleAsk, offset, aLength, aLength, True, "roundA")
        for i in range(4):
            makePhrase(majScales, scaleAsk, offset, aLength, aLength, False, "roundA")
        makePhrase(majScales, scaleAsk, offset, bLength, bLength, True, "roundB")
        for i in range(3):
            makePhrase(majScales, scaleAsk, offset, bLength, bLength, False, "roundB")
        for i in range(4):
            makePhrase(majScales, scaleAsk, offset, aLength, aLength, False, "roundA")
        makePhrase(majScales, scaleAsk, offset, 1, 1, True, "roundEnd")
        
    # ask the user what scale they want to use
    def scaleAsk():
        sc = ""
        viableScales = {"major":0,"major pentatonic":1,"minor":2,"minor pentatonic":3,"harmonic minor":4,"chromatic":5}
        inpStr = "What kind of scale would you like to use for your piece? Enter the corresponding number.\n"
        for x in viableScales.keys():
            inpStr += "\n- " + x + " (" + str(viableScales[x]) + ")" 
        inpStr += "\n- random (6)\n\n"
        ans = input(inpStr)
        print()
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
        if mode == "solo" or mode == "freeform":
            code = "\\header {\n  title = \"" + scaleStart + "\"\n}\n\n"
            code += "\\score {\n"
            code += "\\" + "new Staff { \set Staff.midiInstrument = \"flute\" \clef \"treble\" \\key " + scaleStart + " \\" + scaleQual + " "
            code += "\\time " + time[0] + "\\tempo " + tempo[0] + " " + time[1] + " = " + tempo[1] + " " + m + "}\n"
            code += "\\midi{}\n"
            code += "}\n"
            code += "\\version \"2.22.2\""
            f = open("ConvertMe.ly", "w")
            f.write(code)
            f.close()
        else:
            code = "\\header{\n  title = \"Computery's Masterpiece\"\n}\n\n"
            code += "\\score {\n"
            code += "\\new PianoStaff <<\n"
            code += "\\time " + time[0] + "\n"
            code += "\\tempo " + tempo[0] + " " + time[1] + " = " + tempo[1] + "\n"
            code += "\\" + "new Staff { \set Staff.midiInstrument = \"violin\" \clef \"treble\" \\key " + scaleStart + " \\" + scaleQual + " " + m + "}\n"
            code += "\\" + "new Staff { \set Staff.midiInstrument = \"viola\" \clef \"treble\" \\key " + scaleStart + " \\" + scaleQual + " " + a + "}\n"
            code += "\\" + "new Staff { \set Staff.midiInstrument = \"cello\" \clef \"bass\" \\key " + scaleStart + " \\" + scaleQual + " " + t + "}\n"
            code += "\\" + "new Staff { \set Staff.midiInstrument = \"contrabass\" \clef \"bass\" \\key " + scaleStart + "\\" + scaleQual + " " + b + "}\n"
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
    # REICH: MAKE PARTS HAVE DIFFERENT BUT MATHEMATICALLY RELATED RHYTHM PROFILES
    viableModes = ["solo","reich","freeform"]
    modeChoice = input("Choose your mode by entering its keyword.\n\n- Solo (solo)\n- Multi-Part Phasing (reich)\n- Freeform (freeform)\n\n")
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
    elif modeChoice == "reich":
        print("Reich fan huh? Well - hopefully this will change your mind.\nA two-part phasing piece will be generated.\n")
        reich(majScales, scaleType, offset, meter)
    elif modeChoice == "serial":
        print("You brave soul. Prepare to cover your ears.")
        serial(majScales, scaleAsk, offset, meter)
    elif modeChoice == "freeform":
        print("A freeform melody will be generated.\n")
        freeform(offset, scaleType, random.randrange(32,256))

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