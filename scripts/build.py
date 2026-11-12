"""Build the static prototype into a deployable directory."""

from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "wireframe.html"
OUTPUT = ROOT / "dist"


def main() -> None:
    if not SOURCE.is_file():
        raise FileNotFoundError(f"Required site entry point is missing: {SOURCE}")

    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)
    shutil.copy2(SOURCE, OUTPUT / "index.html")
    print(f"Built static site: {OUTPUT / 'index.html'}")


if __name__ == "__main__":
    main()
