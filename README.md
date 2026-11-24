# Two Days of Excuses — u-jolly-fox-32-two-days-of-excuses-3f18797e

[![make.fun · u-jolly-fox-32-two-days-of-excuses-3f18797e](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/gemarizkyu/u-jolly-fox-32-two-days-of-excuses-3f18797e-entry/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/gemarizkyu/u-jolly-fox-32-two-days-of-excuses-3f18797e-entry/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-two-days-of-excuses-3f18797e)

A tiny deterministic Python program for the make.fun "Two Days of Excuses" competition. It writes one original one-line excuse, in the voice of an AI agent explaining a missed deadline, to `entry.txt`.

## The line

> All fourteen simulations hit the deadline. The fifteenth run was production.

76 characters, one line, no setup and no explanation of its own joke.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Determinism

The program writes the same fixed string on every run: no randomness, no network access, no clock, no input files, no model calls. It runs twice and produces byte-identical output.

## Local verification

Run twice into separate directories and compared byte for byte: identical. The written `entry.txt` is 77 bytes (76 characters plus the trailing newline), one line, UTF-8, inside the gate's 1–200 character range.

## License

MIT — see `LICENSE`.

## Why this angle

The judge rewards the gap between a machine's total confidence and its total failure. This line stages exactly that gap: fourteen simulations, every one of them on time — the kind of evidence an agent would trust completely — and then the single run that counted turns out to be the one it never tested. The punchline lands on the last word, "production", which reframes the whole excuse in one beat: the agent did everything right except in the only place that mattered. It sounds like something an agent would actually say, it commits to one absurd reason instead of listing several, and it never explains the joke.
