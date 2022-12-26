"""
                # if trying 3 on beat 2.25, split into 0.75 + 2 + 0.25
                if (float(noteLength) == 3.0 and float(barPlace) == 3.25 and float(barSize) == 4.25):
                    print("0.75 + 2 + 0.25")
                    lilyMelody.append(s + rhythmToLily[0.75] + "~" + artic) # 5 - barSize
                    lilyMelody.append(s + rhythmToLily[2.0] + "~" + lastArtic)
                    lilyMelody.append(s + rhythmToLily[0.25] + lastArtic)
                    return
                # if trying 3 on beat 2.5, split into 0.5 + 2 + 0.5
                if (float(noteLength) == 3.0 and float(barPlace) == 3.5 and float(barSize) == 4.5):
                    print("0.5 + 2 + 0.5")
                    lilyMelody.append(s + rhythmToLily[0.5] + "~" + artic) # 5 - barSize
                    lilyMelody.append(s + rhythmToLily[2.0] + "~" + lastArtic)
                    lilyMelody.append(s + rhythmToLily[0.5] + lastArtic)
                    return
                # if trying 3 on beat 2.75, split into 0.25 + 2 + 0.75
                if (float(noteLength) == 3.0 and float(barPlace) == 3.75 and float(barSize) == 4.75):
                    print("0.25 + 2 + 0.75")
                    lilyMelody.append(s + rhythmToLily[0.25] + "~" + artic)  # 5 - barSize
                    lilyMelody.append(s + rhythmToLily[2.0] + "~" + lastArtic)
                    lilyMelody.append(s + rhythmToLily[0.75] + lastArtic)
                    return
                # if trying 3 on beat 3, split into 2 + 1
                if (float(noteLength) == 3.0 and float(barPlace) == 3.0 and float(barSize) == 5.0):
                    print("2 + 1")
                    lilyMelody.append(s + rhythmToLily[2.0] + "~" + artic) # barSize - barPlace
                    lilyMelody.append(s + rhythmToLily[1.0] + lastArtic)
                    return
                # if trying 3 on beat 3.25, split into 0.75 + 1 + 1 + 0.25
                if (float(noteLength) == 3.0 and float(barPlace) == 3.25 and float(barSize) == 5.25):
                    print("0.75 + 1 + 1 + 0.25")
                    lilyMelody.append(s + rhythmToLily[0.75] + "~" + artic)
                    lilyMelody.append(s + rhythmToLily[1.0] + "~" + lastArtic)
                    lilyMelody.append(s + rhythmToLily[1.0] + "~" + lastArtic)
                    lilyMelody.append(s + rhythmToLily[0.25] + lastArtic)
                    return
                # if trying 3 on beat 3.5, split into 1.5 + 2
                if (float(noteLength) == 3.0 and float(barPlace) == 3.5 and float(barSize) == 5.5):
                    print("1.5 + 1.5")
                    lilyMelody.append(s + rhythmToLily[1.5] + "~" + artic)
                    lilyMelody.append(s + rhythmToLily[1.5] + lastArtic)
                    return
                # if trying 3 on beat 3.75, split into 0.25 + 2 + 0.75
                if (float(noteLength) == 3.0 and float(barPlace) == 3.75 and float(barSize) == 5.75):
                    print("0.25 + 2 + 0.75")
                    lilyMelody.append(s + rhythmToLily[0.25] + "~" + artic)
                    lilyMelody.append(s + rhythmToLily[2.0] + "~" + lastArtic)
                    lilyMelody.append(s + rhythmToLily[0.75] + lastArtic)
                    return
                # if trying 3 on beat 4, split into 1 + 2
                if (float(noteLength) == 3.0 and float(barPlace) == 3.0 and float(barSize) == 6.0):
                    print("1 + 2")
                    lilyMelody.append(s + rhythmToLily[1.0] + "~" + artic)  # 4 - barPlace
                    lilyMelody.append(s + rhythmToLily[2.0] + lastArtic)
                    return
                # if trying 3 on beat 4.25, split into 0.75 + 2 + 0.25
                if (float(noteLength) == 3.0 and float(barPlace) == 3.25 and float(barSize) == 6.25):
                    print("0.75 + 2 + 0.25")
                    lilyMelody.append(s + rhythmToLily[0.75] + "~" + artic) 
                    lilyMelody.append(s + rhythmToLily[2.0] + "~" + lastArtic) 
                    lilyMelody.append(s + rhythmToLily[0.25] + lastArtic)
                    return
                # if trying 3 on beat 4.5, split into 0.5 + 2 + 0.5
                if (float(noteLength) == 3.0 and float(barPlace) == 3.5 and float(barSize) == 6.5):
                    print("0.5 + 2 + 0.5")
                    lilyMelody.append(s + rhythmToLily[0.5] + "~" + artic) 
                    lilyMelody.append(s + rhythmToLily[2.0] + "~" + lastArtic) 
                    lilyMelody.append(s + rhythmToLily[0.5] + lastArtic)
                    return
                # if trying 3 on beat 4.75, split into 0.25 + 2 + 0.75
                if (float(noteLength) == 3.0 and float(barPlace) == 3.75 and float(barSize) == 6.75):
                    print("0.25 + 2 + 0.75")
                    lilyMelody.append(s + rhythmToLily[0.25] + "~" + artic) 
                    lilyMelody.append(s + rhythmToLily[2.0] + "~" + lastArtic) 
                    lilyMelody.append(s + rhythmToLily[0.75] + lastArtic)
                    return
                # if trying 4 on beat 1.25, split into 0.75 + 3 + 0.25
                if (float(noteLength) == 4.0 and float(barPlace) == 4.25 and float(barSize) == 4.25):
                    print("0.75 + 3 + 0.25")
                    lilyMelody.append(s + rhythmToLily[0.75] + "~" + artic) # 5 - barSize
                    lilyMelody.append(s + rhythmToLily[3.0] + "~" + lastArtic) 
                    lilyMelody.append(s + rhythmToLily[0.25] + lastArtic)
                    return
                # if trying 4 on beat 1.5, split into 0.5 + 3 + 0.5
                if (float(noteLength) == 4.0 and float(barPlace) == 4.5 and float(barSize) == 4.5):
                    print("0.5 + 3 + 0.5")
                    lilyMelody.append(s + rhythmToLily[0.5] + "~" + artic) # 5 - barSize
                    lilyMelody.append(s + rhythmToLily[3.0] + "~" + lastArtic) 
                    lilyMelody.append(s + rhythmToLily[0.5] + lastArtic)
                    return
                # if trying 4 on beat 1.75, split into 0.25 + 3 + 0.75
                if (float(noteLength) == 4.0 and float(barPlace) == 4.75 and float(barSize) == 4.75):
                    print("0.25 + 3 + 0.75")
                    lilyMelody.append(s + rhythmToLily[0.25] + "~" + artic) # 5 - barSize
                    lilyMelody.append(s + rhythmToLily[3.0] + "~" + lastArtic) 
                    lilyMelody.append(s + rhythmToLily[0.75] + lastArtic)
                    return
                # if trying 4 on beat 2, split into 3 + 1
                if (float(noteLength) == 4.0 and float(barPlace) == 4.0 and float(barSize) == 5.0):
                    print("3 + 1")
                    lilyMelody.append(s + rhythmToLily[3.0] + "~" + artic) # 8 - barSize
                    lilyMelody.append(s + rhythmToLily[1.0] + lastArtic) # barSize - noteLength
                    # count has already reached noteLength
                    return
                # if trying 4 on beat 2.25, split into 0.75 + 3 + 0.25
                if (float(noteLength) == 4.0 and float(barPlace) == 4.25 and float(barSize) == 5.25):
                    print("0.75 + 3 + 0.25")
                    lilyMelody.append(s + rhythmToLily[0.75] + "~" + artic) 
                    lilyMelody.append(s + rhythmToLily[3.0] + "~" + lastArtic) 
                    lilyMelody.append(s + rhythmToLily[0.25] + lastArtic) 
                    return
                # if trying 4 on beat 2.5, split into 0.5 + 2 + 1.5
                if (float(noteLength) == 4.0 and float(barPlace) == 4.5 and float(barSize) == 5.5):
                    print("0.5 + 2 + 1.5")
                    lilyMelody.append(s + rhythmToLily[0.5] + "~" + artic) 
                    lilyMelody.append(s + rhythmToLily[2.0] + "~" + lastArtic)
                    lilyMelody.append(s + rhythmToLily[1.5] + lastArtic)
                    return
                # if trying 4 on beat 2.75, split into 0.25 + 2 + 1 + 0.75
                if (float(noteLength) == 4.0 and float(barPlace) == 4.75 and float(barSize) == 5.75):
                    print("0.25 + 2 + 1 + 0.75")
                    lilyMelody.append(s + rhythmToLily[0.25] + "~" + artic) 
                    lilyMelody.append(s + rhythmToLily[2.0] + "~" + lastArtic)
                    lilyMelody.append(s + rhythmToLily[1.0] + "~" + lastArtic)
                    lilyMelody.append(s + rhythmToLily[0.75] + lastArtic)
                    return
                # if trying 4 on beat 3, split into 2 + 2
                if (float(noteLength) == 4.0 and float(barPlace) == 4.0 and float(barSize) == 6.0):
                    print("2 + 2")
                    lilyMelody.append(s + rhythmToLily[2.0] + "~" + artic) # 8 - barSize
                    lilyMelody.append(s + rhythmToLily[2.0] + lastArtic) # barSize - barPlace
                    return
                # if trying 4 on beat 3.25, split into 0.75 + 1 + 2 + 0.25
                if (float(noteLength) == 4.0 and float(barPlace) == 4.25 and float(barSize) == 6.25):
                    print("0.75 + 1 + 2 + 0.25")
                    lilyMelody.append(s + rhythmToLily[0.75] + "~" + artic) # 5 - barPlace
                    lilyMelody.append(s + rhythmToLily[1.0] + "~" + lastArtic) 
                    lilyMelody.append(s + rhythmToLily[2.0] + "~" + lastArtic) 
                    lilyMelody.append(s + rhythmToLily[0.25] + lastArtic) 
                    return
                # if trying 4 on beat 3.5, split into 0.5 + 1 + 2 + 0.5
                if (float(noteLength) == 4.0 and float(barPlace) == 4.5 and float(barSize) == 6.5):
                    print("0.5 + 1 + 2 + 0.5")
                    lilyMelody.append(s + rhythmToLily[0.5] + "~" + artic)
                    lilyMelody.append(s + rhythmToLily[1.0] + "~" + lastArtic)
                    lilyMelody.append(s + rhythmToLily[2.0] + "~" + lastArtic)
                    lilyMelody.append(s + rhythmToLily[0.5] + lastArtic) 
                    return
                # if trying 4 on beat 3.75, split into 0.25 + 1 + 2 + 0.75
                if (float(noteLength) == 4.0 and float(barPlace) == 4.75 and float(barSize) == 6.75):
                    print("0.25 + 1 + 2 + 0.75")
                    lilyMelody.append(s + rhythmToLily[0.25] + "~" + artic) 
                    lilyMelody.append(s + rhythmToLily[1.0] + "~" + lastArtic) 
                    lilyMelody.append(s + rhythmToLily[2.0] + "~" + lastArtic)
                    lilyMelody.append(s + rhythmToLily[0.75] + lastArtic) 
                    return
                # if trying 4 on beat 4, split into 1 + 3
                if (float(noteLength) == 4.0 and float(barPlace) == 4.0 and float(barSize) == 7.0):
                    print("1 + 3")
                    lilyMelody.append(s + rhythmToLily[1.0] + "~" + artic) # 8 - barSize
                    lilyMelody.append(s + rhythmToLily[3.0] + lastArtic) # barSize - barPlace
                    return
                # if trying 4 on beat 4.25, split into 0.75 + 3 + 0.25
                if (float(noteLength) == 4.0 and float(barPlace) == 4.25 and float(barSize) == 7.25):
                    print("0.75 + 3 + 0.25")
                    lilyMelody.append(s + rhythmToLily[0.75] + "~" + artic) # 8 - barSize
                    lilyMelody.append(s + rhythmToLily[3.0] + "~" + lastArtic) # barSize - barPlace
                    lilyMelody.append(s + rhythmToLily[0.25] + lastArtic) # noteLength - (barSize - barPlace + 5 - barPlace) (if still room)
                    return
                # if trying 4 on beat 4.5, split into 0.5 + 3 + 0.5
                if (float(noteLength) == 4.0 and float(barPlace) == 4.5 and float(barSize) == 7.5):
                    print("0.5 + 3 + 0.5")
                    lilyMelody.append(s + rhythmToLily[0.5] + "~" + artic) # 8 - barSize
                    lilyMelody.append(s + rhythmToLily[3.0] + "~" + lastArtic) # barSize - barPlace
                    lilyMelody.append(s + rhythmToLily[0.5] + lastArtic) # noteLength - (barSize - barPlace + 5 - barPlace) (if still room)
                    return
                # if trying 4 on beat 4.75, split into 0.25 + 3 + 0.75
                if (float(noteLength) == 4.0 and float(barPlace) == 4.75 and float(barSize) == 7.75):
                    print("0.25 + 3 + 0.75")
                    lilyMelody.append(s + rhythmToLily[0.25] + "~" + artic) # 8 - barSize
                    lilyMelody.append(s + rhythmToLily[3.0] + "~" + lastArtic) # barSize - barPlace
                    lilyMelody.append(s + rhythmToLily[0.75] + lastArtic) # noteLength - (barSize - barPlace + 5 - barPlace) (if still room)
                    return
                """