# four-part-composer

ACE™ (Algorithmic Composition Engine).

Current supported features:
- 'makeFourParts.py' -> Writes a 16-bar, AABA, four-part harmonized tune.
- 'melody.py' -> Equipped with many modes of generating a melody.

'melody.py' TODO: 
- Implement slurs
- Implement logic for dynamics
- Implement 'tie over bar' logic for PDFs in melToLily
- Implement 'weighted scale degrees' when choosing leaps and steps
- Implement pickup notes
- Implement 'raga' feature (drone, long meter, etc.)
- Implement 'mirror' melody feature
- Release control of hardcoded values (phraseLength, genRhythmVals, articChoices, etc.)
- Add features to support serialism, talea and color, etc.

Development Road Map for 'Fugue' Feature: 
- Jan 31, 2023 - 'bassline.py' -> Writes a bassline which harmonizes a given melody
- Feb 28, 2023 - 'harmony.py -> Decides vertical harmonies to correspond with a given melody and bassline
- March 31, 2023 - 'voiceLead.py' -> Creates solid voice leading for four-part harmony
- April 30, 2023 - 'form.py' -> Handles the writing and usage of main themes, motifs, and the tonal road map.
- May 31, 2023 - 'fugue.py' -> Combines all of the above scripts into the ultimate composition script.

Prerequisites:
- Python3
- LilyPond (http://lilypond.org/download.html)
- Notation software that can open MIDI files (MuseScore for example)

Setup Instructions:
- Open terminal.
- Clone this repository onto your computer.
- Navigate to the repository in your terminal (cd four-part-composer).

Generating Music:
- Run the script of your choice by entering the command 'python3 _filename_'.
- This will create a 'ConvertMe.ly' file in that same repository.
- Open 'ConvertMe.ly' using LilyPond.
- Press cmd-R to convert the LilyPond file to MIDI. You should then see the MIDI file 'ConvertMe.midi' appear in the repository. If a PDF is made instead, you will need to add "\midi{}" to the .ly file directly after the second-to-last closed curly brace. Save and redo the cmd-R, and you should now see that the MIDI file has been generated within the repository.
- Open 'ConvertMe.midi' with your notation software of choice.
- Playback the score.
- Want to generate another tune/melody? Simply repeat the 'Generating Music' steps!

Enjoy!


