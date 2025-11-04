# #313 "Element Selector xxx"

## Overview
Element selectors apply directives with custom tag names, allowing semantic meaning and accessibility assistance without templates.

## Learning Objectives
- Understand element selector definition methods
- Balance custom elements with accessibility
- Learn judgment criteria for treating as Directive rather than Component

## Technical Points
- Specify with tag name like `selector: 'app-marquee'`
- DOM structure is composed of existing elements, Directive focuses on behavior and attribute completion
- Directive supplements accessibility attributes like `role` and `aria-*`

## 📺 Display Code (For Video)
```typescript
@Directive({ selector: 'app-marquee', standalone: true })
export class MarqueeDirective {
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}
  ngOnInit(): void {
    this.renderer.setAttribute(this.el.nativeElement, 'role', 'marquee');
  }
}
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Directive({
  selector: 'app-marquee',
  standalone: true
})
export class MarqueeDirective implements OnInit, OnDestroy {
  @Input() speed = 50;
  private animationId?: number;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    const element = this.el.nativeElement;
    this.renderer.setAttribute(element, 'role', 'marquee');
    this.renderer.setAttribute(element, 'aria-live', 'polite');
    const animate = () => {
      element.scrollLeft = (element.scrollLeft + 1) % element.scrollWidth;
      this.animationId = requestAnimationFrame(animate);
    };
    this.animationId = requestAnimationFrame(animate);
  }

  ngOnDestroy(): void {
    if (this.animationId) cancelAnimationFrame(this.animationId);
  }
}

@Component({
  selector: 'app-marquee-demo',
  standalone: true,
  imports: [CommonModule, MarqueeDirective],
  template: `
    <app-marquee class="marquee">
      <span>Adding custom element-like behavior with Directive.</span>
    </app-marquee>
  `,
  styles: [`
    .marquee { display: block; overflow: hidden; white-space: nowrap; }
    .marquee span { display: inline-block; padding-right: 2rem; }
  `]
})
export class MarqueeDemoComponent {}
```

## Best Practices
- Prefix custom tags to avoid collisions with browser native elements
- Consider accessibility and automatically supplement role and aria attributes
- Minimize DOM structure changes to prevent Directive from having too many responsibilities

## Cautions
- Test if unknown tags are handled correctly in SEO and SSR
- Specify styles on CSS side, Directive focuses on semantics and behavior
- Different from Custom Elements (Angular Elements), don't confuse them

## Related Technologies
- Angular Elements
- Renderer2
- Accessibility (ARIA)
