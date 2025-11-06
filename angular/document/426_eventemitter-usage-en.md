# #426 "Using EventEmitter"

## Overview
`EventEmitter` is an Observable-based event firing class provided by Angular, allowing simple event notification from directives and components.

## Learning Objectives
- Understand EventEmitter mechanism and usage
- Learn how to send payload with emit method
- Understand patterns for publishing as Observable

## Technical Points
- Declare typed events with `new EventEmitter<T>()`
- Notify subscribers with `emit(value)`
- Can wrap as read-only with `asObservable()`

## 📺 On-Screen Code (for video)
```typescript
@Output() toggled = new EventEmitter<boolean>();
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appHoverEvent]',
  standalone: true
})
export class HoverEventDirective {
  private readonly hoverSubject = new EventEmitter<boolean>();

  @Output()
  get appHover(): Observable<boolean> {
    return this.hoverSubject.asObservable();
  }

  @HostListener('mouseenter')
  enter(): void {
    this.hoverSubject.emit(true);
  }

  @HostListener('mouseleave')
  leave(): void {
    this.hoverSubject.emit(false);
  }
}
```

## Best Practices
- Specify event type explicitly to enable consumer-side completion
- Publish with `asObservable()` as needed to prevent external `emit`
- Apply RxJS operators on consumer side if Debounce or Throttle is needed

## Considerations
- EventEmitter emits within Angular zone, so wrap external async with `ngZone.run`
- Calling `emit` in large volumes increases Change Detection cost
- Complete/error notification is not recommended in Angular, only `emit` usage is common

## Related Technologies
- RxJS Observable
- Angular zone
- Output bidirectional binding
