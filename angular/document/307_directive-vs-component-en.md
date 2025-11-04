# #307 "Differences Between Directive and Component"

## Overview
While Directives and Components share a common foundation, their roles are divided by the presence or absence of templates and responsibilities for UI construction. Appropriate selection affects app maintainability.

## Learning Objectives
- Clearly explain commonalities and differences between Directives and Components
- Develop judgment criteria for choosing the right abstraction
- Understand design patterns combining both

## Technical Points
- Components have templates and styles with the `@Component` decorator
- Directives add behavior to existing DOM with `@Directive`
- Both share dependency injection and lifecycle hooks

## 📺 Display Code (For Video)
```typescript
@Directive({ selector: '[appFocusTrap]', standalone: true })
export class FocusTrapDirective {}

@Component({
  selector: 'app-focus-trap',
  standalone: true,
  template: `<div appFocusTrap><ng-content /></div>`
})
export class FocusTrapComponent {}
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Directive({
  selector: '[appFocusTrap]',
  standalone: true
})
export class FocusTrapDirective implements OnInit, OnDestroy {
  private removeListener?: () => void;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    const element = this.el.nativeElement;
    this.removeListener = this.renderer.listen(element, 'keydown', event => {
      if ((event as KeyboardEvent).key !== 'Tab') return;
      // Actual focus trap logic omitted
    });
  }

  ngOnDestroy(): void {
    this.removeListener?.();
  }
}

@Component({
  selector: 'app-focus-trap',
  standalone: true,
  imports: [CommonModule, FocusTrapDirective],
  template: `
    <section appFocusTrap role="dialog" aria-modal="true" class="dialog">
      <header><ng-content select="[slot=title]" /></header>
      <div class="dialog__body"><ng-content /></div>
    </section>
  `,
  styles: [`
    .dialog { padding: 1.5rem; background: #fff; border-radius: 1rem; }
    .dialog__body { margin-top: 1rem; }
  `]
})
export class FocusTrapComponent {}
```

## Best Practices
- Use components when UI is involved, separate additional behavior into directives
- Create two-layer structure based on presence of display responsibilities even for the same functionality to clarify test targets
- Organize API with components as external contracts and directives as internal assistance

## Cautions
- Adding templates to Directives makes responsibilities ambiguous and maintenance difficult
- Adding excessive DOM manipulation to Components breaks SRP, so delegate to Directives
- Both affect ChangeDetection, so control with `OnPush` or `signal` as needed

## Related Technologies
- Standalone Components
- HostDirectives
- Angular CDK
