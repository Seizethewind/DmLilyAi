# Security hardening

This branch applies the first production-hardening controls:

- Chat learning is opt-in by default.
- VM code execution is opt-in by default.
- Tool category authorization is enforced at the execution boundary.
- Technical tool exceptions are no longer returned verbatim to users.

Before production deployment, set `ADMIN_TOKEN`, keep `LILYAI_VM_TOOL=0` unless VM execution has been separately reviewed, and configure an explicit `ALLOWED_USER_IDS` list. Configure branch protection so the tests check is required before merging to `main`.

The bearer-token authentication, MFA, service split, persistence redesign, and independent microVM isolation verification remain follow-up work.
