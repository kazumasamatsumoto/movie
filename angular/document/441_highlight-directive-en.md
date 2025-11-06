# #441 "Highlight Directive - Highlighting"

## Overview
The Highlight directive changes the background color or outline of an element to visually emphasize it and attract user attention.

## Learning Objectives
- Understand the basic usage and mechanisms of the Highlight directive
- Learn color changing patterns using HostListener/HostBinding
- Improve accessibility during focus and hover interactions

## Technical Points
- Bind background color/border with HostBinding
- Monitor `mouseenter`/`mouseleave` with HostListener
- Dynamically specify colors with Input

## 📺 On-Screen Code (for video)
```typescript
@HostBinding('style.backgroundColor') bg = '#fef08a';
@HostListener('mouseenter') activate(): void { this.bg = '#fde047'; }
@HostListener('mouseleave') deactivate(): void { this.bg = '#fef08a'; }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appHighlight]',
  standalone: true
})
export class HighlightDirective implements OnChanges {
  @Input('appHighlight') color = '#fde047';
  @Input() hoverColor = '#facc15';
  @HostBinding('style.backgroundColor') background = this.color;

  @HostListener('mouseenter')
  onEnter(): void {
    this.background = this.hoverColor;
  }

  @HostListener('mouseleave')
  onLeave(): void {
    this.background = this.color;
  }

  ngOnChanges(): void {
    this.background = this.color;
  }
}
```

## Best Practices
- Accept color settings via Input and provide default values for flexibility
- Handle focus events to support keyboard operations
- Add ARIA attributes and descriptions to improve accessibility

## Considerations
- Inline styles have high priority; be mindful of consistency with themes
- Set transition in CSS to avoid flickering
- Specify initial values to ensure proper initial color display in SSR

## Related Technologies
- HostBinding/HostListener
- Angular Signals
- Accessibility (focus visualization)
