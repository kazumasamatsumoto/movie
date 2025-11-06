# #450 "Debounce Directive - Debouncing"

## Overview
The Debounce directive is a mechanism that delays input events and other events before firing them for a certain period, which can reduce the load on API calls and search processing.

## Learning Objectives
- Understand the basic principles of debouncing
- Learn how to receive events with HostListener and perform delayed processing with timers or RxJS
- Grasp the design of notifying delayed events with Output

## Technical Points
- `setTimeout`/`clearTimeout` or RxJS `debounceTime`
- Set wait time with Input
- Notify delayed value with Output

## 📺 On-Screen Code (for video)
```typescript
@HostListener('input', ['$event.target.value']) onInput(value: string) { this.schedule(value); }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appDebounce]',
  standalone: true
})
export class DebounceDirective implements OnDestroy {
  @Input() debounceTime = 300;
  @Output() debounce = new EventEmitter<string>();
  private timer?: number;

  @HostListener('input', ['$event.target.value'])
  onInput(value: string): void {
    if (this.timer) {
      clearTimeout(this.timer);
    }
    this.timer = window.setTimeout(() => {
      this.debounce.emit(value);
    }, this.debounceTime);
  }

  ngOnDestroy(): void {
    if (this.timer) {
      clearTimeout(this.timer);
    }
  }
}
```

## Best Practices
- Accept wait time via Input for flexible adjustment
- Clear timer in `ngOnDestroy` to prevent memory leaks
- Using RxJS to convert to Observable supports complex patterns

## Considerations
- Native `setTimeout` executes immediately even when the value is 0, so be careful with edge cases
- Browser guard is necessary because window does not exist in SSR
- Only the latest value is handled in continuous events, so confirm requirements to ensure needed input is not lost

## Related Technologies
- RxJS `debounceTime`
- EventEmitter
- Reactive Forms
