---
type: community
members: 12
---

# Threat model

**Members:** 12 nodes

## Members
- [[API Routes (`appsrcroutesapi`)]] - document - .agents/skills/higgsfield-websites/references/security.md
- [[Asset Classification]] - document - .agents/skills/higgsfield-websites/references/security.md
- [[Detection]] - document - .agents/skills/higgsfield-websites/references/security.md
- [[Entry Point Inventory]] - document - .agents/skills/higgsfield-websites/references/security.md
- [[File Upload Surfaces]] - document - .agents/skills/higgsfield-websites/references/security.md
- [[Output]] - document - .agents/skills/higgsfield-websites/references/security.md
- [[Page Routes (`appsrcroutes`)]] - document - .agents/skills/higgsfield-websites/references/security.md
- [[Pitfalls]] - document - .agents/skills/higgsfield-websites/references/security.md
- [[Server Functions (`createServerFn`)]] - document - .agents/skills/higgsfield-websites/references/security.md
- [[Threat model]] - document - .agents/skills/higgsfield-websites/references/security.md
- [[WebhookCallback Endpoints]] - document - .agents/skills/higgsfield-websites/references/security.md
- [[When to Load]] - document - .agents/skills/higgsfield-websites/references/security.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Threat_model
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Worker hardening]]
- 1 edge to [[_COMMUNITY_Attacker Model]]
- 1 edge to [[_COMMUNITY_Common Threat Patterns for the Stack]]
- 1 edge to [[_COMMUNITY_Trust Boundaries]]

## Top bridge nodes
- [[Threat model]] - degree 9, connects to 4 communities