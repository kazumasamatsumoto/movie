# #437 "Creating Directive Documentation"

## Overview
Directive documentation clearly states purpose, usage, Input/Output, and considerations, providing information that enables users to immediately adopt.

## Learning Objectives
- Understand items to include in documentation
- Learn how to write using Markdown templates
- Understand timing when updates are needed

## Technical Points
- Overview, usage examples, API table, considerations, related links
- Incorporate into README or Storybook Docs
- Track change history with version control

## 📺 On-Screen Code (for video)
```markdown
## Usage Example
```html
<button appLoadingButton [appLoadingButton]="isLoading">Save</button>
```
```

## 💻 Detailed Implementation Example (for learning)
```markdown
# app-loading-button Directive

## Overview
Displays button loading state, disabling clicks and showing spinner.

## Usage Example
```html
<button appLoadingButton [appLoadingButton]="isSaving">Save</button>
```

## API
| Name | Type | Default | Description |
| ---- | ---- | ------- | ----------- |
| `appLoadingButton` | `boolean` | `false` | Loading state |

## Considerations
- Do not apply to elements other than buttons.
```

## Best Practices
- Prepare Markdown templates and use unified format for each directive
- Reflect same information in Storybook Docs and design documents
- Update documentation when changing and include in PR checklist

## Considerations
- Outdated information causes confusion, so validate link breaks and sample code with CI
- Keep API tables concise in table format, avoiding excessive explanation
- Clearly state usage constraints and compatibility information

## Related Technologies
- Markdown
- Storybook Docs
- Docusaurus/Docz
