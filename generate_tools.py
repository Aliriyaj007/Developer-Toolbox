import os
import re

APP_DIR = r"c:\Users\AiSof\Downloads\FOLDERS\DEVELOPMENT\20-in-1 Developer Toolbox"

# 1. Parse app_details.md
with open(os.path.join(APP_DIR, "app_details.md"), "r", encoding="utf-8") as f:
    app_details = f.read()

tool_pattern = re.compile(r"#### (\d+)\. (.*)\n- \*\*Problem:\*\* .*?\n- \*\*How it works:\*\* .*?\n- \*\*Sections:\*\* (.*?)\n- \*\*Unique:\*\* .*?\n- \*\*Core tech:\*\* .*?\n- \*\*Target users:\*\* .*?\n- \*\*3D Design:\*\* (.*)", re.MULTILINE)
tools = []
for match in tool_pattern.finditer(app_details):
    num = int(match.group(1))
    name = match.group(2).strip()
    sections = match.group(3).strip()
    design_3d = match.group(4).strip()
    
    slug = name.replace(" ", "-").replace("/", "-").replace("&", "-&-").replace("(", "").replace(")", "").replace(",", "")
    slug = re.sub(r"-+", "-", slug)
    
    tools.append({
        "num": num,
        "name": name,
        "slug": slug,
        "ui": sections,
        "3d": design_3d
    })

tools.sort(key=lambda x: x["num"])

# 2. Complete ui_designs.md
with open(os.path.join(APP_DIR, "ui_designs.md"), "r", encoding="utf-8") as f:
    ui_designs = f.read()

# Separate header from tool specific designs
header_split = ui_designs.split("## 3. Tool-Specific UI & 3D Elements\n\nEach tool will follow a two-column or stacked layout: Interface in the foreground (contained in a glass panel), 3D visualization as a dynamic accent/background element to the side or fully behind with low opacity.\n\n")
header = header_split[0] + "## 3. Tool-Specific UI & 3D Elements\n\nEach tool will follow a two-column or stacked layout: Interface in the foreground (contained in a glass panel), 3D visualization as a dynamic accent/background element to the side or fully behind with low opacity.\n\n"

# Re-generate the full list for all 100 tools
designs_list = []
for t in tools:
    ui_desc = t['ui'].replace(', ', ' / ') # Simplify sections to UI
    designs_list.append(f"{t['num']}. **{t['name']}**: UI - {ui_desc}. 3D - {t['3d']}")

full_ui_designs = header + "\n".join(designs_list) + "\n"

with open(os.path.join(APP_DIR, "ui_designs.md"), "w", encoding="utf-8") as f:
    f.write(full_ui_designs)

print("Updated ui_designs.md with 100 tools.")

# 3. Read template (we'll use tool-46-CSS-Specificity-Calculator.html as a base)
template_path = os.path.join(APP_DIR, "tool-46-CSS-Specificity-Calculator.html")
with open(template_path, "r", encoding="utf-8") as f:
    template_content = f.read()

# Make the template generic
template_content = re.sub(r"<title>.*?</title>", "<title>%%TOOL_NAME%% - Developer Toolbox</title>", template_content)
template_content = re.sub(r"<h1 class=\"tool-title\">.*?</h1>", "<h1 class=\"tool-title\">%%TOOL_NAME%%</h1>", template_content)

# We want to replace the custom <style> and main tool content inside <div class="tool-content">
tool_content_pattern = re.compile(r"(<div class=\"tool-content\">).*?(</div>\s*</main>)", re.DOTALL)
template_content = tool_content_pattern.sub(r"\1\n        <!-- Tool UI goes here -->\n        <p class=\"text-secondary\">This tool is currently under construction.</p>\n      \2", template_content)

# We want to replace the specific scripts for the tool
script_pattern = re.compile(r"(<script>\s*// Tool Logic).*?(</script>)", re.DOTALL)
template_content = script_pattern.sub(r"\1\n    document.addEventListener('DOMContentLoaded', () => {\n      // Initialize tool\n    });\n  \2", template_content)

# Remove the specific ThreeJS logic for CSS Specificity and replace with generic setup
threejs_pattern = re.compile(r"(<script>\s*// 3D Background).*?(</script>)", re.DOTALL)
template_content = threejs_pattern.sub(r"""\1
    const init3D = () => {
      const container = document.getElementById('canvas-container');
      if (!container || !window.THREE) return;

      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(75, container.clientWidth / container.clientHeight, 0.1, 1000);
      camera.position.z = 5;

      const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
      renderer.setSize(container.clientWidth, container.clientHeight);
      container.appendChild(renderer.domElement);

      const geometry = new THREE.IcosahedronGeometry(2, 0);
      
      const getThemeColor = () => {
        const style = getComputedStyle(document.body);
        return new THREE.Color(style.getPropertyValue('--accent-primary').trim() || '#BB86FC');
      };

      const material = new THREE.MeshBasicMaterial({ 
        color: getThemeColor(), 
        wireframe: true,
        transparent: true,
        opacity: 0.2
      });
      
      const mesh = new THREE.Mesh(geometry, material);
      scene.add(mesh);

      window.addEventListener('themechanged', () => {
        setTimeout(() => material.color = getThemeColor(), 50);
      });

      window.addEventListener('resize', () => {
        camera.aspect = container.clientWidth / container.clientHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(container.clientWidth, container.clientHeight);
      });

      const animate = () => {
        requestAnimationFrame(animate);
        mesh.rotation.x += 0.005;
        mesh.rotation.y += 0.005;
        renderer.render(scene, camera);
      };

      animate();
    };

    document.addEventListener('DOMContentLoaded', init3D);
  \2""", template_content)


# 4. Generate all 100 files if they don't exist
created_count = 0
for t in tools:
    filename = f"tool-{t['num']}-{t['slug']}.html"
    filepath = os.path.join(APP_DIR, filename)
    
    if os.path.exists(filepath):
        continue
        
    tool_html = template_content.replace("%%TOOL_NAME%%", t['name'])
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(tool_html)
    created_count += 1
    
print(f"Generated {created_count} new HTML files for the missing tools.")

