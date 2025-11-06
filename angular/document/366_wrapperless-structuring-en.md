# #366 "Wrapperless Structuring"

## Overview
Utilizing `ng-container` and `ng-template` allows applying structural directives without increasing wrapper elements, enabling logic addition without breaking existing layouts.

## Learning Objectives
- Understand how to apply conditions and loops wrapperlessly
- Learn design techniques to keep DOM minimal
- Minimize impact on accessibility and styling

## Technical Points
- `ng-container` doesn't output to DOM, so no extra divs are added
- `ng-template` lazily evaluates templates, inserting only when needed
- Same concept applies when migrating to Control Flow syntax (@if/@for)

## 📺 Screen Display Code (For Video)
```html
<ng-container *ngIf="visible">
  <button *ngFor="let action of actions">{{ action }}</button>
</ng-container>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-wrapperless-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <header>
      <h2>{{ title }}</h2>
      <ng-container *ngIf="actions.length">
        <button *ngFor="let action of actions" type="button">{{ action }}</button>
      </ng-container>
    </header>
  `
})
export class WrapperlessDemoComponent {
  protected title = 'Wrapperless Structure';
  protected actions = ['Save', 'Share'];
}
```

## Best Practices
- Control with `ng-container` without adding wrappers where markup structure matters
- Define CSS selectors for actual elements, not assuming `ng-container`
- Be conscious of DOM structure minimization when migrating to Control Flow syntax

## Cautions
- Can't attach attributes to `ng-container`, so prepare actual elements if needed
- Becomes hard to read when containing complex logic, so consider component decomposition as appropriate
- `ng-container` isn't output with SSR, but verify template consistency

## Related Technologies
- ng-container
- Control Flow Syntax
- Accessibility
