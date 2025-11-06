# #383 "Style Specification with Objects"

## Overview
Passing an object to `[ngStyle]` allows you to specify styles per property, making conditional styling and simultaneous control of multiple properties easier.

## Learning Objectives
- Understand the advantages of object format
- Grasp the mechanism to remove styles with falsy values
- Learn techniques for generating style objects in components

## Technical Points
- Implementation returning `Record<string, string | null>` is common
- Allow null/undefined to remove styles
- Manage related styles together in the same object

## 📺 Display Code (for video)
```html
<section [ngStyle]="{ background: theme.bg, color: theme.fg }">Theme Panel</section>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
interface Theme {
  bg: string;
  fg: string;
}

@Component({
  selector: 'app-ngstyle-object-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <section [ngStyle]="styles()">
      <h2>Theme</h2>
      <p>Applying styles according to the current theme color.</p>
    </section>
  `
})
export class NgStyleObjectDemoComponent {
  private readonly theme = signal<Theme>({ bg: '#e0f2fe', fg: '#0f172a' });
  protected readonly styles = computed(() => ({
    background: this.theme().bg,
    color: this.theme().fg,
    padding: '1.5rem',
    borderRadius: '1rem'
  }));
}
```

## Best Practices
- Use computed to reuse styles and avoid unnecessary recalculations
- Manage themes and dark mode through services or Signals
- Manage style properties with types to prevent unintended values

## Considerations
- As the number of styles increases, objects become bloated, so keep only important differences
- Properties returning `null` are removed, but adjust with empty strings if different from expectations
- Convert important styles to CSS classes and limit ngStyle to exceptional overrides

## Related Technologies
- Angular Signals
- Theme Service
- CSS Variables
