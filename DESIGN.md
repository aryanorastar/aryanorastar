---
name: Aryan Gupta GitHub Profile
description: Outlined typographic identity with native GitHub reading surfaces.
colors:
  cobalt-nameplate: "#263FE8"
  cobalt-nameplate-dark: "#1D2FD0"
  mint-signal: "#D8F5B1"
  ivory-lettering: "#F7F9F2"
  support-ink: "#14200D"
typography:
  display:
    fontFamily: Archivo
    fontSize: "238px"
    fontWeight: 850
  display-mobile:
    fontFamily: Archivo
    fontSize: "130px"
    fontWeight: 850
  label:
    fontFamily: Archivo
    fontSize: "24px"
    fontWeight: 850
  label-mobile-footer:
    fontFamily: Archivo
    fontSize: "22px"
    fontWeight: 850
  support-label:
    fontFamily: Archivo
    fontSize: "25px"
    fontWeight: 850
rounded:
  square: "0px"
components:
  masthead-desktop:
    backgroundColor: "{colors.cobalt-nameplate}"
    textColor: "{colors.ivory-lettering}"
    typography: "{typography.display}"
    rounded: "{rounded.square}"
    width: "1200px"
    height: "470px"
  masthead-desktop-dark:
    backgroundColor: "{colors.cobalt-nameplate-dark}"
    textColor: "{colors.ivory-lettering}"
    typography: "{typography.display}"
    rounded: "{rounded.square}"
    width: "1200px"
    height: "470px"
  masthead-mobile:
    backgroundColor: "{colors.cobalt-nameplate}"
    textColor: "{colors.ivory-lettering}"
    typography: "{typography.display-mobile}"
    rounded: "{rounded.square}"
    width: "480px"
    height: "480px"
  masthead-mobile-dark:
    backgroundColor: "{colors.cobalt-nameplate-dark}"
    textColor: "{colors.ivory-lettering}"
    typography: "{typography.display-mobile}"
    rounded: "{rounded.square}"
    width: "480px"
    height: "480px"
  support-wise:
    backgroundColor: "{colors.mint-signal}"
    textColor: "{colors.support-ink}"
    typography: "{typography.support-label}"
    rounded: "{rounded.square}"
    width: "224px"
    height: "49px"
  support-github:
    backgroundColor: "{colors.cobalt-nameplate}"
    textColor: "{colors.ivory-lettering}"
    typography: "{typography.support-label}"
    rounded: "{rounded.square}"
    width: "224px"
    height: "49px"
---

# Design System: Aryan Gupta GitHub Profile

## Overview

**Creative North Star: "The Type Specimen"**

A confident typographic identity sits inside GitHub's familiar reading surface. Large outlined Archivo lettering, cobalt fields and an open mint mark establish recognition; the surrounding Markdown lets visitors inspect work and follow direct links with little visual friction.

The system is flat, graphic and self-contained. Vector geometry supplies the identity; GitHub supplies reading typography, spacing and interaction states. The implemented surface composition remains in `.impeccable/surface.md`.

**Key Characteristics:**
- Outlined lettering with no remote font dependency.
- Cobalt, ivory and mint with explicit light and dark asset variants.
- Separate desktop and mobile artwork.
- Native GitHub reading and interaction patterns.

Extracted from `tools/build_assets.py` and `README.md` on 31 October 2026. The initial identity's independent finish-review handoff was **ship**, covering source and actual GitHub desktop/mobile dark captures. Light variants and subsequent support-link additions are documented from source; this document does not claim their rendered verification or broader website certification.

## Colors

Saturated cobalt carries the identity, pale mint marks the signal, and warm ivory carries the lettering.

### Primary
- **Specimen Cobalt** (`cobalt-nameplate`): default/light nameplate and GitHub support-link field.
- **Night Cobalt** (`cobalt-nameplate-dark`): nameplate field for the dark asset.

### Secondary
- **Signal Mint** (`mint-signal`): open geometric marks, selected role/footer lettering and the Wise support-link field.

