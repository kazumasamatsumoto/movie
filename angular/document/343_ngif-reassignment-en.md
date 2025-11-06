# #343 "Value Reassignment and Usage"

## Overview
Values received as aliases in `*ngIf` are read-only and cannot be reassigned, so templates should only reference them while component logic handles operations.

## Learning Objectives
- Understand the lifecycle and scope of alias values
- Learn how to manage state in components instead of reassignment
- Master safe value reference patterns in templates

## Technical Points
- Reassignment within templates is not allowed, read-only access only
- Update state in components via Signals or Observables
- Aliases benefit from type inference and increase safety with strictTemplates

## 📺 Screen Display Code (For Video)
```html
<article *ngIf="user$ | async as user">
  <p>{{ user.name }}</p>
</article>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
interface UserProfile {
  id: number;
  name: string;
}

@Component({
  selector: 'app-alias-usage-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div *ngIf="profile$ | async as profile; else loading">
      <h2>{{ profile.name }}</h2>
      <button type="button" (click)="rename(profile.id)">Change name</button>
    </div>
    <ng-template #loading>
      <p>Loading...</p>
    </ng-template>
  `
})
export class AliasUsageDemoComponent {
  private readonly subject = new BehaviorSubject<UserProfile>({ id: 1, name: 'Initial User' });
  protected profile$ = this.subject.asObservable();

  protected rename(id: number): void {
    this.subject.next({ id, name: 'Updated User' });
  }
}
```

## Best Practices
- Indicate that aliases are read-only through comments or naming
- Handle value updates using component methods or Signals
- Test that aliases reference correct values

## Cautions
- Assigning like `profile = ...` within templates will cause a build error
- Alias scope is limited to within the `*ngIf`, so it cannot be referenced externally
- Provide fallback with else template to handle `null` cases

## Related Technologies
- BehaviorSubject
- Angular Signals
- Template Type Checking
