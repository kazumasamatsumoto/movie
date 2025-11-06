# #322 "Setting Styles with setStyle()"

## Overview
`Renderer2.setStyle` is a safe method for adding inline styles, allowing control over priority and `!important` specification.

## Learning Objectives
- Understand the arguments and return value of `setStyle`
- Learn the balance between applying and removing styles
- Know how to utilize `RendererStyleFlags2`

## Technical Points
- Arguments are `(element, styleName, value, flags?)`
- Use `RendererStyleFlags2.Important` for `!important` specification
- Remove with `removeStyle`

## 📺 On-Screen Code (for video)
```typescript
@Directive({ selector: '[appDim]', standalone: true })
export class DimDirective implements OnChanges {
  @Input({ alias: 'appDim' }) level = 0.5;
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly r: Renderer2) {}
  ngOnChanges(): void {
    this.r.setStyle(this.el.nativeElement, 'opacity', String(this.level));
  }
}
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appDim]',
  standalone: true
})
export class DimDirective implements OnChanges, OnDestroy {
  @Input({ alias: 'appDim' }) level = 0.5;
  @Input() important = false;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnChanges(): void {
    const flags = this.important ? RendererStyleFlags2.Important : undefined;
    this.renderer.setStyle(this.el.nativeElement, 'opacity', String(this.level), flags);
  }

  ngOnDestroy(): void {
    this.renderer.removeStyle(this.el.nativeElement, 'opacity');
  }
}
```

## Best Practices
- Clean up with `removeStyle` to avoid leaving unnecessary inline styles
- Avoid overusing `RendererStyleFlags2.Important` and prioritize CSS design
- When handling numbers, pass them in a consistent format such as stringifying and adding units

## Considerations
- Conflicts may occur if different directives touch the same property on the same element
- When applying transitions, suppress flickering with delayed updates
- In SSR, styles are output inline, so verify consistency with CSS

## Related Technologies
- RendererStyleFlags2
- HostBinding
- CSS Design
