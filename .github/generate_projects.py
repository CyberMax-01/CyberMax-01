import json

with open('projects.json') as f:
    projects = json.load(f)

items = []
for proj in projects:
    name = proj['name']
    desc = proj['description']
    lang = proj.get('language','')
    link = proj.get('link','')
    item = f"### [{name}]({link})\n"
    item += f"{desc}\n\n"
    if lang:
        item += f"**Language:** {lang}\n\n"
    items.append(item)

content = "\n<hr>\n\n## 🚀 Projects\n\n" + "\n<hr>\n\n".join(items)

with open('projects/projects.md','w') as f:
    f.write(content)

print('Generated projects/projects.md')
