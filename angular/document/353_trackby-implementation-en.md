# #353 "trackBy Function Implementation"

## Overview
The trackBy function is a pure function that returns a key for `*ngFor` to identify elements, with implementations returning unique IDs being recommended.

## Learning Objectives
- Understand trackBy function signature and return value constraints
- Learn implementation patterns that return stable keys
- Grasp testing and debugging perspectives

## Technical Points
- Arguments: `(index: number, item: T) => string | number`
- Return stable unique keys to promote reuse after array operations
- Functions should be pure without side effects

## 📺 Screen Display Code (For Video)
```typescript
trackById(_index: number, item: { id: number }) {
  return item.id;
}
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-trackby-impl-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ul>
      <li *ngFor="let user of users; trackBy: trackUser">{{ user.name }}</li>
    </ul>
  `
})
export class TrackByImplDemoComponent {
  protected users = [
    { id: 1, name: 'Metan' },
    { id: 2, name: 'Zundamon' }
  ];

  protected trackUser(_: number, user: { id: number }): number {
    return user.id;
  }
}
```

## Best Practices
- Review data source rather than hash generation for data without IDs
- Define trackBy functions as component methods for testability
- Verify same IDs are returned in unit tests to prevent regressions

## Cautions
- Returning `index` as-is disables DOM reuse on insertion or sorting
- Generating UUIDs each time causes values to keep changing, having reverse effect
- Avoid changing state inside trackBy functions as it causes re-rendering

## Related Technologies
- trackBy
- Pure Functions
- Unit Testing
