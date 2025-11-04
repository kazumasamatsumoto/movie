# #306 "Directive Roles and Responsibilities"

## Overview
Directives are responsible for DOM appearance and local behavior, enhancing reusability by delegating business logic and long-term state to services and other layers.

## Learning Objectives
- Define appropriate responsibility boundaries for Directives
- Understand design patterns that separate views from logic
- Build testable and maintainable Directive structures

## Technical Points
- Limit to view changes with HostBinding/Renderer2
- Delegate business rules through service injection
- Make contracts with host explicit through @Input/@Output

## 📺 Display Code (For Video)
```typescript
@Directive({ selector: '[appValidateState]', standalone: true })
export class ValidateStateDirective implements OnChanges {
  @Input({ alias: 'appValidateState', required: true }) state!: Signal<FormState>;
  constructor(private readonly alert: AlertService) {}
  ngOnChanges(): void {
    if (this.state().invalid) this.alert.notify('There are input errors');
  }
}
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
export interface FormState {
  invalid: boolean;
  touched: boolean;
  errors: readonly string[];
}

@Injectable({ providedIn: 'root' })
export class AlertService {
  notify(message: string): void {
    // Actually delegates to Toast component, etc.
    console.warn('[alert]', message);
  }
}

@Directive({
  selector: '[appValidateState]',
  standalone: true
})
export class ValidateStateDirective implements OnChanges {
  @Input({ alias: 'appValidateState', required: true }) state!: Signal<FormState>;

  constructor(private readonly alert: AlertService) {}

  ngOnChanges(): void {
    const current = this.state();
    if (!current.touched) return;
    if (current.invalid) {
      this.alert.notify(current.errors.join('\n'));
    }
  }
}

@Component({
  selector: 'app-validate-state-demo',
  standalone: true,
  imports: [CommonModule, ValidateStateDirective],
  template: `
    <section [appValidateState]="state">
      <p>Touched: {{ state().touched }}, Invalid: {{ state().invalid }}</p>
    </section>
  `
})
export class ValidateStateDemoComponent {
  private readonly stateSignal = signal<FormState>({ invalid: true, touched: true, errors: ['Required field'] });
  protected state = computed(() => this.stateSignal());
}
```

## Best Practices
- Focus Directives on UI boundaries, delegating business rules to services or Signals
- Manage side effect start/end in `ngOnInit` and `ngOnDestroy` to maintain lifecycle integrity
- Limit API to Input/Output to prevent introducing unexpected external dependencies

## Cautions
- Holding large state internally makes testing difficult, so escape to external stores
- When depending on services, prepare test stubs that can be injected
- Even when DOM manipulation is needed, do it via Renderer2 to avoid environment dependencies

## Related Technologies
- Dependency Injection
- Angular Signals
- Smart/Dumb component pattern
