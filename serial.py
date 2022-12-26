import random

def lilyIze(ls):
    return [[pitchTrans[x[0]] for x in ls][i] + [rhythmTrans[x[1]] for x in ls][i] + " " for i in range(len(ls))]
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
                
# Create a list named 'notes' containing integers from 0 to 11.
notes = list(range(12))

# Create a new empty list named 'choices'.
pitches = []
rhythms = [0.25,0.5,0.75,1,1.5,2,3,4]
pitchTrans = {None:"r",0:"c'",1:"cis'",2:"d'",3:"dis'",
              4:"e'",5:"f'",6:"fis'",7:"g'",8:"gis'",
              9:"a'",10:"ais'",11:"b'"}
rhythmTrans = {0.25:"16",0.5:"8",0.75:"8.",1:"4",1.5:"4.",2:"2",3:"2.",4:"1"}

while len(notes) > 0:
    dieRoll = random.randint(0, 9)
    if dieRoll < 2:
        pitches.append(None)
    else:
        choice = random.choice(notes)
        pitches.append(choice)
        notes.remove(choice)
    
def genRhythms():
    c = 0
    rhythmChoices = [random.choice(rhythms)]
    row_length_good = False
    row_choice_good = False
    while not row_length_good:
        while not row_choice_good:
            choice = random.choice(rhythms)
            if c == 4:
                row_length = sum(rhythmChoices) + choice
                if row_length % 1 == 0:
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

row_length_ok = False
while not row_length_ok:
    rhythmList = genRhythms()
    sumRhythms = sum(rhythmList)
    if sumRhythms % 1 == 0 and (sumRhythms % 2 == 0 or sumRhythms % 3 == 0):
        row_length_ok = True

tone_row = [(pitches[i], rhythmList[i]) for i in range(len(pitches))]
row_length = sum([x[1] for x in tone_row])
print("Row:")
# print(pitches)
# print(rhythmList)
print(tone_row)
bottom_meter = 4
if row_length % 8 == 0:
    top_meter = row_length / 8
elif row_length % 4 == 0:
    top_meter = row_length / 4
elif row_length % 3 == 0:
    top_meter = row_length / 3
elif row_length % 2 == 0:
    top_meter = row_length / 2
meter = str(int(top_meter)) + "/" + str(bottom_meter)

# FORMAT LILYPOND CODE
s = "\\header { title = \"Serial Piece\"}"
s += "\\score { \\new Staff { \\set Staff.midiInstrument = \"oboe\" \\clef \"treble\" "
s += "\\key c \\major \\time " + meter + " \\tempo Andante 4 = 80 "
row_a = lilyIze(tone_row)
for _ in range(2):
    for x in row_a:
        s += x
invPitches = makeInversion([x for x in pitches])
print()
print("Inverted Row:")
# print(invPitches)
# print(rhythmList)
tone_row = [(invPitches[i], rhythmList[i]) for i in range(len(invPitches))]
print(tone_row)
row_b = lilyIze(tone_row)
for x in row_b:
    s += x
for x in row_a:
    s += x
s += "}\n}\\version \"2.22.2\""
#print()
#print("Output code:")
#print(s)
o = open("serial.ly", "w")
o.write(s)
o.close()
# s += "f'8\accent  g'8~\accent  g'8 a'8 g'2\accent  a'8^\markup pizz.  g'8~\accent  g'8 a'8~ a'8 c''8^\markup arco  c'''8.\staccato  a''16~ a''16 g''8.~ g''4~ g''16 f''8.\staccato