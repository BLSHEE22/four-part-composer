\header{
  title = "Computery's Masterpiece"
}

\score {
\new PianoStaff <<
\new Staff { \set Staff.midiInstrument = "violin" \clef "treble" \key ees \major ees'4 f'4 aes'4 c''4 d''4 c''4 d''2 c''4 d''8 c''8 bes'4 g'4 aes'8 g'8 ees'4 c'4 bes4 ees'4 f'4 aes'4 c''4 d''4 c''4 d''2 c''4 d''8 c''8 bes'4 g'4 aes'8 g'8 d'4 ees'4 bes'4 c''4 d''8 f''8 d''4 ees''4 c''4 a'2 f'4 a'8 g'8 a'4 bes'4 c''2 d''8 ees''8 bes'2 ees'4 f'4 aes'4 c''4 d''4 c''4 d''2 c''4 d''8 d'8 ees'4 d'4 ees'1 }
\new Staff { \set Staff.midiInstrument = "viola" \clef "treble" \key ees \major g4 d'4 c'4 bes2 bes4 ees'4 bes2 f'4 d'4 ees'4 bes4 c'4 aes2 g4 aes4 f'4 ees'4 bes4 f'2 f'4 ees'4 aes4 ees'4 c'2 aes4 g4 d'4 f'2 g'4 bes'2 bes'4 ees'2 g'4 f'2 g'4 a'2 f'4 d'4 g4 c'2 ees'4 b4 aes4 ees'4 bes4 aes4 c'4 aes2 g1 }
\new Staff { \set Staff.midiInstrument = "cello" \clef "bass" \key ees \major ees4 aes4 ees4 f2 f4 aes4 f2 bes4 f4 aes4 g4 aes4 ees4 f4 ees2 bes4 g4 f4 aes2 bes4 f4 ees4 aes2 aes4 bes4 ees4 bes4 a4 bes2 ees'2 ees'4 g4 bes4 d'4 c'4 bes4 c'4 ees'4 c'4 d'4 aes4 ees4 aes4 f2 f2 aes2 f2 c'4 f4 ees1 }
\new Staff { \set Staff.midiInstrument = "contrabass" \clef "bass" \key ees\major ees,4 bes,4 aes,4 g,4 aes,4 g,4 c4 f,4 g,4 d4 bes,4 c4 d4 f,2 bes,4 ees,4 f,4 d4 g,4 aes,4 d4 bes,2 aes,4 f,4 c4 aes,2 bes,,4 ees,4 bes,4 d2 ees4 g4 f4 g4 c2 bes,4 c4 d4 ees4 f2 f4 bes,4 ees,4 f,2 aes,2 f,4 c4 f,2 aes,4 f,4 bes,,4 ees,1 }
>>
\midi{}
}
\version "2.22.2"