\header{
  title = "Computery's Masterpiece"
}

\score {
\new PianoStaff <<
\new Staff { \set Staff.midiInstrument = "violin" \clef "treble" \key c \major \tempo 4 = 63 c'4 a2 g4 f'2 d'4 e'2 d'4 c'8 d'8 e'4 d'4 f'4 g'2 c'4 a2 g4 f'2 d'4 e'2 d'4 c'8 d'8 e'4 d'4 b4 c'4 g'4 a'4 b'4 e'4 fis'2 a2 c'2 a4 g4 fis4 g4 c'4 d'4 g'4 c'4 a2 g4 f'2 d'4 e'2 d'4 c'8 b8 b4 c'1 }
\new Staff { \set Staff.midiInstrument = "viola" \clef "treble" \key c \major e4 c'4 c'4 g4 a4 a4 f4 e4 f4 f4 g4 a4 g4 a4 b4 d'4 e4 a4 b4 c'4 a4 a4 b4 e4 c'4 b4 g4 g4 f4 f4 e4 b,4 c4 b,4 fis4 a4 d4 c4 fis4 a4 g4 e4 e4 d4 d4 fis4 fis4 b,4 e4 c'4 g4 e4 c'4 a4 g4 f4 f4 a4 a4 f4 e1 }
\new Staff { \set Staff.midiInstrument = "cello" \clef "bass" \key c \major c4 e4 e4 c4 d4 d4 c4 b,4 c4 c4 b,4 c4 b,4 d4 f4 f4 c4 e4 f4 e4 c4 c4 f4 b,4 a4 f4 c4 c4 c4 g4 c4 g,4 g,4 fis,4 a,4 c4 a,4 a,4 c4 d4 c4 a,4 c4 c4 g,4 a,4 c4 f,4 c4 f4 d4 c4 f4 d4 b,4 c4 c4 d4 d4 d4 c1 }
\new Staff { \set Staff.midiInstrument = "contrabass" \clef "bass" \key c\major c,4 a,4 e,4 e,4 d,4 d,4 d,4 g,4 d,4 d,4 e,4 f,4 e,4 a,4 g,4 b,4 c,4 c,4 g,4 a,4 f,4 f,4 g,4 g,4 a,4 g,4 e,4 g,4 d,4 g,,4 c,4 g,,4 a,,4 d,4 c,4 e,4 b,,4 e,4 d,4 fis,4 e,4 c,4 c,4 a,,4 b,,4 d,4 d,4 g,,4 c,4 f,4 e,4 g,4 a,4 d,4 f,4 d,4 d,4 f,4 f,4 g,,4 c,1 }
>>
\midi{}
}
\version "2.22.2"