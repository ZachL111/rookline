# Rookline Walkthrough

This note is the quickest way to read the extra review model in `rookline`.

| Case | Focus | Score | Lane |
| --- | --- | ---: | --- |
| baseline | position pressure | 184 | ship |
| stress | move ordering | 220 | ship |
| edge | search width | 205 | ship |
| recovery | endgame risk | 218 | ship |
| stale | position pressure | 220 | ship |

Start with `stress` and `baseline`. They create the widest contrast in this repository's fixture set, which makes them better review anchors than the middle cases.

`stress` is the optimistic case; use it to make sure the scoring path still rewards strong signal.
