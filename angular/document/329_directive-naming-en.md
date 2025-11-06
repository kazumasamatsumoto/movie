# #329 "Directive Naming Conventions"

## Overview
Unified naming conventions improve directive discoverability and maintainability, preventing collisions by aligning prefixes and suffixes.

## Learning Objectives
- Understand naming rules for class names, file names, and selector names
- Learn collision avoidance using prefixes
- Grasp how to align test files and directory structure

## Technical Points
- Class names use `PascalCase` + `Directive`
- File names use `kebab-case.directive.ts`
- Selectors use project prefix + purpose name

## 📺 On-Screen Code (for video)
```typescript
@Directive({ selector: '[appHighlight]', standalone: true })
export class HighlightDirective {}
```

## 💻 Detailed Implementation Example (for learning)
```typescript
// src/app/directives/highlight/highlight.directive.ts
@Directive({
  selector: '[appHighlight]',
  standalone: true
})
export class HighlightDirective {
  @Input({ alias: 'appHighlight' }) color = '#fde047';
}

// src/app/directives/highlight/highlight.directive.spec.ts
describe('HighlightDirective', () => {
  // Test file following naming conventions
});
```

## Best Practices
- Add a prefix (e.g., `app`, `lib`) to the beginning of selectors to distinguish from external libraries
- Align directory and file names, placing `highlight.directive.ts` and `highlight.directive.spec.ts` side by side
- Unify naming conventions for export names and `exportAs`, documenting them

## Considerations
- If namespaces collide, DI tokens also get confused, so define prefixes per project
- Mixing uppercase and lowercase may prevent recognition in component templates
- If the selector meaning is ambiguous, users will misunderstand, so use verbs or adjectives to clarify purpose

## Related Technologies
- Angular Style Guide
- Schematics
- Storybook documentation
