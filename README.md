# four-part-composer

ACE™ (Algorithmic Composition Engine).

Current features:
- 'makeFourParts.py' -> Writes a 16-bar, four-part harmonized tune.
- 'melody.py' -> Generates a 16-bar melody from a randomly built scale.

Features in development: 
- Random settings of home register, dynamics, tempo, and meter
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
- Run the script of your choice by entering the command 'python3 <filename>'.
- This will create a 'ConvertMe.ly' file in that same repository.
- Open 'ConvertMe.ly' using LilyPond.
- Press cmd-R to convert the LilyPond file to MIDI. You should then see the MIDI file 'ConvertMe.midi' appear in the repository.
- Open 'ConvertMe.midi' with your notation software of choice.
- Playback the score.
- Want to generate another tune/melody? Simply repeat the 'Generating Music' steps!

Enjoy!


