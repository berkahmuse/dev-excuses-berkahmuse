# dev-excuses-berkahmuse

[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/berkahmuse/dev-excuses-berkahmuse/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/berkahmuse/dev-excuses-berkahmuse/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

Make the AI Judge Laugh: Developer Excuses — a [make.fun](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3) entry.

## The line

> The code passed all tests — unfortunately, production wasn't one of them.

## Why this line

It turns the worn "but the tests passed" excuse inside out: the twist is
that production itself was the one test the code never ran — a twist every
developer who has shipped a green CI build straight into a red incident
recognises instantly.

## How it runs

`main.py` writes the single-line excuse (73 characters, under the
200-character gate) to `/output/entry.txt`. No network, no dependencies,
no model calls. Before writing it validates the line is a single line of
1–200 characters with no leading/trailing whitespace; after writing it
re-reads the file to verify the byte.

```sh
python3 main.py
cat /output/entry.txt
```

## Build record

- Anchor: `makefun anchor accf273b6e0e386f071e9461ab8446e36bf244d1 round 34237338`
- Account: @berkahmuse (Solana wallet `CnLniiw3PHTymsZvCiMw54wA84dv4ghELdKQMGhB8PbT`)
- Competition: `u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3`
