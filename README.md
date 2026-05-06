# rookline

`rookline` packages a practical chess and game engines exercise in Python. The emphasis is on deterministic behavior, a small public API, and examples that explain the tradeoffs.

## How I Read Rookline

The useful thing to inspect here is how the same score rule is represented in code, metadata, and examples. If those three pieces disagree, the audit script should make the drift visible.

## Problem Shape

This project keeps the domain idea close to the tests. That makes it useful as a reference implementation, a small experiment, or a starting point for a more specialized tool.

## Scenario Walkthrough

`examples/extended_cases.csv` adds six named cases. I kept the names plain so failures are easy to read in a terminal: baseline, pressure, surge, degraded, recovery, and boundary.

## Internal Model

The core is a scoring model over demand, capacity, latency, risk, and weight. That keeps position state, move ranking, and turn flow in one explicit decision path. The threshold is 165, with risk penalty 5, latency penalty 4, and weight bonus 2. The Python code favors standard library tools and direct tests over framework weight.

## Main Behaviors

- Models position state with deterministic scoring and explicit review decisions.
- Uses fixture data to keep move ranking changes visible in code review.
- Includes extended examples for turn flow, including `recovery` and `degraded`.
- Documents search limits tradeoffs in `docs/operations.md`.
- Runs locally with a single verification command and no external credentials.

## How To Run It

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

This runs the language-level build or test path against the compact fixture set.

## Validation

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/audit.ps1
```

The audit command checks repository structure and README constraints before it delegates to the verifier.

## Repository Map

- `src`: primary implementation
- `tests`: verification harness
- `fixtures`: compact golden scenarios
- `examples`: expanded scenario set
- `metadata`: project constants and verification metadata
- `docs`: operations and extension notes
- `scripts`: local verification and audit commands
- `pyproject.toml`: Python project metadata

## Follow-Up Work

- Add malformed input fixtures so the failure path is as visible as the happy path.
- Split the scoring constants into a typed configuration object and validate it before use.
- Add a comparison mode that shows how decisions change when one signal is adjusted.
- Add one more chess and game engines fixture that focuses on a malformed or borderline input.

## Known Edges

The scoring model is simple by design. More domain-specific behavior should be added through explicit adapters or extra fixture classes rather than hidden constants.

## Run It Locally

Use a normal shell with Python available on `PATH`. The verifier is written as a PowerShell script because the portfolio was assembled on Windows.
