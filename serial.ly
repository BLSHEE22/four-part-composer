\header { title = "P-0, P-1, P-0"}\score { \new Staff { \set Staff.midiInstrument = "violin" \clef "treble" \key c \major \time 4/4 \tempo Allegro 4 = 128b'16\ppp c'8.~ c'4~ c'16\< ees'16\staccatissimo  e'8\accent  fis'4~ fis'2. a'8.\marcato  d'16~\> d'8 cis'16\accent \pp r16 f'8^\markup flautando  g'8 aes'4~\mp aes'8\< bes'8\mf \fermata \set Score.repeatCommands = #'(end-repeat)c'8.\f cis'16~ cis'8 e'8~\tenuto \ff e'2~\tenuto \> e'8\tenuto  f'8~\glissando  f'16 g'8.\< bes'2~\> bes'4 ees'4^\markup non-vib.  d'8\p r8 fis'4~ fis'2 aes'4~\ff aes'8\< a'8~ a'2~\> a'8 b'8~^\markup vib.  b'4\f \fermata \bar "||"b'16\ppp c'8.~ c'4~ c'16 ees'16\< e'8 fis'4~\marcato  fis'2. a'8.^\markup "sul tasto"  d'16~\> d'8 cis'16\pp r16 f'8\ff g'8 aes'4~ aes'8 bes'8\mf \fermata \bar "|."}
}\version "2.22.2"