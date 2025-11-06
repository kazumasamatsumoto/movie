# #439 "Directive Best Practices"

## Overview
Directive best practices are guidelines centered on single responsibility, platform independence, and test/documentation organization to improve maintainability and reusability.

## Learning Objectives
- Understand major best practices systematically
- Learn safety measures for DOM manipulation and side effect management
- Recognize the importance of testing and documentation

## Technical Points
- Utilize Renderer2/HostBinding to avoid direct DOM access
- Reliably release side effects with DestroyRef or ngOnDestroy
- Clearly define Input/Output

## 📺 On-Screen Code (for video)
```typescript
@HostBinding('class.is-active') active = false;
@HostListener('click') toggle(): void { this.active = !this.active; }
```

## 💻 Detailed Implementation Example (for learning)
```markdown
- Single Responsibility: Focus only on appearance changes, business logic to services
- Platform Independence: Guard with Renderer2/PLATFORM_ID
- Testing: Verify behavior using host component
- Documentation: Organize purpose, API, usage examples
```

## Best Practices
- Prevent conflicts with selector naming and prefix unification
- Minimize state updates with Signals and Computed
- Always cleanup events/listeners

## Considerations
- Don't pack complex features into one directive
- Abuse of DOM manipulation impairs performance and portability
- Don't omit documentation and tests for maintainability

## Related Technologies
- Renderer2
- DestroyRef
- Angular Style Guide
