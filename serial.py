import datetime
import random
import math

# CONFIGURATION
# Python Note:
# Tuple -> (pitch, rhythm, tie, articulation, dynamic)
# Lily Pond Formatted Note:
# String -> pitchToLily[pitch] + rhythmToLily[rhythm] + tie + articulation + dynamic

# GLOBALS
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
rows = []
mels = []
rhythmMotifs = {}
a_mels = []
a_pitches = []
b_mels = []
b_pitches = []
a_length = 0
b_length = 0
sectionsWritten = []
partLengths = []
scales = []
rhythmKey = [0.25,0.5,0.75,1,1.5,2,3,4]
rhythms = [0.25,0.5,0.75,1,1.5,2,3,4]
melRange = [i for i in range(-5,32)]
pitchToLily = {None:"r",0:"c'",1:"cis'",2:"d'",3:"dis'",
              4:"e'",5:"f'",6:"fis'",7:"g'",8:"gis'",
              9:"a'",10:"ais",11:"b"}
rhythmTrans = {0.25:"16",0.5:"8",0.75:"8.",1:"4",1.5:"4.",2:"2",3:"2.",4:"1"}
tempos = [("Largo",(40,60)),("Adagio",(61,75)),("Andante",(76,107)),("Moderato",(108,119)),("Allegro",(120,155)),("Vivace",(156,175)),("Presto",(168,200))]
meters = [("3/4",3),("4/4",4),("4/4",4),("4/4",4),("4/4",4),("5/4",5),("6/4",3),("7/4",7)]
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
                3:{0:"c",1:"des",2:"d",3:"ees",4:"e",5:"f",6:"ges",7:"g",8:"aes",9:"a",10:"bes",11:"ces"},
                4:{0:"c",1:"cis",2:"d",3:"dis",4:"e",5:"f",6:"fis",7:"g",8:"gis",9:"a",10:"ais",11:"b"},
                5:{0:"c",1:"des",2:"d",3:"ees",4:"e",5:"f",6:"ges",7:"g",8:"aes",9:"a",10:"bes",11:"b"},
                6:{0:"c",1:"cis",2:"d",3:"dis",4:"e",5:"eis",6:"fis",7:"g",8:"gis",9:"a",10:"ais",11:"b"},
                7:{0:"c",1:"des",2:"d",3:"ees",4:"e",5:"f",6:"fis",7:"g",8:"aes",9:"a",10:"bes",11:"b"},
                8:{0:"c",1:"cis",2:"d",3:"dis",4:"e",5:"f",6:"fis",7:"g",8:"gis",9:"a",10:"ais",11:"b"},
                9:{0:"c",1:"cis",2:"d",3:"dis",4:"e",5:"f",6:"fis",7:"g",8:"gis",9:"a",10:"ais",11:"b"},
                10:{0:"c",1:"des",2:"d",3:"ees",4:"e",5:"f",6:"ges",7:"g",8:"aes",9:"a",10:"bes",11:"b"},
                11:{0:"c",1:"cis",2:"d",3:"dis",4:"e",5:"f",6:"fis",7:"g",8:"gis",9:"a",10:"ais",11:"b"},} 
pieceLength = 0
lead = ""
alto = ""
tenor = ""
bass = ""

# print ACE header
def printHeader():
    print(OKGREEN,end="")
    print("#"*218,end="")
    print(FAIL,end="")
    print("ALGORITHMIC COMPOSITION ENGINE",end="")
    print(OKGREEN,end="")
    print("#"*220,end="")
    print(ENDC)
# chooses pitch order of a set
def genToneRow(length=12):
    noteMap = list(range(length))
    """
    noteMap = [0,0,0,3,3,3,5,5,5,7,7,7,10,10,10]
    center = random.randint(0,11)
    noteMap = [x+center for x in noteMap]
    print(center)
    print(noteMap)
    """
    pitches = []
    restFreq = random.randrange(10, 20)
    while len(noteMap) > 0:
        dieRoll = random.randint(0, restFreq)
        if dieRoll < 0: #RESTS DISABLED
            pitches.append(None)
        else:
            choice = random.choice(noteMap)
            regBounce = random.randint(0,4)
            if regBounce < 1:
                pitches.append(choice+12)
            else:
                pitches.append(choice)
            noteMap.remove(choice)
            # register correct
            def regCorrect(p, l, r):
                if len(p) > 1 and not l < 0-len(p):
                    if type(p[l]) == int and type(p[r]) == int:
                        if abs(p[r] - p[l]) > 12:
                            if p[r] < p[l]:
                                p[r] += 12
                            elif p[l] < p[r]:
                                p[l] += 12
                            regCorrect(p,l-1,l)
                        return p
                    return p
                return p
            pitches = regCorrect(pitches, -2, -1)
    #print("Pitches: " + str(pitches) + "\n")
    return pitches
# generates rhythms
def genRhythms(meter, length, exactLength=(False, 64)):
    def goodLength(length):
        c = 0
        rhythmSplat = []
        #luckyRhythm = random.choice(rhythms)
        #luckyRhythm = 0
        for r in range(len(rhythms)):
            lottery = random.randrange(1, random.randrange(2,10))
            # LUCKY RHYTHM
            #if rhythms[r] == luckyRhythm:
                #lottery *= 100
            for _ in range(lottery):
                rhythmSplat.append(rhythms[r])    
        rhythmChoices = [random.choice(rhythmSplat)]
        row_length_good = False
        row_choice_good = False
        while not row_length_good:
            while not row_choice_good:
                choice = random.choice(rhythmSplat)
                #print("Trying rhythm " + str(choice) + "...")
                if c == 1:
                    row_length = sum(rhythmChoices) + choice
                    if row_length % 1 == 0 or row_length % 1 == 0.5:
                        row_choice_good = True
                        c = 0
                else:
                    row_choice_good = True
                    c += 1
            rhythmChoices.append(choice)
            if not length == 0:
                if len(rhythmChoices) == length:
                    row_length_good = True
            elif length == 0:
                if sum(rhythmChoices) > (int(meter[0][0])*8)-0.25 and sum(rhythmChoices) % 4 == 0:
                    row_length_good = True 
            row_choice_good = False
        #print(rhythmChoices)
        return rhythmChoices
    row_length_ok = False
    while not row_length_ok:
        rhythmList = goodLength(length)
        #print(rhythmList)
        sumRhythms = sum(rhythmList)
        #print(sumRhythms)
        if exactLength[0]:
            if sumRhythms == exactLength[1]:
                row_length_ok = True
        else:
            if sumRhythms % int(meter[0][0]) == 0:
                row_length_ok = True
    return rhythmList
