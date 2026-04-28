# PPT Density Playbook

This playbook provides techniques for creating high-density, professional slides. High density means more information per slide without sacrificing readability or aesthetics.

## Core Principle: Mixed Layouts

**A professional slide is rarely just one thing.** Avoid "One-Grid Syndrome" where the entire slide is just a bulleted list.

**Goal:** Every slide should combine at least **3 different content types** to maximize information density and visual interest.

## Density Techniques (8 Methods)

### 1. KPI Stats & Callouts
Large numbers + small labels. Use at the top of a slide to summarize key metrics.
*   **PptxGenJS**: Use `fontSize: 36-48` for the number and `fontSize: 10-12` for the label.

### 2. Evidence Screenshots
Real screenshots of products, dashboards, or code provide more credibility than text descriptions.
*   **PptxGenJS**: Use `slide.addImage()` with a thin gray border (`line: { color: "CCCCCC", width: 1 }`).

### 3. Comparison Matrices (Tables)
Tables are naturally high-density. Use them for feature comparisons, multi-dimensional analysis, or status trackers.
*   **PptxGenJS**: Use alternating row fills and bold headers with brand colors.

### 4. SmartArt & Flowcharts
Visualizing a process with arrows is far superior to a numbered list.
*   **PptxGenJS**: Use `RECTANGLE` or `ROUNDED_RECTANGLE` for steps and `LINE` (with `endArrowType: 'triangle'`) for flow.

### 5. Summary/Takeaway Bar
A one-sentence conclusion that encapsulates the slide's purpose. Place it at the bottom or side in a highlighted box.
*   **PptxGenJS**: A full-width rectangle with light fill and bold text.

### 6. Sectional Zoning
Use background shapes to divide the slide into logical zones.
*   **PptxGenJS**: Use light gray (`F5F5F5`) or light red (`FEF2F2`) rectangles as background panels for specific sections.

### 7. Icon + Text Grids
Combines visual cues with text. Great for capability lists or feature sets.
*   **PptxGenJS**: Use a grid of 3-4 columns. Each item has an icon, a bold title, and 1-2 lines of description.

### 8. Multi-Level Information Hierarchy
Use distinct font sizes to signal importance.
*   **L1 (Title)**: 24pt Bold
*   **L2 (Sub-header)**: 14-16pt Bold
*   **L3 (Body)**: 10pt Regular
*   **L4 (Auxiliary/Gray)**: 9pt Regular
*   **L5 (Footnote)**: 8pt Regular Gray

---

## Spacing Rules for Density

| Element | Value (Inches) | Description |
|---------|----------------|-------------|
| **Page Margin** | 0.3" - 0.4" | Tighter margins = more content area |
| **Gutter/Gap** | 0.15" - 0.25" | Gap between cards or columns |
| **Card Padding** | 0.1" - 0.15" | Internal padding inside a card/box |
| **Section Gap** | 0.25" - 0.35" | Gap between major vertical layers |

---

## High-Density Page Archetypes

### 1. Strategic Overview / Capability Map
*   **Top**: KPI Stats (3-4 items)
*   **Middle**: Layered Architecture Diagram (3 layers: App, Platform, Infra)
*   **Bottom**: Comparison table vs competitors or previous version

### 2. Technical Deep-Dive / Process
*   **Top**: Goal/Objective summary bar
*   **Center**: Detailed horizontal flowchart (5-6 steps)
*   **Bottom**: Grid of 4 cards explaining "What happens under the hood"

### 3. Data Insight / Performance
*   **Top**: Key takeaway in large bold text
*   **Left**: Chart or Table with data
*   **Right**: List of 4-5 insights/observations
*   **Bottom**: Source & methodology footer

---

## Common Density Mistakes

1.  **"One-Slide-One-Idea" taken too literally**: Leading to sparse, wasteful slides.
2.  **Excessive Whitespace**: Leaving more than 20% of the usable area empty.
3.  **Monotonous Layouts**: Using the same 2-column layout for 20 slides in a row.
4.  **Low Information Ratio**: Using large 18pt font for body text, forcing you to cut 70% of the content.
5.  **Lack of Hierarchy**: Everything is the same font size, so nothing stands out.
