# whispercpp-benchmark

Benchmark [pywhispercpp](https://github.com/absadiki/pywhispercpp) inference speed on an audio file.

Reports per-run time and summary stats (mean, min, max, stdev).

## Usage

```sh
uv sync
uv run main.py audio.mp3 --model small --runs 3
uv run main.py --model=medium # use audio.mp3 in the main.py directory

# usage
uv run main.py [audio] [--model MODEL] [--runs N]
# - `audio` — path to an audio file (mp3, wav, m4a, flac, ogg, opus). 
#             Defaults to the first audio file found in the script directory.
# - `--model` — Whisper model name (default: `base`). See available models below.
# - `--runs` — number of timed runs (default: `5`).
```

## Models

- tiny:       `tiny`, `tiny-q5_1`, `tiny-q8_0`, `tiny.en`, `tiny.en-q5_1`, `tiny.en-q8_0`
- base:       `base`, `base-q5_1`, `base-q8_0`, `base.en`, `base.en-q5_1`, `base.en-q8_0`
- small:      `small`, `small-q5_1`, `small-q8_0`, `small.en`, `small.en-q5_1`, `small.en-q8_0`
- medium:     `medium`, `medium-q5_0`, `medium-q8_0`, `medium.en`, `medium.en-q5_0`, `medium.en-q8_0`
- large-v1:   `large-v1`
- large-v2:   `large-v2`, `large-v2-q5_0`, `large-v2-q8_0`
- large-v3:   `large-v3`, `large-v3-q5_0`, `large-v3-turbo`, `large-v3-turbo-q5_0`, `large-v3-turbo-q8_0`



## Results
```
MBA M2 ram=8G  model=medium         -> 5.651s, 4.622s, 5.059s, 4.606s
MBA M2 ram=8G  model=large-v2-q5_0  -> 8.625s, 8.513s
MBA M2 ram=8G  model=large-v2-q8_0  -> 8.700s, 8.588s
MBA M2 ram=8G  model=large-v3-turbo -> 4.654s
MBA M2 ram=8G  model=large-v3       -> 9.483s, 9.436s
MBA M2 ram=8G  model=large-v3-q5_0  -> 8.778s, 8.700s

MBA M5 ram=16G model=medium         -> 3.322s, 3.223s
MBA M5 ram=16G model=large-v2-q8_0  -> 5.467s, 5.363s
```
