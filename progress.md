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

- Restored the desktop linkup rendering path to the last known working implementation from `d3713e0`: card faces and shuffle track are back to direct `<img>` rendering instead of the later background-window wrappers.
- Kept only the user-confirmed non-breaking tweaks on top of that restore, specifically the yellow selected-state highlight and the tighter board gap.
- Verified SCSS compilation with `npx sass`; local Jekyll preview is blocked on this machine because Ruby/Bundler are not installed, so final verification must be done against the deployed GitHub Pages build.

- Adjusted the mobile home game panel again: widened the left control column, narrowed the right core area, increased shell side padding, increased slot lever size, and increased the vertical spacing between the three slot rows.
- Removed the mobile-only yellow inner frame from both face-up linkup cards and shuffle animation cells; mobile linkup art now fills the outer card window directly with `object-fit: cover`.
- Tightened the mobile shell width by shifting more width back to the profile column, while keeping slot and linkup shell heights equal.
- Adjusted large-screen desktop shells so slot and linkup now share the same fixed outer height; the slot control strip is anchored to the bottom with extra top spacing instead of relying on a near-threshold auto height.
- Verification in Playwright against the live site with injected CSS: desktop slot/linkup shell heights matched exactly (`329.21px` each, no overflow), and mobile linkup shuffle/front pseudo-frame display was `none` with shell size `204.38px x 201.30px`.
