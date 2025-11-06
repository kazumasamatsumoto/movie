# #451 "Input Event Delay"

## Overview
Debouncing input events performs processing after a certain period of time when the user stops typing, suppressing unnecessary API calls and state updates.

## Learning Objectives
- Understand the mechanism of input debounce processing
- Learn implementation of delayed processing using timers or RxJS
- Grasp how to notify results after delayed processing with Output

## Technical Points
- Leave only the final input with `setTimeout`/`clearTimeout`
- Set wait time with Input
- Notify delayed value with Output event

## 📺 On-Screen Code (for video)
```typescript
@HostListener('input', ['$event.target.value'])
onInput(value: string): void { this.schedule(value); }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appInputDebounce]',
  standalone: true
})
export class InputDebounceDirective implements OnDestroy {
  @Input() delay = 300;
  @Output() debounceValue = new EventEmitter<string>();
  private timer?: number;

  @HostListener('input', ['$event.target.value'])
  handleInput(value: string): void {
    if (this.timer) {
      clearTimeout(this.timer);
    }
    this.timer = window.setTimeout(() => {
      this.debounceValue.emit(value);
    }, this.delay);
  }

  ngOnDestroy(): void {
    if (this.timer) {
      clearTimeout(this.timer);
    }
  }
}
```

## Best Practices
- Make delay time configurable from component and adjust per scenario
- Notify only the final value with Output event and integrate with forms
- Release timer in `ngOnDestroy` to prevent leaks

## Considerations
- Browser check is needed when using `window` as it causes errors in SSR
- Confirm performance is not affected by high-frequency input as timer is created for each input
- Define behavior when set to 0ms as specification

## Related Technologies
- RxJS `debounceTime`
- EventEmitter
- Reactive Forms
