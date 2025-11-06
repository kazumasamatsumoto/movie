# #429 "Generic Design"

## Overview
Generic design aims for directives that combine single responsibility with extension points, utilizing Generics and Strategy pattern to adapt to various cases.

## Learning Objectives
- Understand design principles for generalization
- Learn how to design extension points with Strategy and DI
- Understand flexible APIs using type parameters

## Technical Points
- Receive Strategy objects or functions with Input
- Inject abstract services with Dependency Injection
- Make Input type constraints flexible with Generics

## 📺 On-Screen Code (for video)
```typescript
@Input() appValidator!: (value: string) => boolean;
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appValidator]',
  standalone: true
})
export class ValidatorDirective {
  @Input() appValidator?: (value: string) => boolean;
  @Output() validation = new EventEmitter<boolean>();

  @HostListener('input', ['$event.target.value'])
  onInput(value: string): void {
    const fn = this.appValidator ?? ((v: string) => v.length > 0);
    this.validation.emit(fn(value));
  }
}
```

## Best Practices
- Receive Strategy or Callback with Input so consumer side can freely replace behavior
- Utilize type parameters to handle multiple types of data
- Enrich documentation and tests to be resistant to specification changes

## Considerations
- Too much generalization makes usage difficult, so clarify default behavior
- Balance as too many dependencies make configuration cumbersome
- Don't forget fallback implementation when Strategy is not passed

## Related Technologies
- Strategy pattern
- Generics
- Dependency Injection
