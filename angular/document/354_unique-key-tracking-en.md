# #354 "Tracking with Unique Keys"

## Overview
Returning unique keys with trackBy allows DOM to be reused even when item positions change, improving performance during list operations.

## Learning Objectives
- Understand design of stable unique keys
- Learn coordination between data sources and authentication keys
- Grasp behavior when applying trackBy

## Technical Points
- Use stable identifiers like primary keys or UUIDs
- Sequential numbers aren't appropriate as they may change on regeneration
- Consider attaching at server or store layer if unique keys don't exist

## 📺 Screen Display Code (For Video)
```html
<li *ngFor="let note of notes; trackBy: trackByNoteId">
  {{ note.title }}
</li>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
interface Note {
  noteId: string;
  title: string;
}

@Component({
  selector: 'app-unique-key-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ul>
      <li *ngFor="let note of notes; trackBy: trackByNoteId">{{ note.title }}</li>
    </ul>
  `
})
export class UniqueKeyDemoComponent {
  protected notes: Note[] = [
    { noteId: 'n-100', title: 'Structural Directive Overview' },
    { noteId: 'n-101', title: 'trackBy Deep Dive' }
  ];

  protected trackByNoteId(_: number, note: Note): string {
    return note.noteId;
  }
}
```

## Best Practices
- Consult with backend to provide stable keys
- Cache when generating on client side to avoid regeneration
- Combine trackBy with OnPush to avoid unnecessary Change Detection

## Cautions
- Changing unique keys causes Angular to treat elements as different, regenerating DOM
- Key collisions disrupt rendering, so detect in tests
- Be careful handling unique keys with JSON serialization as types may change

## Related Technologies
- Entity Adapter
- NGRX/Signal Store
- ChangeDetectionStrategy.OnPush
