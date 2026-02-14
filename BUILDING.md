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
