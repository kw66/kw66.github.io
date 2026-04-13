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

- Reworked the mobile featured-project carousel logic to stop cloning cards for looping. The new logic keeps a constant item count and rotates the real DOM items as a circular queue while the viewport scrolls.
- The mobile featured carousel now keeps autoplay alive after manual dragging: interaction only pauses autoplay temporarily, and the queue resumes by itself after the pause window.
- Tightened vertical spacing around the mobile mascot strip and the project/paper boundary, increased the mobile project gap slightly, and made the paper-filter right arrow larger and more visible.
- Verification: `_pages/about.md` inline script still parses successfully; a Playwright minimal carousel repro confirmed manual forward drag keeps the count at `3` and autoplay resumes afterwards; live-page CSS injection confirmed the mobile project gap is now non-zero (`4.2px` after fixed-scale transform), the paper-filter arrow is larger, and the mascot strip / filter spacing reductions took effect.

- Increased the desktop-only game shell stage height again because the slot/linkup bottom control row was sitting too close to the shell edge. The large-breakpoint shell height token moved from `22.72rem` to `23.12rem`.
- Verification in Playwright against the live site with injected CSS: both desktop shells remained equal in height (`335.01px` each) and the bottom inset under the control row increased to about `6.17px`.

- Tightened the mobile game panel again: the control column is wider, the control-to-core gap is smaller, the mobile shell height is reduced, and the slot/linkup inline button font is slightly smaller.
- Increased the mobile featured-project gap again so adjacent project cards no longer read as touching.
- Compacting the mobile shell also required a slightly tighter mobile linkup grid gap so the linkup shell does not grow taller than the slot shell.
- Verification in Playwright against the live site with injected CSS using the chosen candidate: mobile featured gap reached about `6.30px`; mobile control width increased to about `39.30px`; control-to-core gap dropped to about `30.59px`; slot shell height dropped to about `195.59px`; linkup shell height stayed near `195.73px`; inline button font reduced to about `13.8px`.

- Follow-up mobile game alignment pass: the real issue in the screenshot was that the slot reels and linkup board were still right-aligned inside the core column, leaving a wide blank seam between the control column and the game area.
- Fixed by left-aligning the mobile reel/board wrapper inside column 2 and restoring only a tiny explicit column gap (`0.08rem`) instead of letting the core content float to the far right.
- Verification in Playwright against the live site with injected CSS: mobile control-to-core gap dropped again from about `30.59px` to about `1.19px`, while shell height stayed around `195.6px`.

- The next screenshot revealed the remaining problem: once the core area was left-aligned, the shell itself was still too wide, so the blank area simply moved to the shell's right side.
- Fixed by narrowing the mobile game column at the sidebar layout level, changing the mobile sidebar split from `0.86fr / 1.14fr` to `0.98fr / 1.02fr` and trimming the inter-column gap slightly.
- Verification in Playwright against the live site with injected CSS: the mobile shell width dropped from about `204.38px` to about `183.33px`, while the right inset next to the core area dropped to about `12.05px`.

- Another alignment pass was needed after the narrower shell: the user wanted the three control blocks spaced farther apart, the control column bottom aligned with the linkup board bottom, and a slightly taller shell so the bottom edge did not feel cramped.
- Fixed by raising the mobile shell stage height back up to `13.42rem`, increasing the mobile slot row height to `3.34rem`, increasing the reel-to-reel vertical gap to `0.44rem`, and raising the mobile control stack minimum height to `3 * row + 1.46rem`; the shell bottom padding also increased to `0.24rem`.
- Verification in Playwright against the live site with injected CSS: mobile shell height became about `201.30px`; control bottom inset became about `8.92px`; linkup board bottom inset became about `9.25px`; and the control-vs-board bottom delta tightened to about `0.33px`.

- Final mobile centering pass: after narrowing the shell, the core area was still slightly too left-heavy. Switching the reel and linkup board wrapper from `start` to `center` alignment gave a better visual balance inside the narrower shell.
- Verification in Playwright against the live site with injected CSS: mobile control-to-core gap became about `5.36px` and the core-to-right inset became about `7.88px`, which is much closer to symmetric than the previous `1.19px / 12.05px`.

- Desktop/mobile cleanup pass for the latest homepage request:
  - Removed the featured-project `<` / `>` buttons from `_pages/about.md`, kept the desktop carousel at `2.5` visible items, and added real mouse drag support on top of the existing infinite autoplay/manual-scroll loop so desktop now matches the mobile interaction model more closely.
  - Kept the fixed-scale home masthead hidden, and relied on the already-added homepage author markup so the desktop profile column now shows the bio plus inline Github / visitor stats instead of only the name/avatar block.
  - Recentered the mobile game shells by centering the whole `control column + core column` group inside each shell, rather than only centering the right core area; both slot and linkup now use the same centered internal width logic.
  - Verification: using a clean Playwright source-injected preview (scripts stripped from `output/live-home.html`, current `_pages/about.md` script re-injected, current CSS overrides injected), desktop masthead display was `none`, desktop bio display was `block`, desktop profile inline display was `flex`, carousel autoplay advanced by about `45px` over `1.8s`, mouse dragging changed carousel scroll by about `57px`, featured item count stayed `3`, and the paper toolbar left edge aligned with the featured viewport. On mobile, both the slot shell and linkup shell measured `183.33px` wide with internal left/right insets `7.86px / 7.88px` (delta about `0.02px`), confirming the new centering is effectively symmetric.

