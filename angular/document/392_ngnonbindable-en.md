# #392 "ngNonBindable - Disabling Binding"

## Overview
`ngNonBindable` disables Angular's binding evaluation and is used when you want to display templates like `{{ }}` or `<app-component>` as-is.

## Learning Objectives
- Understand the use cases and behavior of `ngNonBindable`
- Learn how to utilize it for documentation display or sample code embedding
- Grasp design patterns for partially disabling binding

## Technical Points
- Specified as an attribute (e.g., `<div ngNonBindable>...</div>`)
- Angular expressions and directives under the element are not evaluated
- Can also suppress evaluation in SSR

## 📺 Display Code (for video)
```html
<code ngNonBindable>{{ user.name }}</code>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-non-bindable-demo',
  standalone: true,
  template: `
    <p>Display Angular expressions as-is</p>
    <pre ngNonBindable>
      {{ hero.name }} lives in {{ hero.city }}
    </pre>
  `
})
export class NonBindableDemoComponent {}
```

## Best Practices
- Utilize for displaying templates in documentation components or Markdown viewers
- Prepare wrapper elements and disable binding only for the necessary scope
- Convenient when displaying sample code combined with highlight libraries

## Considerations
- Directives written within disabled elements won't function, so use with clear intent
- Sanitization is needed when mixing with user-entered content
- `ngNonBindable` cannot be attached to self-closing tags, so secure an enclosing element

## Related Technologies
- Markdown Rendering
- Syntax Highlight
- Angular Universal
