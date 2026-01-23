# GitHub Projects Field Operations Reference

Complete reference for querying and manipulating project fields.

## Field Types

GitHub Projects V2 supports these field types:

| Type | GraphQL Type | Value Format |
|------|--------------|--------------|
| Single Select | `ProjectV2SingleSelectField` | `singleSelectOptionId: "OPTION_ID"` |
| Text | `ProjectV2Field` | `text: "value"` |
| Number | `ProjectV2Field` | `number: 42` |
| Date | `ProjectV2Field` | `date: "2024-01-15"` |
| Iteration | `ProjectV2IterationField` | `iterationId: "ITERATION_ID"` |

## Querying Fields

### Get All Fields with Options
```bash
gh api graphql -f query='
query {
  node(id: "PROJECT_ID") {
    ... on ProjectV2 {
      fields(first: 50) {
        nodes {
          ... on ProjectV2SingleSelectField {
            id
            name
            options {
              id
              name
            }
          }
          ... on ProjectV2Field {
            id
            name
            dataType
          }
          ... on ProjectV2IterationField {
            id
            name
            configuration {
              iterations {
                id
                title
                startDate
              }
            }
          }
        }
      }
    }
  }
}'
```

### Get Specific Field by Name
```bash
gh api graphql -f query='
query {
  node(id: "PROJECT_ID") {
    ... on ProjectV2 {
      field(name: "Status") {
        ... on ProjectV2SingleSelectField {
          id
          name
          options { id name }
        }
      }
    }
  }
}'
```

### One-liner to Get Field Options
```bash
gh api graphql -f query='{ node(id: "PROJECT_ID") { ... on ProjectV2 { fields(first: 50) { nodes { ... on ProjectV2SingleSelectField { id name options { id name } } } } } } }' | jq '.data.node.fields.nodes[] | select(.name != null)'
```

## Setting Field Values

### Single Select Field
Most common for Status, Priority, Issue Type fields:
```bash
gh api graphql -f query='
mutation {
  updateProjectV2ItemFieldValue(input: {
    projectId: "PROJECT_ID"
    itemId: "ITEM_ID"
    fieldId: "FIELD_ID"
    value: {
      singleSelectOptionId: "OPTION_ID"
    }
  }) {
    projectV2Item { id }
  }
}'
```

### Text Field
```bash
gh api graphql -f query='
mutation {
  updateProjectV2ItemFieldValue(input: {
    projectId: "PROJECT_ID"
    itemId: "ITEM_ID"
    fieldId: "FIELD_ID"
    value: {
      text: "My text value"
    }
  }) {
    projectV2Item { id }
  }
}'
```

### Number Field
```bash
gh api graphql -f query='
mutation {
  updateProjectV2ItemFieldValue(input: {
    projectId: "PROJECT_ID"
    itemId: "ITEM_ID"
    fieldId: "FIELD_ID"
    value: {
      number: 42.5
    }
  }) {
    projectV2Item { id }
  }
}'
```

### Date Field
```bash
gh api graphql -f query='
mutation {
  updateProjectV2ItemFieldValue(input: {
    projectId: "PROJECT_ID"
    itemId: "ITEM_ID"
    fieldId: "FIELD_ID"
    value: {
      date: "2024-01-15"
    }
  }) {
    projectV2Item { id }
  }
}'
```

### Iteration Field
```bash
gh api graphql -f query='
mutation {
  updateProjectV2ItemFieldValue(input: {
    projectId: "PROJECT_ID"
    itemId: "ITEM_ID"
    fieldId: "FIELD_ID"
    value: {
      iterationId: "ITERATION_ID"
    }
  }) {
    projectV2Item { id }
  }
}'
```

## Clearing Field Values

```bash
gh api graphql -f query='
mutation {
  clearProjectV2ItemFieldValue(input: {
    projectId: "PROJECT_ID"
    itemId: "ITEM_ID"
    fieldId: "FIELD_ID"
  }) {
    projectV2Item { id }
  }
}'
```

## Reading Field Values

### Get All Field Values for an Item
```bash
gh api graphql -f query='
query {
  node(id: "PROJECT_ITEM_ID") {
    ... on ProjectV2Item {
      fieldValues(first: 20) {
        nodes {
          ... on ProjectV2ItemFieldSingleSelectValue {
            field { ... on ProjectV2SingleSelectField { name } }
            name
            optionId
          }
          ... on ProjectV2ItemFieldTextValue {
            field { ... on ProjectV2Field { name } }
            text
          }
          ... on ProjectV2ItemFieldNumberValue {
            field { ... on ProjectV2Field { name } }
            number
          }
          ... on ProjectV2ItemFieldDateValue {
            field { ... on ProjectV2Field { name } }
            date
          }
        }
      }
    }
  }
}'
```

## Common Field Patterns

### Status Field (Typical Options)
```
Status Field ID: PVTSSF_...
Options:
  - Todo: "abc123..."
  - In Progress: "def456..."
  - Done: "ghi789..."
```

### Priority Field (Typical Options)
```
Priority Field ID: PVTSSF_...
Options:
  - P0-Urgent: "..."
  - P1-Critical: "..."
  - P2-High: "..."
  - P3-Medium: "..."
  - P4-Low: "..."
```

## Workflow: Set Multiple Fields on One Item

```bash
#!/bin/bash
PROJECT_ID="PVT_kwDO..."
ITEM_ID="PVTI_..."

# Field IDs and Option IDs (query these first!)
STATUS_FIELD="PVTSSF_..."
STATUS_OPTION="abc123"  # "In Progress"

PRIORITY_FIELD="PVTSSF_..."
PRIORITY_OPTION="def456"  # "P1-Critical"

TYPE_FIELD="PVTSSF_..."
TYPE_OPTION="ghi789"  # "Research"

# Set all fields
gh api graphql -f query="
mutation {
  status: updateProjectV2ItemFieldValue(input: {
    projectId: \"$PROJECT_ID\"
    itemId: \"$ITEM_ID\"
    fieldId: \"$STATUS_FIELD\"
    value: { singleSelectOptionId: \"$STATUS_OPTION\" }
  }) { projectV2Item { id } }

  priority: updateProjectV2ItemFieldValue(input: {
    projectId: \"$PROJECT_ID\"
    itemId: \"$ITEM_ID\"
    fieldId: \"$PRIORITY_FIELD\"
    value: { singleSelectOptionId: \"$PRIORITY_OPTION\" }
  }) { projectV2Item { id } }

  type: updateProjectV2ItemFieldValue(input: {
    projectId: \"$PROJECT_ID\"
    itemId: \"$ITEM_ID\"
    fieldId: \"$TYPE_FIELD\"
    value: { singleSelectOptionId: \"$TYPE_OPTION\" }
  }) { projectV2Item { id } }
}"
```

## Error Handling

### Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| "Could not resolve to a field" | Wrong field ID | Query project fields to get correct ID |
| "Could not resolve to an option" | Wrong option ID | Query field options to get correct ID |
| "Field value type mismatch" | Wrong value type | Check field type and use correct value format |
| "Item not found in project" | Item not added to project | Add issue to project first with `addProjectV2ItemById` |

### Validate IDs Before Using

```bash
# Validate project ID exists
gh api graphql -f query='{ node(id: "PROJECT_ID") { ... on ProjectV2 { title } } }'

# Validate field ID exists and get options
gh api graphql -f query='{ node(id: "FIELD_ID") { ... on ProjectV2SingleSelectField { name options { id name } } } }'
```
