# #335 "*ngIf - Conditional Display"

## Overview
`*ngIf` is a structural directive that adds or removes elements from the DOM based on conditions, allowing both display control and accessibility.

## Learning Objectives
- Understand the basic concept and uses of *ngIf
- Explain the differences from CSS display control
- Learn key points in condition design

## Technical Points
- Evaluates boolean values to generate/destroy elements
- Organize branching display with else/then templates
- Reuse values and use for `null` guards with `as` syntax

## 📺 On-Screen Code (for video)
```html
<p *ngIf="isReady">Loading completed.</p>
<p *ngIf="!isReady">Loading...</p>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-ngif-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <button type="button" (click)="toggle()">Toggle state</button>
    <p *ngIf="loading; else content">Loading...</p>
    <ng-template #content>
      <article>
        <h2>Loading completed</h2>
        <p>{{ message }}</p>
      </article>
    </ng-template>
  `
})
export class NgIfDemoComponent {
  protected loading = true;
  protected message = 'Data fetching completed';

  protected toggle(): void {
    this.loading = !this.loading;
  }
}
```

## Best Practices
- Manage state in components or Signals, keeping conditional expressions simple in templates
- Utilize else templates to organize loading displays and error displays
- Consider focus management and animations, keeping in mind that DOM generation/destruction occurs

## Considerations
- Writing heavy expressions that are repeatedly evaluated in conditions degrades performance
- When using `template reference`, understand the reference scope
- If conditions differ in SSR, it can cause Hydration errors, so align server and client logic

## Related Technologies
- Angular Signals
- AsyncPipe
- Angular Universal
