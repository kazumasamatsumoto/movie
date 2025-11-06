# #385 "Conditional Style Application"

## Overview
Conditional styles are a pattern that achieves visual changes and accessibility improvements by switching between ngStyle and classes based on state.

## Learning Objectives
- Understand tips for designing conditional styles
- Learn how to perform value calculations in components and keep templates concise
- Grasp the coordination of style changes and accessibility attributes

## Technical Points
- Update style objects based on state
- Remove styles with falsy values and return to original state
- Consider a wide range of users by setting `aria-live` and `role`

## 📺 Display Code (for video)
```html
<div [ngStyle]="{ background: progress > 80 ? '#22c55e' : '#e2e8f0' }">Progress</div>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-conditional-style-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div
      [ngStyle]="styleByScore()"
      role="status"
      aria-live="polite">
      Score: {{ score }}%
    </div>
    <button type="button" (click)="increase()">Add</button>
  `
})
export class ConditionalStyleDemoComponent {
  protected score = 40;

  protected styleByScore(): Record<string, string> {
    return {
      background: this.score >= 80 ? '#22c55e' : '#e2e8f0',
      color: this.score >= 80 ? '#fff' : '#0f172a',
      padding: '0.75rem',
      borderRadius: '0.75rem'
    };
  }

  protected increase(): void {
    this.score = Math.min(100, this.score + 10);
  }
}
```

## Best Practices
- Clarify conditions such as when state exceeds a threshold, extract complex expressions into methods
- Provide consideration for voice users with ARIA while making visual changes
- Verify in tests that styles change as intended at boundary values (79→80, etc.)

## Considerations
- Numeric comparisons written directly in templates become complex, so manage with methods or computed
- Make it accessible by using icons or text alongside color changes, not relying on color alone
- If animation is needed, prioritize CSS class switching and use ngStyle as supplementary

## Related Technologies
- Accessibility (ARIA)
- Angular Signals
- Renderer2 / ngClass
