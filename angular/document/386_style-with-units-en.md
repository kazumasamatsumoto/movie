# #386 "Specifying Values with Units"

## Overview
When handling numeric values in `ngStyle`, you need to pass strings with units like `'16px'`, and managing them uniformly with template literals or helpers is safe.

## Learning Objectives
- Understand the reason and method for adding units to style values
- Learn techniques for adding units with template literals or helper functions
- Grasp the difference between unitless properties and unit-required properties

## Technical Points
- Pass CSS units like `px`, `rem`, `%` as strings
- Some properties like `lineHeight` can handle numeric values, but unifying is more readable
- Providing helpers like `px(value)` improves reusability

## 📺 Display Code (for video)
```html
<div [ngStyle]="{ width: width + 'px', height: height + 'px' }">Size</div>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-style-with-units-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div [ngStyle]="boxStyle()">Resizable</div>
    <input type="range" min="100" max="300" [value]="size" (input)="update($event)" />
  `
})
export class StyleWithUnitsDemoComponent {
  protected size = 150;

  protected boxStyle(): Record<string, string> {
    return {
      width: `${this.size}px`,
      height: `${this.size}px`,
      borderRadius: '1rem',
      background: '#38bdf8'
    };
  }

  protected update(event: Event): void {
    this.size = Number((event.target as HTMLInputElement).value);
  }
}
```

## Best Practices
- Add units with helper functions to reduce string concatenation in templates
- Unify units used by the team to avoid mixing `px` and `rem`
- Consider stringifying even properties that can handle direct numeric specification for readability

## Considerations
- Passing numeric values directly like `borderWidth={2}` may result in unintended rendering
- When using `rem` or `em` for internationalization, pay attention to base font size
- If unit addition is missed, output like `NaNpx` may occur, so add validation

## Related Technologies
- CSS Units
- Template Literals
- Angular Forms
