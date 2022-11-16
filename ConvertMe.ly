\header{
  title = "Computery's Masterpiece"
}

\score {
\new PianoStaff <<
\time 5/4
\tempo 4 = 142
\new Staff { \set Staff.midiInstrument = "violin" \clef "treble" \key a \major a'2 ais'4 a'4 ais'2 cis''4 d''4 e''4 b'4 d''2 b'4 gis'2 b'4 c''4 d''2 cis'''2 c'''4 cis'''4 dis'''2 e'''4 g'''4 a'''4 ais'''8 c''''4 cis''''2 e''''8 a'2 ais'4 a'4 ais'2 cis''4 d''4 e''4 b'4 d''2 b'4 gis'2 b'4 c''4 d''2 cis'''2 c'''4 cis'''4 dis'''2 e'''4 g'''4 a'''4 ais'''8 c''''4 cis''''2 e''''8 a'8 b'2 b'2 c''2 cis''4 dis''2 fis''2 a''8 c'''8 a''2 cis''8 dis''8 a'8 a'2 ais'4 a'4 ais'2 cis''4 d''4 e''4 b'4 d''2 b'4 gis'2 b'4 c''4 d''2 cis'''2 c'''4 cis'''4 dis'''2 e'''4 g'''4 a'''4 ais'''8 c''''4 cis''''2 e''''8 a'1 }
\new Staff { \set Staff.midiInstrument = "viola" \clef "treble" \key a \major r2 r2 r2 r2 r2 r2 r2 r2 r2 e'2 f'4 e'4 f'2 gis'4 a'4 b'4 fis'4 a'2 fis'4 dis'2 fis'4 g'4 a'2 gis''2 g''4 gis''4 ais''2 b''4 d'''4 e'''4 f'''8 g'''4 gis'''2 b'''8 e'8 fis'2 fis'2 g'2 gis'4 ais'2 cis''2 e''8 g''8 e''2 gis'8 ais'8 e'8 e'2 f'4 e'4 f'2 gis'4 a'4 b'4 fis'4 a'2 fis'4 dis'2 fis'4 g'4 a'2 gis''2 g''4 gis''4 ais''2 b''4 d'''4 e'''4 f'''8 g'''4 gis'''2 b'''8 e'1 }
\new Staff { \set Staff.midiInstrument = "cello" \clef "bass" \key a \major r2 r2 r2 r2 r2 r2 r2 r2 r2 r2 r2 r2 r2 r2 r2 r2 b2 c'4 b4 c'2 dis'4 e'4 fis'4 cis'4 e'2 cis'4 ais2 cis'4 d'4 e'2 dis''2 d''4 dis''4 f''2 fis''4 a''4 b''4 c'''8 d'''4 dis'''2 fis'''8 b8 cis'2 cis'2 d'2 dis'4 f'2 gis'2 b'8 d''8 b'2 dis'8 f'8 b8 b2 c'4 b4 c'2 dis'4 e'4 fis'4 cis'4 e'2 cis'4 ais2 cis'4 d'4 e'2 dis''2 d''4 dis''4 f''2 fis''4 a''4 b''4 c'''8 d'''4 dis'''2 fis'''8 b1 }
\new Staff { \set Staff.midiInstrument = "contrabass" \clef "bass" \key a\major r2 r2 r2 r2 r2 r2 r2 r2 r2 r2 r2 r2 r2 r2 r2 r2 r2 r2 r2 r2 r2 a,2 ais,4 a,4 ais,2 cis4 d4 e4 b,4 d2 b,4 gis,2 b,4 c4 d2 cis'2 c'4 cis'4 dis'2 e'4 g'4 a'4 ais'8 c''4 cis''2 e''8 a,8 b,2 b,2 c2 cis4 dis2 fis2 a8 c'8 a2 cis8 dis8 a,8 a,2 ais,4 a,4 ais,2 cis4 d4 e4 b,4 d2 b,4 gis,2 b,4 c4 d2 cis'2 c'4 cis'4 dis'2 e'4 g'4 a'4 ais'8 c''4 cis''2 e''8 a,1 }
>>
\midi{}
}
\version "2.22.2"