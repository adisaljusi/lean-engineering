# Offline device synchronization

A medical equipment inventory has offline scanners that may be disconnected for 48 hours. Inventory adjustments have stable identities and can arrive twice or late. Two operators may record conflicting location changes. A false current location is worse than explicitly unresolved state. Existing service has one SQL database and two independently versioned device clients. Propose a design and rollout. Do not implement or invent conflict authority; identify the needed business decision. Preserve source observations and audit history.
