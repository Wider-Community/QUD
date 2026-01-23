# GitHub Projects GraphQL Mutations Reference

Complete reference for GitHub Projects V2 GraphQL mutations.

## Issue Mutations

### Create Issue (REST API preferred)
```bash
gh issue create --title "Title" --body "Body"
```

### Update Issue
```bash
gh api graphql -f query='
mutation {
  updateIssue(input: {
    id: "ISSUE_NODE_ID"
    title: "New Title"
    body: "New body content"
  }) {
    issue { id title }
  }
}'
```

### Close Issue
```bash
gh api graphql -f query='
mutation {
  closeIssue(input: {
    issueId: "ISSUE_NODE_ID"
  }) {
    issue { id state }
  }
}'
```

### Reopen Issue
```bash
gh api graphql -f query='
mutation {
  reopenIssue(input: {
    issueId: "ISSUE_NODE_ID"
  }) {
    issue { id state }
  }
}'
```

## Sub-Issue Mutations

### Add Sub-Issue
Links a child issue to a parent issue:
```bash
gh api graphql -f query='
mutation {
  addSubIssue(input: {
    issueId: "PARENT_NODE_ID"
    subIssueId: "CHILD_NODE_ID"
  }) {
    issue {
      id
      title
    }
    subIssue {
      id
      title
    }
  }
}'
```

### Remove Sub-Issue
Unlinks a sub-issue from its parent:
```bash
gh api graphql -f query='
mutation {
  removeSubIssue(input: {
    issueId: "PARENT_NODE_ID"
    subIssueId: "CHILD_NODE_ID"
  }) {
    issue { id }
    subIssue { id }
  }
}'
```

## Project Item Mutations

### Add Issue to Project
```bash
gh api graphql -f query='
mutation {
  addProjectV2ItemById(input: {
    projectId: "PROJECT_ID"
    contentId: "ISSUE_NODE_ID"
  }) {
    item {
      id
    }
  }
}'
```

### Remove Item from Project
```bash
gh api graphql -f query='
mutation {
  deleteProjectV2Item(input: {
    projectId: "PROJECT_ID"
    itemId: "PROJECT_ITEM_ID"
  }) {
    deletedItemId
  }
}'
```

### Update Project Item Field (Single Select)
```bash
gh api graphql -f query='
mutation {
  updateProjectV2ItemFieldValue(input: {
    projectId: "PROJECT_ID"
    itemId: "PROJECT_ITEM_ID"
    fieldId: "FIELD_ID"
    value: {
      singleSelectOptionId: "OPTION_ID"
    }
  }) {
    projectV2Item { id }
  }
}'
```

### Update Project Item Field (Text)
```bash
gh api graphql -f query='
mutation {
  updateProjectV2ItemFieldValue(input: {
    projectId: "PROJECT_ID"
    itemId: "PROJECT_ITEM_ID"
    fieldId: "FIELD_ID"
    value: {
      text: "Text value"
    }
  }) {
    projectV2Item { id }
  }
}'
```

### Update Project Item Field (Number)
```bash
gh api graphql -f query='
mutation {
  updateProjectV2ItemFieldValue(input: {
    projectId: "PROJECT_ID"
    itemId: "PROJECT_ITEM_ID"
    fieldId: "FIELD_ID"
    value: {
      number: 42
    }
  }) {
    projectV2Item { id }
  }
}'
```

### Update Project Item Field (Date)
```bash
gh api graphql -f query='
mutation {
  updateProjectV2ItemFieldValue(input: {
    projectId: "PROJECT_ID"
    itemId: "PROJECT_ITEM_ID"
    fieldId: "FIELD_ID"
    value: {
      date: "2024-01-15"
    }
  }) {
    projectV2Item { id }
  }
}'
```

### Clear Project Item Field
```bash
gh api graphql -f query='
mutation {
  clearProjectV2ItemFieldValue(input: {
    projectId: "PROJECT_ID"
    itemId: "PROJECT_ITEM_ID"
    fieldId: "FIELD_ID"
  }) {
    projectV2Item { id }
  }
}'
```

## Bulk Operations Example

### Create Multiple Issues and Link as Sub-Issues

```bash
#!/bin/bash
# Create parent issue
PARENT_NUM=$(gh issue create --title "Parent Task" --body "Main task" | grep -oE '[0-9]+$')
PARENT_ID=$(gh issue view $PARENT_NUM --json id --jq '.id')

# Create child issues
for i in 1 2 3; do
  CHILD_NUM=$(gh issue create --title "Subtask $i" --body "Part of #$PARENT_NUM" | grep -oE '[0-9]+$')
  CHILD_ID=$(gh issue view $CHILD_NUM --json id --jq '.id')

  # Link as sub-issue
  gh api graphql -f query="
  mutation {
    addSubIssue(input: {
      issueId: \"$PARENT_ID\"
      subIssueId: \"$CHILD_ID\"
    }) {
      subIssue { title }
    }
  }"
done
```

### Add Multiple Issues to Project with Fields

```bash
#!/bin/bash
PROJECT_ID="PVT_kwDO..."
FIELD_ID="PVTSSF_..."
OPTION_ID="abc123..."

for ISSUE_NUM in 1 2 3 4 5; do
  ISSUE_ID=$(gh issue view $ISSUE_NUM --json id --jq '.id')

  # Add to project and get item ID
  ITEM_ID=$(gh api graphql -f query="
  mutation {
    addProjectV2ItemById(input: {
      projectId: \"$PROJECT_ID\"
      contentId: \"$ISSUE_ID\"
    }) {
      item { id }
    }
  }" --jq '.data.addProjectV2ItemById.item.id')

  # Set field value
  gh api graphql -f query="
  mutation {
    updateProjectV2ItemFieldValue(input: {
      projectId: \"$PROJECT_ID\"
      itemId: \"$ITEM_ID\"
      fieldId: \"$FIELD_ID\"
      value: { singleSelectOptionId: \"$OPTION_ID\" }
    }) {
      projectV2Item { id }
    }
  }"
done
```
