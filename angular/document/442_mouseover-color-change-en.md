# #442 "Mouseover Color Change"

## Overview
A directive that changes color on mouseover emphasizes style on hover and indicates to users that an element is interactive.

## Learning Objectives
- Understand color changing logic using hover events
- Learn the combination of HostListener and HostBinding
- Provide equivalent behavior on focus for accessibility compliance

## Technical Points
- Switch background color with `mouseenter`/`mouseleave`
- Handle `focus`/`blur` for keyboard operation support
- Apply styles with Renderer2 or HostBinding

## 📺 On-Screen Code (for video)
```typescript
@HostListener('mouseenter') onEnter(): void { this.bg = this.hoverColor; }
@HostListener('mouseleave') onLeave(): void { this.bg = this.baseColor; }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appHoverHighlight]',
  standalone: true
})
export class HoverHighlightDirective {
  @Input() baseColor = '#fef08a';
  @Input() hoverColor = '#facc15';

  @HostBinding('style.backgroundColor') background = this.baseColor;

  @HostListener('mouseenter')
  handleEnter(): void {
    this.background = this.hoverColor;
  }

  @HostListener('mouseleave')
  handleLeave(): void {
    this.background = this.baseColor;
  }

  @HostListener('focus')
  handleFocus(): void {
    this.background = this.hoverColor;
  }

  @HostListener('blur')
  handleBlur(): void {
    this.background = this.baseColor;
  }
}
```

## Best Practices
- Monitor `focus`/`blur` for keyboard users
- Accept colors via Input to adapt to themes and states
- Smooth changes with CSS transition

## Considerations
- Background color may not display as expected if element is `display: inline`
- Be careful when specifying transparent colors as they overlap with backgrounds
- Consider event duplication (touch on mobile devices)

## Related Technologies
- HostBinding
- HostListener
- CSS Transition
