\header{
  title = "Computery's Masterpiece"
}

\score {
\new PianoStaff <<
\new Staff { \set Staff.midiInstrument = "violin" \clef "treble" \key f \major \tempo 4 = 82 f'4 d'4 c''4 a'8 bes'8 g''4 f''4 a''4 bes''8 c'''8 e'''4 d'''4 e'''2 bes''8 d'''8 f'''4 d'''4 c'''4 f'4 d'4 c''4 a'8 bes'8 g''4 f''4 a''4 bes''8 c'''8 e'''4 d'''4 e'''2 bes''8 d'''8 e'''4 f'''4 c''4 b'4 a'4 c'4 e'8 f'8 a'4 d'4 f'4 a'4 g'4 c'8 a8 c'8 d'8 b4 c'4 b2 c'4 f'4 d'4 c''4 a'8 bes'8 g''4 f''4 a''4 bes''8 c'''8 e'''4 g'8 c''8 g'8 g'8 e'4 f'1 }
\new Staff { \set Staff.midiInstrument = "viola" \clef "treble" \key f \major a4 e'4 e'4 e'4 bes4 bes4 f'4 c'4 c'4 bes4 c'4 c'4 f'4 d'4 bes4 bes4 a4 f'4 a4 d'4 c'4 d'4 c'4 c'4 bes4 f'4 c'4 bes4 c'4 bes4 a4 e4 d'4 b4 a4 a4 c'4 f4 c'4 f4 d'4 g4 g4 f4 g4 g4 e4 e4 a4 f'4 e'4 d'4 c'4 c'4 c'4 a4 c'4 a4 bes4 bes4 a1 }
\new Staff { \set Staff.midiInstrument = "cello" \clef "bass" \key f \major f4 g4 bes4 g4 g4 g4 bes4 f4 g4 f4 bes4 g4 g4 bes4 f4 g4 f4 bes4 f4 bes4 e4 a4 e4 f4 d4 bes4 g4 d4 g4 c'4 f4 c4 f4 d4 d4 c4 d4 d4 f4 c4 g4 d4 c4 a,4 e4 f4 bes,4 bes,4 f4 a4 bes4 f4 e4 f4 e4 f4 g4 f4 d'4 g4 f1 }
\new Staff { \set Staff.midiInstrument = "contrabass" \clef "bass" \key f\major f,4 bes,4 c4 c4 d4 c4 d4 a,4 g,4 g,4 g,4 bes,4 bes,4 bes,4 g,4 c4 f,4 bes,4 c4 bes,4 a,4 a,4 a,4 a,4 g,4 bes,4 g,4 g,4 a,4 c,4 f,4 c,4 a,4 f,4 f,4 f,4 f,4 a,4 a,4 d,4 b,4 e,4 e,4 d,4 g,4 d,4 c,4 c,4 f,4 d4 c4 g,4 a,4 a,4 a,4 c4 a,4 c4 g,4 c,4 f,1 }
>>
\midi{}
}
\version "2.22.2"