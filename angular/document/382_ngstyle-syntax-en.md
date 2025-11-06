# #382 "[ngStyle] Basic Syntax"

## Overview
`[ngStyle]` is a syntax that specifies style properties and values using an object, allowing you to apply multiple styles at once.

## Learning Objectives
- Understand the `[ngStyle]` syntax
- Grasp how to write property names and values
- Master style application combined with conditional expressions and calculations

## Technical Points
- Property names can be in camelCase or hyphenated strings
- Numbers are converted to strings, so units must be added
- Falsy values can be used to remove styles

## 📺 Display Code (for video)
```html
<div [ngStyle]="{ borderColor: accentColor, borderWidth: border + 'px', borderStyle: 'solid' }"></div>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-ngstyle-syntax-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div [ngStyle]="boxStyle">Box</div>
  `
})
export class NgStyleSyntaxDemoComponent {
  protected border = 2;
  protected accentColor = '#38bdf8';

  protected get boxStyle(): Record<string, string> {
    return {
      borderColor: this.accentColor,
      borderWidth: `${this.border}px`,
      borderStyle: 'solid',
      padding: '1rem',
      borderRadius: '0.75rem'
    };
  }
}
```

## Best Practices
- Build style objects in the component to minimize template logic
- Use template literals to avoid forgetting units
- Define shared styles as CSS classes and limit ngStyle to differences only

## Considerations
- Properties with hyphens in strings require quotes like `'background-color'`
- For large-scale style control, consider creating dedicated directives as view responsibilities expand
- Memoization is effective when objects are frequently regenerated during change detection

## Related Technologies
- Renderer2
- CSS Custom Properties
- HostBinding
