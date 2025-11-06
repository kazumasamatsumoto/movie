# #355 "Minimizing Re-rendering"

## Overview
Lists using `*ngFor` can minimize re-rendering by combining immutable data, trackBy, and OnPush strategy.

## Learning Objectives
- Understand the mechanism that causes re-rendering
- Learn in-memory array update strategies
- Grasp coordination between trackBy and ChangeDetection

## Technical Points
- Make array diffs easier to detect with immutable updates
- Set Change Detection boundary with trackBy for DOM reuse & OnPush
- Using Signals can limit to local re-rendering

## 📺 Screen Display Code (For Video)
```html
<item-card *ngFor="let card of cards(); trackBy: trackById"
           [card]="card"></item-card>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
interface Card {
  id: number;
  title: string;
}

@Component({
  selector: 'app-minimize-rerender-demo',
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [CommonModule],
  template: `
    <button (click)="shuffle()">Shuffle</button>
    <ul>
      <li *ngFor="let card of cards(); trackBy: trackById">{{ card.title }}</li>
    </ul>
  `
})
export class MinimizeRerenderDemoComponent {
  private readonly cardsSignal = signal<Card[]>([
    { id: 1, title: 'Directive' },
    { id: 2, title: 'Component' },
    { id: 3, title: 'Service' }
  ]);
  protected cards = this.cardsSignal.asReadonly();

  protected shuffle(): void {
    this.cardsSignal.update(list => [...list].reverse());
  }

  protected trackById(_: number, card: Card): number {
    return card.id;
  }
}
```

## Best Practices
- Introduce immutable updates and trackBy as a set, visualizing and confirming re-rendering
- In OnPush components, rendering occurs only when external inputs change, so keep data flow clear
- Using Signals allows re-rendering only the parts that need updating

## Cautions
- Mutable updates may not render in OnPush in some cases
- Be careful as trackBy functions returning new references have reverse effect
- Measure performance with browser dev tools to verify optimization effects

## Related Technologies
- ChangeDetectionStrategy.OnPush
- Angular Signals
- Performance Profiling
