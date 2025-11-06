# #374 "ngClass - Class Control"

## Overview
`ngClass` is an Attribute Directive that dynamically controls CSS classes applied to elements, allowing styles to be switched based on conditions.

## Learning Objectives
- Understand ngClass role and application examples
- Grasp multiple specification methods (string, array, object)
- Be able to design conditional class application patterns

## Technical Points
- Evaluate class sets with `[ngClass]="expression"`
- Supports 3 formats: string/array/object
- Merges with existing class attribute

## 📺 Screen Display Code (For Video)
```html
<button [ngClass]="{ 'is-active': active, 'is-disabled': disabled }">Action</button>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-ngclass-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <button
      type="button"
      class="btn"
      [ngClass]="buttonClasses"
      (click)="toggle()">
      {{ active ? 'ON' : 'OFF' }}
    </button>
  `,
  styles: [`
    .btn { padding: 0.5rem 1rem; border-radius: 9999px; }
    .btn.is-active { background: #0ea5e9; color: #fff; }
    .btn.is-disabled { opacity: .5; pointer-events: none; }
  `]
})
export class NgClassDemoComponent {
  protected active = false;
  protected disabled = false;

  protected get buttonClasses(): Record<string, boolean> {
    return {
      'is-active': this.active,
      'is-disabled': this.disabled
    };
  }

  protected toggle(): void {
    this.active = !this.active;
  }
}
```

## Best Practices
- Name classes to clarify their role
- Calculate class sets on component side to keep templates simple
- Create derived states with `computed`/`signal` when conditions increase

## Cautions
- Be careful of conflicts when using utility classes like Tailwind
- Typos in string specification are hard to detect, so verify in reviews
- Don't write heavy calculations in expressions as they're frequently evaluated during change detection

## Related Technologies
- Renderer2.addClass
- HostBinding
- Angular Signals
