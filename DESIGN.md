---
name: Aryan Gupta GitHub Profile
description: Connected engineering stories in self-contained SVG artwork and native GitHub Markdown.
colors:
  signal-mint: "#8FE3CF"
  verification-coral: "#FFAD94"
  campus-periwinkle: "#A9BFFF"
  ink-ground: "#0D1117"
  work-panel: "#141C26"
  header-ground: "#111A25"
  mira-ground: "#231F27"
  cloud-lettering: "#F1F5F9"
  supporting-text: "#B2C1D1"
  connector-edge: "#344357"
  email-ground: "#243C3C"
  linkedin-ground: "#243444"
  linkedin-lettering: "#D7E7F7"
  portfolio-ground: "#3F302E"
  portfolio-lettering: "#FFD0C0"
  wise-ground: "#9FE870"
  wise-lettering: "#163300"
  sponsors-ground: "#392C39"
  sponsors-lettering: "#F6CAE8"
typography:
  display:
    fontFamily: Archivo
    fontSize: "48px"
    fontWeight: 650
  display-mobile:
    fontFamily: Archivo
    fontSize: "39px"
    fontWeight: 650
  showcase-title:
    fontFamily: Archivo
    fontSize: "42px"
    fontWeight: 650
  project-title:
    fontFamily: Archivo
    fontSize: "28px"
    fontWeight: 600
  artwork-body:
    fontFamily: Archivo
    fontSize: "20px"
    fontWeight: 450
  diagram-label:
    fontFamily: Archivo
    fontSize: "17px"
    fontWeight: 450
  control-label:
    fontFamily: Archivo
    fontSize: "16px"
    fontWeight: 600
rounded:
  panel: "16px"
  control: "12px"
components:
  header:
    backgroundColor: "{colors.header-ground}"
    textColor: "{colors.cloud-lettering}"
    typography: "{typography.display}"
    rounded: "{rounded.panel}"
    width: "960px"
    height: "300px"
  header-mobile:
    backgroundColor: "{colors.header-ground}"
    textColor: "{colors.cloud-lettering}"
    typography: "{typography.display-mobile}"
    rounded: "{rounded.panel}"
    width: "480px"
    height: "282px"
  work-omi:
    backgroundColor: "{colors.work-panel}"
    textColor: "{colors.cloud-lettering}"
    typography: "{typography.showcase-title}"
    rounded: "{rounded.panel}"
    width: "960px"
    height: "248px"
  work-mira:
    backgroundColor: "{colors.mira-ground}"
    textColor: "{colors.cloud-lettering}"
    typography: "{typography.showcase-title}"
    rounded: "{rounded.panel}"
    width: "960px"
    height: "248px"
  project-panel:
    backgroundColor: "{colors.work-panel}"
    textColor: "{colors.cloud-lettering}"
    typography: "{typography.project-title}"
    rounded: "{rounded.panel}"
    width: "960px"
    height: "166px"
  contact-email:
    backgroundColor: "{colors.email-ground}"
    textColor: "{colors.signal-mint}"
    typography: "{typography.control-label}"
    rounded: "{rounded.control}"
    width: "154px"
    height: "46px"
  contact-linkedin:
    backgroundColor: "{colors.linkedin-ground}"
    textColor: "{colors.linkedin-lettering}"
    typography: "{typography.control-label}"
    rounded: "{rounded.control}"
    width: "154px"
    height: "46px"
  contact-portfolio:
    backgroundColor: "{colors.portfolio-ground}"
    textColor: "{colors.portfolio-lettering}"
    typography: "{typography.control-label}"
    rounded: "{rounded.control}"
    width: "154px"
    height: "46px"
  support-wise:
    backgroundColor: "{colors.wise-ground}"
    textColor: "{colors.wise-lettering}"
    typography: "{typography.control-label}"
    rounded: "{rounded.control}"
    width: "218px"
    height: "46px"
  support-github:
    backgroundColor: "{colors.sponsors-ground}"
    textColor: "{colors.sponsors-lettering}"
    typography: "{typography.control-label}"
    rounded: "{rounded.control}"
    width: "218px"
    height: "46px"
---

# Design System: Aryan Gupta GitHub Profile

## Overview

**Creative North Star: "The Connected Workbench"**

An ink-ground developer profile connects Aryan's identity to inspectable engineering work. Cloud lettering, seafoam paths and coral checkpoints carry a continuous visual language through the greeting, project stories, toolkit and contact controls. Distinct compositions give each project its own explanation within that shared language.

Artwork is authored vector geometry; reading content and interactions belong to GitHub. The two supplied developer-profile references inform visible work, activity and support discovery. Surface composition and the review record live in `.impeccable/surface.md`.

**Key Characteristics:**
- Outlined Archivo lettering and bundled icon geometry.
- Dark, self-contained artwork across GitHub appearances.
- Explanatory diagrams with distinct desktop and mobile compositions.
- Native Markdown evidence and ordinary linked images.

Extracted from `tools/build_assets.py`, `assets/*.svg` and `README.md` on 31 October 2026. V2's finish review permits the local preview, which Aryan accepted on 31 October 2026. Preview evidence uses GitHub Markdown API sanitized HTML in a local GitHub-style wrapper at desktop CSS width (1440px) and mobile width (390px). The local captures do not establish exact live GitHub surrounding layout; verify it when publishing. Light appearance and motion-preference behavior were not exercised.

## Colors

A dark neutral foundation supports two main signals; project and destination colors supply restrained local distinctions. The frontmatter owns the extracted values.

### Primary
- **Signal Mint** (`signal-mint`): agent/app paths, Omi and Astar details, the first activity figure and email lettering.

