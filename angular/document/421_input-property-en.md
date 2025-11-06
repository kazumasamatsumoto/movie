# #421 "@Input() Property"

## Overview
The `@Input()` decorator is a mechanism for passing values from templates to directives, allowing flexible management of attribute names and property names through alias specification.

## Learning Objectives
- Understand `@Input()` syntax and alias settings
- Learn safe Input design with type annotations
- Understand the processing flow when Input changes

## Technical Points
- `@Input() color = '#facc15';`
- `@Input('appHighlight') set highlight(color: string) {...}`
- Detect changes with `ngOnChanges(changes: SimpleChanges)`

## 📺 On-Screen Code (for video)
```typescript
@Input('appHighlight') color = '#fde047';
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appHighlight]',
  standalone: true
})
export class HighlightDirective implements OnChanges {
  @Input('appHighlight') color = '#fde047';

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnChanges(): void {
    this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', this.color);
  }
}
```

## Best Practices
- Make template binding names easier to understand with attribute name aliases
- Restrict received values with Union types or interfaces for type safety
- Execute side effects only when changes occur to avoid unnecessary updates

## Considerations
- Guard against using Input properties before initialization
- Be aware of change detection frequency and delay heavy processing
- Even with standalone directives, `@Input` can be used but don't forget `imports` registration

## Related Technologies
- OnChanges
- Signals and Input
- Directive API design
