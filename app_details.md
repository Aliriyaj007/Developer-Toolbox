# 🌟 Ultimate Developer Toolbox – 100 Tools with Unique 3D Designs  

Create a **fully client‑side** web application that hosts **100 distinct developer tools**, each presented in its own **standalone HTML file**. The main landing page (`index.html`) displays a responsive grid of tool cards. Every tool page must have a **unique, interactive 3D design element** (using Three.js or advanced CSS 3D) that reflects the tool’s purpose.  

The project must be **modular, scalable, and readable**, with **multiple premium colour themes** and a **backup/restore feature** for user preferences (theme, last used tools, etc.). **No backend or AI** – everything runs in the browser.  

---

## 📁 File Structure  

```
📦 developer-toolbox/
├── index.html                 # Main grid page
├── tool-1-Formatter-&-Validator.html                 # Tool #1: JSON Formatter & Validator
├── tool-2-Base64-Encoder-Decoder.html                 # Tool #2: Base64 Encoder/Decoder
├── ...
├── tool-100-Web-Animations-API-Playground.html               # Tool #100: Web Animations API Playground
└── assets/ (optional)          # Shared images/fonts (if any)
```

- **Each HTML file must be completely self‑contained** – it can load external libraries (Three.js, date‑fns, etc.) from a CDN, but all logic and styling must reside inside that file.  
- **Shared code** (theme switcher, backup/restore) can be duplicated across files for simplicity, but keep it organised in separate `<script>` blocks.

---

## 🎨 Design Requirements  

### 1. Main Page (`index.html`)  
- **Header:**  
  - Title: “Developer Toolbox”  
  - Theme switcher (dropdown or icon toggles) – switches between at least 5 premium themes (Light, Dark, Solarized, High‑Contrast, Neon Glow).  
  - Backup/Restore buttons:  
    - **Backup:** Downloads a JSON file containing all `localStorage` keys (user preferences, tool‑specific data).  
    - **Restore:** Lets the user upload a JSON file and merge its contents into `localStorage` (with validation and user feedback).  
- **Tool Grid:**  
  - Use CSS Grid with `grid-template-columns: repeat(auto-fit, minmax(250px, 1fr))`.  
  - Each card shows: tool name, a short description, and a small 3D icon or preview (optional). Clicking a card opens the corresponding tool page.  
- **Footer:**  
  - `Made with ❤️ by <a href="https://github.com/Aliriyaj007" target="_blank">Aliriyaj007</a>`  

### 2. Tool Page Template (common structure)  
Each tool page must follow this layout:  
- **Header:**  
  - Tool name  
  - Theme switcher (same as on index)  
  - “← Back” link to `index.html`  
- **Main Content:** The tool’s interface (inputs, buttons, visualisations).  
- **3D Scene:** A `<canvas>` or `<div>` that holds the unique 3D effect. The scene should be placed as a background or a subtle accent – it must not interfere with the UI (`pointer-events: none` if behind).  
- **Footer:** Same credit line as index.  

### 3. Responsiveness  
- All pages must be fully responsive (mobile, tablet, desktop) using fluid layouts and media queries.  
- On small screens, the 3D scene can be reduced in size or hidden to prioritise usability.  

### 4. Themes  
- Define at least 5 colour themes using CSS custom properties (variables).  
- Example themes:  
  ```css
  :root { /* light theme */ }
  .theme-dark { /* dark theme */ }
  .theme-solarized { /* solarized */ }
  .theme-highcontrast { /* high contrast */ }
  .theme-neon { /* neon glow */ }
  ```  
- The selected theme is stored in `localStorage` and applied on page load.  

### 5. Backup & Restore  
- **Backup:** Gather all keys from `localStorage` (except any temporary ones) and save them as a JSON file named `toolbox-backup-YYYY-MM-DD.json`.  
- **Restore:** On file upload, parse the JSON, validate its structure (must contain expected keys), and merge into `localStorage`. Show success/error messages.  

