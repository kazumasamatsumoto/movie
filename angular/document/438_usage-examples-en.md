# #438 "Writing Usage Examples"

## Overview
Documentation usage examples show template code, configuration values, and handler examples in a form that allows users to immediately implement.

## Learning Objectives
- Understand effective usage example composition
- Learn how to include Input and Output examples
- Understand techniques for concisely presenting multiple patterns

## Technical Points
- Two-tier structure of basic example + advanced example
- Keep code blocks short and supplement with comments
- Coordinate with Storybook Canvas/Docs

## 📺 On-Screen Code (for video)
```html
<div appHoverToggle>Hover to toggle</div>
```

## 💻 Detailed Implementation Example (for learning)
```markdown
## Basic Usage Example
```html
<button appToggle (appToggle)="onToggle($event)">Toggle</button>
```

## Option Specification
```html
<div appTooltip [appTooltip]="{ message: 'Details', placement: 'bottom' }"></div>
```
```

## Best Practices
- Clearly state input values and output events so consumer side can understand expected types
- Refine examples to a level that works with copy-paste
- Maintain consistency with Storybook and design system samples

## Considerations
- Consider readability by collapsing in separate section when examples become long
- Always update examples when API changes with version upgrades
- Also include import statements and dependencies needed in actual implementation

## Related Technologies
- Storybook
- Markdown code blocks
- Playground/StackBlitz
