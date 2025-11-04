# #305 "Attribute Directive - Attribute Directives"

## Overview
Attribute Directives are lightweight DOM extensions that are applied like attributes to existing elements, locally modifying styles and behavior.

## Learning Objectives
- Understand the responsibilities and use cases of Attribute Directives
- Learn host element control through HostBinding/HostListener
- Safely change styles and classes using Renderer2

## Technical Points
- Applied to existing elements with attribute selector
- Synchronize properties with `HostBinding`, handle events with `HostListener`
- Platform-independent DOM manipulation with Renderer2

## 📺 Display Code (For Video)
```typescript
@Directive({ selector: '[appAccentBorder]', standalone: true })
export class AccentBorderDirective {
  @HostBinding('style.outline') outline = '2px solid #22d3ee';
  @HostListener('focus') onFocus(): void { this.outline = '2px solid #0ea5e9'; }
  @HostListener('blur') onBlur(): void { this.outline = '2px solid #22d3ee'; }
}
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Directive({
  selector: '[appAccentBorder]',
  standalone: true
})
export class AccentBorderDirective implements OnInit, OnDestroy {
  @Input() appAccentBorder = '#22d3ee';
  private removeFocus?: () => void;
  private removeBlur?: () => void;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    this.renderer.setStyle(this.el.nativeElement, 'outline', `2px solid ${this.appAccentBorder}`);
    this.removeFocus = this.renderer.listen(this.el.nativeElement, 'focus', () =>
      this.renderer.setStyle(this.el.nativeElement, 'outline-color', '#0ea5e9')
    );
    this.removeBlur = this.renderer.listen(this.el.nativeElement, 'blur', () =>
      this.renderer.setStyle(this.el.nativeElement, 'outline-color', this.appAccentBorder)
    );
  }

  ngOnDestroy(): void {
    this.removeFocus?.();
    this.removeBlur?.();
    this.renderer.removeStyle(this.el.nativeElement, 'outline');
  }
}

@Component({
  selector: 'app-accent-border-demo',
  standalone: true,
  imports: [CommonModule, FormsModule, AccentBorderDirective],
  template: `
    <input appAccentBorder [(ngModel)]="value" placeholder="Attribute directive example" />
    <p>Input value: {{ value }}</p>
  `
})
export class AccentBorderDemoComponent {
  protected value = '';
}
```

## Best Practices
- Provide initial values for visual changes with HostBinding, delegate detailed control to Renderer2
- Accept input values with `@Input` and perform validation with `transform` option if possible
- Hold event listener cleanup functions and always unregister in ngOnDestroy

## Cautions
- Consider structural directives if modifying DOM structure to avoid mixing responsibilities
- Check for CSS property conflicts when applying multiple Directives to the same element
- In SSR environments, focus events don't fire, so consider fallbacks

## Related Technologies
- HostBinding / HostListener
- Renderer2
- Angular Forms
