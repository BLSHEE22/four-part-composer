\version "2.22.4"
\header{
  title = "Chorale in A Major"
}

\score {
\new PianoStaff <<
\new Staff { \set Staff.midiInstrument = "violin" \clef "treble" \key a \major \tempo 4 = 56 a'4 gis'4 d'8 cis'8 e'4 b8 a8 cis'4 a'4 gis'4 b'4 cis''8 a'8 gis'4 fis'2 e''4 e''2 a'4 gis'4 d'8 cis'8 e'4 b8 a8 cis'4 a'4 gis'4 b'4 cis''8 a'8 gis'4 fis'2 gis'4 a'4 e''4 dis''4 cis''2 e''8 fis''8 e''8 dis''8 b'4 cis''4 b'4 a'4 gis'4 cis'4 e'4 fis'4 dis'4 fis'4 e'4 a'4 gis'4 d'8 cis'8 e'4 b8 a8 cis'4 a'4 gis'4 b'4 cis''8 a'8 d''8 a'8 gis'4 a'1 }
\new Staff { \set Staff.midiInstrument = "viola" \clef "treble" \key a \major cis'4 e'4 fis'4 e'4 fis'4 cis'4 d'4 e'4 a'4 fis'4 b'4 gis'4 e'4 e'4 b'4 b'4 cis'4 e'4 fis'4 fis'4 d'4 e'4 fis'4 e'4 gis'4 fis'4 d'4 a'4 a'4 d'4 cis'4 gis4 b4 cis'4 e'4 a4 fis'4 gis4 cis'4 cis'4 cis'4 e'4 b4 a4 b4 b4 b4 gis4 cis'4 b'4 d'4 cis'4 fis'4 d'4 d'4 e'4 e'4 e'4 d'4 d'4 cis'1 }
\new Staff { \set Staff.midiInstrument = "cello" \clef "bass" \key a \major a4 d'4 a4 a4 cis'4 gis4 a4 b4 d'4 d'4 d'4 d'4 b4 a4 d'4 d'4 a4 b4 a4 a4 a4 a4 d'4 b4 d'4 cis'4 fis4 cis'4 cis'4 e'4 a4 e4 fis4 gis4 gis4 e4 a4 e4 gis4 fis4 e4 a4 fis4 fis4 dis4 fis4 a4 d4 a4 d'4 a4 a4 cis'4 a4 a4 b4 gis4 a4 b4 b4 a1 }
\new Staff { \set Staff.midiInstrument = "contrabass" \clef "bass" \key a\major a,4 b,4 d4 cis4 cis4 e4 fis4 cis4 e4 d4 e4 e4 cis4 cis4 gis4 gis4 a,4 d4 d4 d4 fis4 e4 b,4 d4 e4 fis4 b,4 fis4 cis4 e,4 a,4 e,4 fis,4 e,4 gis,4 fis,4 b,4 b,4 e,4 a,4 e,4 cis4 gis,4 b,4 gis,4 a,4 dis4 e,4 a,4 fis4 b,4 e4 fis4 b,4 fis4 cis4 d4 cis4 b,4 e,4 a,1 }
>>
\layout{}
\midi{}
}
