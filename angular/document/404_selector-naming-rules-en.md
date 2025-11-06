# #404 "selector Naming Rules"

## Overview
Directive selectors are named with prefix + role name to avoid conflicts with other libraries while improving readability.

## Learning Objectives
- Understand attribute directive selector notation
- Be able to explain the importance of prefixes
- Learn how to establish naming conventions within a project

## Technical Points
- Attribute directive: `[appHighlight]`
- Class directive: `.appDraggable`
- Element directive: `app-card` (mainly for components)

## 📺 On-Screen Code (for video)
```typescript
@Directive({ selector: '[appHighlight]', standalone: true })
export class HighlightDirective {}
```

## 💻 Detailed Implementation Example (for learning)
```typescript
export const DIRECTIVE_PREFIX = 'app';

function selector(name: string): string {
  return `[${DIRECTIVE_PREFIX}${name[0].toUpperCase()}${name.slice(1)}]`;
}

@Directive({
  selector: selector('focusRing'),
  standalone: true
})
export class FocusRingDirective {}
```

## Best Practices
- Define selectors that convey their role with prefix + PascalCase
- Adopt brand prefixes like `lib`, `acme` for custom libraries
- Document naming conventions in README or style guide

## Considerations
- Publishing without a prefix makes it easy to conflict with other libraries
- Typos within string literals won't be detected at build time
- When using class selectors, ensure consistency with CSS naming

## Related Technologies
- Angular Style Guide
- Schematics configuration
- ESLint template rules
