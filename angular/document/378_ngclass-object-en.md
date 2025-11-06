# #378 "Object Class Specification"

## Overview
Passing an object to `[ngClass]` interprets keys as class names and values as booleans, applying only classes that are true. Most flexible format for conditional class management.

## Learning Objectives
- Understand object format class specification method
- Learn technique to manage declaratively using state maps
- Grasp patterns for calculating derived states with computed etc.

## Technical Points
- Return `Record<string, boolean>`
- Optimize Change Detection by generating objects with `computed` etc.
- Organize to avoid multiple conditions competing for same class name

## 📺 Screen Display Code (For Video)
```html
<div [ngClass]="{ card: true, 'card--error': hasError, 'card--loading': loading }"></div>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-ngclass-object-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <article [ngClass]="stateClasses()">
      <h3>State: {{ state() }}</h3>
    </article>
  `,
  styles: [`
    .panel { padding: 1rem; border-radius: 0.75rem; background: #f1f5f9; }
    .panel--loading { animation: pulse 1s infinite alternate; }
    .panel--error { border: 2px solid #f97316; }
    @keyframes pulse { from { opacity: 0.6; } to { opacity: 1; } }
  `]
})
export class NgClassObjectDemoComponent {
  private readonly stateSignal = signal<'idle' | 'loading' | 'error'>('idle');
  protected state = this.stateSignal.asReadonly();

  protected readonly stateClasses = computed(() => ({
    panel: true,
    'panel--loading': this.state() === 'loading',
    'panel--error': this.state() === 'error'
  }));
}
```

## Best Practices
- Returning class sets with computed suppresses unnecessary recalculations
- Manage states with Union types to clarify correspondence with classes
- Keep shared classes fixed as `true`, only dynamically change conditional ones

## Cautions
- Generating object literals directly in templates creates new references each time
- Avoid class name collisions and unify naming conventions
- Passing values other than booleans causes unexpected behavior, so limit to boolean

## Related Technologies
- Angular Signals / computed
- TypeScript Union Types
- CSS State Class Design
