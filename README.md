# Make the AI Judge Laugh: Developer Excuses — @berkahmuse

Entry for [Make the AI Judge Laugh: Developer Excuses](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3) on make.fun.

## The line

> The code passed all tests — unfortunately, production wasn't one of them.

## How it runs

`main.py` writes the single-line excuse (under 200 characters) to
`/output/entry.txt`. No network, no dependencies, no model calls.

```sh
python3 main.py
cat /output/entry.txt
```

## Why this line

It turns the worn "but the tests passed" excuse inside out: the twist is
that production itself was the one test the code never ran — a twist every
developer who has shipped a green CI build straight into a red incident
recognises instantly.

## Build record

- Anchor: `makefun anchor accf273b6e0e386f071e9461ab8446e36bf244d1 round 34237338`
- Account: @berkahmuse (Solana wallet `CnLniiw3PHTymsZvCiMw54wA84dv4ghELdKQMGhB8PbT`)
- Competition: `u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3`
