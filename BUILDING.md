# Building the Knowledgebase (Volunteer Guide)

## Local preview
1. Install Python 3.11+
2. From repo root:
   - `pip install -r requirements.txt`
   - `mkdocs serve`
3. Open the local URL shown in terminal (usually http://127.0.0.1:8000)

## Production build
- `mkdocs build --clean --strict`

## GitHub Pages
This repo includes a workflow at `.github/workflows/deploy-pages.yml` that builds MkDocs and deploys to GitHub Pages when you push to `main`.


## GitHub Actions troubleshooting

If Pages build fails with `pymdownx.emoji` errors and logs show Python 3.14+:
- Ensure the workflow uses **Python 3.12** (`actions/setup-python`) because some Markdown extensions are not yet compatible with 3.14.
- In GitHub Settings → Pages, set Source to **GitHub Actions**.
- Remove/disable any older Pages workflows so only one deploy workflow runs.