# generates pitches
def genPitches(mel, scale, offset, domStart=0):
    # choose ###PITCH### of next note
    pitches = []
    if not domStart == 0:
        pitches = [offset+7]
    else:
        pitches = [random.choice(list(scale))]
    notesLeft = len(mel)-1
    goLeap = False
    justLeaped = (0, 0)
    # create instrumental range of notes
    phraseRange = [x-offset for x in melRange]
    while notesLeft > 0:
        # find last pitch
        nonRests = [x for x in pitches if not x == None]
        lastPitch = nonRests[-1]
        # initialize newPitch to tonal center
        newPitch = 0
        # roll for a rest (0), rests have a 1/16 chance of getting picked
        rest = random.randrange(0,16)
        if rest == 0:
            pitches.append(None)
        else:
            # 0 or 1 is a leap, leaps have a 4/10 chance of getting picked
            # mod2==0 is up, mod2==1 is down.
            motionType = random.randrange(0, 10)
            # if we didn't just leap previously and we rolled a leap, set goLeap to True
            if justLeaped[0] == 0 and motionType < 4: goLeap = True
            # find legal moves
            def findMoves(note, scale, moveType, direction, bounds):
                legalMoves = []
                moveStart = moveType[0]
                moveEnd = moveType[1]
                moveInc = 1
                # if downward move, flip all signs
                if direction == 1:
                    moveStart = 0-moveType[0]
                    moveEnd = 0-moveType[1]
                    moveInc = 0-1
                dist = moveStart
                while not dist == moveEnd:
                    possMove = note + dist
                    if possMove%12 in scale:
                        if possMove in bounds:
                            #print("MOVE ADDED")
                            legalMoves.append(possMove)
                    dist += moveInc
                # if failed to find any moves in one direction, TRY THE OTHER DIRECTION.
                if not legalMoves:
                    #print("No legal moves found.")
                    # Try other direction!
                    if direction == 0:
                        return findMoves(note, scale, moveType, direction+1, bounds)
                    else:
                        return findMoves(note, scale, moveType, direction-1, bounds)
                #print("Legal moves found.")
                return (legalMoves, direction)

            # LEAP LOGIC
            if goLeap:
                # find legal leaps
                legalLeaps = findMoves(lastPitch, scale, (5,13), motionType%2, phraseRange)
                newPitch = random.choice(legalLeaps[0])
                justLeaped = (2, legalLeaps[1])
                goLeap = False
            # POST-LEAP BALANCE LOGIC
            elif justLeaped[0] > 0:
                prevVal = justLeaped[0]
                # balance direction overrided to the opposite of the previous leap
                oppFromLeap = 1
                if justLeaped[1] == 1:
                    oppFromLeap = 0
                legalSteps = findMoves(lastPitch, scale, (1,4), oppFromLeap, phraseRange)
                newPitch = random.choice(legalSteps[0])
                lastDir = justLeaped[1]
                justLeaped = (prevVal-1, lastDir)
            # STEP LOGIC
            else:
                # find legal steps
                legalSteps = findMoves(lastPitch, scale, (1,4), motionType%2, phraseRange)
                newPitch = random.choice(legalSteps[0])
            pitches.append(newPitch) 
        notesLeft -= 1
    return [x+offset if not x==None else None for x in pitches]
# insert rests into a row
def insertRests(row):
    i = 0
    restFreq = random.randrange(10, 20)
    while i < 12:
        dieRoll = random.randint(0, restFreq)
        if dieRoll < 2:
            row.insert(i, None)
        i += 1
    return row
