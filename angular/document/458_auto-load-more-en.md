# #458 "Auto Load More Data"

## Overview
Auto loading more data is achieved through a flow where scroll monitoring events fire Output, and the component side calls API to expand the list.

## Learning Objectives
- Understand the event flow of auto loading
- Learn how to make service calls through Output events
- Grasp loading state and duplicate call prevention measures

## Technical Points
- `loadMore` event with Output
- Manage loading flag in component
- Resume scroll monitoring after completion

## 📺 On-Screen Code (for video)
```html
<div appInfiniteScroll (scrolled)="loadMore()" [disabled]="loading"></div>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-infinite-list',
  standalone: true,
  imports: [CommonModule, InfiniteScrollDirective],
  template: `
    <div class="list" appInfiniteScroll (scrolled)="loadMore()" [disabled]="loading">
      <article *ngFor="let item of items">{{ item }}</article>
      <p *ngIf="loading">Loading...</p>
    </div>
  `
})
export class InfiniteListComponent {
  protected items = Array.from({ length: 20 }, (_, i) => `Item ${i}`);
  protected loading = false;

  protected loadMore(): void {
    if (this.loading) return;
    this.loading = true;
    fakeFetch(this.items.length).subscribe(more => {
      this.items = [...this.items, ...more];
      this.loading = false;
    });
  }
}
```

## Best Practices
- Disable directive during loading state to prevent duplicate loading
- Implement retry and error messages for API failures
- Inform directive of load completion (all items retrieved) to stop monitoring

## Considerations
- Adjust initial data amount to avoid loop-like calls in cases where end is reached immediately
- Set appropriate threshold as scroll speed is fast in mobile environments
- Stop monitoring when new data is empty

## Related Technologies
- IntersectionObserver
- RxJS switchMap/concatMap
- Loading indicator
