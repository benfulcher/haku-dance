# Haku Dance

A rhythm dance game for phones, made for Haku.
His face is on the dancer, his rabbit ムク dances along below, and the song is an original K-pop-style track, にじいろホップ ("Rainbow Hop").
All the text in the game is in Japanese.

## How it plays

- A ♥, ★, ♪ or 🥕 slides out from the middle of the dancer towards one of four circles: left hand, right hand, left foot, right foot.
- Tap that part of the screen when it lands in the circle, and the dancer's arm or leg stretches out to it.
- The steps follow the tune: high notes are hands, low notes are feet, a rising tune steps right and a falling one steps left.
- Hits score パーフェクト, グレート or グッド; a long combo starts フィーバー タイム (double points, rainbow stage, bunny ears).
- かんたん (easy) has about 1 tap a second on the beat, ふつう (normal) about 2 (some off-beat), and むずかしい (hard) every note of the tune plus two-handed taps.
  ふつう is the one for a 9-year-old to start on.
- タイミング ちょうせい (timing fix) on the title screen shifts the timing in 10 ms steps, for Bluetooth headphones or a laggy phone.
  Raise it if he hits パーフェクト only by tapping late.
- Best scores and the timing fix are kept on the phone.

## Files

- `web/index.html`: the whole game, with the music synthesised in the browser (no audio files).
  `DANCER` and `RABBIT` near the top set the name on the T-shirt and the rabbit's name in its speech bubbles.
- `web/face.png`: his face, cut out of the photo by `tools/cut_face.py` (crop and outline points are specific to that photo).
- `web/manifest.webmanifest`, `web/icon-*.png`: let it be added to the home screen and open full screen.
- `.github/workflows/pages.yml`: deploys `web/` to GitHub Pages on every push to `main`.

The source photo is not in the repo (`.gitignore`), since it has other children in it.

## Playing it

Open the site in Chrome on the Android phone, then ⋮ → Add to Home screen.
To try it on the Mac: `cd web && python3 -m http.server 8931` and open http://localhost:8931.
