# #339 "Using else Blocks"

## Overview
The else block in `*ngIf` is a template displayed when the condition is false, allowing explicit definition of fallback UI.

## Learning Objectives
- Understand how to design and manage else blocks
- Handle template reference scope appropriately
- Reuse common fallback templates

## Technical Points
- Templates referenced by `else` are defined within the same scope
- Manage without increasing DOM by using in combination with `ng-container`
- Enhance versatility by passing context to templates

## 📺 On-Screen Code (for video)
```html
<article *ngIf="items.length; else empty">List display</article>
<ng-template #empty><p>No items.</p></ng-template>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-else-block-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ul *ngIf="products.length; else emptyTpl">
      <li *ngFor="let product of products">{{ product }}</li>
    </ul>
    <ng-template #emptyTpl>
      <p>No products registered.</p>
      <button type="button" (click)="seed()">Add dummy data</button>
    </ng-template>
  `
})
export class ElseBlockDemoComponent {
  protected products: string[] = [];

  protected seed(): void {
    this.products = ['Angular Handbook', 'Directive Mastery'];
  }
}
```

## Best Practices
- Clearly state operation methods and next actions in fallback templates
- When used by multiple elements, extract `ng-template` to a separate component
- In tests, verify both true and false cases and confirm templates switch correctly

## Considerations
- Elements in else templates are newly generated when displayed, so form states etc. are reset
- Sharing `#elseTpl` in nested `*ngIf` may cause scope collisions
- In SSR, condition mismatches cause Hydration errors, so align judgments

## Related Technologies
- ng-container
- Angular Testing Library
- SSR/Hydration
