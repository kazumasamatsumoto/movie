# #473 "Permission Check"

## Overview
Permission check verifies user permissions through authorization service, determines if specified permission exists to control UI. Must support asynchronous checks as well.

## Learning Objectives
- Understand basic logic of permission check
- Learn handling of synchronous and asynchronous permission data
- Grasp how to reflect check results in directive

## Technical Points
- AuthService's `hasPermission` or `observePermissions`
- Process Observable with `async` pipe or subscribe
- Display loading state until asynchronous completion

## 📺 On-Screen Code (for video)
```typescript
const allowed = this.auth.hasPermission(permission);
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Injectable({ providedIn: 'root' })
export class AuthService {
  private readonly permissions$ = new BehaviorSubject<string[]>(['read', 'write']);

  hasPermission(permission: string): boolean {
    return this.permissions$.value.includes(permission);
  }

  observePermissions(): Observable<string[]> {
    return this.permissions$.asObservable();
  }
}

@Directive({
  selector: '[appPermissionCheck]',
  standalone: true
})
export class PermissionCheckDirective implements OnDestroy {
  @Input('appPermissionCheck') permission = '';
  @HostBinding('hidden') hidden = true;
  private sub?: Subscription;

  constructor(private readonly auth: AuthService) {}

  ngOnInit(): void {
    this.sub = this.auth.observePermissions().subscribe(perms => {
      this.hidden = !perms.includes(this.permission);
    });
  }

  ngOnDestroy(): void {
    this.sub?.unsubscribe();
  }
}
```

## Best Practices
- Provide permission information as Observable in AuthService for real-time updates
- Thoroughly manage subscriptions on directive side
- Prepare message to present to user on permission error

## Considerations
- Decide how to handle initial display when permission determination delays due to network latency
- Client-side permission check alone is insufficient, server-side verification also needed
- Utilize cache when many directives perform permission checks

## Related Technologies
- AuthService/Permissions
- BehaviorSubject
- Async Pipe
