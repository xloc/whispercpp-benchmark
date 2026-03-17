import argparse
import statistics
import timeit
from pathlib import Path

from mutagen import File
from pywhispercpp.constants import AVAILABLE_MODELS
from pywhispercpp.model import Model


def get_audio_duration(path: str) -> float:
    return File(path).info.length


def models_epilog() -> str:
    order = ['tiny', 'base', 'small', 'medium', 'large-v1', 'large-v2', 'large-v3']
    group = {k: [m for m in AVAILABLE_MODELS if m.startswith(k)] for k in order}
    misc = set(AVAILABLE_MODELS) - {m for ms in group.values() for m in ms}
    if misc:
        group['misc'] = sorted(misc)
    lines = [f'  {k + ":":<18}{", ".join(v)}' for k, v in group.items() if v]
    return f'models:\n{"\n".join(lines)}'


def find_default_audio() -> str | None:
    for p in sorted(Path(__file__).parent.iterdir()):
        if p.suffix.lower() in {'.mp3', '.wav', '.m4a', '.flac', '.ogg', '.opus'}:
            return str(p)
    return None


def main():
    parser = argparse.ArgumentParser(
        description="Benchmark pywhispercpp inference speed",
        epilog=models_epilog(),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("audio", nargs="?", help="Path to an audio file (default: first audio file in script directory)")
    parser.add_argument("--model", default="base", metavar="MODEL", choices=AVAILABLE_MODELS, help="Whisper model name (default: base)")
    parser.add_argument("--runs", type=int, default=5, help="Number of timed runs (default: 5)")
    args = parser.parse_args()

    audio = args.audio or find_default_audio()
    if audio is None:
        parser.error("no audio file provided and none found in script directory")

    duration = get_audio_duration(audio)
    print(f"Model:          {args.model}")
    print(f"Audio duration: {duration:.1f}s")
    print(f"Runs:           {args.runs}")
    print("Loading model...")

    model = Model(args.model, print_progress=False)

    print("Benchmarking...")
    times = []
    for i in range(args.runs):
        t = timeit.timeit(lambda: model.transcribe(audio), number=1)
        times.append(t)
        print(f"  Run {i + 1}: {t:.3f}s")

    mean = statistics.mean(times)
    print(f"\n{'Mean:':<8} {mean:.3f}s")
    print(f"{'Min:':<8} {min(times):.3f}s")
    print(f"{'Max:':<8} {max(times):.3f}s")
    if args.runs > 1:
        print(f"{'Stdev:':<8} {statistics.stdev(times):.3f}s")


if __name__ == "__main__":
    main()