---


## 🛠 Tool Specifications & Audit List (1–107)

#### 1. JSON Formatter Validator
- **File:** tool-1-JSON-Formatter-Validator.html
#### 2. Base64 Encoder Decoder
- **File:** tool-2-Base64-Encoder-Decoder.html
#### 3. URL Encoder Decoder
- **File:** tool-3-URL-Encoder-Decoder.html
#### 4. Regex Tester Builder
- **File:** tool-4-Regex-Tester-Builder.html
#### 5. JWT Debugger Validator
- **File:** tool-5-JWT-Debugger-Validator.html
#### 6. Timestamp Converter
- **File:** tool-6-Timestamp-Converter.html
#### 7. HTML Entity Encoder Decoder
- **File:** tool-7-HTML-Entity-Encoder-Decoder.html
#### 8. CSS Minifier Formatter
- **File:** tool-8-CSS-Minifier-Formatter.html
#### 9. JavaScript Minifier Beautifier
- **File:** tool-9-JavaScript-Minifier-Beautifier.html
#### 10. Diff Checker
- **File:** tool-10-Diff-Checker.html
#### 11. YAML to JSON Converter
- **File:** tool-11-YAML-to-JSON-Converter.html
#### 12. SQL Formatter Analyzer
- **File:** tool-12-SQL-Formatter-Analyzer.html
#### 13. Markdown Preview Editor
- **File:** tool-13-Markdown-Preview-Editor.html
#### 14. Hash Generator
- **File:** tool-14-Hash-Generator.html
#### 15. Color Picker Converter
- **File:** tool-15-Color-Picker-Converter.html
#### 16. UUID Generator
- **File:** tool-16-UUID-Generator.html
#### 17. HTML Preview Sandbox
- **File:** tool-17-HTML-Preview-Sandbox.html
#### 18. Lorem Ipsum Generator
- **File:** tool-18-Lorem-Ipsum-Generator.html
#### 19. Cron Expression Builder
- **File:** tool-19-Cron-Expression-Builder.html
#### 20. HTTP Status Code Explorer
- **File:** tool-20-HTTP-Status-Code-Explorer.html
#### 21. MIME Type Lookup
- **File:** tool-21-MIME-Type-Lookup.html
#### 22. Epoch Human Date Converter
- **File:** tool-22-Epoch-Human-Date-Converter.html
#### 23. RSA Key Pair Generator
- **File:** tool-23-RSA-Key-Pair-Generator.html
#### 24. Character Counter with Unicode Analysis
- **File:** tool-24-Character-Counter-with-Unicode-Analysis.html
#### 25. CSS Gradient Generator
- **File:** tool-25-CSS-Gradient-Generator.html
#### 26. Box Shadow Generator
- **File:** tool-26-Box-Shadow-Generator.html
#### 27. Text Diff Checker
- **File:** tool-27-Text-Diff-Checker.html
#### 28. JSON Path Tester
- **File:** tool-28-JSON-Path-Tester.html
#### 29. Password Strength Meter
- **File:** tool-29-Password-Strength-Meter.html
#### 30. Git Ignore Generator
- **File:** tool-30-Git-Ignore-Generator.html
#### 31. CSV to JSON Converter
- **File:** tool-31-CSV-to-JSON-Converter.html
#### 32. HTML to Markdown Converter
- **File:** tool-32-HTML-to-Markdown-Converter.html
#### 33. XML Formatter Validator
- **File:** tool-33-XML-Formatter-Validator.html
#### 34. JavaScript Object Inspector
- **File:** tool-34-JavaScript-Object-Inspector.html
#### 35. SSL TLS Certificate Decoder
- **File:** tool-35-SSL-TLS-Certificate-Decoder.html
#### 36. Mock API Response Generator
- **File:** tool-36-Mock-API-Response-Generator.html
#### 37. HTML Escape Unescape Tool
- **File:** tool-37-HTML-Escape-Unescape-Tool.html
#### 38. Base64 Image Encoder
- **File:** tool-38-Base64-Image-Encoder.html
#### 39. CSS Animation Timing Visualizer
- **File:** tool-39-CSS-Animation-Timing-Visualizer.html
#### 40. HTTP Request Builder
- **File:** tool-40-HTTP-Request-Builder.html
#### 41. HTML Formatter Beautifier
- **File:** tool-41-HTML-Formatter-Beautifier.html
#### 42. JSON to CSV Converter
- **File:** tool-42-JSON-to-CSV-Converter.html
#### 43. YAML Validator Linter
- **File:** tool-43-YAML-Validator-Linter.html
#### 44. Strong Password Generator
- **File:** tool-44-Strong-Password-Generator.html
#### 45. QR Code Generator
- **File:** tool-45-QR-Code-Generator.html
#### 46. CSS Specificity Calculator
- **File:** tool-46-CSS-Specificity-Calculator.html
#### 47. Git Command Visualizer
- **File:** tool-47-Git-Command-Visualizer.html
#### 48. Date Difference Calculator
- **File:** tool-48-Date-Difference-Calculator.html
#### 49. SVG Path Editor
- **File:** tool-49-SVG-Path-Editor.html
#### 50. Color Accessibility Grid
- **File:** tool-50-Color-Accessibility-Grid.html
#### 51. Browser Storage Inspector
- **File:** tool-51-Browser-Storage-Inspector.html
#### 52. Shortcut Cheatsheet Generator
- **File:** tool-52-Shortcut-Cheatsheet-Generator.html
#### 53. Timezone Overlap Finder
- **File:** tool-53-Timezone-Overlap-Finder.html
#### 54. CSS Flexbox Visualizer
- **File:** tool-54-CSS-Flexbox-Visualizer.html
#### 55. Image Palette Extractor
- **File:** tool-55-Image-Palette-Extractor.html
#### 56. Markdown Table Generator
- **File:** tool-56-Markdown-Table-Generator.html
#### 57. URL Query String Parser
- **File:** tool-57-URL-Query-String-Parser.html
#### 58. Font Loading Analyzer
- **File:** tool-58-Font-Loading-Analyzer.html
#### 59. CSS Media Query Bookmarklet Generator
- **File:** tool-59-CSS-Media-Query-Bookmarklet-Generator.html
#### 60. JavaScript Error Simulator
- **File:** tool-60-JavaScript-Error-Simulator.html
#### 61. Cookie Consent Generator
- **File:** tool-61-Cookie-Consent-Generator.html
#### 62. Web Component Playground
- **File:** tool-62-Web-Component-Playground.html
#### 63. PR Template Builder
- **File:** tool-63-PR-Template-Builder.html
#### 64. CSS to Tailwind Converter
- **File:** tool-64-CSS-to-Tailwind-Converter.html
#### 65. Terminal Color Scheme Designer
- **File:** tool-65-Terminal-Color-Scheme-Designer.html
#### 66. NPM Dependency Graph Explorer
- **File:** tool-66-NPM-Dependency-Graph-Explorer.html
#### 67. OpenAPI Schema Visualizer
- **File:** tool-67-OpenAPI-Schema-Visualizer.html
#### 68. JavaScript Memory Leak Simulator
- **File:** tool-68-JavaScript-Memory-Leak-Simulator.html
#### 69. CORS Debugger
- **File:** tool-69-CORS-Debugger.html
#### 70. Shell Script Builder
- **File:** tool-70-Shell-Script-Builder.html
#### 71. gitignore Generator with Context
- **File:** tool-71-gitignore-Generator-with-Context.html
#### 72. Webhook Tester Client Side
- **File:** tool-72-Webhook-Tester-Client-Side.html
#### 73. README Structure Analyzer
- **File:** tool-73-README-Structure-Analyzer.html
#### 74. Environment Variable Validator
- **File:** tool-74-Environment-Variable-Validator.html
#### 75. Bundle Size Analyzer Offline Cache
- **File:** tool-75-Bundle-Size-Analyzer-Offline-Cache.html
#### 76. Lighthouse CI Config Builder
- **File:** tool-76-Lighthouse-CI-Config-Builder.html
#### 77. Semantic Version Calculator
- **File:** tool-77-Semantic-Version-Calculator.html
#### 78. HTML to JSX Converter
- **File:** tool-78-HTML-to-JSX-Converter.html
#### 79. CSS Grid Generator with Naming
- **File:** tool-79-CSS-Grid-Generator-with-Naming.html
#### 80. Git Hook Builder
- **File:** tool-80-Git-Hook-Builder.html
#### 81. Dockerfile Linter Optimizer
- **File:** tool-81-Dockerfile-Linter-Optimizer.html
#### 82. CSS Inheritance Visualizer
- **File:** tool-82-CSS-Inheritance-Visualizer.html
#### 83. WebAssembly Size Analyzer
- **File:** tool-83-WebAssembly-Size-Analyzer.html
#### 84. HTTP Header Security Checker
- **File:** tool-84-HTTP-Header-Security-Checker.html
#### 85. GraphQL Query Complexity Analyzer
- **File:** tool-85-GraphQL-Query-Complexity-Analyzer.html
#### 86. Sass SCSS to CSS Playground
- **File:** tool-86-Sass-SCSS-to-CSS-Playground.html
#### 87. IP Address Calculator Subnetting
- **File:** tool-87-IP-Address-Calculator-Subnetting.html
#### 88. Color Contrast Checker WCAG
- **File:** tool-88-Color-Contrast-Checker-WCAG.html
#### 89. Keycode Event Explorer
- **File:** tool-89-Keycode-Event-Explorer.html
#### 90. JSON Schema Generator
- **File:** tool-90-JSON-Schema-Generator.html
#### 91. JSON Schema Generator from Sample
- **File:** tool-91-JSON-Schema-Generator-from-Sample.html
#### 92. ASCII Art Generator
- **File:** tool-92-ASCII-Art-Generator.html
#### 93. Microfrontend Architecture Visualizer
- **File:** tool-93-Microfrontend-Architecture-Visualizer.html
#### 94. React Vue Svelte Snippet Generator
- **File:** tool-94-React-Vue-Svelte-Snippet-Generator.html
#### 95. JSON Web Key JWK Generator
- **File:** tool-95-JSON-Web-Key-JWK-Generator.html
#### 96. Responsive Type Scale Generator
- **File:** tool-96-Responsive-Type-Scale-Generator.html
#### 97. Git Ignore Generator
- **File:** tool-97-Git-Ignore-Generator.html
#### 98. GraphQL to REST Comparator
- **File:** tool-98-GraphQL-to-REST-Comparator.html
#### 99. GraphQL to REST Comparator
- **File:** tool-99-GraphQL-to-REST-Comparator.html
#### 100. CSS Box Shadow Generator
- **File:** tool-100-CSS-Box-Shadow-Generator.html
#### 101. Browser Feature Support Matrix
- **File:** tool-101-Browser-Feature-Support-Matrix.html
#### 102. CSS Custom Property Organizer
- **File:** tool-102-CSS-Custom-Property-Organizer.html
#### 103. Web Component Lifecycle Debugger
- **File:** tool-103-Web-Component-Lifecycle-Debugger.html
#### 104. Service Worker Cache Inspector
- **File:** tool-104-Service-Worker-Cache-Inspector.html
#### 105. Monorepo Dependency Visualizer
- **File:** tool-105-Monorepo-Dependency-Visualizer.html
#### 106. HTTP Status Code Simulator
- **File:** tool-106-HTTP-Status-Code-Simulator.html
#### 107. Web Animations API Playground
- **File:** tool-107-Web-Animations-API-Playground.html
