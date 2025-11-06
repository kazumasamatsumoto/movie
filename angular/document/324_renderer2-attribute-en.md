# #324 "setAttribute() / removeAttribute()"

## Overview
`setAttribute` and `removeAttribute` are used to dynamically control accessibility and data attributes, enabling value setting that follows HTML specifications.

## Learning Objectives
- Understand the mechanism and uses of attribute manipulation
- Learn how to handle Boolean and ARIA attributes
- Manage removal timing

## Technical Points
- Boolean attributes are enabled with an empty string and removed with `removeAttribute`
- `setAttribute` expects string values, so perform type conversion
- ARIA attributes are effective for improving accessibility

## 📺 On-Screen Code (for video)
```typescript
@Directive({ selector: '[appBusy]', standalone: true })
export class BusyDirective implements OnChanges {
  @Input({ alias: 'appBusy' }) busy = false;
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly r: Renderer2) {}
  ngOnChanges(): void {
    if (this.busy) this.r.setAttribute(this.el.nativeElement, 'aria-busy', 'true');
    else this.r.removeAttribute(this.el.nativeElement, 'aria-busy');
  }
}
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appBusy]',
  standalone: true
})
export class BusyDirective implements OnChanges, OnDestroy {
  @Input({ alias: 'appBusy' }) busy = false;
  @Input() label?: string;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnChanges(): void {
    const host = this.el.nativeElement;
    if (this.busy) {
      this.renderer.setAttribute(host, 'aria-busy', 'true');
      this.renderer.setAttribute(host, 'aria-live', 'polite');
      if (this.label) {
        this.renderer.setAttribute(host, 'aria-label', this.label);
      }
    } else {
      this.renderer.removeAttribute(host, 'aria-busy');
      this.renderer.removeAttribute(host, 'aria-live');
      if (this.label) {
        this.renderer.removeAttribute(host, 'aria-label');
      }
    }
  }

  ngOnDestroy(): void {
    const host = this.el.nativeElement;
    this.renderer.removeAttribute(host, 'aria-busy');
    this.renderer.removeAttribute(host, 'aria-live');
    this.renderer.removeAttribute(host, 'aria-label');
  }
}
```

## Best Practices
- Actively supplement ARIA attributes to assist users in understanding their situation
- For Boolean attributes, pass an empty string with `setAttribute` and remove with `removeAttribute`
- Cache previous values to perform differential updates, minimizing DOM operations

## Considerations
- Misspelled attribute names will be output to HTML as-is, so detect them in reviews
- For custom attributes, follow the specification by adding the `data-` prefix
- Understand the attribute→property difference and use `setProperty` when necessary

## Related Technologies
- ARIA
- Renderer2
- Web Accessibility
