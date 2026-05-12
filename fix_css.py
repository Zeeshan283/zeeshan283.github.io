import os
import glob

directories = [
    '/Users/zeeshan/Documents/cv/porfolio/zeeshan283.github.io/services',
    '/Users/zeeshan/Documents/cv/porfolio/zeeshan283.github.io/case-studies'
]

files = []
for d in directories:
    files.extend(glob.glob(os.path.join(d, '*.html')))

files.append('/Users/zeeshan/Documents/cv/porfolio/zeeshan283.github.io/page-generator.php')

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if we already applied the fix
    if 'min-width: 0;' in content and '.hero-content, .hero-profile' in content:
        continue
        
    # Replace grid definition to add min-width: 0
    old_grid = """.hero-container {
            display: grid;
            grid-template-columns: 1.2fr 1fr;
            gap: 4rem;
            align-items: center;
        }"""
        
    new_grid = """.hero-container {
            display: grid;
            grid-template-columns: 1.2fr 1fr;
            gap: 4rem;
            align-items: center;
        }
        
        .hero-content, .hero-profile {
            min-width: 0;
            max-width: 100%;
        }"""
        
    # Apply box-sizing
    old_body = """body {
            font-family: var(--font-sans);"""
            
    new_body = """*, *::before, *::after {
            box-sizing: border-box;
        }
        
        body {
            font-family: var(--font-sans);"""
            
    # Apply width: 100% to code-window
    old_code = """.code-window {
            background: rgba(13, 17, 23, 0.85);"""
            
    new_code = """.code-window {
            width: 100%;
            background: rgba(13, 17, 23, 0.85);"""
            
    new_content = content.replace(old_grid, new_grid)
    new_content = new_content.replace(old_body, new_body)
    new_content = new_content.replace(old_code, new_code)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print(f"Fixed {len(files)} files.")
