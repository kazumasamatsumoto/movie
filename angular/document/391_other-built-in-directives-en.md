# #391 "Other Built-in Directives"

## Overview
Besides `ngClass` and `ngStyle`, Angular has various other Attribute Directives that enhance template expressiveness and support dynamic rendering.

## Learning Objectives
- Grasp the types of major built-in Attribute Directives
- Be able to select appropriate directives for each use case
- Envision combination with custom directives

## Technical Points
- `ngNonBindable`, `ngPlural`, `ngTemplateOutlet`, `ngComponentOutlet`, etc.
- Special-purpose directives are included in `CommonModule` or `RouterModule`
- When using, need `imports` configuration compatible with standalone components

## 📺 Display Code (for video)
```html
<ng-container [ngTemplateOutlet]="itemTpl" [ngTemplateOutletContext]="{ $implicit: item }"></ng-container>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-builtins-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <p ngNonBindable>{{ magic incantation }}</p>
    <ng-container [ngTemplateOutlet]="cardTpl" [ngTemplateOutletContext]="{ $implicit: 'Angular' }"></ng-container>
    <ng-template #cardTpl let-name>
      <article class="card">Hello {{ name }}</article>
    </ng-template>
  `
})
export class BuiltinsDemoComponent {}
```

## Best Practices
- Catalog built-in directives and share appropriate use cases with the team
- In standalone environments, explicitly add necessary directives to `imports`
- Organize naming conventions to avoid conflicts with custom directives

## Considerations
- Directives exported vary by module, so check dependencies
- Dynamic rendering directives may affect performance, so take profiles
- Check official documentation for SSR support

## Related Technologies
- CommonModule
- RouterModule
- Angular Material directive suite
