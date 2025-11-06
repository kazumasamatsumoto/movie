# #367 "Applying Multiple Directives"

## Overview
Since only one Structural Directive can be applied per element, split elements with `ng-container` when combining multiple directives.

## Learning Objectives
- Understand constraints on applying multiple directives
- Learn splitting techniques using `ng-container`
- Grasp patterns for combining with Attribute Directives

## Technical Points
- Structural Directives can't coexist as they replace templates
- Apply processing stepwise with `ng-container` or child components
- Attribute Directives can be used together on same element

## 📺 Screen Display Code (For Video)
```html
<ng-container *ngIf="ready">
  <li *ngFor="let item of items">{{ item }}</li>
</ng-container>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-multi-directive-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ng-container *ngIf="filtered().length">
      <p *ngFor="let tag of filtered(); trackBy: trackByTag">{{ tag }}</p>
    </ng-container>
  `
})
export class MultiDirectiveDemoComponent {
  private readonly tagsSignal = signal(['Angular', 'Directive', 'Signals']);
  protected filtered = computed(() => this.tagsSignal().filter(tag => tag.length > 4));

  protected trackByTag(_: number, tag: string): string {
    return tag;
  }
}
```

## Best Practices
- Clarify intent with `ng-container` when applying multiple structural directives in sequence
- Check for excessive directive nesting in code reviews
- Combine Attribute Directives with style control etc. to separate template responsibilities

## Cautions
- Writing `*ngIf` and `*ngFor` on same element causes build error
- Avoid excessive `ng-container` added for splitting
- Clarify naming and responsibilities when combining custom Structural Directives

## Related Technologies
- ng-container
- Attribute Directives
- Custom Structural Directives