# places articulations on notes of the melody
def articulate(mel):
    artics = []
    # 0-8 artics, (9 openSlur, 18 port, 19 closeSlur), (10 non-vib, 20 vib), 
    # (11 pizz, 21 snap, 22 stopped, 23 arco)
    # think of something for 2,6,8 
    # don't let staccato go onto long notes (2 or greater)
    articToLily = {0:"",1:"\\accent ",2:"\\tenuto ",3:"\\marcato ",4:"\\staccato ",
                   5:"\\staccatissimo ",6:":32 ",7:"\\glissando ", 8:":32 ",
                   9:"\\( ", 10:"^\\markup non-vib. ", 11:"^\\markup pizz.", 
                  12:"^\\markup \"sul ponticello\" ", 13:"^\\markup \"sul tasto\" ", 
                  14:"\\staccato ^\\markup \"col legno\" ", 
                  15:"\\marcato ^\\markup \"au talon\" ", 16:"^\\markup \"sotto voce\" ",  
                  17:"^\\markup flautando ", 18:"\\portato ", 19:"\\) ", 20:"^\\markup vib. ",
                  21:"\\snappizzicato \\accent ", 22:"\\stopped ", 23:"^\\markup arco ", 24:"^\\markup naturale "}
    defMode = []
    for h in range(2):
        slurMode = [[0,0,0,0,18,(19,defMode)], [0,0,0,0,18,(19,defMode)], [0,0,0,0,18,(19,defMode)],
                    [0,0,0,0,18,(19,defMode)], [0,0,0,0,18,(19,defMode)], [0,0,0,0,18,(19,defMode)],
                    [0,0,0,0,18,(19,defMode)], [0,0,0,0,18,(19,defMode)]]
        nonvibMode = [[0,0,0,(20,defMode)], [0,0,0,(20,defMode)], [0,0,0,(20,defMode)],
                    [0,0,0,(20,defMode)], [0,0,0,(20,defMode)], [0,0,0,(20,defMode)],
                    [0,0,0,(20,defMode)], [0,0,0,(20,defMode)]]
        pizzMode = [[22,(23, defMode),(23, defMode),(23, defMode)], [22,(23, defMode),(23, defMode),(23, defMode)], [22,(23, defMode),(23, defMode),(23, defMode)],
                    [22,(23, defMode,(23, defMode),(23, defMode))], [21,22,(23, defMode),(23, defMode),(23, defMode)], [21,22,(23, defMode),(23, defMode),(23, defMode)],
                    [0,21,22,(23, defMode)], [0,21,22,(23, defMode)]]
        sulPMode = [[0,0,6,(24,defMode)], [0,0,6,(24,defMode)], [0,0,6,(24,defMode)], [0,0,6,(24,defMode)],
                    [0,0,6,(24,defMode)], [0,0,6,(24,defMode)], [0,0,6,(24,defMode)], [0,0,6,(24,defMode)]]
        sulTMode = [[0,0,6,(24,defMode)], [0,0,6,(24,defMode)], [0,0,6,(24,defMode)], [0,0,6,(24,defMode)],
                    [0,0,6,(24,defMode)], [0,0,6,(24,defMode)], [0,0,6,(24,defMode)], [0,0,6,(24,defMode)]]
        colLegMode = [[4,(24,defMode)], [4,(24,defMode)], [4,(24,defMode)], [4,(24,defMode)], [4,(24,defMode)],
                    [4,(24,defMode)], [4,(24,defMode)], [4,(24,defMode)]]
        auTalMode = [[3,(24,defMode)], [3,(24,defMode)], [3,(24,defMode)], [3,(24,defMode)], [3,(24,defMode)],
                    [3,(24,defMode)], [3,(24,defMode)], [3,(24,defMode)]]
        sotVocMode = [[0,(24,defMode)], [0,(24,defMode)], [0,(24,defMode)], [0,(24,defMode)], [0,(24,defMode)],
                    [0,(24,defMode)], [0,(24,defMode)], [0,(24,defMode)]]
        flautMode = [[0,(24,defMode)], [0,(24,defMode)], [0,(24,defMode)], [0,(24,defMode)], [0,(24,defMode)],
                    [0,(24,defMode)], [0,(24,defMode)], [0,(24,defMode)]]
        defMode = [[0,1,2,3,4,5,(9,slurMode),(9,slurMode),(10,nonvibMode),(11,pizzMode),(12,sulPMode),(13,sulTMode),(14,colLegMode),(15,auTalMode),(16, sotVocMode),(17,flautMode)],
                   [0,1,2,3,4,5,(9, slurMode),(9,slurMode),(10,nonvibMode),(11,pizzMode),(12,sulPMode),(13,sulTMode),(14,colLegMode),(15,auTalMode),(16,sotVocMode),(17,flautMode)],
                   [0,1,2,3,4,5,7,(9, slurMode),(9,slurMode),(10,nonvibMode),(11,pizzMode),(12,sulPMode),(13,sulTMode),(14,colLegMode),(15,auTalMode),(16,sotVocMode),(17,flautMode)], 
                   [0,1,2,3,4,5,7,(9, slurMode),(9,slurMode),(10,nonvibMode),(11,pizzMode),(12,sulPMode),(13,sulTMode),(14,colLegMode),(15,auTalMode),(16,sotVocMode),(17,flautMode)],
                   [0,1,3,7,(9, slurMode),(9,slurMode),(10,nonvibMode),(11,pizzMode),(12,sulPMode),(13,sulTMode),(15,auTalMode),(16,sotVocMode),(17,flautMode)], 
                   [0,1,2,3,7,8,(9, slurMode),(9,slurMode),(10,nonvibMode),(11,pizzMode),(12,sulPMode),(13,sulTMode),(15,auTalMode),(16,sotVocMode),(17,flautMode)], 
                   [0,1,2,3,7,8,(9, slurMode),(9,slurMode),(10,nonvibMode),(11,pizzMode),(12,sulPMode),(13,sulTMode),(15,auTalMode),(16,sotVocMode),(17,flautMode)], 
                   [0,1,2,3,7,8,(9, slurMode),(9,slurMode),(10,nonvibMode),(11,pizzMode),(12,sulPMode),(13,sulTMode),(15,auTalMode),(16,sotVocMode),(17,flautMode)]]

    # LOOP
    currMode = defMode
    modeCt = 0
    for i in range(len(mel)):
        #print("Pitch Val: " + str(mel[i][0]))
        #print("Rhythm Val: " + str(mel[i][1]))
        #print("Option Index: " + str(rhythms.index(mel[i][1])))
        #print("Length of currMode: " + str(len(currMode)) + ", SlurMode: " + str(currMode == slurMode))
        #print("Length of defMode: " + str(len(defMode)))
        #print("ModeCt: " + str(modeCt))
        if len(currMode) == 0:
            currMode = defMode
            #print("Fixing empty list....")
            #print("Length of currMode: " + str(len(currMode)))
        currSlur = False
        nonZs = [x for x in artics if not x == 0]
        if nonZs:
            currSlur = nonZs[-1]
        # automatically end modes that go on too long
        if mel[i][0] == None or ((currSlur == 9 or currSlur == 18) and modeCt > 1):
            #print("Rest recognized OR slur limit reached.")
            if (currSlur == 9 or currSlur == 18) and modeCt > 1 and not mel[i][0] == None:
                #print("Slur limit reached.")
                artic = (19, defMode)
            else:
                #print("Rest recognized.")
                if currSlur == 9:
                    #print("Don't begin slur. If we just began slur, remove it.")
                    if artics[-1] == 9:
                        artics[-1] = 0
                    else:
                        artics[-1] = 19
                    artic = 0
                    currMode = defMode
                    modeCt = 0
                elif currMode == nonvibMode:
                    artic = random.choice((0, (20, defMode)))
                elif currMode == pizzMode:
                    artic = random.choice((0,(23, defMode)))
                elif not currMode == defMode:
                    artic = random.choice((0,(24, defMode)))
                else:
                    artic = 0
        else:
            #print("Note recognized.")
            if currMode == colLegMode:
                #print("ColLegMode recognized.")
                artic = random.choice([4,(24,defMode)])
            else:
                #print("Non ColLegMode recognized.")
                artic = random.choice(currMode[rhythms.index(mel[i][1])])
                modeCt += mel[i][1]
        # end slur on final note if still slurring
        if i == len(mel)-1:
            if currSlur == 9 or currSlur == 18:
                artic = (19,defMode)
        if type(artic) is tuple:
            #print(artic[0])
            #print(i)
            #print(len(mel)-1)
            # don't start slur on final note
            if artic[0] == 9 and i == len(mel)-1:
                artic = (0,defMode)
            # only change mode if following a REST OR RHYTHM LONGER THAN 2
            #print("Is following REST or RHYTHM LONGER THAN 2?")
            if mel[i-1][0] == None or mel[i-1][1] > 2:
                #print("Yes, changing mode. Unless trying to start slur on last note, that has been overrided.")    
                artics.append(artic[0])
                currMode = artic[1]
                modeCt = 0
                if artic[0] == 9:
                    modeCt += mel[i][1]
            else:
                #print("No, keeping mode - unless at the end of melody.")
                if currMode == colLegMode or currMode == pizzMode:
                    if not mel[i][0] == None:
                        #print("Non rest in pizz mode, placing non-artic.")
                        artics.append(0)
                    else:
                        #print("Rest in pizz mode, time for arco.")
                        artics.append(23)
                        currMode = defMode
                elif not artic[0] == 19:
                    artics.append(0)
                else:
                    artics.append(artic[0])
                    currMode = defMode
        else:
            artics.append(artic)
        # print("Artic chosen: " + articToLily[artics[-1]])
        # print("Artics So Far: " + str(artics) + "\n")
    #print("Articulations: " + str([articToLily[a] for a in artics]) + "\n")
    return [(mel[i][0], mel[i][1], articToLily[artics[i]]) for i in range(len(mel))]
