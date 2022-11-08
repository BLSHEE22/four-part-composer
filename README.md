# four-part-composer

ACE™ (Algorithmic Composition Engine).

Current features:
- makeFourParts.py -> Writes a 16-bar, four-part harmonized tune.
- melody.py -> Generates a 16-bar melody from a randomly built scale.

Features in development: 
- 'counter.py' -> Writes a counter-melody to a given melody.
- 'harmony.py -> Combines the power of 'counter.py' and the original harmonization logic to create natural sounding four-part harmonies.

Setup instructions:

Prerequisites:
- Python3
- LilyPond
- Notation software that can open MIDI files (MuseScore for example)

Open terminal.

Clone this repository onto your computer.

Navigate to the repository in your terminal (cd four-part-composer).

Run makeFourParts.py by entering the command 'python3 makeFourParts.py'.

This will create a 'ConvertMe.ly' file in that same repository.

Open 'ConvertMe.ly' using LilyPond.

Press cmd-R to convert the LilyPond file to MIDI. You should see the following message as well as the MIDI file 'ConvertMe.midi' appear in the repository.

Open 'ConvertMe.midi' with your notation software of choice.

Playback the score and enjoy the algorithmic composition engine!


