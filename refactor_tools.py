import os
import re

APP_DIR = r"c:\Users\AiSof\Downloads\FOLDERS\DEVELOPMENT\20-in-1 Developer Toolbox"

with open(os.path.join(APP_DIR, "app_details.md"), "r", encoding="utf-8") as f:
    app_details = f.read()

# Extract 100 tools
tool_pattern = re.compile(r"#### (\d+)\. (.*)\n- \*\*Problem:\*\* (.*?)\n- \*\*How it works:\*\* (.*)", re.MULTILINE)
tools = []
for match in tool_pattern.finditer(app_details):
    num = int(match.group(1))
    name = match.group(2).strip()
    desc = match.group(4).strip()
    
    # create slug
    slug = name.replace(" ", "-").replace("/", "-").replace("&", "-&-").replace("(", "").replace(")", "").replace(",", "")
    slug = re.sub(r"-+", "-", slug)
    
    tools.append({
        "num": num,
        "name": name,
        "slug": slug,
        "desc": desc
    })

tools.sort(key=lambda x: x["num"])

old_to_new_mapping = {
    1: 46,
    2: 20,
    3: 48,
    4: 24,
    5: 49,
    6: 4,
    7: 50,
    8: 51,
    9: 52,
    10: 53,
    11: 54,
    12: 55,
    13: 56,
    14: 2,
    15: 57,
    16: 58,
    17: 59,
    18: 60,
    19: 61,
    20: 62
}

new_to_old = {v: k for k, v in old_to_new_mapping.items()}

# Rename HTML files and update their contents
for old_num, new_num in old_to_new_mapping.items():
    old_file = os.path.join(APP_DIR, f"tool-{old_num}.html")
    if not os.path.exists(old_file):
        continue
    
    tool_info = next((t for t in tools if t["num"] == new_num), None)
    if not tool_info:
        continue
        
    new_filename = f"tool-{new_num}-{tool_info['slug']}.html"
    new_file = os.path.join(APP_DIR, new_filename)
    
    # Read old file and update title/headers
    with open(old_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Update title
    content = re.sub(r"<title>.*?</title>", f"<title>{tool_info['name']} - Developer Toolbox</title>", content)
    # Update tool title inside header
    content = re.sub(r"<h1 class=\"tool-title\">.*?</h1>", f"<h1 class=\"tool-title\">{tool_info['name']}</h1>", content)
    # If the user clicks back or there are links to index, make sure they stand
    # Usually it's <a href="index.html" class="back-btn">
    
    with open(old_file, "w", encoding="utf-8") as f: # write first before rename
        f.write(content)
        
    os.rename(old_file, new_file)
    print(f"Renamed tool-{old_num}.html to {new_filename}")

# Update ui_designs.md
with open(os.path.join(APP_DIR, "ui_designs.md"), "r", encoding="utf-8") as f:
    ui_designs = f.read()

for old_num in range(20, 0, -1): # backward to prevent '1' replacing '10' etc.
    new_num = old_to_new_mapping[old_num]
    # Replace the numbered list item. E.g., "1. **CSS Specificity**:"
    pattern = re.compile(rf"^{old_num}\. \*\*", re.MULTILINE)
    ui_designs = pattern.sub(f"{new_num}. **", ui_designs)

with open(os.path.join(APP_DIR, "ui_designs.md"), "w", encoding="utf-8") as f:
    f.write(ui_designs)

# Update index.html
with open(os.path.join(APP_DIR, "index.html"), "r", encoding="utf-8") as f:
    index_html = f.read()

# Generate the new grid cards
cards_html = ""
for t in tools:
    filename = f"tool-{t['num']}-{t['slug']}.html"
    icon = "🔧"
    if t['num'] in new_to_old:
        # extract old icon from existing index.html if possible
        pass # we'll just use a generic icon for now or leave it
    cards_html += f'''          <!-- Tool {t["num"]} -->
          <a href="{filename}" class="tool-card">
            <div class="tool-icon">🔧</div>
            <h3 class="tool-title">{t["name"]}</h3>
            <p class="tool-desc">{t["desc"]}</p>
          </a>\n\n'''

grid_start = index_html.find('<div class="tool-grid">')
grid_end = index_html.find('</section>', grid_start)

if grid_start != -1 and grid_end != -1:
    new_index = index_html[:grid_start + len('<div class="tool-grid">\n')] + cards_html + index_html[grid_end - 16:]
    with open(os.path.join(APP_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(new_index)

print("Done. Renamed HTML files, updated ui_designs.md, and updated index.html to 100 tools.")
