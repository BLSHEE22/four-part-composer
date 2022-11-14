# four-part-composer

ACE™ (Algorithmic Composition Engine).

Current features:
- 'makeFourParts.py' -> Writes a 16-bar, four-part harmonized tune.
- 'melody.py' -> Generates a 16-bar melody from either a major, minor, chromatic, or randomly built scale.

Features in development: 
- Support for sixteenth notes.
- Random variables to control appoggiaturas, dynamics, articulations, tempo, and meter.
- 'Rhythmic Motif' feature that writes and develops rhythmic motifs.
- Expanded choice of forms (need more variety than AABA).
- 'counter.py' -> Writes a counter-melody to a given melody.
- 'harmony.py -> Combines the power of 'counter.py' and the original harmonization logic to create natural sounding four-part harmonies.

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


