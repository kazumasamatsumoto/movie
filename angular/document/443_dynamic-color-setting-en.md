# #443 "Dynamic Color Setting"

## Overview
By passing colors to the Highlight directive via Input, different emphasis colors can be used for each component. Provides flexible configuration while maintaining default values.

## Learning Objectives
- Understand techniques for dynamically receiving colors via Input
- Learn how to reflect values using `ngOnChanges` or setters
- Grasp merging with default values and validation

## Technical Points
- `@Input('appHighlight') color = '#fde047';`
- Reflect to style with setter or `ngOnChanges`
- Fallback for invalid color codes

## 📺 On-Screen Code (for video)
```typescript
@Input('appHighlight') set color(value: string) { this.background = value ?? '#fde047'; }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appHighlight]',
  standalone: true
})
export class HighlightDirective implements OnChanges {
  private readonly defaultColor = '#fde047';
  @Input('appHighlight') color?: string;
  @HostBinding('style.backgroundColor') background = this.defaultColor;

  ngOnChanges(): void {
    this.background = this.isValidColor(this.color) ? this.color! : this.defaultColor;
  }

  private isValidColor(value?: string): boolean {
    return !!value && /^#([0-9a-f]{3}|[0-9a-f]{6})$/i.test(value);
  }
}
```

## Best Practices
- Prepare validation and default values for invalid inputs
- Consider structures that accept `CSSColorValue` in addition to color codes
- Document accepted formats (HEX, RGB, etc.) clearly

## Considerations
- Style conflicts occur if color code formats are not unified
- Consider performance if Input changes frequently
- Set initial background to ensure initial color is reliably reflected in SSR

## Related Technologies
- Input Transform
- HostBinding
- Color validation utilities
