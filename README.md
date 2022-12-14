# four-part-composer

ACE™ (Algorithmic Composition Engine).

Current supported features:
- 'makeFourParts.py' -> Writes a 16-bar, AABA tune with four-part harmony.
- 'melody.py' -> Writes a melody and applies it to various piece contexts.
- 'serial.py' -> Writes a violin solo in the style of serialism.

'serial.py' TODO: 
- REFACTOR CODE!!!!!!!!!!
- Boost slurs and observe stability.
- Decide whether or not to TieUp every staccato note that's longer than a quarter.
- Implement harmonics
- Implement function to keep the contour the same for the b section (interval check)
- Implement function that intersperses rests in a tone row (same count that are in prime)
- Implement set-matrix function
- Implement ability to choose instrument for solo
- Implement 'melody analyzer'
- Implement metric change ability
- Implement tempo change ability
- Implement 'key-defining scale degrees' that hold more weight
- Implement pickup notes
- Implement 'passacaglia' feature
- Implement 'multi-harmonize' feature
- Implement 'raga' feature (bass drone, long meter, etc.)
- Implement 'mirror' melody feature (build from both ends!)
- Implement feature which supports talea and color

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
- This will create a '.ly' file in that same repository.
- Open the '.ly' file using LilyPond.
- Press cmd-R to convert the LilyPond file to MIDI. You should then see a similarly named MIDI file '.midi' appear in the repository. If a PDF is made instead, you will need to add "\midi{}" to the .ly file directly after the second-to-last closed curly brace. Save and redo the cmd-R, and you should now see that the MIDI file has been generated within the repository.
- Open the '.midi' with your notation software of choice.
- Play back the score.
- Want to generate another tune/melody? Simply repeat the 'Generating Music' steps!

Enjoy!


