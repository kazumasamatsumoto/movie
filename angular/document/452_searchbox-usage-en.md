# #452 "Search Box Usage"

## Overview
Applying debounce to search boxes improves efficiency and user experience by performing searches after a certain period of time instead of calling API with every typed input.

## Learning Objectives
- Understand the advantages of applying debounce to search boxes
- Learn how to receive Output events in components and connect to search processing
- Combine with loading control and error handling

## Technical Points
- Apply Debounce directive to input element
- Receive search term in Output event and call service
- Reflect loading state in UI

## 📺 On-Screen Code (for video)
```html
<input appDebounce [debounceTime]="400" (debounce)="search($event)" />
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-search-box',
  standalone: true,
  imports: [CommonModule, FormsModule, DebounceDirective],
  template: `
    <label>
      Search
      <input appDebounce [debounceTime]="400" (debounce)="search($event)" />
    </label>
    <p *ngIf="loading">Searching...</p>
    <ul>
      <li *ngFor="let item of results">{{ item }}</li>
    </ul>
  `
})
export class SearchBoxComponent {
  protected results: string[] = [];
  protected loading = false;

  protected search(keyword: string): void {
    this.loading = true;
    fakeApi(keyword).subscribe(data => {
      this.results = data;
      this.loading = false;
    });
  }
}
```

## Best Practices
- Adjust delay time according to API performance and UX
- Clearly define processing for empty string input (such as clearing search results)
- Display loading indicator to provide feedback to users

## Considerations
- Confirm requirements as delay can harm UX when rapid response is needed
- Set result discard conditions if API response order changes midway
- Display error message when search after debounce fails

## Related Technologies
- Observable search (RxJS switchMap)
- Angular HttpClient
- DebounceDirective
