# Visual QA and launch readiness checklist

This checklist exists so volunteers can quickly verify the knowledgebase looks correct and works well for ReddHeads before announcing updates.

## Visual checks (light mode and dark mode)
- Header text is readable (no “white on white”).
- Buttons render as buttons (not raw text with `{ .md-button }`).
- Icon shortcodes render (e.g., `:material-download:`).
- Links are visibly links (underlined) and have sufficient contrast.
- Focus outlines are visible when tabbing (keyboard navigation).

## Interaction checks
- Navigation tabs/sections expand and collapse as expected.
- Search returns results for: “PoSV”, “ReddID”, “downloads”, “tipbot”, “staking”.
- External links open and point where they claim.

## Content checks (user perspective)
- **Start Here** routes a new user to Downloads, Self-custody, Tipping, Staking, Troubleshooting in 1 click.
- Troubleshooting pages include safe “stop and back up” warnings.
- Developer section contains the ReddID hub + namespaces/schema/plan.

## Known technical prerequisites
Material “cards/buttons/icons” require these Markdown extensions in `mkdocs.yml`:
- `attr_list`
- `md_in_html`
- `pymdownx.emoji` with Material emoji config

(If cards render as plain text, check those first.)

## Last updated
2026-02-13
