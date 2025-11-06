# #411 "Obtaining the event Object"

## Overview
By receiving `$event` with HostListener, you can access the native event object and perform processing using detailed event information.

## Learning Objectives
- Understand how to obtain the `$event` argument
- Access event properties safely with type annotations
- Learn techniques for propagating event information to business logic

## Technical Points
- `@HostListener('click', ['$event'])`
- Add TypeScript types (`MouseEvent`, `KeyboardEvent`, etc.)
- Pass multiple arguments as needed (`['$event', '$event.target']`)

## 📺 On-Screen Code (for video)
```typescript
@HostListener('click', ['$event']) onClick(event: MouseEvent) { console.log(event.clientX); }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appCaptureEvent]',
  standalone: true
})
export class CaptureEventDirective {
  @HostListener('mousemove', ['$event'])
  onMove(event: MouseEvent): void {
    const { clientX, clientY } = event;
    console.log(`mouse at ${clientX}, ${clientY}`);
  }
}
```

## Best Practices
- Add type annotations to improve IDE completion and safety
- Pass event information to services or EventEmitter for reuse
- Extract only necessary properties to keep logic lightweight

## Considerations
- Be mindful of performance when events fire frequently
- Custom events may require type definitions
- `$event.target` is `EventTarget` type, so narrow it with `instanceof`

## Related Technologies
- HostListener
- EventEmitter
- TypeScript type guards
