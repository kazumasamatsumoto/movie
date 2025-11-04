# #303 "Component Directive - Components"

## Overview
Component Directives are Angular components for reusing UI fragments with templates and styles, and dependencies can be minimized by making them standalone.

## Learning Objectives
- Understand the definition and responsibilities of Component Directives
- Learn the steps to declare as a standalone component
- Study Input/Output interface design

## Technical Points
- `@Component` decorator with `standalone: true`
- Declare dependent directives in the `imports` property
- Build UI component contracts with `@Input`/`@Output`

## 📺 Display Code (For Video)
```typescript
@Component({
  selector: 'app-pill',
  standalone: true,
  template: `<span class="pill"><ng-content /></span>`
})
export class PillComponent {}
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-pill',
  standalone: true,
  imports: [CommonModule],
  template: `
    <span class="pill" [class.pill--active]="active">
      <ng-content />
      <button type="button" (click)="toggle.emit(!active)">×</button>
    </span>
  `,
  styles: [`
    .pill { display: inline-flex; align-items: center; gap: 0.25rem; padding: 0.25rem 0.5rem; border-radius: 9999px; background: #e0f2fe; }
    .pill--active { background: #1d4ed8; color: #fff; }
    button { all: unset; cursor: pointer; font-size: 0.75rem; }
  `]
})
export class PillComponent {
  @Input({ required: true }) active!: boolean;
  @Output() toggle = new EventEmitter<boolean>();
}

@Component({
  selector: 'app-pill-demo',
  standalone: true,
  imports: [CommonModule, PillComponent],
  template: `
    <app-pill [active]="selected" (toggle)="selected = $event">
      Component Directive
    </app-pill>
    <p>Status: {{ selected ? 'ON' : 'OFF' }}</p>
  `
})
export class PillDemoComponent {
  protected selected = false;
}
```

## Best Practices
- Specify standalone to reduce module dependencies, allowing consumers to use it by simply adding to `imports`
- Make contracts explicit with Input/Output using required flags and type definitions while maintaining stateless design
- Allow flexible content insertion with `ng-content` while keeping styles encapsulated within the component

## Cautions
- Delegate business logic to services and focus on UI presentation
- Avoid excessive style or size dependencies, leaving room for consumers to customize
- Switch ChangeDetection strategy to `OnPush` as needed to reduce re-rendering costs

## Related Technologies
- Standalone Components
- Angular Signals
- ChangeDetectorRef
