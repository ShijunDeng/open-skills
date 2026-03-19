---
name: pptx
description: "Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill."
license: Proprietary. LICENSE.txt has complete terms
---

# PPTX Skill

## Quick Reference

| Task | Guide |
|------|-------|
| Read/analyze content | `python -m markitdown presentation.pptx` |
| Edit or create from template | Read [editing.md](editing.md) |
| Create from scratch | Read [pptxgenjs.md](pptxgenjs.md) |

---

## Reading Content

```bash
# Text extraction
python -m markitdown presentation.pptx

# Visual overview
python scripts/thumbnail.py presentation.pptx

# Raw XML
python scripts/office/unpack.py presentation.pptx unpacked/
```

---

## Editing Workflow

**Read [editing.md](editing.md) for full details.**

1. Analyze template with `thumbnail.py`
2. Unpack → manipulate slides → edit content → clean → pack

---

## Creating from Scratch

**Read [pptxgenjs.md](pptxgenjs.md) for full details.**

Use when no template or reference presentation is available.

---

## Design System: Red / White / Gray

The default visual style is **white background + red accents + gray text hierarchy**. This produces clean, professional slides that work for both technical and executive audiences.

### Color Tokens

| Role | Hex | Usage |
|------|-----|-------|
| **Slide background** | `FFFFFF` | All content slides |
| **Primary red** | `C0392B` | Header bars, accent borders, callout highlights, icons |
| **Dark title text** | `1A1A1A` | Slide titles, section headers |
| **Body text** | `333333` | All body copy, bullet points |
| **Secondary text** | `666666` | Captions, source lines, sub-bullets |
| **Divider / border** | `CCCCCC` | Table borders, card outlines, separator lines |
| **Light background** | `F5F5F5` | Alternating table rows, card fills, callout boxes |
| **Red panel bg** | `C0392B` | Left-side accent panels, header bars only — never full slide |

**Applying the system in PptxGenJS:**
```javascript
// ALL slides — title, content, closing — use white background
slide.background = { color: "FFFFFF" };

// Header bar (left-side accent or top bar)
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0, y: 0, w: 13.3, h: 0.6,
  fill: { color: "C0392B" }, line: { color: "C0392B" }
});
slide.addText("SLIDE TITLE", { x: 0.4, y: 0.1, w: 12, h: 0.4,
  fontSize: 24, bold: true, color: "FFFFFF", fontFace: "Microsoft YaHei" });

// Card with gray fill and red left accent
slide.addShape(pres.shapes.RECTANGLE, { x: 0.4, y: 1.0, w: 5.8, h: 2.0,
  fill: { color: "F5F5F5" }, line: { color: "CCCCCC", width: 0.5 }});
slide.addShape(pres.shapes.RECTANGLE, { x: 0.4, y: 1.0, w: 0.08, h: 2.0,
  fill: { color: "C0392B" }, line: { color: "C0392B" }});
```

**Other palettes:** When the user specifies a different color scheme, follow their preference. The red/white/gray system is the default when nothing is specified.

---

## Design Ideas

**Don't create boring slides.** Plain bullets on a white background won't impress anyone. Consider ideas from this list for each slide.

### Before Starting

- **Apply the red/white/gray system** by default (see above). White backgrounds on ALL slides — including title, section dividers, and closing slides. Red is strictly an accent (header bars, card borders, icons), never a full-slide background.
- **Dominance over equality**: White dominates (backgrounds everywhere), red is a sharp accent (max 15% of any slide), gray structures typography hierarchy. This produces clean, professional decks that are easy to read and print.
- **No dark backgrounds**: Do not use `1A1A1A`, `000000`, or any dark color as a slide background — not even on title or closing slides. A red left-panel + white right-panel title slide looks far more professional than a full-black slide, and avoids the "corporate deck circa 2010" feel.
- **Commit to a visual motif**: Pick ONE distinctive element and repeat it — left red accent bars on all cards, red circle icons, thick red top border. Carry it across every slide.

