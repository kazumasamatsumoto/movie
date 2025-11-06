# #397 "Combination with Form Control"

## Overview
Combining forms with Attribute Directives makes UI feedback such as validation result display and input assistance reusable.

## Learning Objectives
- Understand how to monitor form state and change appearance with directives
- Learn coordination patterns with Reactive Forms
- Grasp design for abstracting input assistance as directives

## Technical Points
- Receive `@Input() control: AbstractControl` to monitor state
- Subscribe to `statusChanges`/`valueChanges` and reflect in UI
- Switch classes/attributes with Renderer2

## 📺 Display Code (for video)
```typescript
@Directive({ selector: '[appControlState]', standalone: true })
export class ControlStateDirective {
  @Input({ required: true }) set appControlState(ctrl: AbstractControl | null) { this.update(ctrl); }
}
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appControlState]',
  standalone: true
})
export class ControlStateDirective implements OnDestroy {
  private control?: AbstractControl;
  private subscription?: Subscription;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  @Input({ required: true })
  set appControlState(control: AbstractControl | null) {
    this.subscription?.unsubscribe();
    this.control = control ?? undefined;
    if (this.control) {
      this.subscription = merge(this.control.statusChanges, of(this.control.status)).subscribe(() => this.apply());
      this.apply();
    }
  }

  private apply(): void {
    if (!this.control) return;
    const invalid = this.control.invalid && (this.control.dirty || this.control.touched);
    this.renderer[invalid ? 'addClass' : 'removeClass'](this.el.nativeElement, 'is-invalid');
  }

  ngOnDestroy(): void {
    this.subscription?.unsubscribe();
  }
}

@Component({
  selector: 'app-control-state-demo',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, ControlStateDirective],
  template: `
    <form [formGroup]="form">
      <input formControlName="email" [appControlState]="form.controls.email" placeholder="Email Address" />
    </form>
  `
})
export class ControlStateDemoComponent {
  protected form = new FormGroup({
    email: new FormControl('', { nonNullable: true, validators: [Validators.required, Validators.email] })
  });
}
```

## Best Practices
- Manage subscriptions on directive side and release in `ngOnDestroy` to prevent leaks
- Also set accessibility attributes (`aria-invalid`, etc.) based on form state
- Convert common validation display logic to directives to reduce duplication

## Considerations
- Consider cases where Control becomes null and implement guards
- `statusChanges` may fire synchronously multiple times, so write defensively
- Forgetting subscription management causes memory leaks and extra class additions

## Related Technologies
- Reactive Forms
- Subscription Management
- Accessibility Attributes
