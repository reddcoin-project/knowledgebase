# ReddCoin Knowledgebase (MkDocs)

This repository is an MkDocs (Material theme) documentation site.

## View locally

### Option A: Python + pip (recommended)

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
source .venv/bin/activate

pip install -r requirements.txt
mkdocs serve
```

Then open the local URL shown in the terminal (usually http://127.0.0.1:8000/).

### Build a static site

```bash
pip install -r requirements.txt
mkdocs build
```

The static site is written to the `site/` directory.

## Deploy to GitHub Pages

### Recommended: GitHub Actions (auto-deploy on push)

1. Push this repo to GitHub.
2. In your GitHub repo, go to **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to **GitHub Actions**.
4. Push to `main` (or run the workflow manually). The site will deploy automatically.

The workflow file is at `.github/workflows/pages.yml`.

### Alternative: deploy to `gh-pages` branch (manual)

```bash
pip install -r requirements.txt
mkdocs gh-deploy --force
```

Then in **Settings → Pages**, set the publishing source to the `gh-pages` branch and `/ (root)`.

## Notes

- If you use a project repo (e.g. `reddcoin-kb`) your Pages URL will be:
  `https://<USER_OR_ORG>.github.io/<REPO_NAME>/`
- If you use a user/org Pages repo (e.g. `<USER_OR_ORG>.github.io`) your site will be at:
  `https://<USER_OR_ORG>.github.io/`