# writes dynamics for the melody
def dynamicize(mel):
    dynList = ["\\ppp","\\pp","\\p","\\mp","\\mf","\\f","\\ff","\\fff","\\<","\\>","\\!"]
    dyns = []
    delayStart = 0
    swelling = (False, "\\!", 0)
    # place dynamic on first sounding note
    #print("\nStart: " + str(delayStart))
    #print("Pitch: " + str(mel[delayStart][0]))
    if mel[delayStart][0] == None:
        dyns.append("")
        delayStart += 1
        #print("Start: " + str(delayStart))
        #print("Dyns: " + str(dyns))
        #print("Dyns is all rests? " + str(all([x == "" for x in dyns])))
        while all([x == "" for x in dyns]):
            #print("Pitch: " + str(mel[delayStart][0]))
            if not mel[delayStart][0] == None:
                break
            else:
                dyns.append("")
            delayStart += 1
    #print("First pitch found: " + str(mel[delayStart][0]))
    dyns.append(random.choice(dynList[:-3]))
    prevDyn = dyns[-1]
    ghostDyn = dynList.index(prevDyn)
    justDyned = True
    # choose dynamics
    for i in range(delayStart+1, len(mel)-1):
        # don't dynamicize rests or notes preceded by a tie
        #print("Prev: " + str(mel[i-1]))
        #print("Curr: " + str(mel[i]))
        #print("Swelling: " + str(swelling))
        #print("PrevDyn: " + str(prevDyn))
        #print("GhostDyn: " + str(ghostDyn))
        #print("JustDyned: " + str(justDyned))
        place = sum([m[1] for m in mel[:i]])
        bucket = []
        backProp = False
        #print(place)
        # NON-REST
        if not mel[i][0] == None:
            # downbeat
            if place % 1 == 0 or place % 1 == 0.5:
                # initial attack of note or tied note during a swell
                if not mel[i-1][2] == "~" or (mel[i-1][2] == "~" and swelling[0]):
                    #print("Good to dynamicize!")
                    if swelling == (True, "\\<"):
                        if not justDyned:
                            bucket.append([x for x in dynList[dynList.index(prevDyn):] if not x == prevDyn and not x == swelling[1]] + [""]*20)
                        else:
                            bucket.append([x for x in dynList[8:] if not x == prevDyn and not x == swelling[1]] + [""]*20)
                        if math.floor(ghostDyn) == 0:
                            if "\\>" in bucket[0]:
                                bucket[0].remove("\\>")
                        dyns.append(random.choice(bucket[0]))
                    elif swelling == (True, "\\>"):
                        if not justDyned:
                            bucket.append([x for x in dynList[:dynList.index(prevDyn)] if not x == prevDyn and not x == swelling[1]] + [""]*20)
                        else:
                            bucket.append([x for x in dynList[8:] if not x == prevDyn and not x == swelling[1]] + [""]*20)
                        if math.ceil(ghostDyn) == 7:
                            if "\\<" in bucket[0]:
                                bucket[0].remove("\\<")
                        dyns.append(random.choice(bucket[0]))
                    else:
                        if not justDyned:
                            bucket.append([x for x in dynList[:-1] if not x == prevDyn] + [""]*20)
                        else:
                            bucket.append([x for x in dynList[8:-1] if not x == prevDyn] + [""]*20)
                        dyns.append(random.choice(bucket[0]))
                # tied note not during a swell deserves no dynamic, can start swelling
                else:
                    #print("Tied note not during a swell, don't dynamicize. Can start swelling.")
                    opts = ["\\>","\\<","",""]
                    if math.ceil(ghostDyn) == 7:
                        opts.remove("\\<")
                    elif math.floor(ghostDyn) == 0:
                        opts.remove("\\>")
                    dyns.append(random.choice(opts))
            # on offbeat, just keep swelling/non-swelling. Essentially, also no dynamic.
            else:
                #print("Offbeat. Just keep swelling/non-swelling.")
                if not i == len(mel)-1-delayStart:
                    swellOpts = ["\\<","\\>","",""]
                    if swelling[0]:
                        swellOpts.remove(swelling[1])
                        if math.ceil(ghostDyn) == 7:
                            if "\\<" in swellOpts:
                                swellOpts.remove("\\<")
                        elif math.floor(ghostDyn) == 0:
                            if "\\>" in swellOpts:
                                swellOpts.remove("\\>")
                        dyns.append(random.choice(swellOpts))
                    else:
                        if math.ceil(ghostDyn) == 7:
                            swellOpts.remove("\\<")
                        elif math.floor(ghostDyn) == 0:
                            swellOpts.remove("\\>")
                        dyns.append(random.choice(swellOpts))
                else:
                    dyns.append("")
            # only store dynamics as prevDyn
            if dyns[-1] in dynList[:-3]:
                #print("Storing dynamic " + dyns[-1] + " as prevDyn.")
                swelling = (False,"\\!")
            # if transitional, update booleans accordingly
            elif dyns[-1] in dynList[8:]:
                #print("Updating swelling boolean because of chosen transitional " + dyns[-1] + ".")
                if dyns[-1] == "\\<":
                    swelling = (True,"\\<")
                if dyns[-1] == "\\>":
                    swelling = (True,"\\>")
                if dyns[-1] == "\\!":
                    swelling = (False,"\\!")  
                    if not dynList[math.floor(ghostDyn)] == prevDyn:   
                        dyns[-1] = dynList[math.floor(ghostDyn)]
                    else:
                        dyns[-1] = "\\!"
        # REST
        else:
            #print("Not good to dynamicize. If swelling, cut it off.")
            if swelling[0]:
                if swelling[1] == "\\<":
                    if not dynList[math.ceil(ghostDyn)] == prevDyn:
                        if not dyns[-1] == "\\<":
                            dyns[-1] = dynList[math.ceil(ghostDyn)]
                            backProp = True
                            dyns.append("")
                        else:
                            dyns.append("\\!")
                            ghostDyn = dynList.index(prevDyn)
                    else:
                        if not dyns[-1] == "\\<":
                            dyns.append("\\!")
                        else:
                            dyns[-1] = "\\!"
                            dyns.append("")
                            backProp = True
                elif swelling[1] == "\\>":
                    if not dynList[math.floor(ghostDyn)] == prevDyn:
                        if not dyns[-1] == "\\>":
                            dyns[-1] = dynList[math.floor(ghostDyn)]
                            backProp = True
                            dyns.append("")
                        else:
                            dyns.append("\\!")
                            ghostDyn = dynList.index(prevDyn)
                    else:
                        if not dyns[-1] == "\\>":
                            dyns.append("\\!")
                        else:
                            dyns[-1] = "\\!"
                            dyns.append("")
                            backProp = True
                swelling = (False,"\\!")
            else:
                dyns.append("")
        if swelling == (True, "\\<"):
            if not ghostDyn == len(dynList)-4:
                ghostDyn += 0.5
        elif swelling == (True, "\\>"):
            if not ghostDyn == 0:
                ghostDyn -= 0.5            
        if dyns[-1] in dynList[:-3]:
            prevDyn = dyns[-1]
            ghostDyn = dynList.index(prevDyn)
            #print("Updating justDyned to True.")
            justDyned = True
        else:
            #print("Updating justDyned to False.")
            justDyned = False
        prevDyn = [x for x in dyns if x not in ["\\<","\\>","\\!",""]][-1]
        #print(dyns)
        #print()
    # append automatic dynamic on final note
    if not mel[-2][2] == "~":
        if swelling[0]:
            if swelling[1] == "\\<":
                if not dynList[math.ceil(ghostDyn)] == prevDyn:
                    dyns.append(dynList[math.ceil(ghostDyn)])
                else:
                    dyns.append("\\!")
            elif swelling[1] == "\\>":
                if not dynList[math.floor(ghostDyn)] == prevDyn:
                    dyns.append(dynList[math.floor(ghostDyn)])
                else:
                    dyns.append("\\!")
            prevDyn = dyns[-1]
        else:
            dyns.append(random.choice([x for x in dynList if not x == prevDyn and not x == dyns[-1]] + [""]*20))
    else:
        if not swelling[0]:
            dyns.append("")
        else:
            if swelling[1] == "\\<":
                if not dynList[math.ceil(ghostDyn)] == prevDyn:
                    dyns.append(dynList[math.ceil(ghostDyn)])
                else:
                    dyns.append("\\!")
            elif swelling[1] == "\\>":
                if not dynList[math.floor(ghostDyn)] == prevDyn:
                    dyns.append(dynList[math.floor(ghostDyn)])
                else:
                    dyns.append("\\!")
    #print("Dynamics: " + str(dyns) + "\n")
    #print(len(dyns))
    #print(len(mel))
    return [(mel[i][0], mel[i][1], mel[i][2], mel[i][3], dyns[i]) for i in range(len(dyns))]
