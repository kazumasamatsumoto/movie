# #433 "Directive Behavior Verification"

## Overview
Directive behavior verification confirms behaviors required by specifications such as DOM changes, attribute updates, and event notifications through tests to prevent regressions.

## Learning Objectives
- Understand how to clarify assertion targets
- Learn techniques for verifying DOM and class/style
- Understand how to verify Output events

## Technical Points
- Verify results with `classList.contains`, `getAttribute`
- Confirm EventEmitter `emit` calls with `spyOn`
- Apply updates with `fixture.detectChanges()`

## 📺 On-Screen Code (for video)
```typescript
expect(button.classList.contains('is-active')).toBeTrue();
```

## 💻 Detailed Implementation Example (for learning)
```typescript
it('should emit toggle event', () => {
  const fixture = TestBed.createComponent(HostComponent);
  const directive = fixture.debugElement.query(By.directive(ToggleDirective)).injector.get(ToggleDirective);
  const spy = spyOn(directive.appToggle, 'emit');
  const button: HTMLButtonElement = fixture.nativeElement.querySelector('button');
  button.click();
  expect(spy).toHaveBeenCalledWith(true);
});
```

## Best Practices
- List assertion items based on specifications and reflect in tests
- Verify behavior from both DOM and event perspectives to prevent regressions
- Make tests as independent as possible, not depending on external state

## Considerations
- Update tests appropriately when specifications change to prevent divergence from implementation
- Check appearance with Storybook, etc. rather than unit tests for CSS
- Use fakeAsync/tick when complex timing is involved

## Related Technologies
- Jasmine/Jest matchers
- Angular Testing Library
- Storybook Visual tests
