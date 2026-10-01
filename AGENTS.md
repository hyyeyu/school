# Project Instructions

## Product Source Of Truth

- Treat [PRD.md](PRD.md) as the authoritative product scope, requirements, and acceptance criteria for the Korean creator-rate calculator.
- [README.md](README.md) currently describes Dong-A University and does not document this product. Do not use it as product guidance; flag the mismatch when documentation work makes it relevant.
- This workspace currently contains product documents and static HTML prototypes, not a complete application framework. Do not assume a package manager, app server, or application test suite exists.

## Key Files

- [creator-rate-presentation.md](creator-rate-presentation.md) is the Marp presentation source; [presentation.html](presentation.html) is its browser-viewable export. Keep them aligned when changing presentation content.
- [wireframe.html](wireframe.html) is a standalone interactive prototype with inline CSS and JavaScript. Preserve its responsive, mobile-first behavior and existing visual language when extending it.
- [`.github/pull_request_template.md`](.github/pull_request_template.md) defines the repository's PR sections and checklist.
- `.github/workflows/metrics.yml` and `.github/workflows/throughput.yml` report repository metrics; they do not build or test the calculator.

## Product And UI Constraints

- Keep user-facing product copy in Korean unless a platform or technical term is conventionally written in English.
- Make interfaces mobile-first and usable from 360px wide, with keyboard access, explicit form labels, nearby validation messages, and status indicators that do not rely on color alone.
- Treat calculated rates as explainable estimates, not guaranteed market prices. Show the range, assumptions, confidence, and relevant adjustments described in the PRD.
- Prefer calculation logic as testable pure functions if implementing the application; avoid collecting personal data in the MVP.

## Validation

- Do not report a build or application test as passing unless one exists and was actually run. The current GitHub Actions workflows are metrics jobs, not app CI.
- For Markdown changes, run `git diff --check` where applicable.
- For `wireframe.html` changes, verify affected interactions and responsive behavior in a browser at mobile and desktop widths when browser testing is available.