# #310 "Selector Definition"

## Overview
A Directive's selector is an identifier that determines application targets, and can be specified in multiple formats such as elements, attributes, and classes. Organizing naming conventions prevents collisions.

## Learning Objectives
- Understand basic selector formats (element, attribute, class)
- Learn notation for combining multiple selectors
- Practice selector design following project naming conventions

## Technical Points
- `selector: '[appX]'` for attributes, `selector: '.appX'` for classes, `selector: 'app-x'` for elements
- Multiple selectors can be defined with comma separation
- Declaration method is the same for both Standalone and traditional NgModule

## 📺 Display Code (For Video)
```typescript
@Directive({
  selector: 'button[appCta], a[appCta], [appPrimary]',
  standalone: true
})
export class CtaDirective {}
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Directive({
  selector: 'button[appCta], a[appCta], [appPrimary]',
  standalone: true
})
export class CtaDirective {
  @Input() appPrimary = true;
  @HostBinding('class.is-primary') get isPrimary(): boolean {
    return this.appPrimary;
  }
}

@Component({
  selector: 'app-selector-demo',
  standalone: true,
  imports: [CommonModule, CtaDirective],
  template: `
    <button appCta>CTA button</button>
    <a appCta href="#">CTA link</a>
    <span appPrimary="false">Styled element</span>
  `
})
export class SelectorDemoComponent {}
```

## Best Practices
- Unify project-specific prefixes (e.g., `app`, `lib`) to avoid collisions
- Use meaningful naming by role when providing multiple selectors
- Clearly document usage in API documentation when mixing attributes and classes

## Cautions
- Element selectors may be treated as unknown tags by HTML validators
- When multiple selectors hit the same element, responsibilities mix, so organize priorities
- Follow HTML specification for case handling and unify to lowercase

## Related Technologies
- Angular Style Guide
- HostDirectives
- Schematics naming conventions
