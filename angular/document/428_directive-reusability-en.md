# #428 "Directive Reusability"

## Overview
Highly reusable directives are designed with configurable APIs and minimal side effects without depending on specific scenarios, and can be utilized across many components.

## Learning Objectives
- Understand design guidelines to improve reusability
- Learn how to ensure flexibility with Input/Output
- Build architecture with few dependencies

## Technical Points
- Receive configuration values with Input and provide defaults
- Notify events with Output to enable external control
- Abstract DOM manipulation with Renderer2/HostBinding

## 📺 On-Screen Code (for video)
```typescript
@Input() appToggleClass = 'is-active';
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appToggleClass]',
  standalone: true
})
export class ToggleClassDirective {
  @Input() appToggleClass = 'is-active';
  @HostBinding('class') hostClass = '';

  @HostListener('click')
  onClick(): void {
    this.hostClass = this.hostClass === this.appToggleClass ? '' : this.appToggleClass;
  }
}
```

## Best Practices
- Place as common utilities in `shared/directives`, etc.
- Organize tests and documentation to clarify usage methods
- Abstract dependent services to allow replacement through injection

## Considerations
- Don't include domain-specific wording or API dependencies
- Trying to make too generic leads to complexity, so identify appropriate scope
- Change carefully to avoid Breaking Changes on version upgrades

## Related Technologies
- Dependency Injection
- Storybook
- Shared Module/Standalone organization
