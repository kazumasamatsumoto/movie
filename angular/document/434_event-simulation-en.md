# #434 "Event Simulation"

## Overview
In tests, simulate events using `dispatchEvent` or `triggerEventHandler` to verify that HostListener works as expected.

## Learning Objectives
- Understand DOM event simulation methods
- Learn MouseEvent/KeyboardEvent generation and dispatch
- Write stable tests with fakeAsync and timer control

## Technical Points
- `element.dispatchEvent(new Event('click'))`
- `new MouseEvent('mousemove', { clientX: 10 })`
- `fixture.debugElement.triggerEventHandler('click', {})`

## 📺 On-Screen Code (for video)
```typescript
button.dispatchEvent(new MouseEvent('click'));
```

## 💻 Detailed Implementation Example (for learning)
```typescript
it('should handle keydown', () => {
  const fixture = TestBed.createComponent(HostComponent);
  const input: HTMLInputElement = fixture.nativeElement.querySelector('input');
  input.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter' }));
  fixture.detectChanges();
  expect(...).toBeTrue();
});
```

## Best Practices
- Generate events close to actual usage patterns and set properties
- Control timer-dependent behavior with `fakeAsync`/`tick` for stabilization
- Test cleanup for global events (document/window)

## Considerations
- Event generation options may behave differently across browsers
- Use `await fixture.whenStable()` when firing events multiple times
- Be aware of DOM API support in Jest environments and introduce Polyfills

## Related Technologies
- fakeAsync / tick
- Angular DebugElement
- Jest DOM
