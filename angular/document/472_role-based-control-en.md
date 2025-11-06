# #472 "Role-Based Display Control"

## Overview
Role-based display control specifies required roles via Input and switches element display/hide based on authorization service inquiry results. Design supporting OR/AND conditions for multiple roles and permissions is important.

## Learning Objectives
- Understand role condition evaluation methods
- Learn coordination between authorization service and directive
- Design display control modes (hidden/ngIf)

## Technical Points
- `@Input() appPermission: string | string[]`
- Authorization service `hasRole`, `hasAllRoles`
- Control display with HostBinding or `ViewContainerRef`

## 📺 On-Screen Code (for video)
```html
<button appPermission="admin">Admin only</button>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appPermission]',
  standalone: true
})
export class PermissionDirective implements OnChanges {
  @Input('appPermission') roles: string | string[] = [];
  @Input() appPermissionMode: 'hidden' | 'remove' = 'hidden';

  constructor(
    private readonly auth: AuthService,
    private readonly viewContainer: ViewContainerRef,
    private readonly template: TemplateRef<unknown>
  ) {}

  ngOnChanges(): void {
    const required = Array.isArray(this.roles) ? this.roles : [this.roles];
    const allowed = required.length === 0 || required.some(role => this.auth.hasRole(role));
    if (allowed) {
      if (this.viewContainer.length === 0) {
        this.viewContainer.createEmbeddedView(this.template);
      }
    } else {
      if (this.appPermissionMode === 'remove') {
        this.viewContainer.clear();
      } else {
        if (this.viewContainer.length === 0) {
          this.viewContainer.createEmbeddedView(this.template);
        }
        this.viewContainer.element.nativeElement.style.display = 'none';
      }
    }
  }
}
```

## Best Practices
- Make DOM removal and simple hiding selectable with mode switching
- Authorization service provides permission change notifications with Observable
- Extend to specify role condition combinations (AND/OR) via Input

## Considerations
- Fallback to prevent flicker in initial state if authorization information is asynchronously acquired
- Be careful of timing to release `display: none` in hidden mode
- Avoid hardcoding Role names, manage with constants or Enum

## Related Technologies
- AuthService
- Structural Directive
- Angular Security guide
