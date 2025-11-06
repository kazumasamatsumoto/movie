# #393 "ngPlural - Plural Control"

## Overview
`ngPlural` is a directive that switches templates based on numeric values, making it easy to express plural differences in multilingual support.

## Learning Objectives
- Understand the relationship between `ngPlural` and `ngPluralCase`
- Learn how to define categories (=0, =1, other, etc.)
- Grasp best practices for handling plurals in internationalization

## Technical Points
- Specify target numeric value with `[ngPlural]="count"`
- Define cases with `<ng-template ngPluralCase="=0">`, etc.
- Always provide an `other` case

## 📺 Display Code (for video)
```html
<p [ngPlural]="items.length">
  <ng-template ngPluralCase="=0">No items</ng-template>
  <ng-template ngPluralCase="=1">1 item</ng-template>
  <ng-template ngPluralCase="other">{{ items.length }} items</ng-template>
</p>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-ngplural-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <p [ngPlural]="count">
      <ng-template ngPluralCase="=0">No notifications</ng-template>
      <ng-template ngPluralCase="=1">1 notification</ng-template>
      <ng-template ngPluralCase="other">{{ count }} notifications</ng-template>
    </p>
  `
})
export class NgPluralDemoComponent {
  protected count = 3;
}
```

## Best Practices
- When combining with i18n, manage plural messages in translation files
- Check `Intl.PluralRules` to grasp the number of cases per language
- Also adjust numeric formatting with `DecimalPipe`, etc.

## Considerations
- If case specification is forgotten, it falls back to `other`, so define all necessary cases
- Depending on language, additional categories like `dual`, `few`, `many` may be needed
- If count is non-numeric, an error occurs, so be strict with types

## Related Technologies
- Angular i18n
- Intl.PluralRules
- Transloco/ngx-translate
