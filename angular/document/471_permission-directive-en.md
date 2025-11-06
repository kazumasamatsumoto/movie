# #471 "Permission Directive - Permission Control"

## Overview
The Permission directive shows or hides elements according to user permissions, implementing access control in UI. Implemented in coordination with role-based authorization service.

## Learning Objectives
- Understand the design philosophy of permission control directive
- Learn the mechanism to get permission information from authorization service
- Grasp implementation combining display control and ARIA support

## Technical Points
- Accept required role/permission via Input
- DI authorization service `hasRole`/`hasPermission`
- Control display with HostBinding or ngIf

## 📺 On-Screen Code (for video)
```typescript
@Input('appPermission') requiredRoles: string[] = [];
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appPermission]',
  standalone: true
})
export class PermissionDirective implements OnChanges {
  @Input('appPermission') roles: string[] = [];
  @HostBinding('hidden') hidden = false;

  constructor(private readonly auth: AuthService) {}

  ngOnChanges(): void {
    const allowed = this.roles.length === 0 || this.roles.some(role => this.auth.hasRole(role));
    this.hidden = !allowed;
  }
}
```

## Best Practices
- Specify authorization conditions flexibly via Input, default to display
- Also provide method to remove from DOM with `ngIf` instead of `hidden`
- Support asynchronous permissions with service cache or Observable

## Considerations
- Guard processing is needed as permission information may not yet be available in SSR
- Not only UI hiding but backend verification is also essential
- Update directive in line with authorization logic changes

## Related Technologies
- AuthService
- Role-based Access Control
- Structural Directive (ngIf)
