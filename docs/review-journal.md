# Review Journal

The review surface for `rookline` is deliberately narrow: one fixture, one scoring rule, and one local check.

The local checks classify each case as `ship`, `watch`, or `hold`. That gives the project a small review vocabulary that matches its chess and game engines focus without claiming live deployment or external usage.

## Cases

- `baseline`: `position pressure`, score 184, lane `ship`
- `stress`: `move ordering`, score 220, lane `ship`
- `edge`: `search width`, score 205, lane `ship`
- `recovery`: `endgame risk`, score 218, lane `ship`
- `stale`: `position pressure`, score 220, lane `ship`

## Note

The repository should be understandable without pretending it is larger than it is.