### For Each Slide

**Every slide needs a visual element** — image, chart, icon, or shape. Text-only slides are forgettable.

**Title slide layout (white background):**
- Left 30-40% column: light gray fill (`F5F5F5`) or red fill (`C0392B`) as a narrow accent panel; right 60-70%: white with title text
- OR: Full white background with large red header bar at top, title text below
- Never fill the entire slide with a dark or black color

**Layout options:**
- Two-column (text left, illustration on right) — use red accent borders on cards
- Icon + text rows (icon in red circle, bold header in dark gray, description below)
- 2x2 or 2x3 grid (image on one side, grid of content blocks on other)
- Half-bleed panel (narrow red left panel ~30% width with white text, white right panel with content)

**Data display:**
- Large stat callouts (big numbers 60-72pt in red with gray label below)
- Comparison columns (before/after, pros/cons) with red header bar on each column
- Timeline or process flow (red numbered circles, gray connector lines)

**Visual polish:**
- Icons in red circles next to section headers
- Italic accent text for key stats or taglines (in secondary gray `666666`)

### Typography

**Recommended font:** Microsoft YaHei (微软雅黑) for all text. Bold weight for titles, Regular for body. Falls back to Arial on systems without CJK fonts.

| Element | Size | Weight | Color |
|---------|------|--------|-------|
| Slide title (main heading) | 24pt | Bold | `FFFFFF` on red bar, or `1A1A1A` on white |
| Section header / subtitle | 18pt | Bold | `1A1A1A` |
| Body text / bullets | 10pt | Regular | `333333` |
| Sub-bullets / secondary | 9pt | Regular | `666666` |
| Captions / source / footnote | 8pt | Regular | `666666` |
| Large callout numbers | 36-48pt | Bold | `C0392B` |

**Why 10pt body text:** At 10pt with Microsoft YaHei, a single slide can hold 8-12 bullet points or a 10-row table without feeling cramped. This maximizes information density per slide — the audience reads the deck, not squints at it. Pair with tight line spacing (1.0-1.1x) and `paraSpaceAfter: 2` for maximum density.

**Font setup in PptxGenJS:**
```javascript
const FONT = "Microsoft YaHei";  // or "微软雅黑"
// Use this for ALL addText calls: fontFace: FONT
```

### Content Density

**Target: substantive slides, not sparse ones.** A slide with 2 bullet points and a lot of whitespace wastes the audience's time. Aim for:

