# 07 Operation Contracts

<!-- Larman-style contracts for the system operations discovered in the SSDs.
Postconditions become test assertions — write them checkably. -->

## OC-001: operation(args)

- **Operation:**
- **Cross references:** UC-###, SSD event, FR-XXX-###
- **Preconditions:**
- **Postconditions:** (state changes, associations formed/broken, attributes set)
- **Invariants protected:** (from `03_DOMAIN_MODEL.md`)
- **Failure outcomes:** (what happens on each precondition violation)
- **Test cases:** TC-XXX-###

## Exit Criteria

- Every SSD event has a contract.
- Every postcondition is phrased so a test can assert it.
- Every contract lists its test IDs.
