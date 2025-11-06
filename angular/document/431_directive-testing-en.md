# #431 "Directive Testing"

## Overview
Directive testing improves reliability by preparing a host component to verify behavior and confirming that event firing and DOM changes occur as expected.

## Learning Objectives
- Understand basic steps for directive testing
- Learn setup methods using TestBed
- Understand verification methods for DOM assertions and event firing

## Technical Points
- Create host component and render with TestBed
- Update with `fixture.detectChanges()`, obtain DOM with `fixture.nativeElement`
- Simulate events with `dispatchEvent`

## 📺 On-Screen Code (for video)
```typescript
@Component({ template: `<button appToggle>btn</button>` })
class HostComponent {}
```

## 💻 Detailed Implementation Example (for learning)
```typescript
describe('ToggleDirective', () => {
  @Component({
    standalone: true,
    imports: [ToggleDirective],
    template: `<button appToggle>Toggle</button>`
  })
  class HostComponent {}

  beforeEach(() => TestBed.configureTestingModule({ imports: [HostComponent] }).compileComponents());

  it('should toggle class on click', () => {
    const fixture = TestBed.createComponent(HostComponent);
    fixture.detectChanges();
    const button: HTMLButtonElement = fixture.nativeElement.querySelector('button');
    button.click();
    fixture.detectChanges();
    expect(button.classList.contains('is-active')).toBe(true);
  });
});
```

## Best Practices
- Keep host component standalone and simple
- Always call `detectChanges` after event simulation
- Spy on Renderer2 or Output calls to verify expected behavior

## Considerations
- Keep verification as simple as possible to avoid test instability from DOM API differences
- Also test cleanup processing for directives handling global events
- Control async behavior with `fakeAsync` or `waitForAsync`

## Related Technologies
- Angular TestBed
- Testing Library
- Jest/Jasmine
