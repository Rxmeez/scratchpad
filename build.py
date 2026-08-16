"""
Rebuilds index.html from artifacts.json.
Run this after adding a new entry to artifacts.json and dropping the
matching HTML file into /artifacts/<slug>/index.html
"""
import json
import os
from datetime import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(ROOT, "artifacts.json"), encoding="utf-8") as f:
    artifacts = json.load(f)

artifacts.sort(key=lambda a: a["date"], reverse=True)

cards = []
if not artifacts:
    cards.append('<div class="empty-state">Nothing here yet.</div>')
else:
    for a in artifacts:
        cards.append(f'''  <div class="card">
    <a class="title" href="artifacts/{a['slug']}/">{a['title']}</a>
    <div class="desc">{a['description']}</div>
    <div class="meta-row">
      <span class="badge">{a['topic']}</span>
      <span>{a['date']}</span>
    </div>
  </div>''')

cards_html = "\n".join(cards)

with open(os.path.join(ROOT, "index_template.html"), encoding="utf-8") as f:
    template = f.read()

output = template.replace("<!--ARTIFACT_CARDS-->", cards_html)

with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
    f.write(output)

print(f"Built index.html with {len(artifacts)} artifact(s).")
