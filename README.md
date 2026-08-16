# scratchpad

Personal archive of AI-generated artifacts, visual explainers, and one-off HTML
reports, published by [zero_rxpc](https://github.com/Rxmeez) at
`scratchpad.rameez.co`.

- Static HTML/CSS, no build framework, no JS dependencies.
- `robots.txt` + per-page `noindex` meta tags — not search-indexed.
- Public URL, unlisted — do not publish sensitive content here.

## Structure

```
index.html          Homepage (auto-generated, do not hand-edit)
index_template.html  Template used by build.py
artifacts.json       Metadata for every artifact (title, date, topic, slug)
build.py             Regenerates index.html from artifacts.json
artifacts/<slug>/    One folder per artifact, each with its own index.html
assets/style.css     Shared theme
```

## Adding a new artifact

1. Add an entry to `artifacts.json`
2. Create `artifacts/<slug>/index.html` (link back to `../../assets/style.css`)
3. Run `python build.py` to regenerate the homepage
4. Commit and push — GitHub Pages redeploys automatically