- Desktop featured/paper alignment pass:
  - Switched the desktop featured-project card sizing from the old fixed `2.5-up` equal-width formula to the same aspect-ratio-driven width logic used on mobile, while keeping the overall featured section width unchanged.
  - Tightened the desktop featured-project gap to match the mobile carousel scale, so the interaction and spacing now read as one design rather than separate desktop/mobile variants.
  - Removed the leftover desktop paper-list horizontal padding and constrained the paper toolbar / paper list / empty state to the same `61.5rem` content width as the featured carousel, so the paper section is now left-aligned directly under the project section with no extra indent.
  - Verification: in Playwright desktop preview, the featured gap measured about `6.3px`, the three featured-card widths became `276.44px / 301.03px / 340.03px` (variable by image ratio instead of equal width), and both `paper-filter-toolbar` and `paper-list` had the same left edge and width as `featured-viewport` (`left delta = 0`, `width = 891.14px` after fixed-scale transform).

- Desktop horizontal-spacing pass:
  - Added a dedicated `--side-mascot-gap` token for the fixed-scale home shell so the left/right mascot rails can move inward symmetrically without being tied to the main sidebar/page column gap.
  - Reduced that outer mascot gap from the old hard-coded `1.08rem` equivalent down to `0.72rem`, and updated both the stage padding and the rail offsets to use the same shared token.
  - At the same time, increased the inner desktop sidebar/page gap from `1.08rem` to `1.32rem` so the profile/game column and the main content column separate a bit more clearly.
  - Verification: source-injected desktop preview confirmed the updated composition visually, and the measured sidebar/page inner gap increased from about `15.76px` to about `19.27px` after fixed-scale transform.

- Featured-carousel mechanism rewrite:
  - Replaced the old scroll-range-dependent desktop loop with a virtual-offset + DOM-rotation mechanism, so the carousel no longer depends on the small real `scrollLeft` overflow available on desktop when only three project cards are present.
  - The loop now advances by translating the track and rotating the real DOM items whenever the virtual offset crosses an item step, which restores true bidirectional dragging and prevents the old “teleport then stop” failure mode.
  - Unified pointer dragging across desktop and mobile under the same loop core, kept click suppression only after meaningful horizontal drag, and added horizontal-wheel support for desktop while leaving vertical page scrolling alone unless the wheel input is clearly horizontal.
  - Verification: source-injected Playwright checks showed desktop autoplay transform changing from `-43px` to `-69px` over `1.2s`, left drag rotated item order to `小游戏 -> 科研绘图 -> 全时段行人重识别`, right drag restored reverse movement successfully, and after release desktop autoplay resumed again (`-72px -> -85px`). Mobile stayed healthy under the same mechanism, with autoplay and post-drag resume both still progressing (`-33px -> -59px` before drag, then `0px -> -13px` after the pause window).

- Desktop gap correction pass:
  - The remaining “second gap” bug turned out not to be only the mascot-rail offset. The desktop `page / inner-wrap / page__content` chain was still wider than the actual featured/paper content block, so the visible content stopped early and left a large fake right blank.
  - Fixed by clearing the inherited `#main` horizontal padding, locking `#main > .page`, `.page__inner-wrap`, and `.page__content` to the same desktop content width token, increasing the inner sidebar/content gap, and shrinking the outer mascot gap token at the same time.
  - Final desktop tokens in this pass: `--main-column-gap: 2rem`, `--side-mascot-gap: 0.42rem`, with the page/content chain constrained to the same width as the featured/paper section.
  - Verification: source-injected desktop preview measured the first requested gap (sidebar -> featured/paper left edge) at `30px`, and the second requested gap (featured/paper right edge -> mascot rail) at `6.30px` on both sides, i.e. the outer left/right gaps matched exactly.

- Desktop gap/width/avatar follow-up:
  - Restored the featured/paper width back to the normal desktop width while keeping the exact-gap tuning active, instead of leaving the temporary 90% narrower content width.
  - Moved the profile block further downward by increasing the fixed-scale desktop `profile_box` top margin again.
  - Final desktop tokens after this pass: `--desktop-page-width: 61.5rem`, `--main-column-gap: 3.333333rem`, `--side-mascot-gap: 2rem`, with featured/paper width following the page width again.
  - Verification: source-injected desktop preview measured `featured/paper width = 922.5px`, `avatar top = 22.80px`, `inner gap ≈ 49.98px`, and `right outer gap = 30px`, which matches the latest requested geometry.