# beam where appropriate
def beam(mel):
    beamedMel = []
    i = 0
    qsUsed = 0
    totalUsed = 0
    #m = float(meter[:meter.index("/")])/float(int(meter[meter.index("/")+1:])/4)
    m = meter[1]
    qsBeforeTie = 1
    while i < len(mel):
        rhythmToLily = {0.25:"16",0.5:"8",0.75:"8.",1:"4",1.5:"4.",2:"2",3:"2.",4:"1",6:"1.",8:"\\breve"}
        s = ""
        qsUsed += mel[i][1]
        totalUsed += mel[i][1]
        artic = mel[i][2]
        # tie logic
        def tieUp(pitch, val, firstPiece, artic, meterSize, noteLength, barPlace, barSize):
            #print("Writing tie piece of length " + str(val) + "...")
            colLegArtics = ["\\staccatissimo ","\\staccato ","\\staccato ^\\markup \"col legno\" ","^\\markup pizz. \\staccato ","\\snappizzicato \\accent "]
            persistArtics = ["\\) ","\\( ","\\portato ",":32 ","\\tenuto ","\\glissando "]
            lastArtic = artic
            if artic not in persistArtics:
                lastArtic = ""
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
                        if ((barSize - noteLength + preLeg) < m) and not ((barSize - noteLength + preLeg + p[j] + p[j+1]) > m) and not len(p) == 2:
                            temp = p[j] + p[j+1]
                            tempList.append((j, temp))

                if tempList:
                    #print("MERGE COMPLETED")
                    p.insert(tempList[0][0], tempList[0][1])
                    del(p[tempList[0][0]+1])
                    del(p[tempList[0][0]+1])
                return p
            # DEBUG
            #print("TieUp: " + str(mel[i]))
            #print("Note/Place/Bar: " + str(float(noteLength)) + " " + str(float(barPlace)) + " " + str(float(barSize)) + " " + str(float(meterSize)))
            # if need to tie inside bar and noteLength is whole and landing spot isn't on the quarter
            if noteLength % 1 == 0 and not barSize % 1 == 0 and barSize < m:
                #print("Tying inside bar...")
                startPiece = 1 - (barSize % 1)
                endPiece = noteLength - startPiece
                pieces = [startPiece, endPiece]
                #print("After chop: " + str(pieces))
                pieces = split(pieces)
                #print("After split: " + str(pieces))
                pieces = merge(pieces)
                #print("After merge: " + str(pieces))
                if len(pieces) == 1:
                    beamedMel.append((mel[i][0], pieces[0], "", artic))
                else:
                    # if staccato, replace second half of tie with rest
                    if artic in colLegArtics and not artic in persistArtics:
                        beamedMel.append((mel[i][0], pieces[0], "", artic))
                    else:
                        beamedMel.append((mel[i][0],pieces[0],"~",artic))
                    for k in range(1, len(pieces)-1):
                        if artic in colLegArtics and not artic in persistArtics:
                            beamedMel.append((None, pieces[k], "", lastArtic))
                        else:
                            beamedMel.append((mel[i][0], pieces[k], "~", lastArtic))
                    if artic in colLegArtics and not artic in persistArtics:
                        beamedMel.append((None, pieces[-1], "", lastArtic))
                    else:
                        beamedMel.append((mel[i][0], pieces[-1], "", lastArtic))
                return
            # if need to tie over bar
            if barSize > m:
                #print("Tying over bar...")
                if barSize % 1 == 0:
                    endPiece = barSize - m
                    startPiece = noteLength - endPiece
                    if artic in colLegArtics and not artic in persistArtics:
                        beamedMel.append((mel[i][0], startPiece, "", artic))
                    else:
                        beamedMel.append((mel[i][0], startPiece, "~", artic))
                    # if staccato, replace second half of tie with rest
                    if artic in colLegArtics and not artic in persistArtics:
                        beamedMel.append((None, endPiece, "", lastArtic))
                    else:
                        beamedMel.append((mel[i][0], endPiece, "", lastArtic))
                else:
                    endPiece = barSize - m
                    startPiece = min(1 - (barSize % 1), noteLength - endPiece)
                    middlePiece = noteLength - (startPiece + endPiece)
                    pieces = [startPiece, middlePiece, endPiece]
                    #print("After chop: " + str(pieces))
                    pieces = split(pieces)
                    #print("After split: " + str(pieces))
                    pieces = merge(pieces)
                    #print("After merge: " + str(pieces))
                    if len(pieces) == 1:
                        beamedMel.append((mel[i][0], pieces[0], "", artic))
                    else:
                        # if staccato, replace second half of tie with rest
                        if artic in colLegArtics and not artic in persistArtics:
                            beamedMel.append((mel[i][0], pieces[0], "", artic))
                        else:
                            beamedMel.append((mel[i][0], pieces[0], "~", artic))
                        for k in range(1, len(pieces)-1):
                            if artic in colLegArtics and not artic in persistArtics:
                                beamedMel.append((None, pieces[k], "", lastArtic))
                            else:
                                beamedMel.append((mel[i][0], pieces[k], "~", lastArtic))
                        if artic in colLegArtics and not artic in persistArtics:
                            beamedMel.append((None, pieces[-1], "", lastArtic))
                        else:
                            beamedMel.append((mel[i][0], pieces[-1], "", lastArtic))
                return
            # if we can cancel the tie, do it
            elif (float(noteLength) == 2.0 and not float(barPlace) > m and float(barPlace) % 1 == 0.0 and 
                not float(barSize) > m) or (float(noteLength) == 3.0 and not float(barPlace) > m and 
                float(barPlace) % 1 == 0.0 and not float(barSize) > m) or (float(noteLength) == 4.0 and 
                not float(barPlace) > m and float(barPlace) % 1 == 0.0 and not float(barSize) > m) or (float(noteLength) == float(barPlace) == float(barSize)):
                #print("Cancelling tie due to measure-starting/measure-non-exceeding note.")
                beamedMel.append((mel[i][0], noteLength, "", artic))
                return
            # if piece is bigger than our chop limit
            elif val > meterSize:
                #print("Val is too big, shortening...")
                fillLength = val
                pieceLength = fillLength
                pieceDone = 0
                while not pieceLength == 0:
                    end = ""
                    while pieceLength > meterSize:
                        pieceLength -= 0.25      
                        end = "~"
                    if pieceDone == 0:
                        if artic in colLegArtics and not artic in persistArtics:
                            beamedMel.append((mel[i][0], pieceLength, "", artic))
                        else:
                            beamedMel.append((mel[i][0], pieceLength, end, artic))
                    else:
                        if artic in colLegArtics and not artic in persistArtics:
                            beamedMel.append((None, pieceLength, "", artic))
                        else:
                            beamedMel.append((mel[i][0], pieceLength, end, artic))
                    pieceDone += pieceLength
                    pieceLength = fillLength - pieceDone
            # if piece is a valid rhythm
            else:
                #print("Piece is valid, use it...")
                # if staccato, replace second half of tie with rest
                if artic in colLegArtics and not artic in persistArtics:
                    beamedMel.append((pitch, val, "", artic))
                else:
                    beamedMel.append((pitch, val, firstPiece, artic))
            # if a non-final piece
            if firstPiece == "~":
                #print("More pieces to tie, work on them...")
                if artic in colLegArtics:
                    tieUp(None, mel[i][1]-val, "", "",meterSize,noteLength,barPlace,barSize)
                else:
                    tieUp(mel[i][0], mel[i][1]-val, "", "",meterSize,noteLength,barPlace,barSize)
            # if a final piece
            else:
                #print("Final piece, finish.")
                return
        # DEBUG
        #print(mel[i][1],qsUsed,totalUsed)
        # is there a note that extends beyond the qsBeforeTie threshold?
        if qsUsed > qsBeforeTie: # and not ((totalUsed-rhythmValsPicked[i])%meterSub == 0):
            #print("NOTE OVER THE BAR!!!")
            #print("Note beyond qsBeforeTie...")
            qsUsed -= mel[i][1]
            qsLeft = qsBeforeTie-qsUsed
            tieUp(mel[i][0], qsLeft, "~", mel[i][2], qsBeforeTie, mel[i][1],qsUsed+mel[i][1],totalUsed)
            qsUsed += mel[i][1]
        # no need to tie
        else:
            #print("No need to tie!")
            beamedMel.append((mel[i][0], mel[i][1], "", artic))
        # refresh placement stats
        if qsUsed > qsBeforeTie or qsUsed == qsBeforeTie:
            #print("Refresh placement stats...")
            qsUsed = qsUsed%qsBeforeTie
            totalUsed = totalUsed%m
        i += 1
    #print("Beams: " + str([n[2] for n in beamedMel]) + "\n")
    return beamedMel
