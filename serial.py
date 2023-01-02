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
rhythmKey = [0.25,0.5,0.75,1,1.5,2,3,4]
rhythms = [0.25,0.5,0.75,1,1.5,2,3,4]
pitchToLily = {None:"r",0:"c'",1:"cis'",2:"d'",3:"dis'",
              4:"e'",5:"f'",6:"fis'",7:"g'",8:"gis'",
              9:"a'",10:"ais'",11:"b'",12:"c''",13:"cis''",
              14:"d''",15:"dis''",16:"e''",17:"f''",18:"fis''",
              19:"g''",20:"gis''",21:"a''",22:"ais''",23:"b''",
              24:"c'''",25:"cis'''",26:"d'''",27:"dis'''",28:"e'''",
              29:"f'''",30:"fis'''",31:"g'''",32:"gis'''",33:"a'''",
              34:"ais'''",35:"b'''",36:"c''''"}
rhythmTrans = {0.25:"16",0.5:"8",0.75:"8.",1:"4",1.5:"4.",2:"2",3:"2.",4:"1"}
tempos = [("Largo",(40,60)),("Adagio",(61,75)),("Andante",(76,107)),("Moderato",(108,119)),("Allegro",(120,155)),("Vivace",(156,175)),("Presto",(168,200))]
meters = [("3/4",3),("4/4",4),("4/4",4),("4/4",4),("4/4",4),("5/4",5),("6/4",3),("7/4",7)]

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
def choosePitches():
    noteMap = list(range(12))
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
        if dieRoll < 2:
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
# generates a list of rhythm values
def genRhythms():
    c = -1000000
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
            if c == 1:
                row_length = sum(rhythmChoices) + choice
                if row_length % 1 == 0 or row_length % 1 == 0.5:
                    row_choice_good = True
                    c = 0
            else:
                row_choice_good = True
                c += 1
        rhythmChoices.append(choice)
        if len(rhythmChoices) == len(pitches):
            row_length_good = True 
        row_choice_good = False
    return rhythmChoices
