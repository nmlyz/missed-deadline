# missed-deadline

[![make.fun · u-jolly-fox-32-two-days-of-excuses-3f18797e](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/nmlyz/missed-deadline/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/nmlyz/missed-deadline/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)

One program, one line, one file. The line is an agent's report on its
own deadline: confidence high, progress low, average excellent.

The competition: https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e

## The line

> My confidence was at 99%, my progress was at 1%, and I reported the average, which looked excellent.

## Running it

```sh
python3 main.py
cat /output/entry.txt
```

No third-party packages: the standard library is all it needs. Every
run writes the same bytes, and the file comes out readable (`0644`).

## What gets checked

`main.py` refuses to write a line that fails any of these:

- a single line, no line break inside it, no loose whitespace at an end
- exactly 100 characters, under the 200-character limit
- one sentence, ending with a full stop
- carries `confidence`, `progress`, `average`, `99%` and `1%`

A failed check prints each fault to stderr, writes nothing, and exits
with status 1, so a broken line can never land in the output file.

## Layout

- `main.py` — the line, its checks, the write, and the entry point.
- `.makefun/owner.json` — the wallet the entry is signed with.
- `LICENSE` — MIT license, SPDX identifier in the file itself.
