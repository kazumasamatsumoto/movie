# #304 "Structural Directive - Structural Directives"

## Overview
Structural Directives manage template creation and destruction, providing functionality to replace the DOM structure itself based on conditions or collections.

## Learning Objectives
- Understand the impact Structural Directives have on DOM structure
- Learn the roles of TemplateRef and ViewContainerRef
- Implement custom structural directives for conditional rendering

## Technical Points
- Provide `*` syntax with `@Directive` and attribute selector
- Create and destroy embedded views with `ViewContainerRef`
- Design intuitive APIs with `@Input` alias

## 📺 Display Code (For Video)
```typescript
@Directive({ selector: '[appIfRole]', standalone: true })
export class IfRoleDirective implements OnChanges {
  @Input({ alias: 'appIfRole', required: true }) role!: string;
  constructor(private view: ViewContainerRef, private tpl: TemplateRef<unknown>, private auth: AuthService) {}
  ngOnChanges(): void {
    this.view.clear();
    if (this.auth.hasRole(this.role)) this.view.createEmbeddedView(this.tpl);
  }
}
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Injectable({ providedIn: 'root' })
export class AuthService {
  private readonly roles = signal<string[]>(['reader', 'editor']);
  hasRole(role: string): boolean {
    return this.roles().includes(role);
  }
}

@Directive({
  selector: '[appIfRole]',
  standalone: true
})
export class IfRoleDirective implements OnChanges, OnDestroy {
  @Input({ alias: 'appIfRole', required: true }) role!: string;
  private embedded?: EmbeddedViewRef<unknown>;

  constructor(
    private readonly view: ViewContainerRef,
    private readonly template: TemplateRef<unknown>,
    private readonly auth: AuthService
  ) {}

  ngOnChanges(): void {
    this.view.clear();
    this.embedded = undefined;
    if (this.auth.hasRole(this.role)) {
      this.embedded = this.view.createEmbeddedView(this.template);
    }
  }

  ngOnDestroy(): void {
    this.embedded?.destroy();
  }
}

@Component({
  selector: 'app-if-role-demo',
  standalone: true,
  imports: [CommonModule, IfRoleDirective],
  template: `
    <p *appIfRole="'editor'">Block visible only to editors.</p>
    <p *appIfRole="'admin'">Admin-only content.</p>
  `
})
export class IfRoleDemoComponent {}
```

## Best Practices
- Call `ViewContainerRef.clear()` reliably during initialization and cleanup to prevent view duplication
- Use `@Input` alias to provide readable `*appX="condition"` syntax
- For large templates, be mindful of memory usage and destroy unnecessary views immediately

## Cautions
- When conditions change frequently, consider differential updates rather than creating new views each time
- Mock `TemplateRef` dependency in tests to verify embedded view creation
- In SSR, align initial display state with the browser to avoid hydration errors

## Related Technologies
- TemplateRef
- EmbeddedViewRef
- Structural Directives (`*ngIf`, `@for`)
