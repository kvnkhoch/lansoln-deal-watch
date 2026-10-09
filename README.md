# lansoln-deal-watch

English/Chinese Singapore acquisition opportunity panel for Lansoln Consultancy.

Live panel: https://lansoln-deal-watch.kvnkhoch.workers.dev/

## Publishing status

The panel is live with an empty initial feed. The existing Monday research task prepares a complete public JSON snapshot and keeps its source links and seller contacts in the private report. GitHub Actions validates and publishes a changed snapshot to the existing Cloudflare Worker once Cloudflare publishing credentials are configured. End-to-end unattended publishing has not yet been verified.

## One-time Cloudflare connection

In this repository open Settings → Secrets and variables → Actions → New repository secret. Add:

| Name | Value |
| --- | --- |
| `CLOUDFLARE_ACCOUNT_ID` | The Cloudflare Account ID containing the live `lansoln-deal-watch` Worker |
| `CLOUDFLARE_API_TOKEN` | A token from Cloudflare's Edit Cloudflare Workers template, scoped to that account |

Enter the token only into GitHub's secure secret field. Do not commit it or paste it into chat.

Then open Actions → Publish Lansoln Deal Watch → Run workflow. A successful deployment should preserve the live panel URL.

## Data and Hostinger embed

The public snapshot lives at `public/deals.json`. Validation: `python3 scripts/validate_feed.py public/deals.json`.

Copy `hostinger-embed.html` into Hostinger's Embed code element once. Use full width and at least 980px height in desktop/mobile layouts. The panel scrolls internally for larger snapshots. Reports older than ten days show a freshness notice.

Never commit the private research report, seller contact list, API tokens or confidential deal details to this repository. Public records are anonymised, prices are seller-reported, and enquiry links point to Lansoln.

See SETUP.md for the feed schema and publishing details.
