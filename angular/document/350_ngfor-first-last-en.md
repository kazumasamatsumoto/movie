# #350 "first / last - First/Last Determination"

## Overview
Using `let isFirst = first` or `let isLast = last` in `*ngFor` allows you to conditionally change UI for first and last elements.

## Learning Objectives
- Understand how to use the boolean values of `first`/`last`
- Learn control patterns like separators and button display
- Perform flexible style control combining multiple conditions

## Technical Points
- `first` is true for the first item, `last` is true for the last item
- Can express complex conditions combining with `even`/`odd`
- Can switch styles and element display without changing DOM structure

## 📺 Screen Display Code (For Video)
```html
<li *ngFor="let step of steps; let isLast = last">
  {{ step }}<span *ngIf="!isLast">→</span>
</li>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-ngfor-first-last-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ul class="timeline">
      <li *ngFor="let step of steps; let isFirst = first; let isLast = last"
          [class.timeline__item--first]="isFirst"
          [class.timeline__item--last]="isLast">
        {{ step }}
      </li>
    </ul>
  `,
  styles: [`
    .timeline { list-style: none; padding: 0; }
    .timeline__item--first { font-weight: 700; }
    .timeline__item--last::after { content: ' ✅'; }
  `]
})
export class NgForFirstLastDemoComponent {
  protected steps = ['Requirements', 'Implementation', 'Testing', 'Release'];
}
```

## Best Practices
- Use CSS class binding for style changes to keep templates concise
- Utilize `last` to control separators and buttons, avoiding unnecessary element generation
- Combine with `ng-container` when displaying different components for first/last

## Cautions
- `first`/`last` are re-evaluated on list updates, so avoid side effects dependent on conditions
- Ensure variable names don't conflict between outer and inner nested lists
- Without trackBy, DOM regeneration occurs easily, potentially causing style flickering

## Related Technologies
- CSS Class Binding
- trackBy
- Structural Directive Context Variables
