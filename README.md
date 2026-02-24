# four-part-composer

a.k.a the 'ACE' (Algorithmic Composition Engine).

Run:
`python3 ace.py`

Currently supported modes:
- **SOLO** -> Writes an AABA solo using the scale of your choice.
- **CHORALE** -> Writes a four-part AABA tune in a random major key.
- **REICH** -> Writes a two-part phasing piece.
- **FUGUE** -> Writes a four-part fugue.
- **SERIALISM** -> Writes a serialist piece.
<br>

'serial.py' TODO: 
- Add support for minor chorale keys
- Offer more harmonic progression options for chorales
- Re-work fugue mode
- Implement harmonics
- Implement function to keep the contour the same for the b section (interval check)
- Implement pickup notes
- Implement 'passacaglia' feature
- Implement 'raga' feature (bass drone, long meter, etc.)
- Implement 'mirror' melody feature (build from both ends!)
- Implement feature which supports talea and color

Development Road Map for 'Fugue' Feature: 
- 'bassline.py' -> Writes a bassline which harmonizes a given melody
- 'harmony.py -> Decides vertical harmonies to correspond with a given melody and bassline
- 'voiceLead.py' -> Creates solid voice leading for four-part harmony
- 'form.py' -> Handles the writing and usage of main themes, motifs, and the tonal road map.
- 'fugue.py' -> Combines all of the above scripts into the ultimate fugue composition script.

Prerequisites:
- Python3
- LilyPond (http://lilypond.org/download.html)
- Notation software that can open MIDI files (MuseScore for example)

Setup Instructions:
- Open terminal.
- Clone this repository onto your computer.
- Navigate to the repository in your terminal (cd four-part-composer).

Generating Music:
- Type 'python3 ace.py' in the terminal and press Enter.
- Follow the instructions in the program to generate your score.

Enjoy!
