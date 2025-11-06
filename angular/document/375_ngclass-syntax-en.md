# #375 "Basic [ngClass] Syntax"

## Overview
With `[ngClass]`, you can evaluate arbitrary expressions to set class names, flexibly specifying with either string, array, or object.

## Learning Objectives
- Understand how to write `[ngClass]`
- Grasp how each data format converts to classes
- Learn extensible class control design

## Technical Points
- String: Apply multiple classes separated by spaces
- Array: Apply classes per element, ignore Falsy values
- Object: Determine application by boolean values

## 📺 Screen Display Code (For Video)
```html
<div [ngClass]="{ badge: true, 'badge--warn': level === 'warn' }">
  Status
</div>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-ngclass-syntax-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <p [ngClass]="statusClasses">Current status: {{ level }}</p>
    <button type="button" (click)="cycle()">Switch</button>
  `
})
export class NgClassSyntaxDemoComponent {
  private readonly levels = ['info', 'warn', 'error'] as const;
  private index = 0;
  protected level = this.levels[this.index];

  protected get statusClasses(): (string | undefined)[] | Record<string, boolean> {
    return [
      'status',
      this.level === 'warn' ? 'status--warning' : undefined,
      this.level === 'error' ? 'status--error' : undefined
    ];
  }

  protected cycle(): void {
    this.index = (this.index + 1) % this.levels.length;
    this.level = this.levels[this.index];
  }
}
```

## Best Practices
- Prepare derived data in component before conditional expressions become complex
- Organize branches by utilizing returning undefined or null to not apply classes
- Extract shared class sets as constants to improve reusability

## Cautions
- Typos in strings won't apply styles, so detect in reviews
- In array format, empty strings remain as classes, so return `undefined`
- In object format, avoid special keys like `__proto__`

## Related Technologies
- CSS BEM Notation
- Angular Signals
- Tailwind / Utility-first CSS
