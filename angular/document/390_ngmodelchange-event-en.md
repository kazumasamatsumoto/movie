# #390 "ngModelChange Event"

## Overview
`ngModelChange` is an event that fires when ngModel updates a value, allowing you to receive the new value and perform additional processing or input validation.

## Learning Objectives
- Understand the role and timing of `ngModelChange` event
- Learn how to retrieve new values from `$event` and execute logic
- Grasp patterns for debouncing change events

## Technical Points
- Get new value with `(ngModelChange)="handler($event)"`
- When `updateOn: 'blur'` is set, event fires on focus out
- Prevent rapid firing with RxJS `Subject` or `debounceTime`

## 📺 Display Code (for video)
```html
<input [(ngModel)]="keyword" (ngModelChange)="search($event)" />
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-ngmodelchange-demo',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <input
      type="text"
      placeholder="Keyword"
      [(ngModel)]="keyword"
      (ngModelChange)="onKeywordChange($event)" />
    <p>Normalized: {{ normalized }}</p>
  `
})
export class NgModelChangeDemoComponent {
  protected keyword = '';
  protected normalized = '';

  protected onKeywordChange(value: string): void {
    this.normalized = value.trim().toLowerCase();
  }
}
```

## Best Practices
- Separate side effect processing like input value normalization or API search with `ngModelChange`
- Mitigate excessive processing from continuous input with `debounceTime`
- Adjust `updateOn` to design for events firing at intended timing

## Considerations
- Writing both `[(ngModel)]="value"` and `(ngModelChange)="value = $event"` simultaneously causes double updates, so be careful
- Don't execute heavy processing directly as events occur frequently
- Unlike Reactive Forms, there's no `valueChanges` Observable, so prepare your own Subject if needed

## Related Technologies
- RxJS debounceTime
- ngModelOptions
- Reactive Forms valueChanges
