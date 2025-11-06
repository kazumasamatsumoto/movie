# #384 "Dynamic Control of Multiple Styles"

## Overview
When dynamically controlling multiple styles, building style objects collectively in the component and reflecting them together based on state makes management easier.

## Learning Objectives
- Understand design patterns for dynamic style control
- Learn how to build styles with computed and minimize re-rendering
- Grasp the distinction between CSS classes and ngStyle usage

## Technical Points
- Define style sets per state and spread as needed
- Add units to numeric properties using template literals
- Perform heavy calculations in components, templates only for reference

## 📺 Display Code (for video)
```html
<div [ngStyle]="boxStyles()">Multiple Control</div>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-multi-style-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div [ngStyle]="boxStyles()">Status: {{ status() }}</div>
    <button type="button" (click)="cycle()">Toggle</button>
  `
})
export class MultiStyleDemoComponent {
  private readonly statuses = ['info', 'warn', 'error'] as const;
  private index = 0;
  private readonly statusSignal = signal<typeof this.statuses[number]>('info');
  protected status = this.statusSignal.asReadonly();

  protected boxStyles(): Record<string, string> {
    switch (this.status()) {
      case 'warn':
        return { background: '#f97316', color: '#fff', padding: '1rem', borderRadius: '0.75rem' };
      case 'error':
        return { background: '#b91c1c', color: '#fff', padding: '1rem', borderRadius: '0.75rem' };
      default:
        return { background: '#0ea5e9', color: '#fff', padding: '1rem', borderRadius: '0.75rem' };
    }
  }

  protected cycle(): void {
    this.index = (this.index + 1) % this.statuses.length;
    this.statusSignal.set(this.statuses[this.index]);
  }
}
```

## Best Practices
- Type style sets with `Record<string, string>` to prevent omissions
- When the same style values are repeated, spread a common base object
- When returning styles with computed, avoid side effects and use pure functions

## Considerations
- Specifying many styles inline breaks CSS design, so limit cases
- If new objects are generated every time during change detection and affect performance, consider memoization
- CSS animations and such are easier to control when managed with classes

## Related Technologies
- Angular Signals
- CSS Class Design
- Renderer2
