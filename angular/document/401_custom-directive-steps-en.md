# #401 "Custom Directive Creation Steps"

## Overview
Custom Directives are built through a series of steps: generating scaffolding with the CLI, implementing behavior for the Host element, and testing and documenting.

## Learning Objectives
- Understand the overall flow of custom Directive creation
- Learn the steps from CLI generation to registration and testing
- Be able to explain the completion process including documentation

## Technical Points
- Generate scaffolding with `ng generate directive`
- Standalone directives are registered to the consumer side via `imports`
- Enhance reusability by setting up tests/documentation together

## 📺 On-Screen Code (for video)
```bash
ng g directive shared/highlight --standalone
```

## 💻 Detailed Implementation Example (for learning)
```typescript
// 1. Generation
// ng g directive shared/highlight --standalone

// 2. Implementation
@Directive({
  selector: '[appHighlight]',
  standalone: true
})
export class HighlightDirective {
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}
  ngOnInit(): void {
    this.renderer.setStyle(this.el.nativeElement, 'backgroundColor', '#fef08a');
  }
}

// 3. Usage
@Component({
  selector: 'app-highlight-demo',
  standalone: true,
  imports: [CommonModule, HighlightDirective],
  template: `<p appHighlight>Directive creation steps demo</p>`
})
export class HighlightDemoComponent {}

// 4. Test generation: highlight.directive.spec.ts
```

## Best Practices
- Adjust standalone settings and selector immediately after scaffolding generation
- Verify behavior early in the consumer component and add test cases
- Share purpose, usage, and Input/Output in documentation

## Considerations
- Failure to unify selectors and prefixes can easily lead to conflicts
- If not standalone, don't forget to register in NgModule
- Postponing tests and documentation makes reuse difficult

## Related Technologies
- Angular CLI
- Standalone API
- Storybook
