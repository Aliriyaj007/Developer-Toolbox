# Universal Design System & UX Architecture

This document serves as the master blueprint for the frontend architecture, UI/UX design patterns, animations, and interactivity models used across this application. It is designed to be fully replicable for any future client-side, offline-first web applications.

## 1. Core Philosophy & Modularity
The application is built on a **Zero-Build, Offline-First** philosophy.
- **No Build Tools Required:** Pure vanilla HTML, CSS, and JS (ES6) run directly in the browser. No Webpack, Vite, or npm layers are necessary.
- **Offline First:** All tools, processing, and state management happen client-side.
- **Modular Asset Architecture:**
  - `assets/core.css`: Contains all global resets, typography, spacing utility classes, theme `:root` variables, and standard button/input styles.
  - `assets/core.js`: A singleton immediately invoked function expression (IIFE) named `AppCore` that automatically binds global UI controls (Backup, Restore, Theme Switching) across all pages.
  - `assets/tools-data.js`: The central manifest. A pure JS array of objects containing tool metadata, decoupling the dynamic grid rendering from hardcoded HTML entries.

## 2. 5-Tier Global Theme Engine
The application relies on CSS Custom Properties (`--bg-main`, `--accent-primary`) defined across 5 distinct themes in `core.css`.
- **Theme Activation:** Managed by `core.js`, which listens to a `<select id="theme-select">` element and applies a class (e.g., `.theme-solarized`) to the document `<body>`.
- **The 5 Themes:**
  1. **Dark Theme:** High contrast greys, soft purple (`#BB86FC`) accents.
  2. **Light Theme:** Clean whites/greys, deep blue (`#0056D2`) and pink accents.
  3. **Solarized:** Classic developer teal (`#002b36`) and cyan palette.
  4. **Neon Glow:** Pure black (`#000000`) with hyper-vibrant Magenta (`#f0f`) and Green (`#39FF14`) borders. Includes aggressive `box-shadow` glows.
  5. **High Contrast:** Pure black and pure yellow (`#FFFF00`). Zero border-radius (square corners) for maximum accessibility.
- **3D Syncing:** When `core.js` changes the theme, it dispatches a window `themechanged` event. 3D WebGL scenes listen to this event, dynamically read the active `--accent-primary` via `getComputedStyle`, and recolor the 3D meshes without refreshing the page.

## 3. UI/UX Interactivity & Feedback
User experience is elevated through continuous micro-interactions that confirm actions visually.
- **Toast Notifications:** Handled by `AppCore.showToast(msg, type)`. These dynamically push sliding alerts to the bottom right and vanish automatically after 3 seconds, eliminating intrusive `alert()` pop-ups.
- **Skeleton Loaders:**
  - Before rendering the true data grid, the UI emits empty `.skeleton` skeleton cards with a CSS-based shimmering gradient (animating `background-position` from `-200%` to `200%`).
  - **Staggered Fade-in:** When the real cards mount, they scale from 0.95x and fade into 1.0x with an inline `animation-delay` step of `0.05s` per card.
- **Card Hover Lifts:** Standard `.tool-card` elements feature a `transform: translateY(-4px)` on hover, paired with an increased box-shadow spread. The internal icon gets rotated `90deg` and scaled by `1.1x` to make the card feel "alive".
- **Dynamic Scroll Progress:** A fixed div at the absolute top of the viewport calculates `scrollTop / scrollHeight` on the window scroll event to grow the width of a 3px magenta bar, showing read progress.

## 4. Personalization & LocalStorage (State Management)
Because the app is entirely local, `localStorage` is completely exploited as a high-speed database.
- **Backup & Restore System:**
  - **Backup:** Iterates over `localStorage`, bundles all keys into a single JSON object, converts to a `Blob`, and forces a `<a download="..">` trigger.
  - **Restore:** Uses a hidden `<input type="file" accept=".json">`. The `FileReader` parses the JSON and blindly re-merges keys into `localStorage`, immediately firing a page reload.
- **Popularity Tracking:** Every card click increments a hit counter in the `tb_pop` JSON object. The "Sort Popularity" view uses this integer mapping.
- **Tags & Favorites System:** Clicking standard star (★) icons pushes the tool ID into a `tb_favs` array. A `prompt` allows injecting arbitrary string tokens into a `tb_tags` array. The search engine inherently queries these local mappings before the base manifest names.

## 5. 3D WebGL Integration (Three.js)
The application leverages Three.js for lightweight abstract backgrounds.
- **Performance:** Render loop handles rotation (`rotation.x`, `rotation.y`).
- **Mouse Interactivity:** Parallax mouse-tracking calculates viewport-normalized coordinates (`-1` to `1`) and applies a subtle lerped tilt to the 3D object on `mousemove`, giving the header depth without blocking the DOM interactions.
- **Encapsulation:** Put behind an absolutely positioned `<div id="hero-canvas">` with `z-index: 1` and `pointer-events: none;`, ensuring user text selection and button clicks hit the DOM (`z-index: 10`), not the canvas.
