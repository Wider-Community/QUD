---
name: github-projects
description: |
  Manage GitHub Projects V2 with full CRUD operations. This skill should be used when users want to:
  create issues with sub-issues, add issues to organization projects, set custom project fields
  (like Priority, Status, Issue Type), query project structure, or perform bulk issue operations.
  Covers the critical distinction between personal and org projects, proper sub-issue linking via
  GraphQL, and field value mutations.
---

# GitHub Projects V2 Management

Manage GitHub Projects V2 including issues, sub-issues, and custom fields using `gh` CLI and GraphQL API.

## Critical: Personal vs Organization Projects

**Common mistake**: Using the wrong project ID. Personal projects and org projects have different IDs even if they share the same name.

### Find the Correct Project ID

**For organization projects** (most common):
```bash
gh repo view OWNER/REPO --json projectsV2 --jq '.projectsV2.nodes[] | {title: .title, id: .id, number: .number}'
```

**For user projects** (personal):
```bash
gh api graphql -f query='{ viewer { projectsV2(first: 20) { nodes { id title number } } } }'
```

**Verify project owner**:
- Org project IDs start with `PVT_kwDO` followed by org-specific characters
- Check the project URL: `github.com/orgs/ORG-NAME/projects/N` vs `github.com/users/USERNAME/projects/N`

## Issue Operations

### Create Issue
```bash
gh issue create --title "Issue Title" --body "$(cat <<'EOF'
Issue body with markdown support.

## Subtasks
- [ ] Task 1
- [ ] Task 2
EOF
)"
```

### Create Issue and Add to Project
```bash
gh issue create --title "Title" --project "Project Name" --body "Body"
```

### Get Issue Node ID
Required for GraphQL operations:
```bash
gh issue view ISSUE_NUMBER --json id --jq '.id'
```

### Update Issue Body
```bash
gh issue edit ISSUE_NUMBER --body "$(cat <<'EOF'
New body content here
EOF
)"
```

### List Issues
```bash
gh issue list --limit 100 --state open
gh issue list --search "label:bug"
```

## Sub-Issues (Parent-Child Linking)

**Important**: Sub-issues require GraphQL API. The `gh issue create` command cannot create sub-issue relationships directly.

### Link Sub-Issue to Parent
```bash
gh api graphql -f query='
mutation {
  addSubIssue(input: {
    issueId: "PARENT_ISSUE_NODE_ID"
    subIssueId: "CHILD_ISSUE_NODE_ID"
  }) {
    issue { id title }
    subIssue { id title }
  }
}'
```

### Remove Sub-Issue Link
```bash
gh api graphql -f query='
mutation {
  removeSubIssue(input: {
    issueId: "PARENT_ISSUE_NODE_ID"
    subIssueId: "CHILD_ISSUE_NODE_ID"
  }) {
    issue { id }
  }
}'
```

### Query Sub-Issues of a Parent
```bash
gh api graphql -f query='
query {
  node(id: "PARENT_ISSUE_NODE_ID") {
    ... on Issue {
      title
      subIssues(first: 50) {
        nodes { id title state }
      }
    }
  }
}'
```

## Project Field Operations

See `references/field-operations.md` for complete field manipulation patterns including:
- Querying project fields and option IDs
- Setting single-select fields (Status, Priority, Issue Type)
- Setting text, number, and date fields
- Bulk field updates

## Adding Issues to Projects

### Add Issue to Project
```bash
gh api graphql -f query='
mutation {
  addProjectV2ItemById(input: {
    projectId: "PROJECT_ID"
    contentId: "ISSUE_NODE_ID"
  }) {
    item { id }
  }
}'
```

### Get Project Item ID
After adding to project, get the item ID for field updates:
```bash
gh api graphql -f query='
mutation {
  addProjectV2ItemById(input: {
    projectId: "PROJECT_ID"
    contentId: "ISSUE_NODE_ID"
  }) {
    item { id }
  }
}' --jq '.data.addProjectV2ItemById.item.id'
```

### Remove Issue from Project
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

## Querying Projects

### List All Project Fields
```bash
gh api graphql -f query='
query {
  node(id: "PROJECT_ID") {
    ... on ProjectV2 {
      fields(first: 50) {
        nodes {
          ... on ProjectV2SingleSelectField {
            id name options { id name }
          }
          ... on ProjectV2Field {
            id name
          }
        }
      }
    }
  }
}'
```

### List Project Items
```bash
gh api graphql -f query='
query {
  node(id: "PROJECT_ID") {
    ... on ProjectV2 {
      items(first: 100) {
        nodes {
          id
          content {
            ... on Issue { title number state }
          }
        }
      }
    }
  }
}'
```

## Workflow: Create Issues with Sub-Issues and Fields

Complete workflow for creating a parent issue with sub-issues, adding to project, and setting fields:

1. **Create parent issue** and capture issue number
2. **Create sub-issues** with "Part of #PARENT" in body
3. **Get node IDs** for all issues using `gh issue view NUMBER --json id`
4. **Link sub-issues** using `addSubIssue` mutation
5. **Add all issues to project** using `addProjectV2ItemById`
6. **Set fields** on each project item using `updateProjectV2ItemFieldValue`

See `references/graphql-mutations.md` for complete mutation examples.

## Common Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| "Could not resolve to a ProjectV2" | Wrong project ID | Use `gh repo view` to get org project ID |
| "Field not found" | Wrong field ID | Query project fields first to get correct IDs |
| "Option not found" | Wrong option ID for single-select | Query field options to get correct option IDs |
| Sub-issues not linked | Used `gh issue create` only | Must use `addSubIssue` GraphQL mutation |
| "Resource not accessible" | Permissions or wrong org | Check gh auth status and org membership |

## Quick Reference

```bash
# Get org project ID
gh repo view OWNER/REPO --json projectsV2

# Get issue node ID
gh issue view NUMBER --json id

# List project fields and options
gh api graphql -f query='{ node(id: "PROJECT_ID") { ... on ProjectV2 { fields(first: 50) { nodes { ... on ProjectV2SingleSelectField { id name options { id name } } } } } } }'

# Update issue body
gh issue edit NUMBER --body "new body"

# Close issue
gh issue close NUMBER

# Reopen issue
gh issue reopen NUMBER
```
