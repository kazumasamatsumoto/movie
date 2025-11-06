# #332 "Meaning of the * (Asterisk) Syntax"

## Overview
The `*` syntax is syntactic sugar for writing Angular structural directives concisely and is actually expanded to `<ng-template>`.

## Learning Objectives
- Understand how the `*` syntax is expanded internally
- Be able to read the expanded template structure
- Gain hints for custom Structural Directive implementation

## Technical Points
- `*directive="expr"` → `<ng-template [directive]="expr"></ng-template>`
- `TemplateRef` and `ViewContainerRef` handle the expanded template
- `let` declarations and `as` syntax are also converted to attributes during expansion

## 📺 On-Screen Code (for video)
```html
<p *ngIf="flag">Asterisk syntax</p>
<!-- After expansion: <ng-template [ngIf]="flag"><p>...</p></ng-template> -->
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appSugar]',
  standalone: true
})
export class SugarDirective implements OnInit {
  @Input({ alias: 'appSugar' }) condition = false;

  constructor(private readonly view: ViewContainerRef, private readonly template: TemplateRef<unknown>) {}

  ngOnInit(): void {
    if (this.condition) {
      this.view.createEmbeddedView(this.template);
    }
  }
}

@Component({
  selector: 'app-sugar-demo',
  standalone: true,
  imports: [CommonModule, SugarDirective],
  template: `
    <p *appSugar="isEnabled">Directive is expanded to <ng-template></p>
    <ng-template [appSugar]="isEnabled">
      <p>This is what it looks like when written manually.</p>
    </ng-template>
  `
})
export class SugarDemoComponent {
  protected isEnabled = true;
}
```

## Best Practices
- Calculate complex conditional expressions in the component rather than in templates, keeping the `*` syntax simple
- Understanding the expanded form makes debugging and custom implementation easier
- To optimize change detection, avoid heavy processing within templates

## Considerations
- The `*` syntax can only be applied to one element; applying multiple will result in a build error
- Nesting without awareness of expansion can result in deep DOM structures
- When writing `<ng-template>` directly, don't forget to specify context variables

## Related Technologies
- TemplateRef
- ViewContainerRef
- Angular Template Syntax