### Neutral
- **Lettering Ivory** (`ivory-lettering`): identity lettering, the thin signal trace and GitHub support-link lettering/arrow.
- **Support Ink** (`support-ink`): Wise support-link lettering and arrow on mint.

**The Palette Roles Rule.** Keep both nameplate variants tied to their source tokens; GitHub owns surrounding content colors.

The sidecar's tonal ramps are synthesized panel swatches, not additional shipped palette tokens.

## Typography

**Display Font:** Archivo, bundled under the OFL and instantiated at width (100), then converted to filled SVG paths. The frontmatter sizes are builder inputs; `max_width` may reduce the effective scale to fit the artwork. These are solid glyph outlines, not stroked letterforms.

**Body Font:** GitHub's native rendered Markdown typography. No custom body family, scale, line height or spacing tokens are authored here.

The desktop and mobile display roles establish identity. The identity label roles carry the uppercase role and subject line; the support label uses mixed-case lettering. Native Markdown headings, paragraphs, emphasis and subtext establish the reading hierarchy below the artwork.

**The Native Reading Rule.** Use outlined Archivo only inside authored SVGs; leave reading text, link interaction and spacing to GitHub.

## Layout

The nameplate uses the intrinsic dimensions in the component tokens and scales with the README image. Desktop lettering is staggered; mobile uses its own square composition. The `<picture>` sources select mobile artwork at a maximum viewport width (600px), with the combined dark/mobile source evaluated first. Dark desktop selection follows; the default asset is the fallback.

Below the identity, a single Markdown flow uses headings, short paragraphs, direct links, subtext and one native disclosure. GitHub controls the outer container and reading rhythm. There is no authored grid or reusable spacing scale to extract.

## Elevation & Depth

No custom shadows, gradients or elevation layers. Solid fields, scale, position and negative space establish hierarchy. GitHub controls the surrounding page surface.

## Shapes

The identity and support graphics have square edges. The signature mark uses six separate radial strokes, square line caps, an open center at a fraction of the radius (0.24), and a stroke width proportional to the radius (0.20). Desktop repeats the mark at different scales; mobile uses one.

**The Open Mark Rule.** Keep the center open and the six square-ended rays separate.

## Components

### Nameplate

A self-contained SVG image, with four generated variants: desktop/mobile and default/dark. Each carries a title and description; the README image supplies equivalent descriptive alt text. Lettering is geometry and needs no runtime font request. Regenerate all variants from the shared builder.

### Signal trace

A thin ivory line passes through one mark. Its stroke width (2px), dash pattern (`0 28 250 28`) and offset change (278 to 0) create one trace over a duration (5s), using `cubic-bezier(.16,1,.3,1)`. Reduced-motion preference disables the animation. Motion is source-defined; static dark captures establish appearance, not playback behavior.

### Native reading patterns

Navigation is a line of ordinary links, including a support-section anchor. Evidence entries use native headings, linked titles, paragraphs and subtext. Additional work uses `<details>` and `<summary>`. Contact paths remain text links. Their hover, focus and expanded states are host/browser behavior.

### Support links

Two generated SVG link graphics reuse the identity's palette and square geometry. Their source canvas (320 × 70px) contains outlined Archivo lettering and an outbound arrow with a stroke width (2.5px). The README renders each at the component dimensions above inside a real outbound anchor with descriptive image alt text. Wise pairs mint with Support Ink; GitHub Sponsors pairs cobalt with ivory. Both remain static and share the same artwork across appearances. Anchor hover and focus behavior belongs to GitHub.

The sidecar renders exact dark masthead geometry, isolated mark/trace excerpts and the support graphics. It does not approximate GitHub's CSS or claim that the panel reproduces the full profile.

## Do's and Don'ts

### Do:
- Do regenerate identity and support SVGs from `tools/build_assets.py`.
- Do preserve the mobile artwork selection and descriptive text alternatives.
- Do keep reading content in native Markdown with direct, inspectable links.

### Don't:
- Don't add remote font or widget dependencies to the identity.
- Don't treat preview tonal ramps as additional shipped colors.
- Don't replace native body typography with outlined display lettering.