# final lilypond output formatter
def lilyIze(ls, offset):
    # ls = [0, -7, -5, -3, -5, 4, 2, 0, 2]
    # scale = {0,2,4,5,7,9,11}
    # offset = 2
    # minScales[offset] = {0:"c",1:"cis",2:"d",3:"ees",4:"e",5:"f",6:"ges",7:"g",8:"aes",9:"a",10:"bes",11:"b"}
    #print(ls)
    lilyMel = [minScales[offset][x[0]%12] if not x[0] == None else "r" for x in ls]
    for i in range(len(ls)):
        if not ls[i][0] == None:
            #ls[i] = (ls[i][0]+12, ls[i][1], ls[i][2], ls[i][3], ls[i][4])
            if ls[i][0] < -12:
                while ls[i][0] < -12:
                    lilyMel[i] += ","
                    ls[i] = (ls[i][0]+12, ls[i][1], ls[i][2], ls[i][3], ls[i][4])
            elif ls[i][0] > -1:
                while ls[i][0] > -1:
                    lilyMel[i] += "'"
                    ls[i] = (ls[i][0]-12, ls[i][1], ls[i][2], ls[i][3], ls[i][4])  
    return [lilyMel[i] + rhythmTrans[ls[i][1]] + ls[i][2] + ls[i][3] + ls[i][4] + " " for i in range(len(ls))]
