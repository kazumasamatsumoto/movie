# #331 "What is a Structural Directive?"

## Overview
Structural Directives are a general term for directives that dynamically modify the DOM structure of Angular templates, adding/removing elements and performing conditional branching.

## Learning Objectives
- Explain the role and characteristics of Structural Directives
- Understand the benefits and considerations of manipulating DOM structure
- Grasp the positioning as an introduction to representative directives

## Technical Points
- Generate/destroy templates with `TemplateRef` and `ViewContainerRef`
- The `*` syntax is syntactic sugar for `<ng-template>`
- Representative examples: `*ngIf`, `*ngFor`, `*ngSwitch`, custom Structural Directives

## 📺 On-Screen Code (for video)
```typescript
@Directive({ selector: '[appVisible]' })
export class VisibleDirective {}
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appVisible]',
  standalone: true
})
export class VisibleDirective implements OnChanges {
  @Input({ alias: 'appVisible', required: true }) visible!: boolean;

  constructor(private readonly view: ViewContainerRef, private readonly template: TemplateRef<unknown>) {}

  ngOnChanges(): void {
    this.view.clear();
    if (this.visible) {
      this.view.createEmbeddedView(this.template);
    }
  }
}

@Component({
  selector: 'app-visible-demo',
  standalone: true,
  imports: [CommonModule, VisibleDirective],
  template: `
    <button type="button" (click)="toggle()">Toggle</button>
    <p *appVisible="state">Visible element</p>
  `
})
export class VisibleDemoComponent {
  protected state = true;
  protected toggle(): void {
    this.state = !this.state;
  }
}
```

## Best Practices
- Focus on DOM structure responsibilities and delegate business logic to services
- Use `Renderer2` in combination to avoid direct DOM manipulation
- Test the number of views generated and conditional branches to prevent unexpected display issues

## Considerations
- Frequent generation/destruction can be costly, so be mindful of differential updates
- In SSR environments, the DOM doesn't exist, so guard with `isPlatformBrowser`
- Complex nesting reduces readability, so split templates

## Related Technologies
- TemplateRef / ViewContainerRef
- Renderer2
- Angular Change Detection
