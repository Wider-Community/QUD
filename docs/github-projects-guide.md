# GitHub Projects Guide

**Project**: QUD Research & Development
**Owner**: Wider-Community (organization)
**Project Number**: 1
**Project ID**: `PVT_kwDODeq8VM4BMW7f`

---

## Custom Fields

| Field | Type | Field ID |
|-------|------|----------|
| System | Single Select | `PVTSSF_lADODeq8VM4BMW7fzg7qwOA` |
| Category | Single Select | `PVTSSF_lADODeq8VM4BMW7fzg7qw7g` |
| Priority | Single Select | `PVTSSF_lADODeq8VM4BMW7fzg7qd_Y` |
| Issue Type | Single Select | `PVTSSF_lADODeq8VM4BMW7fzg7qxBM` |

### System Options

| Value | Option ID |
|-------|-----------|
| Munajjam | `88fa7b92` |
| Mujarrad | `7fc1152b` |
| Mudmaj | `45b5aa6c` |
| QUD-General | `46a28319` |
| AI-Research | `629735cb` |

### Category Options

| Value | Option ID |
|-------|-----------|
| Layer-Foundation | `8a859d20` |
| Semantic-Hashing | `58fd7c5e` |
| Cross-Layer-Mapping | `a43a0e5b` |
| Architecture | `c243222f` |
| Database | `c17c8654` |
| Backend | `45660218` |
| AI-Research | `4222c407` |
| Integration | `24888c0e` |

### Priority Options

| Value | Option ID |
|-------|-----------|
| P1-Critical | `79628723` |
| P2-High | `0a877460` |
| P3-Medium | `da944a9c` |
| P4-Low | `0ac0acc0` |

### Issue Type Options

| Value | Option ID |
|-------|-----------|
| Research | `059dab11` |
| Design | `12feb67d` |
| Implementation | `936ffcb3` |
| Documentation | `611c2fa0` |
| Review | `7e42aa14` |

---

## Labels

```
system:munajjam, system:mujarrad, system:mudmaj, system:qud, system:ai
type:research, type:design, type:implementation, type:docs
priority:critical, priority:high, priority:medium, priority:low
```

---

## CLI Commands

### List Projects

```bash
# List your personal projects
gh project list

# List organization projects
gh project list --owner Wider-Community
```

### List Project Fields

```bash
gh project field-list 1 --owner Wider-Community
```

### List Project Items

```bash
gh project item-list 1 --owner Wider-Community

# With JSON output
gh project item-list 1 --owner Wider-Community --format json | jq '.items[]'
```

---

## Creating Issues

### 1. Create Issue

> **Note**: Metadata (System, Category, Priority, Issue Type) should NOT be included in the issue body since they are captured as project fields.

```bash
gh issue create --title "[ID] Title" --body "$(cat <<'EOF'
## Research Questions
- **RQ1**: First question?
- **RQ2**: Second question?
- **Related**: RR-001, RR-002

## Description
Description text here.

Arabic description here.

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2

## References (Primary)
- `/path/to/file.md` - Description

## References (Secondary)
- `/path/to/other.md` - Description
EOF
)"
```

### 2. Add Issue to Project

```bash
# Get the issue URL from step 1, then:
ITEM_ID=$(gh project item-add 1 --owner Wider-Community --url "https://github.com/Wider-Community/QUD/issues/NUMBER" --format json | jq -r '.id')
echo $ITEM_ID
```

### 3. Set Field Values

```bash
PROJECT_ID="PVT_kwDODeq8VM4BMW7f"

# Set System
gh project item-edit --project-id $PROJECT_ID --id $ITEM_ID \
  --field-id PVTSSF_lADODeq8VM4BMW7fzg7qwOA \
  --single-select-option-id 46a28319  # QUD-General

# Set Category
gh project item-edit --project-id $PROJECT_ID --id $ITEM_ID \
  --field-id PVTSSF_lADODeq8VM4BMW7fzg7qw7g \
  --single-select-option-id 8a859d20  # Layer-Foundation

# Set Priority
gh project item-edit --project-id $PROJECT_ID --id $ITEM_ID \
  --field-id PVTSSF_lADODeq8VM4BMW7fzg7qd_Y \
  --single-select-option-id 79628723  # P1-Critical

# Set Issue Type
gh project item-edit --project-id $PROJECT_ID --id $ITEM_ID \
  --field-id PVTSSF_lADODeq8VM4BMW7fzg7qxBM \
  --single-select-option-id 059dab11  # Research
```