# init tone row with chosen pitch order
def initRow(p):
    global rows
    rows.append([x for x in p if not x == None])
# init melody with chosen pitches and rhythms, artics, beams, dynamics, and lilycode
def initMel(p, r, o, instr, section):
    global mels
    instrOffset = {"violin":0,"viola":-12,"cello":-12,"contrabass":-18}
    melody = [(p[i]+instrOffset[instr], r[i]) if not p[i] == None else (p[i], r[i]) for i in range(len(p))]
    mels.append(melody)
    if section == "a":
        a_mels.append(melody)
        a_pitches.append(p)
    elif section == "b":
        b_mels.append(melody)
        b_pitches.append(p)
    finalMel = articulate(melody)
    finalMel = beam(finalMel)
    finalMel = dynamicize(finalMel)
    finalMel = lilyIze(finalMel, o)
    return finalMel
# format lilypond output code
def startPart(s, instr, meter, tempo, scaleQual, offset):
    instrClefs = {"violin":"treble", "viola":"alto", "cello":"bass", "contrabass":"bass"}
    s += "\\new Staff { \\set Staff.midiInstrument = \"" + instr + "\" \\clef \"" + instrClefs[instr] + "\""
    s += "\\key " + minScales[-1][offset] + "\\" + scaleQual + "\\time " + meter[0] + " \\tempo " + tempo[0] + " 4 = " + tempo[1] 
    return s  
# write a section of the form in the lilypond output code
def section(mel, s, phraseStop, rowName, repeat=False, bSec = False):
    s += mel[0]
    s += " \\finger \markup \\text \"" + rowName + "\" " 
    for i in range(1, len(mel)):
        s += mel[i]
    if repeat:
        s += phraseStop + "\\set Score.repeatCommands = #'(end-repeat)" 
    elif bSec:
        s += phraseStop + "\\bar \"||\""
    return s
# finish lilypond output code
def finishPart(s):
    s += "\\fermata \\bar \"|.\"}"
    return s
# write the lilypond file
def finishLilyFile(s):
    if "solo" not in pieceType:
        s += ">>}"
    s += "\n\\version \"2.22.2\""
    o = open("serial.ly", "w")
    o.write(s)
    o.close()   
# write a serialist piece
def serialPart(s, instr, meter, tempo, row):
    global a_length
    global b_length
    global pieceLength
    global sectionsWritten
    global title
    instrOffset = {"violin":0,"viola":-12,"cello":-12,"contrabass":-18}
    noNones = [x for x in row[1]]
    if "a" not in sectionsWritten:
        pitches = insertRests(noNones)
        rhythms = genRhythms(meter, len(pitches))
        a_length = sum(rhythms)
        rhythmMotifs["b"] = rhythms
    elif "duet" in pieceType:
        noneIndexes = []
        b_pitches_temp = b_pitches[-1]
        while None in b_pitches_temp:
            noneIndexes.append(b_pitches_temp.index(None))
            del b_pitches_temp[b_pitches_temp.index(None)]
        for i in noneIndexes:
            noNones.insert(i, None)
        pitches = [x for x in noNones]
        rhythms = rhythmMotifs["a"]
    else:
        pitches = insertRests(noNones)
        rhythms = genRhythms(meter, len(pitches), (True, a_length))
    print(f"{instr} A: {pitches}, length={sum(rhythms)}")
    row_a = initMel(pitches, rhythms, 0, instr, "a")
    sectionsWritten.append("a")
    row_b_start = (rows[0][0]-rows[0][-1])%12
    # KEEP THE RESTS IN THE SAME SPOT AS A
    row_b_pitches = [(x + row_b_start)%12 if not x == None else x for x in pitches]
    initRow(row_b_pitches)
    if "b" not in sectionsWritten:
        b_rhythms = genRhythms(meter, len(row_b_pitches), (True, a_length))
        b_length = sum(b_rhythms)
        rhythmMotifs["a"] = b_rhythms
    elif "duet" in pieceType:
        b_rhythms = rhythmMotifs["b"]
    else:
        b_rhythms = genRhythms(meter, len(row_b_pitches), (True, b_length))
    print(f"{instr} B: {row_b_pitches}, length={sum(b_rhythms)}")
    b_trans = initMel(row_b_pitches, b_rhythms, 0, instr, "b")
    sectionsWritten.append("b")
    phraseEnding = ""
    if "solo" in pieceType:
        phraseEnding = "\\fermata "
    # P-0 (restatement)
    def mod12(n):
        return n%12
    output = startPart(s, instr, meter, tempo, "major", 0)
    output = section(row_a, output, phraseEnding, list(toneRowDict.keys())[[list(map(mod12, m)) for m in toneRowDict.values()].index([(x+instrOffset[instr])%12 for x in pitches if not x == None])], True)
    output = section(b_trans, output, phraseEnding, list(toneRowDict.keys())[[list(map(mod12, m))for m in toneRowDict.values()].index([(x+instrOffset[instr])%12 for x in row_b_pitches if not x == None])], False, True)
    # print(mels[-1])
    print(f"{instr} A: {pitches}, length={sum(rhythms)}")
    row_a_final = articulate(a_mels[-1])
    row_a_final = beam(row_a_final)
    row_a_final = dynamicize(row_a_final)
    row_a_final = lilyIze(row_a_final, 0)
    output = section(row_a_final, output, "", list(toneRowDict.keys())[[list(map(mod12, m)) for m in toneRowDict.values()].index([(x+instrOffset[instr])%12 for x in pitches if not x == None])])
    totalSectionBeats = sum(rhythms)+sum(b_rhythms)+sum(rhythms)
    lenDiff = 0
    if partLengths:
        lenDiff = abs(totalSectionBeats-partLengths[-1])
        if lenDiff > meter[1]-1:
            print(str(lenDiff) + " quarter-beat length difference than previous part. That's " + str(lenDiff/meter[1]) + " measures.") 
            # writeGapMaterial()
    else:
        pieceLength = totalSectionBeats
    partLengths.append(totalSectionBeats) 
    output = finishPart(output)
    return output
