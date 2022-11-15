# four-part-composer

ACE™ (Algorithmic Composition Engine).

Current supported features:
- 'makeFourParts.py' -> Writes a 16-bar, four-part harmonized tune.
- 'melody.py' -> Generates a melody (AABA, 16 measure default) from either a major, minor, chromatic, or randomly built scale.

'makeFourParts.py' TODO:
- Implement sixteenth notes.
- Increase rhythmic vocabulary of supporting lines. 
- Implement ability to create 'rhythm profile' and have the parts stick to it.
- Implement ability for all four lines to communicate in 'keeping the quaver.'

'melody.py' TODO: 
- Implement sixteenth notes.
- Implement smarter rests that punctuate phrases and are not just random.
- Add 'rhythmic motif' feature that writes and employs rhythmic motifs.
- Create more random variables to control dynamics, articulations, ornaments, tempo, and meter.
- Implement the ability to use pickup notes.
- Expand choice of forms (need more variety than AABA).
- Create more user parameter support to decide form, phrase length, and tune length.

Development Road Map: 
- Dec 31, 2022 - 'makeFourParts.py' (being deprecated) -> Generates four-part music.
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


