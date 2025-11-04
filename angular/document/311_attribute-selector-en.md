# #311 "Attribute Selector [appXxx]"

## Overview
Attribute selectors are the most common way to apply directives, allowing behavior to be added to existing elements like attributes. They also work well with binding.

## Learning Objectives
- Understand attribute selector syntax and application methods
- Master the procedure for passing values through binding
- Learn cautions when coexisting with multiple attributes

## Technical Points
- Enclose in brackets like `selector: '[appHighlight]'`
- Templates can use `<div appHighlight></div>` or `[appHighlight]="value"` notation
- Align with property name using `@Input({ alias: 'appHighlight' })`

## 📺 Display Code (For Video)
```typescript
@Directive({ selector: '[appHighlight]', standalone: true })
export class HighlightDirective {
  @Input({ alias: 'appHighlight' }) color = '#fde047';
  constructor(private readonly renderer: Renderer2, private readonly el: ElementRef<HTMLElement>) {}
  ngOnChanges(): void {
    this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', this.color);
  }
}
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Directive({
  selector: '[appHighlight]',
  standalone: true
})
export class HighlightDirective implements OnChanges {
  @Input({ alias: 'appHighlight' }) color = '#fde047';
  @Input() appHighlightHover?: string;

  constructor(private readonly renderer: Renderer2, private readonly el: ElementRef<HTMLElement>) {}

  ngOnChanges(): void {
    this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', this.color);
  }

  @HostListener('mouseenter')
  onMouseEnter(): void {
    if (this.appHighlightHover) {
      this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', this.appHighlightHover);
    }
  }

  @HostListener('mouseleave')
  onMouseLeave(): void {
    this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', this.color);
  }
}

@Component({
  selector: 'app-attribute-selector-demo',
  standalone: true,
  imports: [CommonModule, HighlightDirective],
  template: `
    <p appHighlight="#fef3c7" [appHighlightHover]="'#facc15'">
      Switch background color with attribute selector.
    </p>
  `
})
export class AttributeSelectorDemoComponent {}
```

## Best Practices
- Use Input alias to align template attribute names with property names
- Prepare default values so it doesn't break even if consumers omit values
- Limit style override scope to coexist with other attributes

## Cautions
- Writing complex expressions in binding reduces readability, so pass calculated values from the view side
- Attribute order doesn't matter, but unify team formatting rules to reduce diffs
- In SSR, DOM events don't work, so verify initial state is appropriate

## Related Technologies
- HostBinding / HostListener
- Renderer2
- Angular Style Guide
