# #365 "Utilizing ng-container"

## Overview
`ng-container` is a virtual container that can apply structural directives without generating actual DOM elements, helping keep markup clean.

## Learning Objectives
- Understand the role and use cases of ng-container
- Learn how to combine directives without increasing DOM
- Master techniques for organizing conditions and loops

## Technical Points
- `ng-container` is not rendered, only exists within templates
- Acts as a bridge to apply multiple structural directives in sequence
- Can also be used as template reference with `#ref`

## 📺 Screen Display Code (For Video)
```html
<ng-container *ngIf="items.length">
  <li *ngFor="let item of items">{{ item }}</li>
</ng-container>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-ng-container-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ng-container *ngIf="menu().length; else emptyTpl">
      <button *ngFor="let action of menu()">{{ action }}</button>
    </ng-container>
    <ng-template #emptyTpl>
      <p>No actions available.</p>
    </ng-template>
  `
})
export class NgContainerDemoComponent {
  private readonly menuSignal = signal<string[]>(['Save', 'Share', 'Delete']);
  protected menu = this.menuSignal.asReadonly();
}
```

## Best Practices
- Avoid unnecessary div wrapping, maintaining structure that doesn't affect CSS or accessibility
- Insert `ng-container` when combining multiple directives
- Organize template logic per block to improve readability

## Cautions
- `ng-container` doesn't appear in DOM, so can't directly apply styles or events
- Excessive nesting makes it harder to read, so use moderately
- Since it doesn't appear in DOM during testing, template understanding is needed to understand structure

## Related Technologies
- ng-template
- Structural Directives
- Accessibility
