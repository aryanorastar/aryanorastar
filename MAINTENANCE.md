# Maintaining this profile

Native Markdown carries content and links; self-contained SVGs carry the header, workflow diagrams, project showcases, technology icons and contact/support controls. No badge server, tracking pixel, script, API key or scheduled workflow is required.

## Rebuild the SVGs

```sh
python3 -m venv .tools/venv
.tools/venv/bin/python -m pip install -r tools/requirements.txt
.tools/venv/bin/python tools/build_assets.py
```

Archivo comes from [Google Fonts](https://github.com/google/fonts/tree/main/ofl/archivo), with its SIL Open Font License in `assets/fonts/OFL.txt`. Lettering is converted to paths so GitHub need not fetch fonts. README text provides the accessible equivalent. The signal animation runs once, defaults to visible content and respects reduced motion.

## Evidence and counts

Refresh `assets/public-work.json`, the README alt text and date together, then rebuild the SVGs:

```sh
gh api -X GET search/issues -f q='repo:BasedHardware/omi author:aryanorastar is:pr is:merged' --jq .total_count
gh api -X GET search/issues -f q='author:aryanorastar is:pr is:merged is:public' --jq .total_count
```

Feature only public repositories. Verify authorship, merge state and scope before adding a contribution; credit collaborators. A merge does not prove deployment, adoption or customer recovery.

Technology marks are vendored from Simple Icons with their CC0 license under `assets/icons`. The header and workflow shapes are authored geometry, not product screenshots. The workflow illustrations explain engineering boundaries rather than claiming a particular production result.

## Support links

The public Wise link was supplied by Aryan. GitHub's Sponsors listing was verified public on 2026-10-31. Keep README buttons and `.github/FUNDING.yml` consistent. These are outbound support links; this repository never creates or processes a payment.

## Verification

Check SVG XML, image paths, readable mobile/desktop rendering, dark/light appearances, reduced motion, links and factual claims. Preserve a screenshot of major visual changes. Git history keeps earlier versions.
