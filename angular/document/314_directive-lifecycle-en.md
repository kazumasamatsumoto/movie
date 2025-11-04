# #314 "Directive Lifecycle"

## Overview
Directives have lifecycle hooks like components, allowing safe processing during initialization, input value changes, and cleanup timing.

## Learning Objectives
- Understand main lifecycle hooks available in Directives
- Learn responsibilities and usage distinctions for each hook
- Practice resource management following lifecycle

## Technical Points
- Can implement `OnInit`, `OnChanges`, `OnDestroy`, `AfterViewInit`, etc.
- Input processing in `ngOnChanges`, DOM manipulation initialization in `ngOnInit`
- Perform cleanup in `ngOnDestroy` to prevent leaks

## 📺 Display Code (For Video)
```typescript
@Directive({ selector: '[appAutoFocus]', standalone: true })
export class AutoFocusDirective implements OnInit, OnChanges, OnDestroy {
  @Input({ alias: 'appAutoFocus' }) enabled = true;
  constructor(private readonly el: ElementRef<HTMLInputElement>) {}
  ngOnInit(): void { if (this.enabled) this.el.nativeElement.focus(); }
  ngOnChanges(): void { if (this.enabled) this.el.nativeElement.focus(); }
  ngOnDestroy(): void { this.el.nativeElement.blur(); }
}
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Directive({
  selector: '[appAutoFocus]',
  standalone: true
})
export class AutoFocusDirective implements OnInit, OnChanges, OnDestroy {
  @Input({ alias: 'appAutoFocus' }) enabled = true;
  @Input() focusDelay = 0;
  private timeoutId?: number;

  constructor(private readonly el: ElementRef<HTMLElement>) {}

  ngOnInit(): void {
    this.tryFocus();
  }

  ngOnChanges(): void {
    this.tryFocus();
  }

  ngOnDestroy(): void {
    if (this.timeoutId) {
      clearTimeout(this.timeoutId);
    }
  }

  private tryFocus(): void {
    if (!this.enabled) return;
    if (this.timeoutId) clearTimeout(this.timeoutId);
    this.timeoutId = window.setTimeout(() => this.el.nativeElement.focus(), this.focusDelay);
  }
}
```

## Best Practices
- Execute processing requiring DOM preparation in `ngOnInit` or `ngAfterViewInit`
- Serialize processing responding to Input changes in `ngOnChanges`, being aware of differential updates
- Thoroughly unregister listeners and stop timers in `ngOnDestroy` to prevent leaks

## Cautions
- Use `SimpleChanges` in `OnChanges` to reference previous values
- In SSR, browser APIs don't exist, so guard usage in hooks
- Understand hook invocation order and be careful with synchronous/asynchronous mixing

## Related Technologies
- OnInit / OnDestroy
- ChangeDetection
- Angular Signals
