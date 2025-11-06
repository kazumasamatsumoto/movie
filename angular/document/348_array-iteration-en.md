# #348 "Array Iteration"

## Overview
When iterating over arrays, the combination of `*ngFor` and immutable data is recommended, which has high compatibility with change detection.

## Learning Objectives
- Understand the relationship between array operations and Angular's change detection
- Learn patterns utilizing immutable updates and trackBy
- Complete array transformation logic within components

## Technical Points
- Immutable updates like `items = [...items, newItem]`
- Provide filtered/sorted arrays via Signals or getters
- Return IDs with trackBy to promote DOM reuse

## 📺 Screen Display Code (For Video)
```html
<li *ngFor="let log of logs; trackBy: trackById">
  {{ log.message }}
</li>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
interface LogEntry {
  id: number;
  message: string;
}

@Component({
  selector: 'app-array-iteration-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <button type="button" (click)="add()">Add log</button>
    <ul>
      <li *ngFor="let log of logs(); trackBy: trackById">{{ log.message }}</li>
    </ul>
  `
})
export class ArrayIterationDemoComponent {
  private readonly logsSignal = signal<LogEntry[]>([]);
  protected logs = this.logsSignal.asReadonly();
  private nextId = 1;

  protected add(): void {
    this.logsSignal.update(list => [...list, { id: this.nextId++, message: 'Log added' }]);
  }

  protected trackById(_: number, entry: LogEntry): number {
    return entry.id;
  }
}
```

## Best Practices
- Centrally manage array operations in Signals or services, only reference in templates
- Return unique keys with trackBy to suppress re-rendering during change detection
- Consider virtual scrolling or split rendering for long lists

## Cautions
- Direct `push` keeps the same array reference, potentially not updating OnPush components
- Without trackBy, Angular compares items which is costly
- Perform sorting and filtering with stateless functions to avoid side effects

## Related Technologies
- Angular Signals
- trackBy
- CDK Virtual Scroll
