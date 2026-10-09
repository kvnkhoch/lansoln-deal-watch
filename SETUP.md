# Lansoln Singapore Deal Watch

## Current status

The panel is live at https://lansoln-deal-watch.kvnkhoch.workers.dev/ . Its English/Chinese switch works. There are no published deals yet. GitHub is connected and the repository is kvnkhoch/lansoln-deal-watch. The existing Monday research task now generates public JSON alongside its private report. Automatic website publishing is not enabled yet.

The Cloudflare project is a Worker, so this revised package targets the existing Worker instead of Pages. No domain transfer or new Cloudflare project is needed.

## Paste into Hostinger once

Open hostinger-embed.html in a plain-text editor and copy the code. In Hostinger manual mode: Add elements → Embed code → Enter code → paste → Embed code → Update website. Set the element to full width and at least 980px tall in both desktop and mobile layouts. Larger snapshots scroll internally. The frame policy permits lansoln.com and www.lansoln.com; editor previews on other origins may be blocked. Test the live website. The iframe URL is already filled in.

## Finish weekly publishing

1. The repository kvnkhoch/lansoln-deal-watch exists on main and the connected GitHub app has write access. Its current visibility is public; only the panel source and anonymised public feed belong here.
2. Upload this package at the repository root, including .github/workflows/publish.yml and wrangler.jsonc. Production publishing excludes fictional preview data.
3. In Cloudflare create a token using the official Edit Cloudflare Workers template, scoped to the account containing this Worker. Save it in GitHub repository Settings → Secrets and variables → Actions as CLOUDFLARE_API_TOKEN. Save that Cloudflare Account ID as CLOUDFLARE_ACCOUNT_ID. Enter tokens only into the secure provider settings, never in chat or repository files. No CLOUDFLARE_PAGES_PROJECT variable is needed.
4. Run the Publish Lansoln Deal Watch workflow manually. Verify success and that the existing panel URL still loads.
5. Add the verified repository, main branch and public/deals.json destination to the existing Monday task. Preserve the private report and source criteria. Test research → valid snapshot → GitHub commit → successful Action → live panel date. Confirm unattended task runs can write to GitHub and that connector-created commits trigger the workflow before claiming automatic weekly publishing is active. If unattended writes are unavailable, a separate authenticated publishing integration is required. Do not create a duplicate task.

Final flow: Monday task → public JSON → GitHub → GitHub Actions → existing Cloudflare Worker → Hostinger iframe. A scheduled rebuild alone does not discover new deals. Failed research must leave the last valid snapshot and its date unchanged. The panel refreshes every five minutes while open and shows a notice when the report is over ten days old.

The live panel and language toggle were checked. Local automated desktop/mobile checks could not run because the browser executable was unavailable. Mobile and final Hostinger embedding still require live verification.

## Preview without publishing

From this package directory, run `python3 -m http.server 8080 --directory public`, then open `http://localhost:8080/?preview=1`. All preview opportunities and prices are fictional and clearly labelled. Use `?preview=1&lang=zh` to inspect Chinese. Normal mode uses `deals.json`, currently empty with no invented research date. Production deployments remove the fictional data file.

## Public data rules

Use `schema_version: 1`, an ISO timestamp with timezone in `updated_at`, and a complete `deals` array of at most six current listings. Each record needs `id`, `industry`, `title_en`, `title_zh`, `price`, `revenue`, `ebitda`, `angle_en`, `angle_zh`, `checked_at`. Use `Not disclosed` for unavailable financials and retain currency/annual period. Use stable anonymised references. Buyer benefits must be described as potential, not guaranteed.

The validator rejects extra fields, duplicate IDs, HTML, source URLs, emails and malformed dates. It cannot determine whether prose accidentally identifies a seller or whether seller claims are true; research quality and anonymisation still require judgment. Withdraw sold/withdrawn/uncheckable deals. A successful scan with no qualifying deals publishes an empty array and the actual scan time. A failed scan keeps the last valid snapshot; it does not publish a fresh empty feed.

## Sources used for this setup

- Hostinger embed guide: https://www.hostinger.com/support/6463152-hostinger-ai-builder-manual-mode-how-to-embed-custom-code/
- Cloudflare Worker static assets: https://developers.cloudflare.com/workers/static-assets/get-started/
- Cloudflare Worker GitHub Actions: https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/
- GitHub Actions syntax: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
