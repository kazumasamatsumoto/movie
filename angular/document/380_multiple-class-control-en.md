# #380 "Dynamic Control of Multiple Classes"

## Overview
When controlling multiple classes simultaneously, combining array or object formats, or generating class sets in components to pass, makes management easier.

## Learning Objectives
- Understand design methods for controlling multiple classes together
- Generate class lists in components to keep templates simple
- Grasp precautions when using utility classes like Tailwind

## Technical Points
- Use hybrid of objects and arrays to maintain readability
- Return class sets with `computed` to minimize re-rendering
- Clarify naming rules and priority to avoid class conflicts

## 📺 Screen Display Code (For Video)
```html
<div [ngClass]="[baseClass, { 'is-loading': loading, 'is-error': error }]">Card</div>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-multi-class-control-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <article [ngClass]="cardClasses()">
      <h3>{{ title }}</h3>
      <p>{{ description }}</p>
    </article>
  `
})
export class MultiClassControlDemoComponent {
  protected title = 'User Card';
  protected description = 'Switches styles based on state.';
  private readonly status = signal<'idle' | 'loading' | 'error'>('idle');

  protected readonly cardClasses = computed(() => [
    'card',
    {
      'card--loading': this.status() === 'loading',
      'card--error': this.status() === 'error'
    }
  ]);
}
```

## Best Practices
- Separate and manage constant base classes from state-dependent classes
- Utilize computed to reflect differences only on state updates
- When using Tailwind etc., be careful of class duplication and priority, prefer `class` literals over `ngClass` if needed

## Cautions
- Mixing objects and arrays becomes hard to read, so decide team rules
- Too many state combinations breaks class management, so decompose if possible
- Update `aria-*` or `data-*` attributes simultaneously with classes to provide consistent behavior

## Related Technologies
- Angular Signals / computed
- Tailwind CSS
- State Machine Design
