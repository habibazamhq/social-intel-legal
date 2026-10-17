# habib-legal-pages

Static Terms of Service and Privacy Policy for the TikTok developer app **Habib Social Intel**, a private, read-only analytics dashboard for @habibazamhq. They use the Habib Azam "ha" brand (Fog Grey).

Files:
- `index.html`, `terms.html`, `privacy.html`
- `styles.css`, `logo.svg`, `favicon.svg`
- `.nojekyll`
- `build.py`: page content lives here. Edit it, then run `python3 build.py`.
- `preview.png`

## Publish on GitHub Pages (main branch, root)
1. On GitHub, create a **public** repository, e.g. `habib-legal-pages`, without a README.
2. Push this folder:
   ```bash
   cd /workspace/habib-legal-pages
   git init -b main
   git add .
   git commit -m "Legal pages for Habib Social Intel"
   git remote add origin https://github.com/<github-user>/habib-legal-pages.git
   git push -u origin main
   ```
3. In the repo, open **Settings → Pages → Build and deployment**:
   - Source: **Deploy from a branch**
   - Branch: **main**, folder **/ (root)**
   - Click **Save**.
4. Wait about 1–2 minutes. The site will be at `https://<github-user>.github.io/habib-legal-pages/`.
5. In the TikTok developer app, use:
   - Terms of Service URL: `https://<github-user>.github.io/habib-legal-pages/terms.html`
   - Privacy Policy URL: `https://<github-user>.github.io/habib-legal-pages/privacy.html`
6. Optional: to use a custom domain such as `legal.habibazam.com`, add it under Settings → Pages, create a CNAME DNS record pointing to `<github-user>.github.io`, then tick **Enforce HTTPS**.

Free GitHub plans serve Pages only from public repositories.
