# 20-in-1 Developer Toolbox - UI & 3D Design Specifications

This document defines the high-quality, premium visual language and 3D concepts for the Developer Toolbox.

## 1. Global Design System

### Premium Themes (5 Variants)
1. **Dark (Default)**: Deep grays (`#121212`), elevated surfaces (`#1E1E1E`), accents in vibrant purple (`#BB86FC`) and teal (`#03DAC6`). Glassmorphism overlays.
2. **Light**: Crisp white (`#FFFFFF`), soft gray surfaces (`#F5F5F5`), primary accents in deep royal blue (`#0056D2`). Soft, diffuse drop shadows.
3. **Solarized**: Classic Solarized Dark palette. Base (`#002b36`), accented with cyan (`#2aa198`), yellow (`#b58900`), and magenta (`#d33682`).
4. **Neon Glow**: Cyberpunk aesthetic. True black background (`#000000`), with glowing neon pink (`#FF00FF`) and neon green (`#39FF14`) borders. Font: JetBrains Mono.
5. **High-Contrast**: Pitch black (`#000000`) and pure white (`#FFFFFF`) with vivid yellow (`#FFFF00`) for absolute clarity and accessibility focus.

### Typography
- **Headings & UI**: `Inter` or `Outfit` (sans-serif, geometric, highly legible).
- **Code & Inputs**: `Fira Code` or `JetBrains Mono` for a distinctly "developer" feel.

### UI Components
- **Cards**: Soft glassmorphism in Dark/Light modes, stark borders in Neon/High-Contrast. Subtle `transform: translateY(-4px)` on hover.
- **Buttons**: Pill-shaped or sharply rounded corners (`8px`), with interactive micro-animations (ripple or scale effect).
- **Inputs & Selects**: Clean underlining or sleek bordered fields with glowing focus rings.

## 2. Main Page Layout (`index.html`)
- **Header**: Fixed, transparent backdrop-filter (blur). Logo left, Theme Switcher & Settings (Backup/Restore) right.
- **Hero Section**: A brief welcoming title "Developer Toolbox" with a dynamic 3D background object (like a gently rotating abstract wireframe sphere).
- **Grid**: `auto-fit, minmax(300px, 1fr)`.
- **Cards**: Tool Icon (Top), Title, Subtitle. On hover, a subtle CSS-based 3D rotation (tilt effect) activates.

## 3. Tool-Specific UI & 3D Elements

Each tool will follow a two-column or stacked layout: Interface in the foreground, 3D visualization as a dynamic accent/background element.