- **Bullet lists**: 8-12 items per slide at 10pt with `paraSpaceAfter: 2` and `lineSpacingMultiple: 1.0`; use sub-bullets at 9pt for detail
- **Tables**: 8-12 rows with headers is readable at 10pt; don't limit to 4 rows when 10 rows fit
- **Cards/columns**: 3-4 cards per row at LAYOUT_WIDE (13.3") is fine; 2 cards per row leaves too much empty space
- **Multi-level content**: Use sub-bullets (indentLevel: 1, fontSize: 9) to add depth without adding slides
- **Combine related items**: If two mini-topics naturally live together (e.g., context + implication), put them on one split slide rather than two sparse slides

```javascript
// Compact bullet list — 8+ items at 10pt, tight spacing
slide.addText([
  { text: "Item one with specific detail", options: { bullet: true, breakLine: true, fontSize: 10, color: "333333" } },
  { text: "Item two with data point — 42% improvement", options: { bullet: true, breakLine: true, fontSize: 10, color: "333333" } },
  { text: "Sub-detail supporting item two", options: { bullet: true, indentLevel: 1, breakLine: true, fontSize: 9, color: "666666" } },
  // ...
], { x: 0.4, y: 0.8, w: 12.5, h: 4.5, paraSpaceAfter: 2, lineSpacingMultiple: 1.0, fontFace: "Microsoft YaHei" });
```

### Spacing

- 0.3-0.4" margins (tighter margins = more usable content area)
- 0.2-0.3" between content blocks
- Don't pad every block — if content needs the space, use it; if it doesn't, shrink the gap

### Diagrams with Draw.io

**When the content is a system, process, or flow — draw it, don't describe it.**

Architecture diagrams, data flow charts, deployment topologies, onboarding sequences, org charts, and swim lane processes are all much clearer as diagrams than as bullet points. When the source document contains this kind of content, create a diagram using the draw.io MCP and embed it as an image.

**Use the draw.io MCP tools:**
- `mcp__drawio__open_drawio_mermaid` — for flowcharts, sequence diagrams, state machines (write Mermaid syntax)
- `mcp__drawio__open_drawio_xml` — for architecture diagrams with custom shapes and layout (write draw.io XML)
- `mcp__drawio__open_drawio_csv` — for org charts or structured node graphs from tabular data

**Workflow:**
1. Identify diagram-worthy content (architecture, flow, topology, process)
2. Open diagram in draw.io MCP — create meaningful content, not placeholder shapes
3. Export to PNG: `drawio -x -f png -o /tmp/diagram.png diagram.xml` (if `drawio` CLI available)
4. Embed in slide: `slide.addImage({ path: "/tmp/diagram.png", x: 0.4, y: 1.0, w: 12.5, h: 4.5 })`

**If the draw.io CLI (`drawio`) is not available:** Create the diagram via MCP and tell the user the diagram was generated — they can open the draw.io file and export manually. Fall back to a PptxGenJS-drawn approximation (shapes + connectors) only if the diagram is simple enough to represent accurately.

**Good candidates for draw.io diagrams:**
- Microservices architecture (services, APIs, databases)
- CI/CD pipeline or deployment flow
- User onboarding / product journey
- Data pipeline (ingestion → processing → storage → serving)
- Before/after system topology

**Not worth drawing:** Simple lists of steps that read fine as numbered bullets; small 2-3 node flows that are clearer as a PptxGenJS process flow shape.

### Native Diagram Patterns (PptxGenJS)

When draw.io is unavailable or the diagram is better expressed inline, use these PptxGenJS patterns. These are the go-to approaches for architecture content, system overviews, and planning slides — they produce far more professional results than bullet lists or plain cards.

**When to use which pattern:**
- **Layered Architecture**: System has distinct tiers/layers with data flowing between them (e.g., frontend → API → database, or application → transport → platform). The layers are conceptually stacked or sequential.
- **Component Diagram**: System has multiple components/services that interact in non-linear ways (e.g., microservices, module dependencies). Components live within containers or boundaries.
- **Roadmap / Timeline**: Content describes phases, milestones, or quarterly plans. Horizontal progression communicates chronological flow better than vertical lists.

#### Layered Architecture Diagram

For systems with distinct tiers flowing top-to-bottom or left-to-right. Each layer gets a colored header, internal components, and directional arrows between layers.

```javascript
// === LAYERED ARCHITECTURE — vertical stack (3 layers) ===
// Adapt layerCount, colors, and component items to your content.
const layers = [
  { label: "Application Layer", sublabel: "Trace Instrumentation",
    color: "C0392B", components: ["ADK Auto-Instrument", "Custom SDK", "Platform Hook"] },
  { label: "Transport Layer", sublabel: "Protocol Conversion",
    color: "E67E22", components: ["Schema Mapping", "OTel Collector", "Batch & Retry"] },
  { label: "Platform Layer", sublabel: "Storage / Analysis",
    color: "2980B9", components: ["ClickHouse Store", "Analysis Engine", "Eval Pipeline"] }
];

const diagramX = 0.4, diagramY = 1.0, totalW = 12.5;
const layerH = 1.4, layerGap = 0.35; // gap includes arrow space

layers.forEach((layer, i) => {
  const ly = diagramY + i * (layerH + layerGap);

  // Layer background
  slide.addShape(pres.shapes.RECTANGLE, {
    x: diagramX, y: ly, w: totalW, h: layerH,
    fill: { color: "F5F5F5" }, line: { color: "E0E0E0", width: 0.5 }
  });
  // Colored left accent bar
  slide.addShape(pres.shapes.RECTANGLE, {
    x: diagramX, y: ly, w: 0.08, h: layerH,
    fill: { color: layer.color }, line: { color: layer.color }
  });
  // Layer title
  slide.addText(layer.label, {
    x: diagramX + 0.2, y: ly + 0.08, w: 2.5, h: 0.28,
    fontSize: 12, bold: true, color: layer.color, fontFace: "Microsoft YaHei", margin: 0
  });
  slide.addText(layer.sublabel, {
    x: diagramX + 0.2, y: ly + 0.36, w: 2.5, h: 0.22,
    fontSize: 9, italic: true, color: "666666", fontFace: "Microsoft YaHei", margin: 0
  });

  // Component boxes — evenly spaced inside the layer
  const compStartX = diagramX + 2.8;
  const compW = (totalW - 3.2) / layer.components.length - 0.15;
  layer.components.forEach((comp, j) => {
    const cx = compStartX + j * (compW + 0.15);
    slide.addShape(pres.shapes.RECTANGLE, {
      x: cx, y: ly + 0.2, w: compW, h: layerH - 0.4,
      fill: { color: "FFFFFF" }, line: { color: layer.color, width: 1 }
    });
    slide.addText(comp, {
      x: cx + 0.08, y: ly + 0.2, w: compW - 0.16, h: layerH - 0.4,
      fontSize: 10, color: "333333", align: "center", valign: "middle",
      fontFace: "Microsoft YaHei", margin: 0
    });
  });

  // Down-arrow between layers
  if (i < layers.length - 1) {
    const arrowY = ly + layerH + 0.04;
    slide.addText("▼", {
      x: diagramX + totalW / 2 - 0.15, y: arrowY, w: 0.3, h: 0.25,
      fontSize: 14, color: "999999", align: "center", valign: "middle", margin: 0
    });
  }
});
```

**Variations:**
- Horizontal layout (left-to-right): swap x/y math, use `▶` arrows
- Add a "data flow" label on the arrow: place small text next to the arrow symbol
- Highlight one layer: use a bolder border or light-tinted fill to draw attention

#### Component Diagram

For systems where multiple components interact within boundaries/containers. Uses a container box with titled header, internal component boxes, and connector lines.

```javascript
// === COMPONENT DIAGRAM — container with sub-components ===
function drawContainer(slide, pres, opts) {
  const { x, y, w, h, title, color, components } = opts;
  // Container border
  slide.addShape(pres.shapes.RECTANGLE, {
    x, y, w, h,
    fill: { color: "FAFAFA" }, line: { color: color, width: 1.5, dashType: "dash" }
  });
  // Container header bar
  slide.addShape(pres.shapes.RECTANGLE, {
    x, y, w, h: 0.35,
    fill: { color: color }, line: { color: color }
  });
  slide.addText(title, {
    x: x + 0.12, y: y + 0.04, w: w - 0.24, h: 0.28,
    fontSize: 11, bold: true, color: "FFFFFF", fontFace: "Microsoft YaHei", margin: 0
  });
  // Internal component boxes (auto-grid)
  const cols = Math.min(components.length, 3);
  const rows = Math.ceil(components.length / cols);
  const boxW = (w - 0.4 - (cols - 1) * 0.12) / cols;
  const boxH = (h - 0.55 - (rows - 1) * 0.1) / rows;
  components.forEach((comp, i) => {
    const col = i % cols, row = Math.floor(i / cols);
    const bx = x + 0.2 + col * (boxW + 0.12);
    const by = y + 0.45 + row * (boxH + 0.1);
    slide.addShape(pres.shapes.RECTANGLE, {
      x: bx, y: by, w: boxW, h: boxH,
      fill: { color: "FFFFFF" }, line: { color: "CCCCCC", width: 0.75 }
    });
    // Thin colored top accent
    slide.addShape(pres.shapes.RECTANGLE, {
      x: bx, y: by, w: boxW, h: 0.04,
      fill: { color: color }, line: { color: color }
    });
    slide.addText(comp, {
      x: bx + 0.06, y: by + 0.06, w: boxW - 0.12, h: boxH - 0.12,
      fontSize: 9, color: "333333", align: "center", valign: "middle",
      fontFace: "Microsoft YaHei", margin: 0
    });
  });
}

// Usage: draw two containers side by side with an arrow between them
drawContainer(slide, pres, {
  x: 0.4, y: 1.0, w: 5.5, h: 3.0, title: "Agent Runtime",
  color: "C0392B", components: ["Planner", "Tool Executor", "Memory Manager", "LLM Client"]
});
drawContainer(slide, pres, {
  x: 7.4, y: 1.0, w: 5.5, h: 3.0, title: "Observability Platform",
  color: "2980B9", components: ["Trace Store", "Analysis Engine", "Eval Pipeline", "Dashboard"]
});
// Connector arrow between containers
slide.addShape(pres.shapes.LINE, {
  x: 5.9, y: 2.5, w: 1.5, h: 0, line: { color: "999999", width: 1.5, dashType: "dash" }
});
slide.addText("OTLP", {
  x: 6.1, y: 2.15, w: 1.1, h: 0.25,
  fontSize: 8, color: "999999", align: "center", italic: true, margin: 0
});
```

#### Roadmap / Timeline Diagram

For quarterly plans, phased rollouts, or milestone-based planning. Uses a horizontal swim-lane style with phase badges, milestones, and a connecting timeline bar.

```javascript
// === ROADMAP — horizontal timeline with phases ===
const phases = [
  { label: "Q1 2026", title: "Foundation",
    color: "C0392B", milestones: ["Core SDK", "OTel Collector", "Storage Setup"] },
  { label: "Q2 2026", title: "Expansion",
    color: "E67E22", milestones: ["Custom SDK", "Platform Integration", "Eval Engine", "Dashboard"] },
  { label: "Q3 2026", title: "Scale & Optimize",
    color: "2980B9", milestones: ["Memory Loop", "Self-Evolution", "Full Rollout", "Metrics System"] }
];

const rmX = 0.4, rmY = 1.2, rmW = 12.5;
const phaseW = (rmW - (phases.length - 1) * 0.2) / phases.length;
const rmH = 4.5;

// Horizontal timeline bar (the visual spine connecting all phases)
slide.addShape(pres.shapes.RECTANGLE, {
  x: rmX, y: rmY + 0.55, w: rmW, h: 0.06,
  fill: { color: "CCCCCC" }, line: { color: "CCCCCC" }
});

phases.forEach((phase, i) => {
  const px = rmX + i * (phaseW + 0.2);

  // Phase badge (colored pill on the timeline bar)
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: px + phaseW / 2 - 0.55, y: rmY, w: 1.1, h: 0.35,
    fill: { color: phase.color }, rectRadius: 0.06, line: { color: phase.color }
  });
  slide.addText(phase.label, {
    x: px + phaseW / 2 - 0.55, y: rmY, w: 1.1, h: 0.35,
    fontSize: 10, bold: true, color: "FFFFFF", align: "center", valign: "middle",
    fontFace: "Microsoft YaHei", margin: 0
  });

  // Timeline dot (circle sitting on the bar)
  slide.addShape(pres.shapes.OVAL, {
    x: px + phaseW / 2 - 0.08, y: rmY + 0.48, w: 0.2, h: 0.2,
    fill: { color: phase.color }, line: { color: "FFFFFF", width: 2 }
  });

  // Phase content card (hanging below the timeline)
  const cardY = rmY + 0.85;
  const cardH = rmH - 0.85;
  slide.addShape(pres.shapes.RECTANGLE, {
    x: px, y: cardY, w: phaseW, h: cardH,
    fill: { color: "F9F9F9" }, line: { color: "E0E0E0", width: 0.5 }
  });
  // Colored top border on card
  slide.addShape(pres.shapes.RECTANGLE, {
    x: px, y: cardY, w: phaseW, h: 0.05,
    fill: { color: phase.color }, line: { color: phase.color }
  });
  // Phase title
  slide.addText(phase.title, {
    x: px + 0.15, y: cardY + 0.12, w: phaseW - 0.3, h: 0.3,
    fontSize: 12, bold: true, color: "1A1A1A", fontFace: "Microsoft YaHei", margin: 0
  });
  // Milestone items
  const msText = phase.milestones.map(m => ({
    text: m, options: { bullet: true, breakLine: true, fontSize: 10, color: "333333" }
  }));
  slide.addText(msText, {
    x: px + 0.15, y: cardY + 0.45, w: phaseW - 0.3, h: cardH - 0.6,
    fontFace: "Microsoft YaHei", lineSpacingMultiple: 1.3, valign: "top", margin: 0,
    paraSpaceAfter: 4
  });
});
```

**Variations:**
- **Vertical roadmap**: Stack phases top-to-bottom with a vertical timeline bar on the left
- **Gantt-style**: Add horizontal bars showing duration, with overlapping phases
- **Milestone markers**: Replace bullets with checkmark icons for completed items, circles for upcoming

#### Extreme Complex Diagram Reconstruction (极复杂图)

For highly complex diagrams (e.g., system architecture + business flywheels + cross-cutting connections), do not attempt to draw them as static images. Use a **data-driven reconstruction** approach. This ensures every component remains editable in PowerPoint while maintaining perfect alignment.

**Key Strategy:**
1.  **Define a Color/Font Palette**: Centralize styles for consistency.
2.  **Structural Data Objects**: Map the diagram's logic (layers, steps, connections) into JSON-like structures.
3.  **Programmable Loops**: Use `forEach` to render repetitive elements (boxes, labels, arrows).
4.  **Native Connectors**: Use `pres.shapes.ARC` for loops and `LINE` for inter-container relationships.

```javascript
// Example: Complex Architecture + Flywheel
const layers = [
  { title: "Layer 1", color: "C0392B", components: ["A", "B", "C"] },
  { title: "Layer 2", color: "E67E22", components: ["D", "E", "F"] }
];

layers.forEach((layer, i) => {
  const ly = 1.2 + i * 1.6;
  // 1. Render Layer Container
  slide.addShape(pres.shapes.RECTANGLE, {
    x: 0.5, y: ly, w: 7.5, h: 1.2, fill: { color: layer.color }, rectRadius: 0.05
  });
  // 2. Render Components inside Layer
  layer.components.forEach((comp, j) => {
    const cx = 0.8 + j * 2.4;
    slide.addShape(pres.shapes.RECTANGLE, {
      x: cx, y: ly + 0.4, w: 2.1, h: 0.6, fill: { color: "FFFFFF" }
    });
    slide.addText(comp, { x: cx, y: ly + 0.4, w: 2.1, h: 0.6, align: "center" });
  });
});

// 3. Render Complex Loop (Flywheel) using ARC
slide.addShape(pres.shapes.ARC, {
  x: 9.0, y: 1.5, w: 1.5, h: 4.0, angleRange: [270, 90],
  line: { color: "82B366", width: 2, endArrowType: "triangle" }
});
```

### Avoid (Common Mistakes)

- **Don't repeat the same layout** — vary columns, cards, and callouts across slides
- **Don't center body text** — left-align paragraphs and lists; center only titles and callout numbers
- **Don't skimp on size contrast** — titles at 24pt in header bar, subtitles 18pt, body at 10pt; the gap signals hierarchy
- **Don't over-pad sparse slides** — 2 bullets padded to fill a slide is worse than 10 compact bullets that actually inform
- **Don't mix spacing randomly** — choose 0.2" or 0.3" gaps and use consistently
- **Don't use dark/black slide backgrounds** — not on title slides, not on closing slides, not anywhere. `1A1A1A` or `000000` backgrounds look dated and make text harder to read. Use white (`FFFFFF`) everywhere; add a red top bar or left panel for visual interest instead.
- **Don't style one slide and leave the rest plain** — commit fully to red/white/gray throughout
- **Don't create text-only slides** — add diagram, chart, icon grid, or card layout; avoid plain title + bullets
- **Don't forget text box padding** — when aligning shapes with text edges, set `margin: 0` on the text box
- **Don't use low-contrast elements** — icons and text need strong contrast; `666666` on `FFFFFF` is OK, `CCCCCC` on `FFFFFF` is not
- **NEVER use accent lines under titles** — these are a hallmark of AI-generated slides; use the red header bar or card border instead

---

## QA (Required)

**Assume there are problems. Your job is to find them.**

Your first render is almost never correct. Approach QA as a bug hunt, not a confirmation step. If you found zero issues on first inspection, you weren't looking hard enough.

### Content QA

```bash
python -m markitdown output.pptx
```

Check for missing content, typos, wrong order.

**When using templates, check for leftover placeholder text:**

```bash
python -m markitdown output.pptx | grep -iE "xxxx|lorem|ipsum|this.*(page|slide).*layout"
```

If grep returns results, fix them before declaring success.

### Visual QA

**⚠️ USE SUBAGENTS** — even for 2-3 slides. You've been staring at the code and will see what you expect, not what's there. Subagents have fresh eyes.

Convert slides to images (see [Converting to Images](#converting-to-images)), then use this prompt:

```
Visually inspect these slides. Assume there are issues — find them.

Look for:
- Overlapping elements (text through shapes, lines through words, stacked elements)
- Text overflow or cut off at edges/box boundaries
- Decorative lines positioned for single-line text but title wrapped to two lines
- Source citations or footers colliding with content above
- Elements too close (< 0.3" gaps) or cards/sections nearly touching
- Uneven gaps (large empty area in one place, cramped in another)
- Insufficient margin from slide edges (< 0.5")
- Columns or similar elements not aligned consistently
- Low-contrast text (e.g., light gray text on cream-colored background)
- Low-contrast icons (e.g., dark icons on dark backgrounds without a contrasting circle)
- Text boxes too narrow causing excessive wrapping
- Leftover placeholder content

For each slide, list issues or areas of concern, even if minor.

Read and analyze these images:
1. /path/to/slide-01.jpg (Expected: [brief description])
2. /path/to/slide-02.jpg (Expected: [brief description])

Report ALL issues found, including minor ones.
```

### Verification Loop

1. Generate slides → Convert to images → Inspect
2. **List issues found** (if none found, look again more critically)
3. Fix issues
4. **Re-verify affected slides** — one fix often creates another problem
5. Repeat until a full pass reveals no new issues

**Do not declare success until you've completed at least one fix-and-verify cycle.**

---

## Converting to Images

Convert presentations to individual slide images for visual inspection:

```bash
python scripts/office/soffice.py --headless --convert-to pdf output.pptx
pdftoppm -jpeg -r 150 output.pdf slide
```

This creates `slide-01.jpg`, `slide-02.jpg`, etc.

To re-render specific slides after fixes:

```bash
pdftoppm -jpeg -r 150 -f N -l N output.pdf slide-fixed
```

---

## Dependencies

- `pip install "markitdown[pptx]"` - text extraction
- `pip install Pillow` - thumbnail grids
- `npm install -g pptxgenjs` - creating from scratch
- LibreOffice (`soffice`) - PDF conversion (auto-configured for sandboxed environments via `scripts/office/soffice.py`)
- Poppler (`pdftoppm`) - PDF to images