# write a diatonic solo piece (STILL IN DEVELOPMENT)
def diatonicSolo(meter, tempo):
    offset = random.randint(0,11)
    scale = {0,2,3,5,7,8,10}
    scaleQual = "minor"
    print("Scale: " + str(scale))
    # AA
    rhythms = genRhythms(meter, 0)
    pitches = genPitches(rhythms, scale, offset)
    a_melody = initMel(pitches, rhythms, offset)
    output = startOut(meter, tempo, scaleQual, "Solo for Violin", offset) 
    output = section(a_melody, output, "", True)
    # B
    b_rhythms = genRhythms(meter, 0)
    b_pitches = genPitches(b_rhythms, scale, offset, 7)
    b_melody = initMel(b_pitches, b_rhythms, offset)
    output = section(b_melody, output, "", False, True)
    # A
    mel_a_final = articulate(mels[0])
    mel_a_final = beam(mel_a_final)
    mel_a_final = dynamicize(mel_a_final)
    mel_a_final = lilyIze(mel_a_final, offset)
    output = section(mel_a_final, output, "")
    output = finishOut(output)
# returns set matrix for given prime form
def makeMatrix(prime):
    matrix = [prime]
    startNote = prime[0]
    diffs = [x-startNote for x in prime]
    for i in range(1, len(prime)):
        matrix.append([x-diffs[i] for x in prime])  
    return matrix
   
# CHOOSE TEMPO, METER and SOLO INSTRUMENT (perhaps prompt the user for the latter (or all of these!))
def tableize(option_list):
    table = ""
    for x in option_list:
        table += "- "
        table += x
        table += "\n"
    return table
partsForType = {"string solo":["violin"], "string duet":["violin","viola"], 
                "string trio":["violin","viola","cello"], "string quartet":["violin","viola","cello","contrabass"]}
pieceType = ""
pieceTypes = list(partsForType.keys())
pieceTypeTable = tableize(pieceTypes)
soloInstruments = ["violin","viola","cello","contrabass"]
soloInstrTable = tableize(soloInstruments)
tempoMark = random.choice(tempos)
bpm = random.randint(tempoMark[1][0],tempoMark[1][1])
tempo = (tempoMark[0], str(bpm))
meter = random.choice(meters)
printHeader()
lilyFile = ""
altoWait = 5
tenorWait = 9
bassWait = 13
# 1. ASK FOR TYPE OF PIECE (SOLO, DUET, TRIO, QUARTET)
print("\nNeed some music written fast?\n")
def pieceTypeAsk(options):
    global pieceType
    pieceTypeAns = input("What type of piece would you like me to write today? " +
                    "Here are the following types I can write so far...\n\n" + pieceTypeTable + "\n")
    if pieceTypeAns in options:
        pieceType = pieceTypeAns
        return
    else:
        print("\nI'm sorry, I can't write that type of piece.\n")
        pieceTypeAsk(options)

pieceTypeAsk(pieceTypes)
title = pieceType
print(pieceType)
# 2. IF SOLO -> ASK WHAT INSTRUMENT, partsToMake = 1
if "solo" in pieceType:
    soloInstr = input("\nA " + pieceType + ", nice. What instrument would you like me to write the " + pieceType + " for? Currently," +  
                      " only the four main string instruments are supported.\n\n" + soloInstrTable + "\n")
    # CHANGE TITLE TO MATCH SOLO INSTRUMENT
    titleInstr = soloInstr.capitalize()
    title = titleInstr + " Solo"
    lilyFile += "\\header { title = \"" + title + "\"}"
    partsToMake = [soloInstr]
    print("\nA " + soloInstr + " solo, got it. Generating piece...\n")
# ELSE partsToMake corresponds to the numbers of parts in the pieceType
else:
    title = [x.capitalize() for x in pieceType.split()]
    lilyFile += "\\header { title = \"" + " ".join(title) + "\"}"
    lilyFile += "\\score {\\new PianoStaff <<"
    partsToMake = partsForType[pieceType]
    print("\nGenerating " + pieceType + "...\n")

print("Choosing tempo...")
print(tempo)
print("Choosing meter...")
print(meter)
# 3. GENERATE TONE ROW + MATRIX
print("Generating tone row...")
toneRowDict = {}
toneRow = genToneRow()
initRow(toneRow)
p0 = toneRow
print(str([x%12 for x in p0]) + "\n")
startNote = p0[0]%12
primes = makeMatrix(p0)
retrogrades = [x[::-1] for x in primes]
inversions = []
for a in range(len(primes[0])):
    inversions.append([x[a] for x in primes])
retroInversions = [x[::-1] for x in inversions]
# POPULATE TONE ROW DICT
for p in primes:
    toneRowDict[f"P-{(p[0]-startNote)%12}"] = p
# for r in retrogrades:
#     toneRowDict[f"R-{(r[-1]-startNote)%12}"] = r
# for i in inversions:
#     toneRowDict[f"I-{(i[0]-startNote)%12}"] = i
# for ri in retroInversions:
#     toneRowDict[f"RI-{(ri[-1]-startNote)%12}"] = ri

# 4. FORM PARTS, EACH LIKE SO: -> \new Staff { \set Staff.midiInstrument = "instr" \clef "clef" 
#    \key c \major \time 4/4\tempo Moderato 4 = 101 MUSIC }
for instr in partsToMake:
    print("Writing " + instr + " part...")
    if instr == partsToMake[0]:
        rowChoice = ("P-0", toneRowDict["P-0"])
    else:
        rowChoiceId = random.choice(list(toneRowDict.keys()))
        rowChoice = (rowChoiceId, toneRowDict[rowChoiceId])
    lilyFile = serialPart(lilyFile, instr, meter, tempo, rowChoice)
    #print(rows)

# 5. FORM FINISHER -> finishLilyFile(lilyFile)
finishLilyFile(lilyFile)
print("\nPiece generated.\n")