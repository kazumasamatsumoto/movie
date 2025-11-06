# #416 "style Binding"

## Overview
With `@HostBinding('style.<prop>')`, you can bind host element styles to directive properties, applying dynamic styles without using Renderer2.

## Learning Objectives
- Understand style binding syntax
- Learn how to add units to numeric values
- Understand style update patterns accompanying state changes

## Technical Points
- `@HostBinding('style.opacity') opacity = '1';`
- Pass string properties like background color as-is
- Add units to numeric values with template literals

## 📺 On-Screen Code (for video)
```typescript
@HostBinding('style.backgroundColor') bg = '#f1f5f9';
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appFade]',
  standalone: true
})
export class FadeDirective {
  private level = 1;

  @HostBinding('style.opacity')
  get opacity(): string {
    return this.level.toFixed(1);
  }

  fadeOut(): void {
    this.level = Math.max(0, this.level - 0.1);
  }
}
```

## Best Practices
- Building style strings with getters makes it easier to handle multiple conditions
- Delegate to CSS classes when dynamic styles become complex
- Define animations in CSS and focus directives on triggers

## Considerations
- Returning `null` removes the style, so use intentionally
- Consider performance for continuous updates and control with `requestAnimationFrame`, etc.
- Verify that styles are properly initialized with SSR

## Related Technologies
- HostBinding
- Renderer2.setStyle
- CSS design
