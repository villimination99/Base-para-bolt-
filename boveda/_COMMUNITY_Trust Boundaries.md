---
type: community
members: 6
---

# Trust Boundaries

**Members:** 6 nodes

## Members
- [[Auth Routes → Public Routes (access control boundary)]] - document - .agents/skills/higgsfield-websites/references/security.md
- [[Browser → Worker (untrusted → trusted)]] - document - .agents/skills/higgsfield-websites/references/security.md
- [[Trust Boundaries]] - document - .agents/skills/higgsfield-websites/references/security.md
- [[Worker → D1R2KV (trusted → trusted)]] - document - .agents/skills/higgsfield-websites/references/security.md
- [[Worker → External API (trusted → semi-trusted)]] - document - .agents/skills/higgsfield-websites/references/security.md
- [[Worker → fnf.internal (trusted → trusted)]] - document - .agents/skills/higgsfield-websites/references/security.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Trust_Boundaries
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Threat model]]

## Top bridge nodes
- [[Trust Boundaries]] - degree 6, connects to 1 community