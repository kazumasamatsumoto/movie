# #396 "Attribute Directive Practical Examples"

## Overview
Attribute Directives are suitable for providing localized UI behaviors such as button loading states, tooltips, and drag operations in a reusable form.

## Learning Objectives
- Understand representative use cases for Attribute Directives
- Learn how to extract behaviors commonly used in practice as directives
- Be aware of the role division between components and directives

## Technical Points
- Express state by adding classes/attributes to host element
- DOM operations according to events with Renderer2
- Coordinate with services using DI (e.g., Tooltip service)

## 📺 Display Code (for video)
```typescript
@Directive({ selector: '[appLoadingButton]', standalone: true })
export class LoadingButtonDirective {
  @Input() set appLoadingButton(loading: boolean) { this.renderer.setProperty(this.el.nativeElement, 'disabled', loading); }
  constructor(private readonly el: ElementRef<HTMLButtonElement>, private readonly renderer: Renderer2) {}
}
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appLoadingButton]',
  standalone: true
})
export class LoadingButtonDirective implements OnChanges {
  @Input() appLoadingButton = false;

  constructor(private readonly el: ElementRef<HTMLButtonElement>, private readonly renderer: Renderer2) {}

  ngOnChanges(): void {
    this.renderer.setProperty(this.el.nativeElement, 'disabled', this.appLoadingButton);
    this.renderer[this.appLoadingButton ? 'addClass' : 'removeClass'](this.el.nativeElement, 'is-loading');
  }
}

@Component({
  selector: 'app-loading-button-demo',
  standalone: true,
  imports: [CommonModule, LoadingButtonDirective],
  template: `
    <button type="button" [appLoadingButton]="loading" (click)="simulate()">Submit</button>
  `
})
export class LoadingButtonDemoComponent {
  protected loading = false;
  protected simulate(): void {
    this.loading = true;
    setTimeout(() => (this.loading = false), 1200);
  }
}
```

## Best Practices
- Create directives for small responsibilities and combine them to build UIs
- Receive state via Inputs for external management, and keep side effects within directives
- Share usage with Storybook, etc., and integrate into design systems

## Considerations
- Clarify target element type and type like `ElementRef<HTMLButtonElement>`
- For visuals only, limit to class addition and avoid changing DOM properties directly too much
- Beware of conflicts when multiple directives control the same property

## Related Technologies
- Renderer2
- Storybook
- Design System Implementation
