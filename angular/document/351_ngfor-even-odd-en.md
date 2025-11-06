# #351 "even / odd - Even/Odd Determination"

## Overview
Using `let isEven = even` or `let isOdd = odd` in `*ngFor` allows you to switch styles and display content for even and odd rows.

## Learning Objectives
- Understand how to use even/odd context variables
- Learn how to utilize for row style branching
- Grasp best practices for conditional class application

## Technical Points
- `even` is true for even indices (0,2,4...)
- `odd` is true for odd indices (1,3,5...)
- Dynamically change CSS classes or attributes to improve visibility

## 📺 Screen Display Code (For Video)
```html
<tr *ngFor="let row of rows; let isOdd = odd"
    [class.is-odd]="isOdd">
  ...
</tr>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-even-odd-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <table class="striped">
      <tr *ngFor="let row of rows; let isEven = even; let isOdd = odd"
          [class.striped__row--even]="isEven"
          [class.striped__row--odd]="isOdd">
        <td>{{ row }}</td>
      </tr>
    </table>
  `,
  styles: [`
    .striped__row--even { background: #f1f5f9; }
    .striped__row--odd { background: #e2e8f0; }
  `]
})
export class EvenOddDemoComponent {
  protected rows = ['Row A', 'Row B', 'Row C', 'Row D'];
}
```

## Best Practices
- Improve accessibility with `aria` attributes beyond visual distinction
- Use BEM-style class names like `--even`/`--odd` to avoid conflicts
- Minimal performance impact even with many rows due to lightweight conditional expressions

## Cautions
- Avoid duplicate specification by writing odd determination as `i % 2 === 1` along with `isOdd`
- Anticipate re-rendering when dynamically manipulating arrays
- Using the same variable name in nested *ngFor reduces readability

## Related Technologies
- CSS Utility Classes
- trackBy
- Accessibility (ARIA)
