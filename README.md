# four-part-composer

ACE™ (Algorithmic Composition Engine).

Current supported features:
- 'makeFourParts.py' -> Writes a 16-bar, four-part harmonized tune.
- 'melody.py' -> Generates a melody (AABA, 16 measure default) from either a major, minor, chromatic, or randomly built scale.

'melody.py' TODO: 
- Implement sixteenth notes.
- Implement 'target note' feature to create countour and punctuate phrases.
- Add 'rhythmic motif' feature that writes and employs rhythmic motifs.
- Implement smarter rests that punctuate phrases and are not just random.
- Create more random variables to control dynamics, articulations, ornaments, tempo, and meter.
- Implement the ability to use pickup notes.
- Expand choice of forms (need more variety than AABA).
- Create more user parameter support to decide form, phrase length, and tune length.
- Add features to support serialism, talea and color, etc.

Development Road Map: 
- Dec 31, 2022 - 'makeFourParts.py' -> Generates four-part music.
- Jan 31, 2023 - 'melody.py' -> Generates a melody.
- Feb 28, 2023 - 'counter.py' -> Writes a counter-melody based off of a given melody.
- March 31, 2023 - 'harmony.py -> Decides harmonies and writes individual supporting lines which form the chosen harmonies.
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
- Press cmd-R to convert the LilyPond file to MIDI. You should then see the MIDI file 'ConvertMe.midi' appear in the repository.
- Open 'ConvertMe.midi' with your notation software of choice.
- Playback the score.
- Want to generate another tune/melody? Simply repeat the 'Generating Music' steps!

Enjoy!


