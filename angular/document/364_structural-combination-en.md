# #364 "Combining Structural Directives"

## Overview
Combining Structural Directives can express complex UI logic, but requires using `ng-container` to prevent excessive DOM growth while separating responsibilities.

## Learning Objectives
- Understand patterns for combining multiple structural directives
- Learn techniques to organize DOM structure
- Grasp refactoring strategies to keep templates small

## Technical Points
- Cannot apply multiple structural directives to same element, so split with `ng-container`
- Organizing logic in order of condition → loop → branching improves readability
- Delegate responsibilities to child components for complex cases

## 📺 Screen Display Code (For Video)
```html
<ng-container *ngIf="isReady">
  <li *ngFor="let item of items" [ngSwitch]="item.type"></li>
</ng-container>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-structural-combo-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ng-container *ngIf="items().length; else emptyTpl">
      <div *ngFor="let item of items(); trackBy: trackById">
        <ng-container [ngSwitch]="item.type">
          <p *ngSwitchCase="'text'">{{ item.value }}</p>
          <p *ngSwitchCase="'link'"><a [href]="item.href">{{ item.value }}</a></p>
          <p *ngSwitchDefault>Unsupported type</p>
        </ng-container>
      </div>
    </ng-container>
    <ng-template #emptyTpl>
      <p>No items.</p>
    </ng-template>
  `
})
export class StructuralComboDemoComponent {
  private readonly itemsSignal = signal([
    { id: 1, type: 'text', value: 'Hello Angular' },
    { id: 2, type: 'link', value: 'Official Docs', href: 'https://angular.dev' }
  ]);
  protected items = this.itemsSignal.asReadonly();

  protected trackById(_: number, item: { id: number }): number {
    return item.id;
  }
}
```

## Best Practices
- Layer directives with `ng-container` to intentionally separate structure
- Consider component decomposition when conditions or branching becomes complex
- Add comments per section to prevent templates from becoming too long

## Cautions
- Overusing `ng-container` makes understanding difficult, so maintain balance
- Clarify Input contracts when extracting to child components
- For high performance requirements, optimize logic by creating custom structural directives

## Related Technologies
- ng-container
- Component Composition
- Custom Structural Directives
