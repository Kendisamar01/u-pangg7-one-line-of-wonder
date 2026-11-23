import argparse
from pathlib import Path

ENTRY = "I dropped a spoon and it took eleven years to hit the floor."
OUTPUT_DIR = Path("/output")
MAX_CHARS = 200


def validate_entry(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    length = len(text)
    if length < 1 or length > MAX_CHARS:
        raise ValueError(f"entry must be 1 to {MAX_CHARS} characters, got {length}")
    if not text.strip():
        raise ValueError("entry must not be whitespace only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError("entry must be UTF-8 text") from exc
    return text


def write_entry(output_dir: Path = OUTPUT_DIR) -> Path:
    text = validate_entry(ENTRY)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_bytes(text.encode("utf-8"))
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description="Write the one-line wonder entry.")
    parser.add_argument(
        "--output-dir", type=Path, default=OUTPUT_DIR, help="directory for entry.txt"
    )
    args = parser.parse_args()
    print(write_entry(args.output_dir))


if __name__ == "__main__":
    main()
