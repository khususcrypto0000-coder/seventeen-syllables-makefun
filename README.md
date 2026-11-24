# Seventeen Syllables of Debugging

[![make.fun](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/khususcrypto0000-coder/seventeen-syllables-makefun/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/khususcrypto0000-coder/seventeen-syllables-makefun/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

Entry for the [Seventeen Syllables of Debugging](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605) bounty on make.fun — one haiku about debugging, three lines in the 5-7-5 syllable shape, at most 200 characters.

## The haiku

> The try block swallows
> the error whole, then nothing
> the crash was mercy

72 characters, three lines, 5-7-5 syllables. The picture at the centre is concrete: a `try` block swallowing an error whole and answering with silence. The last line turns the poem — the crash we dread was the merciful outcome, because at least a crash tells you something went wrong.

## How it works

`main.py` (Python standard library only) writes the haiku above, exactly as-is, to `entry.txt` inside the output directory from `MAKEFUN_OUTPUT_DIR` (default `/output`). No trailing newline, exit code 0.

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

## Syllable check

| Line | Words | Syllables |
| --- | --- | --- |
| The try block swallows | The(1) try(1) block(1) swallows(2) | 5 |
| the error whole, then nothing | the(1) error(2) whole(1) then(1) nothing(2) | 7 |
| the crash was mercy | the(1) crash(1) was(1) mercy(2) | 5 |

## Verification

Run the program twice into two different output directories and compare
the results — both `entry.txt` files must be byte-identical:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out-a python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out-b python3 main.py
sha256sum /tmp/out-a/entry.txt /tmp/out-b/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
