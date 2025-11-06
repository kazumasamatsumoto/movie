# #420 "Receiving Configuration with Input"

## Overview
By defining `@Input` in a Directive, you can receive configuration values from the consumer template and flexibly customize behavior.

## Learning Objectives
- Understand how to declare `@Input` properties
- Learn attribute name and property name alias settings
- Understand configuration value validation and default application patterns

## Technical Points
- `@Input() appHighlightColor = '#facc15';`
- `@Input('appHighlight') set config(value: HighlightOptions)`
- Validation and fallback processing with `ngOnChanges`

## 📺 On-Screen Code (for video)
```typescript
@Input() appHighlight = '#fde047';
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appHighlight]',
  standalone: true
})
export class HighlightDirective implements OnChanges {
  @Input() appHighlight = '#fde047';

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnChanges(): void {
    this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', this.appHighlight);
  }
}
```

## Best Practices
- Make Input type-safe and document the meaning of received values
- Perform validation and conversion with Setter or `ngOnChanges`
- Set default values to operate safely even without configuration

## Considerations
- When receiving arguments as objects, make reference immutable with `trackBy`, etc.
- Use lifecycle hooks appropriately when side effects are needed on Input changes
- Consider combination with `@Output()` if two-way binding is needed

## Related Technologies
- @Input decorator
- OnChanges
- Directive API design