1. **JSON Formatter Validator**: A powerful developer utility for JSON Formatter Validator.
2. **Base64 Encoder Decoder**: A powerful developer utility for Base64 Encoder Decoder.
3. **URL Encoder Decoder**: A powerful developer utility for URL Encoder Decoder.
4. **Regex Tester Builder**: A powerful developer utility for Regex Tester Builder.
5. **JWT Debugger Validator**: A powerful developer utility for JWT Debugger Validator.
6. **Timestamp Converter**: UI - Timestamp Input / Date Input / Both Conversions / Timezone selector.. 3D - A clock with moving gears that adjust to the entered time.
7. **HTML Entity Encoder Decoder**: A powerful developer utility for HTML Entity Encoder Decoder.
8. **CSS Minifier Formatter**: A powerful developer utility for CSS Minifier Formatter.
9. **JavaScript Minifier Beautifier**: A powerful developer utility for JavaScript Minifier Beautifier.
10. **Diff Checker**: UI - Original Text / Modified Text / Diff View / Navigation buttons.. 3D - Two parallel walls with glowing bricks where differences occur.
11. **YAML to JSON Converter**: UI - YAML Input / JSON Output / JSON Input / YAML Output.. 3D - A transformer robot that shifts between two shapes.
12. **SQL Formatter Analyzer**: A powerful developer utility for SQL Formatter Analyzer.
13. **Markdown Preview Editor**: A powerful developer utility for Markdown Preview Editor.
14. **Hash Generator**: UI - String Input / Algorithm Selector / Hash Output / Multiple hashes at once.. 3D - A spinning cube with different colored faces for each algorithm.
15. **Color Picker Converter**: A powerful developer utility for Color Picker Converter.
16. **UUID Generator**: UI - Generator Button / UUID List / Quantity selector / Copy All.. 3D - Floating tags with UUIDs that shimmer.
17. **HTML Preview Sandbox**: A powerful developer utility for HTML Preview Sandbox.
18. **Lorem Ipsum Generator**: UI - Type selector (paragraphs/words) / Length input / Generated Text / Copy.. 3D - A waterfall of text blocks.
19. **Cron Expression Builder**: UI - Visual Selectors / Cron Expression / Description / Next Run Times / Execution Timeline.. 3D - A clock with multiple hands moving in sync.
20. **HTTP Status Code Explorer**: UI - Code Grid / Detail Panel / Search Filter / Scenario Matcher.. 3D - Rotating plaques with status codes that glow on hover.
21. **MIME Type Lookup**: UI - Extension Input / MIME Output / Reverse Lookup / Common Types List.. 3D - A filing cabinet with labelled drawers.
22. **Epoch Human Date Converter**: A powerful developer utility for Epoch Human Date Converter.
23. **RSA Key Pair Generator**: UI - Bit Length Selector / Generate Button / Public Key / Private Key / Copy buttons.. 3D - Two interlocking gears (public/private) that spin.
24. **Character Counter with Unicode Analysis**: UI - Text Input / Detailed Stats / Unicode Block Visualization / Encoding Comparison.. 3D - Floating letters with different colours for each Unicode block.
25. **CSS Gradient Generator**: UI - Colour Stops Editor / Angle Control / Preview / CSS Code.. 3D - A colour wheel that extrudes into a cone.
26. **Box Shadow Generator**: UI - Controls (X/Y offset / blur / spread / colour) / Live Preview / Code Output / Multiple Shadows.. 3D - A cube casting multiple shadows.
27. **Text Diff Checker**: UI - Original / Modified / Diff Output / Toggle view mode.. 3D - Two blocks with protruding bricks where differences exist.
28. **JSON Path Tester**: UI - JSON Input / Path Expression / Results / Interactive Node Selection.. 3D - A tree structure with highlighted branches.
29. **Password Strength Meter**: UI - Password Input / Strength Gauge / Feedback Tips / Entropy Display.. 3D - A lock that changes colour and grows spikes as strength increases.
30. **Git Ignore Generator**: UI - Language Selector (multi‑select) / Generated Output / Copy/Download.. 3D - A shield that blocks unwanted files.
31. **CSV to JSON Converter**: UI - CSV Input / JSON Output / Delimiter Selector / Header Row Toggle.. 3D - A spreadsheet transforming into a cube.
32. **HTML to Markdown Converter**: UI - HTML Input / Markdown Output / Copy Button / Sample Presets.. 3D - A document folding into a book.
33. **XML Formatter Validator**: A powerful developer utility for XML Formatter Validator.
34. **JavaScript Object Inspector**: UI - Object Input (JSON/text) / Tree View / Path Copier / Search.. 3D - A nested cube structure with transparent layers.
35. **SSL TLS Certificate Decoder**: A powerful developer utility for SSL TLS Certificate Decoder.
36. **Mock API Response Generator**: UI - Schema Editor / Field Type Selector (name / email / date) / Mock Preview / Copy as JSON.. 3D - A 3D bar chart that populates with mock data.
37. **HTML Escape Unescape Tool**: A powerful developer utility for HTML Escape Unescape Tool.
38. **Base64 Image Encoder**: UI - Image Upload / Preview / Base64 Output / Data URL / Copy buttons.. 3D - A picture frame that encodes itself into a string.
39. **CSS Animation Timing Visualizer**: UI - Bezier Graph / Control Points / Animated Preview / Code Output / Presets (ease / ease‑in / etc.).. 3D - A bouncing ball that traces its path in 3D.
40. **HTTP Request Builder**: UI - Method Selector / URL Input / Headers Editor / Body Editor / Response Panel / Request Timeline.. 3D - A network of nodes with data packets travelling.
41. **HTML Formatter Beautifier**: A powerful developer utility for HTML Formatter Beautifier.
42. **JSON to CSV Converter**: UI - JSON Input / CSV Output / Delimiter Selector / Flatten Nested Option.. 3D - A cube unfolding into a flat grid.
43. **YAML Validator Linter**: A powerful developer utility for YAML Validator Linter.
44. **Strong Password Generator**: UI - Length Slider / Character Type Toggles / Generated Password / Strength Meter / Regenerate.. 3D - A vault door with spinning combination lock.
45. **QR Code Generator**: UI - Data Input / Type Selector / QR Canvas / Size Control / Download Options.. 3D - A 3D cube with QR patterns on each face.
46. **CSS Specificity Calculator**: UI - Selector Input / Specificity Visualization / Comparison Mode / Rule Override Predictor.. 3D - Floating coloured cubes representing specificity levels.
47. **Git Command Visualizer**: UI - Commit Graph Canvas / Command Palette (rebase / merge / reset) / History Slider / Undo/Redo Stack.. 3D - A tree of nodes that move and reconnect in 3D space.
48. **Date Difference Calculator**: UI - Date Pickers / Results Matrix / Unit Toggles / Business Day Calculator.. 3D - A perpetual calendar with pages flipping.
49. **SVG Path Editor**: UI - Canvas Editor / Command Palette / Path Code Display / Export Options.. 3D - A 3D curve that can be manipulated by dragging points.
50. **Color Accessibility Grid**: A powerful developer utility for Color Accessibility Grid.
51. **Browser Storage Inspector**: UI - Storage Type Tabs / Key‑Value Editor / Export Tools / Size Calculator.. 3D - A filing cabinet with drawers that open to reveal storage items.
52. **Shortcut Cheatsheet Generator**: UI - Shortcut Builder / Live Preview / Style Customizer / PDF Export.. 3D - A 3D keyboard with keys lighting up for shortcuts.
53. **Timezone Overlap Finder**: UI - Team Member Input / Working Hours Setter / Overlap Calendar / Meeting Time Suggestions.. 3D - A 3D globe with markers for each team member.
54. **CSS Flexbox Visualizer**: UI - Container Controls / Item Controls / Visual Playground / Code Output.. 3D - 3D blocks that rearrange according to flex rules.
55. **Image Palette Extractor**: UI - Image Upload / Colour Palette / Relationship Diagrams / Harmony Suggestions.. 3D - A colour wheel that rotates and highlights relationships.
56. **Markdown Table Generator**: UI - Table Builder Grid / Markdown Preview / CSV Import/Export / Alignment Controls.. 3D - A 3D grid of cells that you can edit.
57. **URL Query String Parser**: UI - URL Input / Parameter Table / Reconstructed URL / Encoding Options.. 3D - A chain of links that can be edited.
58. **Font Loading Analyzer**: UI - URL Analyzer / Font Timeline / Optimisation Tips / Fallback Analysis.. 3D - 3D letter blocks that load one by one.
59. **CSS Media Query Bookmarklet Generator**: UI - Breakpoint Presets / Bookmarklet Generator / Preview Mode / Custom Size Builder.. 3D - A 3D ruler that extends to show screen sizes.
60. **JavaScript Error Simulator**: UI - Error Type Selector / Message Customizer / Trigger Environment / Behaviour Analysis.. 3D - A 3D “error bomb” that explodes into fragments.
61. **Cookie Consent Generator**: A powerful developer utility for Cookie Consent Generator.
62. **Web Component Playground**: UI - Code Editors / Component Preview / Shadow DOM Inspector / Export Package.. 3D - A 3D component cube with shadow layers.
63. **PR Template Builder**: A powerful developer utility for PR Template Builder.
64. **CSS to Tailwind Converter**: UI - CSS Input / Tailwind Output / Property Mapping Table / Alternative Suggestions.. 3D - A bridge connecting two islands.
65. **Terminal Color Scheme Designer**: UI - Base Colour Picker / ANSI Colour Matrix / Terminal Preview / Export (iTerm / VS Code / Alacritty formats).. 3D - A 3D terminal with glowing keys.
66. **NPM Dependency Graph Explorer**: UI - File Drop Zone / Interactive Graph / Duplicate Detector / Version Conflict Highlighter.. 3D - A network of spheres connected by lines.
67. **OpenAPI Schema Visualizer**: UI - Schema Graph / Property Inspector / Reference Tracker / Validation Report.. 3D - A 3D diagram of interconnected schemas.
68. **JavaScript Memory Leak Simulator**: UI - Leak Pattern Selector / Code Example / Memory Timeline Graph / Fix Demonstrator.. 3D - A leaking pipe with water droplets (memory).
69. **CORS Debugger**: UI - Request Builder / CORS Check Matrix / Response Headers Simulator / Fix Suggestions.. 3D - A wall with a door that opens when CORS passes.
70. **Shell Script Builder**: UI - Block Palette / Script Canvas / Live Bash Output / Explanation Panel.. 3D - A 3D flowchart that turns into text.
71. **gitignore Generator with Context**: UI - Project Type Selector / Category Groups (build / secrets / IDE) / Explain Toggles / Copy Output.. 3D - A shield with floating icons of ignored files.
72. **Webhook Tester Client Side**: A powerful developer utility for Webhook Tester Client Side.
73. **README Structure Analyzer**: UI - Markdown Input / Section Detection / Completeness Score / Improvement Suggestions.. 3D - A book with missing chapters highlighted.
74. **Environment Variable Validator**: UI - Schema Builder / .env Input / Validation Results / Type Coercion Preview.. 3D - A control panel with gauges that light up.
75. **Bundle Size Analyzer Offline Cache**: UI - Package Search / Size Visualisation / Alternative Comparison / Tree‑shakable Analysis.. 3D - Bar graphs that grow in 3D.
76. **Lighthouse CI Config Builder**: UI - Budget Builder / Assertion Rules / Threshold Sliders / YAML Output.. 3D - A lighthouse with beams of light.
77. **Semantic Version Calculator**: UI - Change Checklist / Version Display / Release Notes Generator / History Simulator.. 3D - A staircase with steps labelled patch/minor/major.
78. **HTML to JSX Converter**: UI - HTML Input / JSX Output / Transformation Log / Edge Case Highlighter.. 3D - A shape morphing from HTML tag to React component.
79. **CSS Grid Generator with Naming**: UI - Grid Canvas / Area Naming Tool / CSS Output / Responsive Breakpoints.. 3D - A 3D grid with labelled cells.
80. **Git Hook Builder**: UI - Hook Selector / Action Builder / Script Preview / Installation Instructions.. 3D - A hook that catches commits.
81. **Dockerfile Linter Optimizer**: A powerful developer utility for Dockerfile Linter Optimizer.
82. **CSS Inheritance Visualizer**: UI - HTML Tree Builder / Style Editor / Inheritance Map / Computed Values Panel.. 3D - A family tree of elements with colour flows.
83. **WebAssembly Size Analyzer**: UI - File Upload / Function Size Table / Call Graph / Import/Export Inspector.. 3D - A 3D structure with blocks sized by function weight.
84. **HTTP Header Security Checker**: UI - Header Input / Security Scorecard / Fix Suggestions / Server Config Generator (nginx / Apache).. 3D - A shield with bars that fill up.
85. **GraphQL Query Complexity Analyzer**: UI - Schema Input / Query Input / Complexity Tree / Cost Breakdown.. 3D - A tree where branches glow based on cost.
86. **Sass SCSS to CSS Playground**: A powerful developer utility for Sass SCSS to CSS Playground.
87. **IP Address Calculator Subnetting**: A powerful developer utility for IP Address Calculator Subnetting.
88. **Color Contrast Checker WCAG**: A powerful developer utility for Color Contrast Checker WCAG.
89. **Keycode Event Explorer**: A powerful developer utility for Keycode Event Explorer.
90. **JSON Schema Generator**: UI - JSON Input / Schema Output / Type Detection Details / Customisation Options.. 3D - A mould that shapes the JSON data.
91. **JSON Schema Generator from Sample**: UI - JSON Input / Schema Output / Type Detection Details / Customisation Options.. 3D - A mould that shapes the JSON data.
92. **ASCII Art Generator**: A powerful developer utility for ASCII Art Generator.
93. **Microfrontend Architecture Visualizer**: UI - App Definition Panel / Dependency Matrix / Interactive Graph / Shared Module Tracker.. 3D - A cluster of islands connected by bridges.
94. **React Vue Svelte Snippet Generator**: A powerful developer utility for React Vue Svelte Snippet Generator.
95. **JSON Web Key JWK Generator**: A powerful developer utility for JSON Web Key JWK Generator.
96. **Responsive Type Scale Generator**: UI - Base Settings / Scale Preview / Code Output / Visual Test Panel.. 3D - A staircase of letters scaling up.
97. **Git Ignore Generator**: UI - Language Selector (multi‑select) / Generated Output / Copy/Download.. 3D - A shield that blocks unwanted files.
98. **GraphQL to REST Comparator**: UI - GraphQL Input / REST Definition / Comparison Matrix / Over‑fetching Analysis.. 3D - Two scales balancing data weight.
99. **GraphQL to REST Comparator**: UI - GraphQL Input / REST Definition / Comparison Matrix / Over‑fetching Analysis.. 3D - Two scales balancing data weight.
100. **CSS Box Shadow Generator**: UI - Controls (X/Y offset / blur / spread / colour) / Live Preview / Code Output / Multiple Shadows.. 3D - A cube casting multiple shadows.
101. **Browser Feature Support Matrix**: UI - Feature Search / Browser Grid (Chrome/Firefox/Safari) / Polyfill Recommendations / Usage Statistics.. 3D - A matrix of browser logos with glowing cells.
102. **CSS Custom Property Organizer**: UI - CSS Input / Variable List / Dependency Graph / Unused Detector / Themed Grouping.. 3D - A web of interconnected nodes.
103. **Web Component Lifecycle Debugger**: UI - Component Code Input / Action Buttons (mount/update/unmount) / Lifecycle Timeline / State Inspector.. 3D - A timeline with glowing points at lifecycle events.
104. **Service Worker Cache Inspector**: UI - Cache List / Cache Contents Viewer / Strategy Simulator / Clear Controls.. 3D - A set of shelves with cached items.
105. **Monorepo Dependency Visualizer**: UI - Package Upload / Dependency Graph / Version Matrix / Circular Detector.. 3D - A 3D spider web of packages.
106. **HTTP Status Code Simulator**: UI - Code Selector / Response Preview / Browser Behaviour Notes / Handling Examples.. 3D - A signpost with different coloured signs.
107. **Web Animations API Playground**: UI - Keyframe Builder / Timeline Controls / Code Output / Element Preview.. 3D - A bouncing ball that leaves a trail in 3D.
