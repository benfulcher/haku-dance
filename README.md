# Haku Dance

A rhythm dance game for phones, made for Haku.
His face is on the dancer, his rabbit ムク dances along below, and each difficulty has its own original song.
All the text in the game is in Japanese.

## How it plays

- A ♥, ★, ♪ or 🥕 slides out from the middle of the dancer towards one of four circles: left hand, right hand, left foot, right foot.
- Tap that part of the screen when it lands in the circle, and the dancer's arm or leg stretches out to it.
- The steps follow the tune: high notes are hands, low notes are feet, a rising tune steps right and a falling one steps left.
- Hits score パーフェクト, グレート or グッド; a long combo starts フィーバー タイム (double points, rainbow stage, bunny ears).
- Each difficulty has its own song:

  | Mode | Song | Style | Taps |
  |---|---|---|---|
  | かんたん (easy) | ムクの ぴょんぴょん | 100 BPM, bouncy bells, C major, 1:22 | on the beat, about 1 a second |
  | ふつう (normal) | にじいろホップ | 120 BPM, K-pop, A minor, 1:56 | about 2 a second, some off-beat |
  | むずかしい (hard) | ほしぞら ダッシュ | 136 BPM, synth-pop, E minor, 1:35 | every note of the tune, plus two-handed taps |

  ふつう is the one for a 9-year-old to start on.
- Moves: up to a 5 combo each hit is a simple reach to the circle.
  From a 5 combo they turn showy, cycling through versions per limb (big swoop, loop-the-loop, windmill; high kick, knee-up kick, jump kick), with the body leaning into them and a sparkle trail.
- Special dances: at big combos (かんたん 15/35/60, ふつう 30/70/120/170, むずかしい 40/100/160/230/300) the song stops at the next bar line.
  Two bars of fanfare play while he does a routine (spin, star jumps, wave or robot, in turn) with confetti, ムク flipping beside him, and a combo bonus.
  The song then carries on from the same bar, with the next notes already on their way in during the routine's last beats.
- タイミング ちょうせい (timing fix) on the title screen shifts the timing in 10 ms steps, for Bluetooth headphones or a laggy phone.
  Raise it if he hits パーフェクト only by tapping late.
- Best scores and the timing fix are kept on the phone.

## Files

- `web/index.html`: the whole game, with the music synthesised in the browser (no audio files).
  `DANCER` and `RABBIT` near the top set the name on the T-shirt and the rabbit's name tag.
  `SONGS` holds the three songs (tempo, chords, tunes, sections), `DIFFS` the timing windows and special-dance combos, and `DANCES` the routines.
- `web/face.png`: his face, cut out of the photo by `tools/cut_face.py` (crop and outline points are specific to that photo).
- `web/manifest.webmanifest`, `web/icon-*.png`: let it be added to the home screen and open full screen.
- `.github/workflows/pages.yml`: deploys `web/` to GitHub Pages on every push to `main`.

The source photo is not in the repo (`.gitignore`), since it has other children in it.

## Playing it

Open the site in Chrome on the Android phone, then ⋮ → Add to Home screen.
To try it on the Mac: `cd web && python3 -m http.server 8931` and open http://localhost:8931.
