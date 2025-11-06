# #342 "*ngIf=\"value as alias\" - Alias"

## Overview
`*ngIf="expr as alias"` is a syntax that allows you to reuse the evaluation result as a template variable when the condition is satisfied, avoiding redundant re-evaluation of expressions.

## Learning Objectives
- Understand how to define aliases using the `as` syntax
- Learn template patterns for safely handling asynchronous data
- Grasp practical examples combining with null checks

## Technical Points
- Use `*ngIf="user$ | async as user"` to receive async values
- Reference the `alias` within the template and omit null checks
- Combine with `else` to provide fallback

## 📺 Screen Display Code (For Video)
```html
<section *ngIf="profile$ | async as profile">
  <h3>{{ profile.name }}</h3>
</section>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-if-alias-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <article *ngIf="user$ | async as user; else loadingTpl">
      <h2>{{ user.name }}</h2>
      <p>{{ user.description }}</p>
    </article>
    <ng-template #loadingTpl>
      <p>Loading user...</p>
    </ng-template>
  `
})
export class IfAliasDemoComponent {
  protected user$ = of({ name: 'Alias User', description: 'Example of alias syntax' }).pipe(delay(400));
}
```

## Best Practices
- Aliases obtained with the `as` syntax are read-only, so make changes on the component side
- When handling asynchronous data, combine with `AsyncPipe` to automate unsubscription
- Use short descriptive words for alias names (`user`, `result`, etc.)

## Cautions
- The `as` syntax only has the alias when the condition is true, so be careful referencing it when false
- Attempting to reassign an alias will cause a template error
- Even if an Observable result is `undefined`, it's treated the same as `false`, so consider default values

## Related Technologies
- AsyncPipe
- RxJS Observable
- Null Safety Patterns