### Secondary
- **Verification Coral** (`verification-coral`): backend checkpoints, Mira, the lab's claim row and the second activity figure.
- **Campus Periwinkle** (`campus-periwinkle`): ThaparGo's map nodes and outbound arrow.

### Neutral
- **Ink Ground**, **Work Panel** and **Header Ground**: the toolkit base, project surfaces and greeting field.
- **Mira Ground**: a warmer dark surface distinguishing the support-assistant story.
- **Cloud Lettering** and **Supporting Text**: titles and primary statements versus descriptions and diagram labels.
- **Connector Edge**: quiet workflow paths, dividers and node outlines.

Contact and support color pairs are scoped to their matching controls. Wise retains its bright destination color; Sponsors uses plum and pink. The toolkit's individual icon tints and the header's mint-to-blue-to-coral route remain source-local artwork details, not a reusable semantic scale. Sidecar tonal ramps are panel aids, not additional shipped colors.

**The Contained Artwork Rule.** Keep dark fills inside each SVG; let GitHub control the surrounding page's appearance.

## Typography

**Artwork Font:** Archivo, bundled under the OFL, instantiated at width (100) with weights (450, 600, 650), and converted to filled glyph paths. The frontmatter gives representative source-canvas roles; the builder retains composition-specific sizes. These are solid glyph silhouettes, not stroked lettering.

The hierarchy moves from the compact greeting to showcase names, project titles, descriptions and small diagram labels. Mobile showcase names use a smaller size (38px); project titles use (27px). Native GitHub headings, prose, links and subtext provide the surrounding reading hierarchy. No custom body font, line-height scale or browser font fallback is shipped.

**The Native Reading Rule.** Use outlined Archivo inside SVGs and keep the inspectable narrative in native Markdown.

## Layout

A single GitHub README flow holds full-width artwork, short evidence paragraphs and linked controls. GitHub owns its outer container, spacing and wrapping. Canvas coordinates are not CSS display sizes, and there is no authored global spacing scale.

`<picture>` selects dedicated mobile artwork at a maximum viewport width (600px). The fallback is the desktop SVG. No light/dark asset switch is authored: every artwork contains its own dark surface.

| Artwork | Desktop canvas | Mobile canvas |
| --- | --- | --- |
| Greeting | 960 × 300px | 480 × 282px |
| Omi | 960 × 248px | 480 × 345px |
| Mira | 960 × 248px | 480 × 325px |
| Independent project | 960 × 166px | 480 × 232px |
| Toolkit | 960 × 112px | 480 × 230px |
| Activity | 960 × 150px | 480 × 230px |

Desktop stories pair a title/description with a diagram; Mira reverses the balance. Mobile repositions the same story vertically, the greeting route becomes horizontal, and eight toolkit items become two rows of four. Contact and support controls retain their intrinsic sizes and wrap through the host's normal inline flow.

## Elevation & Depth

No authored shadows, blur or lifted-card states. Tonal panels and subdued strokes separate content. The greeting's broad route underlay and narrow gradient path suggest a cable carrying a signal; this is diagram geometry rather than surface elevation.

## Shapes

Panels use gently rounded corners; linked controls use the smaller control radius. Circular nodes, rounded line caps and joins, narrow outbound arrows and simple device silhouettes share one geometric vocabulary. Most diagram strokes use widths (1–2.3px); the desktop greeting combines a route underlay (25px) with a signal path (3px). Preserve these as source-canvas proportions when artwork scales.

## Components

### Greeting and signal

The greeting connects labeled agent, app and backend nodes. A one-shot pulse runs for (4.8s) with `cubic-bezier(.16,1,.3,1)`, dash pattern (`8 992`) and offset (1000 to 0). It fades in and out, ending invisible. The source disables animation under `prefers-reduced-motion: reduce`; the complete static route and nodes remain. Local captures establish appearance, not verified playback or live GitHub preference handling.

### Work and project stories

Omi explains record/persist/recover; Mira presents source, answer and handoff principles. Astar joins screen, voice and tools. ThaparGo uses connected campus points. The lab juxtaposes claim and evidence and explicitly labels its trace synthetic. These illustrations explain workflows; they are not live product interfaces, operational status or proof of customer recovery. Artwork links to its repository; native text supplies contribution evidence and limits.

### Toolkit and activity

Eight bundled technology icons use individually tinted silhouettes and readable labels. Activity uses two dated figures with distinct accents and a source link. Counts remain snapshot data from `assets/public-work.json`; a visual count does not imply release or customer outcomes.

### Contact and support links

Five static SVG controls use an icon and outlined label. Each sits inside a real anchor with descriptive image alt text; the native link owns keyboard focus, hover and activation. These are linked images, not application buttons with custom selected, loading or disabled states. The profile has no authored forms, inputs or navigation shell.

All generated SVGs include a title and description, and README images carry equivalent alt text. Sidecar samples inline exact linked artwork and isolated node geometry with namespaced IDs; native anchors retain browser interaction behavior. The panel is an asset specimen, not a reproduction of GitHub's page CSS.

## Do's and Don'ts

### Do:
- Do regenerate artwork from `tools/build_assets.py` and preserve equivalent alt text.
- Do preserve dedicated mobile compositions and the source reduced-motion rule.
- Do keep public evidence and factual limits readable in native Markdown.
- Do label explanatory workflows and synthetic comparisons honestly.

### Don't:
- Don't interpret merged code counts as release or customer outcomes.
- Don't add remote widget or runtime font dependencies to the artwork.
- Don't invent custom form, navigation or interaction states that GitHub cannot render.
- Don't present the local wrapper preview as verified live GitHub behavior or publication.