### All-in-One Script

```bash
# Create issue, add to project, set all fields in one go
ISSUE_URL=$(gh issue create --title "[LF-XXX] Title" --body "Body content here") && \
ITEM_ID=$(gh project item-add 1 --owner Wider-Community --url "$ISSUE_URL" --format json | jq -r '.id') && \
PROJECT_ID="PVT_kwDODeq8VM4BMW7f" && \
gh project item-edit --project-id $PROJECT_ID --id $ITEM_ID --field-id PVTSSF_lADODeq8VM4BMW7fzg7qwOA --single-select-option-id 46a28319 && \
gh project item-edit --project-id $PROJECT_ID --id $ITEM_ID --field-id PVTSSF_lADODeq8VM4BMW7fzg7qw7g --single-select-option-id 8a859d20 && \
gh project item-edit --project-id $PROJECT_ID --id $ITEM_ID --field-id PVTSSF_lADODeq8VM4BMW7fzg7qd_Y --single-select-option-id 79628723 && \
gh project item-edit --project-id $PROJECT_ID --id $ITEM_ID --field-id PVTSSF_lADODeq8VM4BMW7fzg7qxBM --single-select-option-id 059dab11 && \
echo "Created: $ISSUE_URL"
```

---

## Creating Fields

### Create Single Select Field

```bash
gh project field-create 1 --owner Wider-Community \
  --name "FieldName" \
  --data-type "SINGLE_SELECT" \
  --single-select-options "Option1,Option2,Option3"
```

**Note**: Some names like "Type" are reserved. Use alternatives like "Issue Type".

### Get Field Option IDs

```bash
# Replace FIELD_ID with the actual field ID
gh api graphql -f query='{
  node(id: "FIELD_ID") {
    ... on ProjectV2SingleSelectField {
      options { id name }
    }
  }
}' --jq '.data.node.options[] | "\(.name)=\(.id)"'
```

---

## Querying Project Data

### Get All Items with Fields

```bash
gh project item-list 1 --owner Wider-Community --format json | jq '.items[] | {
  title: .title,
  priority: .priority,
  system: .system,
  category: .category,
  issueType: .["issue Type"]
}'
```

### Get Field Details via GraphQL

```bash
gh api graphql -f query='
query {
  node(id: "PVT_kwDODeq8VM4BMW7f") {
    ... on ProjectV2 {
      fields(first: 20) {
        nodes {
          ... on ProjectV2SingleSelectField {
            id
            name
            options { id name }
          }
        }
      }
    }
  }
}'
```

---

## Quick Reference

### Field IDs (Copy-Paste Ready)

```bash
PROJECT_ID="PVT_kwDODeq8VM4BMW7f"
SYS_FIELD="PVTSSF_lADODeq8VM4BMW7fzg7qwOA"
CAT_FIELD="PVTSSF_lADODeq8VM4BMW7fzg7qw7g"
PRI_FIELD="PVTSSF_lADODeq8VM4BMW7fzg7qd_Y"
TYPE_FIELD="PVTSSF_lADODeq8VM4BMW7fzg7qxBM"
```

### Option IDs (Copy-Paste Ready)

```bash
# System
MUNAJJAM="88fa7b92"
MUJARRAD="7fc1152b"
MUDMAJ="45b5aa6c"
QUD_GENERAL="46a28319"
AI_RESEARCH="629735cb"

# Category
LAYER_FOUNDATION="8a859d20"
SEMANTIC_HASHING="58fd7c5e"
CROSS_LAYER_MAPPING="a43a0e5b"
ARCHITECTURE="c243222f"
DATABASE="c17c8654"
BACKEND="45660218"
CAT_AI_RESEARCH="4222c407"
INTEGRATION="24888c0e"

# Priority
P1_CRITICAL="79628723"
P2_HIGH="0a877460"
P3_MEDIUM="da944a9c"
P4_LOW="0ac0acc0"

# Issue Type
RESEARCH="059dab11"
DESIGN="12feb67d"
IMPLEMENTATION="936ffcb3"
DOCUMENTATION="611c2fa0"
REVIEW="7e42aa14"
```
