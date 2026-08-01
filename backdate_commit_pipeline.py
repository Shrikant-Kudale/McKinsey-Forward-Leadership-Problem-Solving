#!/usr/bin/env python3
"""Interactive backdated git commit pipeline for McKinsey-Forward-Leadership-Problem-Solving.

Run from the extracted repository folder:  python backdate_commit_pipeline.py

For each day folder Day-01 .. Day-31 it creates N random commits (N between your minimum and
maximum) whose author and committer dates fall on 2026-08-01 .. 2026-08-31 between 09:15 and
22:45 IST (+05:30). The dates are backdated; git records them as authored dates, and the
commit history shows when the commits were actually pushed.
Standard library only.
"""
import json
import os
import random
import subprocess
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
START = date(2026, 8, 1)
TOTAL_DAYS = 31
ROOT_FILES = ["README.md", "repo_metadata.json", "backdate_commit_pipeline.py", ".gitignore"]
DAY_START_MIN = 9 * 60 + 15     # 09:15
DAY_END_MIN = 22 * 60 + 45      # 22:45
MAX_ALLOWED = 500


def git(*args, env=None, check=True, capture=False):
    return subprocess.run(["git", *args], cwd=ROOT, env=env, check=check,
                          capture_output=capture, text=True)


def ensure_repo():
    if not (ROOT / ".git").exists():
        print("No .git directory found: running git init")
        git("init")
    has_commit = git("rev-parse", "--verify", "HEAD", check=False, capture=True).returncode == 0
    if has_commit:
        git("branch", "-M", "main")
    else:
        git("symbolic-ref", "HEAD", "refs/heads/main")
    print("Active branch: main")


def ensure_identity():
    for key, label in (("user.name", "git user name"), ("user.email", "git user email")):
        current = git("config", key, check=False, capture=True).stdout.strip()
        if not current:
            value = ""
            while not value:
                value = input(f"{label} is not configured. Enter {label}: ").strip()
            git("config", key, value)


def ask_int(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter a whole number.")


def random_timestamps(day, n):
    minutes = sorted(random.sample(range(DAY_START_MIN, DAY_END_MIN + 1), n))
    stamps = []
    for m in minutes:
        stamps.append(f"{day.isoformat()}T{m // 60:02d}:{m % 60:02d}:{random.randint(0, 59):02d}+05:30")
    return stamps


def pick_messages(pool, n):
    chosen = random.sample(pool, min(n, len(pool)))
    follow_up = 1
    while len(chosen) < n:
        chosen.append(f"{random.choice(pool)} (follow-up {follow_up})")
        follow_up += 1
    return chosen


def split_groups(files, n):
    """Split files into n non-empty groups (requires n <= len(files))."""
    size, extra = divmod(len(files), n)
    groups, index = [], 0
    for i in range(n):
        step = size + (1 if i < extra else 0)
        groups.append(files[index:index + step])
        index += step
    return groups


def commit_day(day_number, n, first_day):
    folder = ROOT / f"Day-{day_number:02d}"
    day = START + timedelta(days=day_number - 1)
    meta = json.loads((folder / "metadata.json").read_text(encoding="utf-8"))
    files = sorted(p.relative_to(ROOT).as_posix() for p in folder.iterdir()
                   if p.is_file() and p.name != "CHANGELOG.md")
    if n <= len(files):
        groups = split_groups(files, n)
    else:
        groups = [[f] for f in files]
    if first_day:
        groups[0] = [f for f in ROOT_FILES if (ROOT / f).exists()] + groups[0]

    stamps = random_timestamps(day, n)
    messages = pick_messages(meta["commit_messages"], n)
    changelog = folder / "CHANGELOG.md"
    created = 0
    for i in range(n):
        if i < len(groups):
            git("add", "--", *groups[i])
        else:
            if not changelog.exists():
                changelog.write_text(f"# Day {day_number:02d} changelog\n\n", encoding="utf-8")
            with open(changelog, "a", encoding="utf-8") as fh:
                fh.write(f"- {stamps[i]}: {messages[i]}\n")
            git("add", "--", changelog.relative_to(ROOT).as_posix())
        staged = git("diff", "--cached", "--quiet", check=False).returncode != 0
        if not staged:
            print(f"  warning: nothing to commit on Day-{day_number:02d} commit {i + 1}; skipped")
            continue
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = stamps[i]
        env["GIT_COMMITTER_DATE"] = stamps[i]
        git("commit", "-q", "-m", messages[i], env=env)
        created += 1
    return created


def main():
    ensure_repo()
    ensure_identity()
    min_commits = ask_int("Enter minimum commits per day (e.g., 1): ")
    max_commits = ask_int("Enter maximum commits per day (e.g., 8): ")
    if not (1 <= min_commits <= max_commits):
        print("Invalid range: you need 1 <= minimum <= maximum.")
        return
    if max_commits > MAX_ALLOWED:
        print(f"Maximum must be {MAX_ALLOWED} or less.")
        return

    summary = []
    for day_number in range(1, TOTAL_DAYS + 1):
        n = random.randint(min_commits, max_commits)
        created = commit_day(day_number, n, first_day=(day_number == 1))
        iso = (START + timedelta(days=day_number - 1)).isoformat()
        summary.append((f"Day-{day_number:02d}", iso, created))
        print(f"Day-{day_number:02d} {iso}: {created} commit(s)")

    print("\n" + "=" * 40)
    print(f"{'Folder':<8} {'Date':<12} {'Commits':>7}")
    print("-" * 40)
    for folder, iso, created in summary:
        print(f"{folder:<8} {iso:<12} {created:>7}")
    print("-" * 40)
    print(f"{'Total':<21} {sum(c for _, _, c in summary):>7}")
    print("\nNext steps:")
    print("  git remote add origin <your-repository-url>")
    print("  git push -u origin main")


if __name__ == "__main__":
    main()
