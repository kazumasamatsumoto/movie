# #381 "ngStyle - Style Control"

## Overview
`ngStyle` is a directive that can control inline styles with objects, allowing multiple style properties to be changed together according to state.

## Learning Objectives
- Understand ngStyle's role and basic usage
- Learn how to safely change styles without using Renderer2
- Grasp patterns for switching styles based on conditions

## Technical Points
- Specify properties with `[ngStyle]="{ property: value }"`
- Values can use strings, numbers, or expression results
- Passing Falsy values removes that property

## 📺 Screen Display Code (For Video)
```html
<div [ngStyle]="{ color: themeColor, fontSize: fontSize + 'px' }">Style control</div>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-ngstyle-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <section [ngStyle]="styleMap()">
      <h3>Design Preview</h3>
      <p>Switching inline styles with state.</p>
    </section>
    <button type="button" (click)="toggle()">Toggle theme</button>
  `
})
export class NgStyleDemoComponent {
  private dark = false;

  protected styleMap(): Record<string, string> {
    return {
      background: this.dark ? '#0f172a' : '#f1f5f9',
      color: this.dark ? '#e2e8f0' : '#0f172a',
      padding: '1.5rem',
      borderRadius: '1rem'
    };
  }

  protected toggle(): void {
    this.dark = !this.dark;
  }
}
```

## Best Practices
- Generate objects in components when switching multiple styles to keep templates concise
- Unify formats like adding units to numeric values
- Consider converting to CSS classes for long-term styles, use ngStyle for exceptions

## Cautions
- Inline styles have high priority and tend to be hard to read, so minimize use
- Transitions etc. are easier to manage with CSS classes
- From performance perspective, consider `computed` or memoization when generating new objects each time

## Related Technologies
- Renderer2.setStyle
- CSS Class Design
- Angular Signals
