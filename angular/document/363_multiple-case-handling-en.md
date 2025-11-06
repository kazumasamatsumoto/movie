# #363 "Handling Multiple Cases"

## Overview
When displaying the same UI for multiple cases, defining multiple `*ngSwitchCase` and sharing `ng-template` avoids duplication.

## Learning Objectives
- Understand how to reuse the same template across multiple cases
- Learn utilization and scope of template references
- Design correspondence between state management and UI

## Technical Points
- Consolidate common UI in `ng-template` and reference from multiple cases
- Branch internally when additional processing per case is needed
- Classify states to group cases

## 📺 Screen Display Code (For Video)
```html
<ng-template #reviewTpl><p>Awaiting review</p></ng-template>
<ng-container *ngSwitchCase="'draft'">
  <ng-container *ngTemplateOutlet="reviewTpl"></ng-container>
</ng-container>
<ng-container *ngSwitchCase="'pending'">
  <ng-container *ngTemplateOutlet="reviewTpl"></ng-container>
</ng-container>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
type ReviewState = 'draft' | 'pending' | 'approved' | 'rejected';

@Component({
  selector: 'app-multi-case-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ng-template #reviewTpl>
      <p>Under review state.</p>
    </ng-template>
    <section [ngSwitch]="state">
      <ng-container *ngSwitchCase="'draft'">
        <ng-container *ngTemplateOutlet="reviewTpl"></ng-container>
      </ng-container>
      <ng-container *ngSwitchCase="'pending'">
        <ng-container *ngTemplateOutlet="reviewTpl"></ng-container>
      </ng-container>
      <p *ngSwitchCase="'approved'">Approved.</p>
      <p *ngSwitchCase="'rejected'">Rejected.</p>
      <p *ngSwitchDefault>Unclassified state.</p>
    </section>
  `
})
export class MultiCaseDemoComponent {
  protected state: ReviewState = 'draft';
}
```

## Best Practices
- Utilize `ng-template` when using same template for multiple cases to follow DRY principle
- Further organize by consolidating states into another enum
- Verify in tests that each state's display and common template applies correctly

## Cautions
- Prior to Angular v17, `ngSwitchCase` can't directly receive multiple values, so share via template reference
- Separate responsibilities to avoid state-specific processing in common templates
- Update tests when cases are added/changed as common templates are affected

## Related Technologies
- ng-template
- DRY Principle
- State Management
