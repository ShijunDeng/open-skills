# SVG-First PPT Craft Workflow

Use this workflow when the user wants a new deck from a topic or outline and asks for a highly designed, high-density, Chinese enterprise-style, or Huawei-style presentation. Prefer `pptxgenjs.md` for ordinary native PowerPoint authoring and `editing.md` for template edits.

## Output Structure

Create a timestamped work directory:

```bash
python scripts/generate_timestamp_dir.py output
```

Expected structure:

```text
output/YYYYMMDD_HHMMSS_000/
├── research_notes.md
├── ppt_plan.md
├── pages/
│   ├── page_1.svg
│   └── page_N.svg
└── pages.pptx
```

Use `python scripts/ensure_output_dir.py <output_dir>` before writing SVG pages. Do not pass a path ending in `pages`.

## Planning

Lock the five parameters from `SKILL.md`: Archetype, Brand, Audience, Scene, and View Mode. Then write `ppt_plan.md` with:

- Topic, generation time, page count, and style id.
- An outline table with page number, title, and core point.
- A detailed section for every page.

Slide titles should be conclusion-style complete statements, not labels. For research-backed decks, search current facts before planning and list sources in `research_notes.md`.

## SVG Page Rules

Generate one final SVG per slide:

- `viewBox="0 0 1280 720"`.
- File names are `pages/page_1.svg`, `pages/page_2.svg`, etc.
- Every page must contain real text and data; never use placeholder blocks.
- Each content slide should include 6-12 meaningful modules such as data cards, charts, comparison boxes, timelines, process flows, callouts, or relationship diagrams.
- Use a clear title zone, body zone, and optional footer zone.
- Keep spacing consistent, avoid overlap, and keep text inside its container.
- Prioritize deeper content, annotations, and causal relationships before decoration.

For Huawei-style or dense enterprise decks, read `styles/huawei.md` before generating pages.

## QA Loop

Run a technical SVG check:

```bash
python scripts/svg_to_pptx/svg_quality_checker.py <output_dir>/pages
```

Generate PNG previews:

```bash
python scripts/svg_to_pptx/svg_to_png_preview.py <output_dir> --suffix "_preview"
```

Inspect the preview images before converting. Check:

- Layout overlap, text overflow, clipped chart labels, and inconsistent spacing.
- Meaningful use of the canvas with no large accidental blank areas.
- Alignment across rows, columns, cards, legends, and chart axes.
- Readable contrast and clear font hierarchy.
- Complete content with no placeholder text.

Fix the SVG and regenerate previews until the affected pages pass.

## Convert To PPTX

Convert the checked SVG pages:

```bash
python scripts/svg_to_pptx/svg_to_pptx.py <output_dir>
```

The default result is `<output_dir>/pages.pptx`. Verify the file exists and opens without repair. If conversion fails, keep the SVG files and report the failing command and error.

## Dependencies

Install the converter dependencies when needed:

```bash
pip install -r scripts/svg_to_pptx/requirements.txt
```
