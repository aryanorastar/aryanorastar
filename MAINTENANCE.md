# Maintaining this profile

Native Markdown carries content and links; self-contained SVGs carry the nameplate. No badge server, tracking pixel, script, API key or scheduled workflow is required.

## Rebuild the SVGs

```sh
python3 -m venv .tools/venv
.tools/venv/bin/python -m pip install -r tools/requirements.txt
.tools/venv/bin/python tools/build_assets.py
```

Archivo comes from [Google Fonts](https://github.com/google/fonts/tree/main/ofl/archivo), with its SIL Open Font License in `assets/fonts/OFL.txt`. Lettering is converted to paths so GitHub need not fetch fonts. README text provides the accessible equivalent. The signal animation runs once, defaults to visible content and respects reduced motion.

## Evidence and counts

Refresh the counts and date together:

```sh
gh api -X GET search/issues -f q='repo:BasedHardware/omi author:aryanorastar is:pr is:merged' --jq .total_count
gh api -X GET search/issues -f q='author:aryanorastar is:pr is:merged is:public' --jq .total_count
```

Feature only public repositories. Verify authorship, merge state and scope before adding a contribution; credit collaborators. A merge does not prove deployment, adoption or customer recovery.

## Verification

Check SVG XML, image paths, readable mobile/desktop rendering, dark/light appearances, reduced motion, links and factual claims. Preserve a screenshot of major visual changes. Git history keeps earlier versions.
