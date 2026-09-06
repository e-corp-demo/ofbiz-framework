# Migration Discovery

Generated discovery reports for the OFBiz-to-microservices migration.

Phase 1 extraction target: Accounting > Invoices. The first modern slice is an invoice projection plus limited invoice-header CRUD over legacy OFBiz Postgres, exposed through `modern-accounting-invoice-service` at `/api/accounting/invoices` and `/modern/accounting/invoices`. The hybrid gateway also strangles the legacy invoice-search route `/accounting/control/findInvoices` and serves it from the modern service while direct legacy fallback remains available on port `18443`.

Run:

```shell
python3 migration/discovery/generate_discovery.py
```

Reports:

- `components.md`: active OFBiz components and contributed resources.
- `routes.md`: webapps, mount points, controller request maps.
- `services.md`: service definitions and engines.
- `entities.md`: entity and view-entity definitions.
- `integrations.md`: keyword-based external integration inventory.