# places articulations on notes of the melody
def articulate(mel):
    artics = []
    # 0-8 artics, (9 openSlur, 18 port, 19 closeSlur), (10 non-vib, 20 vib), 
    # (11 pizz, 21 snap, 22 stopped, 23 arco)
    # think of something for 2,6,8 
    # don't let staccato go onto long notes (2 or greater)
    articToLily = {0:"",1:"\\accent ",2:"\\tenuto ",3:"\\marcato ",4:"\\staccato ",
                   5:"\\staccatissimo ",6:":32 ",7:"\\glissando ", 8:":32 ",
                   9:"\\( ", 10:"^\\markup non-vib. ", 11:"^\\markup pizz. \\staccato ", 
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
        pizzMode = [[4,22,(23, defMode),(23, defMode),(23, defMode)], [4,22,(23, defMode),(23, defMode),(23, defMode)], [4,22,(23, defMode),(23, defMode),(23, defMode)],
                    [4,22,(23, defMode,(23, defMode),(23, defMode))], [4,21,22,(23, defMode),(23, defMode),(23, defMode)], [4,21,22,(23, defMode),(23, defMode),(23, defMode)],
                    [0,4,21,22,(23, defMode)], [0,4,21,22,(23, defMode)]]
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
        print("Pitch Val: " + str(mel[i][0]))
        print("Rhythm Val: " + str(mel[i][1]))
        print("Option Index: " + str(rhythms.index(mel[i][1])))
        print("Length of currMode: " + str(len(currMode)) + ", SlurMode: " + str(currMode == slurMode))
        print("Length of defMode: " + str(len(defMode)))
        print("ModeCt: " + str(modeCt))
        if len(currMode) == 0:
            currMode = defMode
            print("Fixing empty list....")
            print("Length of currMode: " + str(len(currMode)))
        currSlur = False
        nonZs = [x for x in artics if not x == 0]
        if nonZs:
            currSlur = nonZs[-1]
        # automatically end modes that go on too long
        if mel[i][0] == None or ((currSlur == 9 or currSlur == 18) and modeCt > 1):
            print("Rest recognized OR slur limit reached.")
            if (currSlur == 9 or currSlur == 18) and modeCt > 1 and not mel[i][0] == None:
                print("Slur limit reached.")
                artic = (19, defMode)
            else:
                print("Rest recognized.")
                if currSlur == 9:
                    print("Don't begin slur. If we just began slur, remove it.")
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
            print("Note recognized.")
            if currMode == colLegMode:
                print("ColLegMode recognized.")
                artic = random.choice([4,(24,defMode)])
            else:
                print("Non ColLegMode recognized.")
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
                        #print("Non rest in pizz mode, keeping the staccato.")
                        artics.append(4)
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
        #print("Artic chosen: " + articToLily[artics[-1]])
        #print("Artics So Far: " + str(artics) + "\n")
    print("Articulations: " + str([articToLily[a] for a in artics]) + "\n")
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
def lilyIze(ls):
    return [pitchToLily[x[0]] + rhythmTrans[x[1]] + x[2] + x[3] + x[4] + " " for x in ls]
# returns inverted tone row
def makeInversion(ls):
    start = 0
    for l in ls:
        if not l == None:
            start = l
            break
    inv = [x-start if not x == None else None for x in ls]
    inv = [x*-1 if not x == None else None for x in inv]
    inv = [x+start if not x == None else None for x in inv]
    inv = [x%12 if not x == None else None for x in inv]
    return inv

# CHOOSE TEMPO, METER and SOLO INSTRUMENT (perhaps prompt the user for the latter (or all of these!))
tempoMark = random.choice(tempos)
bpm = random.randint(tempoMark[1][0],tempoMark[1][1])
tempo = (tempoMark[0], str(bpm))
meter = random.choice(meters)
printHeader()
print("Tempo chosen: " + str(tempo))
print("Meter chosen: " + meter[0])

# CHOOSE PITCHES
pitches = choosePitches()
rows.append([x for x in pitches if not x == None])

# DETERMINE SCALE AND KEY SIG BASED ON PITCH SELECTION (for non-serial modes)

# CHOOSE RHYTHMS FOR MELODY
row_length_ok = False
while not row_length_ok:
    rhythmList = genRhythms()
    sumRhythms = sum(rhythmList)
    if sumRhythms % int(meter[0][0]) == 0:
        row_length_ok = True
#print("Rhythms: " + str(rhythmList) + "\n")

# CREATE TONE ROW AND CALCULATE LENGTH
tone_row = [(pitches[i], rhythmList[i]) for i in range(len(pitches))]
row_length = sum([x[1] for x in tone_row])

# ADD ARTICULATIONS, BEAMING, and DYNAMICS
#print("Tone Row: " + str(tone_row) + "\n")
row_a_artic = articulate(tone_row)
row_a_beam = beam(row_a_artic)
row_a_dyn = dynamicize(row_a_beam)
row_a = lilyIze(row_a_dyn)
print("\nP-0: " + str([x%12 if not x == None else x for x in pitches]) + "\n")

# FORMAT LILYPOND CODE
#row_b_start = ((rows[0][-1]+6)%12-rows[0][0])%12
row_b_start = (rows[0][0]-rows[0][-1])%12
row_b_pitches = [(x + row_b_start)%12 if not x == None else x for x in pitches]
title = "P-0, P-" + str(row_b_start) + ", P-0"
s = "\\header { title = \"" + title + "\"}"
s += "\\score { \\new Staff { \\set Staff.midiInstrument = \"violin\" \\clef \"treble\" "
s += "\\key c \\major \\time " + meter[0] + " \\tempo " + tempo[0] + " 4 = " + tempo[1]
# A x2: P-0
#print("LilyPond Formatted Row: " + str(row_a) + "\n")
for x in row_a:
    s += x
s += "\\fermata \\set Score.repeatCommands = #'(end-repeat)"
# B: P-(P-0[-1]+6)%12
print("P-" + str(row_b_start) + ": " + str(row_b_pitches) + "\n")
rows.append([x for x in row_b_pitches if not x == None])
row_length_ok = False
while not row_length_ok:
    rhythmList = genRhythms()
    sumRhythms = sum(rhythmList)
    if sumRhythms % int(meter[0][0]) == 0:
        row_length_ok = True
row_b = [(row_b_pitches[i], rhythmList[i]) for i in range(len(row_b_pitches))]
row_length = sum([x[1] for x in row_b])
row_b_artic = articulate(row_b)
row_b_beam = beam(row_b_artic)
row_b_dyn = dynamicize(row_b_beam)
row_b_final = lilyIze(row_b_dyn)
#print("LilyPond Formatted Row: " + str(row_b_final) + "\n")
for x in row_b_final:
    s += x
s += "\\fermata \\bar \"||\""
# A: P-0 
row_a_final = articulate(tone_row)
row_a_final = beam(row_a_final)
row_a_final = dynamicize(row_a_final)
row_a_final = lilyIze(row_a_final)
#print("LilyPond Formatted Row: " + str(row_a_final) + "\n")
for x in row_a_final:
    s += x
s += "\\fermata \\bar \"|.\""
s += "}\n}\\version \"2.22.2\""
o = open("serial.ly", "w")
o.write(s)
o.close()