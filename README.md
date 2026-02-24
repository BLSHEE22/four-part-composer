# four-part-composer

a.k.a the 'ACE' (Algorithmic Composition Engine).

Currently supported modes:
- **SOLO** -> Writes an AABA solo using the scale of your choice.
- **CHORALE** -> Writes a four-part AABA tune in a random major key.
  - TODO: Add support for minor keys!
- **REICH** -> Writes a two-part phasing piece.
- **FUGUE** -> Writes a four-part fugue.
  - TODO: Re-work restatement logic
- **SERIALISM** -> Writes a serialist piece.

'serial.py' TODO: 
- REFACTOR CODE!!!!!!!!!!
- Boost slurs and observe stability.
- Decide whether or not to TieUp every staccato note that's longer than a quarter.
- Implement harmonics
- Implement function to keep the contour the same for the b section (interval check)
- Implement function that intersperses rests in a tone row (same count that are in prime)
- Implement set-matrix function
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
- Run `python3 ace.py`.
- Follow the instructions in the program to generate your score.

Enjoy!
