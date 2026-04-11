Original prompt: Implement option 3 with a simple 6x4 mascot linkup game.

- Added plan to implement three homepage nav states: home, slot, and linkup.
- Added a new `?view=linkup` path target via query param routing.
- Implemented a simple 6x4 mascot linkup board with classic <=2-turn connectivity rules.
- Added a post-clear research-fortune result for the linkup page.
- Preserved the fixed desktop-scale layout and the existing homepage content sections.
- Kept the masthead static to avoid greedy-nav collapsing the custom buttons.
- Pending: push changes, run Playwright against the deployed page, and fix any interaction/layout regressions found there.

- Replaced the old path-based linkup mode with a simpler memory-style pair matching board: all cards start face down, two mismatched cards flip back, and matched cards show a short connection line before clearing.
- Removed linkup hint/status/fortune text and kept only the board plus restart control.
- Added masthead scaling logic so the homepage nav shrinks with narrow viewports instead of staying oversized.
- Pending: verify the deployed linkup board by clicking through real flip/match/mismatch flows and re-check the masthead at narrow widths.

- Moved the slot/linkup choice into the homepage sidebar tool area so the main profile page now has an inline switcher instead of separate visible nav entries.
- Changed the embedded linkup board to 4 rows by 3 columns so it fits the same sidebar slot as the slot machine panel.
- Hid the masthead slot/linkup buttons for now while preserving the existing query-param view logic underneath.
