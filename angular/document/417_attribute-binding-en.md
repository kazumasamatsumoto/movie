# #417 "attribute Binding"

## Overview
`@HostBinding('attr.<name>')` can directly manage attribute values and is suitable for controlling ARIA attributes and data attributes with directives.

## Learning Objectives
- Understand attribute binding syntax
- Learn patterns for dynamically updating ARIA attributes
- Understand that attribute deletion is possible with null/undefined

## Technical Points
- `@HostBinding('attr.aria-expanded')`
- Boolean attributes are added/removed with empty string or null
- Control data attributes with `attr.data-state`

## 📺 On-Screen Code (for video)
```typescript
@HostBinding('attr.aria-busy') get ariaBusy(): 'true' | null { return this.loading ? 'true' : null; }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appAriaBusy]',
  standalone: true
})
export class AriaBusyDirective {
  @Input() loading = false;

  @HostBinding('attr.aria-busy')
  get ariaBusy(): 'true' | null {
    return this.loading ? 'true' : null;
  }
}
```

## Best Practices
- Standardize accessibility attributes with Directive to keep markup concise
- Utilize the specification that returning null removes attributes, avoiding unnecessary attributes
- Expose state with data attributes for easy reference from CSS and tests

## Considerations
- Need to return as string, so directly returning boolean results in `true/false` strings
- Unify attribute names to lowercase to ensure browser compatibility
- Verify in tests that required attributes like form attributes are not mistakenly deleted

## Related Technologies
- Accessibility (ARIA)
- HostBinding
- Testing Library selectors
