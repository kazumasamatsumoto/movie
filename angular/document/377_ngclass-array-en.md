# #377 "Array Class Specification"

## Overview
Passing an array to `[ngClass]` applies class names contained in each element sequentially, ignoring Falsy values. Makes managing ON/OFF of multiple classes easier.

## Learning Objectives
- Understand array format mechanism and Falsy value handling
- Learn patterns for expressing conditional expressions as array elements
- Grasp techniques for constructing arrays on component side

## Technical Points
- Array elements are class strings, not `true`/`false`
- Returning `undefined` or `null` doesn't apply classes
- Can construct arrays in components to simplify templates

## 📺 Screen Display Code (For Video)
```html
<div [ngClass]="['chip', selected ? 'chip--selected' : undefined]">Tag</div>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-ngclass-array-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <button
      *ngFor="let tag of tags"
      type="button"
      [ngClass]="tagClasses(tag)"
      (click)="toggle(tag)">
      {{ tag }}
    </button>
  `
})
export class NgClassArrayDemoComponent {
  protected tags = ['Angular', 'Directive', 'Signals'];
  private readonly selected = signal<Set<string>>(new Set());

  protected tagClasses(tag: string): (string | undefined)[] {
    const isActive = this.selected().has(tag);
    return ['chip', isActive ? 'chip--active' : undefined];
  }

  protected toggle(tag: string): void {
    const next = new Set(this.selected());
    next.has(tag) ? next.delete(tag) : next.add(tag);
    this.selected.set(next);
  }
}
```

## Best Practices
- Prepare method returning array in component to consolidate conditions
- Separate constant base classes (e.g., `'chip'`) from conditional classes
- Managing selection state with `signal` or `computed` localizes re-rendering

## Cautions
- Returning empty string `''` adds empty class, so use `undefined`
- Generating new arrays every time affects performance, so cache if needed
- Make methods called in templates pure functions without side effects

## Related Technologies
- Angular Signals
- trackBy
- Button Tag Design Patterns
