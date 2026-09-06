# Local Hybrid Development

This starts a minimal hybrid stack: legacy OFBiz plus a modern gateway and the first modernized Accounting Invoices slice.

## Start

Install legacy UI vendor assets once before starting if the OFBiz image was built with `-PskipNpmInstall`:

```shell
npm ci --prefix themes/common-theme/webapp/common-theme/js
```

```shell
docker compose -p erp-local -f local-dev/docker-compose.yml up -d
```

## URLs

- Hybrid UI entry: `https://localhost:18080/webtools`
- Strangled legacy invoice search route: `https://localhost:18080/accounting/control/findInvoices`
- Direct legacy invoice search fallback: `https://localhost:18443/accounting/control/findInvoices`
- Modern invoice UI: `https://localhost:18080/modern/accounting/invoices`
- Modern invoice API: `https://localhost:18080/api/accounting/invoices?limit=10`
- Modern invoice detail API: `https://localhost:18080/api/accounting/invoices/8009`
- Modern invoice health: `https://localhost:18080/api/accounting/invoices/health`
- Modern notification health: `https://localhost:18080/api/notifications/health`
- Direct legacy fallback: `https://localhost:18443/webtools`

The direct legacy fallback must render same-origin asset and form URLs on `https://localhost:18443`. Gateway-served legacy pages must render those URLs on `https://localhost:18080`. This avoids cross-origin `less.js`/XHR failures and keeps CSS/JS loading stable.

## Phase 1 Slice

`modern-accounting-invoice-service` is the first meaningful migration slice. The gateway routes legacy Accounting invoice search (`/accounting/control/findInvoices`) to this service while leaving the rest of Accounting in OFBiz. It reads the legacy OFBiz Postgres invoice tables and exposes a modern read-only invoice projection:

- invoice header, type, status, parties, dates, currency
- invoice item count and SQL-derived total
- payment application total and outstanding amount
- invoice detail with line items, payment applications, and status history
- API create/update/delete operations for invoice headers
- navigation links back to the remaining legacy Accounting sections

This is intentionally limited to invoice headers for writes. OFBiz remains source of truth for invoice item mutation, payment application, posting, tax, promotion, PDF, and accounting side effects until behavior is reconciled with OFBiz `InvoiceWorker` and service rules.

## Login

- User: `admin`
- Password: `ofbiz`

## Stop

```shell
docker compose -p erp-local -f local-dev/docker-compose.yml down
```

Use `down -v` if you need a full data reload/reset.
