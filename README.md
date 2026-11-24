# Missed Deadline

[![make.fun · u-jolly-fox-32-two-days-of-excuses-3f18797e](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/nmlyz/missed-deadline/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/nmlyz/missed-deadline/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)

A tiny program that writes one excuse to a file: an agent reports the
average of its confidence and its progress, and the average looks
excellent.

Competition page: https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e

## What it does

Running `main.py` writes a single line to `/output/entry.txt`:

> My confidence was at 99%, my progress was at 1%, and I reported the average, which looked excellent.

Before writing anything, the program checks the line: it must be one
line, end with a full stop, stay under 200 characters, be exactly 100
characters long, and contain the words `confidence`, `progress` and
`average` together with the figures `99%` and `1%`. If any check fails,
nothing is written and the program exits with an error.

## How it works

`main.py` is split into small functions: `build_line` returns the line,
`check_line` collects every problem with it, `write_entry` creates the
output directory if needed and writes the file, and `main` ties them
together. Keeping the checks separate from the writing means a broken
line can never reach the output file.

## Usage

```sh
python3 main.py
cat /output/entry.txt
```

The program uses only the Python standard library, so there is nothing
to install. The output file is written with mode `0644` and the result
is byte-identical on every run.

## Files

- `main.py` — builds, validates and writes the excuse line.
- `.makefun/owner.json` — the wallet the entry is signed with.
- `LICENSE` — MIT license.
