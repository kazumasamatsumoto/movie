# #362 "*ngSwitchDefault - Default"

## Overview
`*ngSwitchDefault` is a fallback displayed when no case matches, serving to inform users of unexpected states.

## Learning Objectives
- Understand the importance of default cases
- Learn message design for exceptions
- Anticipate coordination with logging and error handling

## Technical Points
- One `ngSwitch` block can have 0 or 1 `*ngSwitchDefault`
- Template references can be used in default for sharing
- Providing recovery means in addition to feedback improves UX

## 📺 Screen Display Code (For Video)
```html
<p *ngSwitchDefault>Unsupported state.</p>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
type Mode = 'view' | 'edit';

@Component({
  selector: 'app-switch-default-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div [ngSwitch]="mode">
      <p *ngSwitchCase="'view'">View mode</p>
      <p *ngSwitchCase="'edit'">Edit mode</p>
      <p *ngSwitchDefault>Unknown mode. Please contact support.</p>
    </div>
  `
})
export class SwitchDefaultDemoComponent {
  protected mode: Mode | 'unknown' = 'unknown';
}
```

## Best Practices
- Enable operational actions like log output or Sentry notifications in default
- Present buttons or links showing next actions users should take
- Verify in tests that default fires and expected wording is displayed

## Cautions
- Without default, nothing displays making issues harder to notice
- Keep default itself simple to avoid excessive complexity
- Don't forget to update when states increase and default becomes unnecessary

## Related Technologies
- Error Handling
- Logging
- UX Writing
