"""Decision-support toolkit launcher. Runs any or all analytical tools from Day-01 to Day-30."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = json.loads(Path(__file__).with_name("toolkit_registry.json").read_text(encoding="utf-8"))


def run(entry):
    print(f'\n=== {entry["folder"]} | {entry["description"]} ===')
    subprocess.run([sys.executable, entry["script"]], cwd=ROOT / entry["folder"], check=False)


def main():
    for i, entry in enumerate(REGISTRY, 1):
        print(f'{i:>2}. {entry["folder"]:<7} {entry["script"]:<28} {entry["description"]}')
    choice = input("\nEnter a number, 'all' or 'q': ").strip().lower()
    if choice == "all":
        for entry in REGISTRY:
            run(entry)
    elif choice.isdigit() and 1 <= int(choice) <= len(REGISTRY):
        run(REGISTRY[int(choice) - 1])
    else:
        print("Nothing run.")


if __name__ == "__main__":
    main()
