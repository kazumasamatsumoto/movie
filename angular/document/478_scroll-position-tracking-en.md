# #478 "Scroll Position Tracking"

## Overview
In ScrollSpy, need to track displayed section, monitor position with IntersectionObserver or scroll event to update active section ID.

## Learning Objectives
- Understand scroll position tracking techniques
- Learn concurrent use of IntersectionObserver and scroll events
- Grasp active section determination logic

## Technical Points
- Specify list of monitoring targets
- Use scroll event as fallback if IntersectionObserver is unavailable
- Select section with largest display area as active

## 📺 On-Screen Code (for video)
```typescript
entries.filter(e => e.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
```

## 💻 Detailed Implementation Example (for learning)
```typescript
private handleScrollFallback(): void {
  const scrollTop = window.scrollY;
  const targets = document.querySelectorAll<HTMLElement>('[data-spy]');
  const current = Array.from(targets)
    .map(section => {
      const rect = section.getBoundingClientRect();
      return { id: section.id, offset: Math.abs(rect.top) };
    })
    .sort((a, b) => a.offset - b.offset)[0];
  if (current) {
    this.sectionChange.emit(current.id);
  }
}
```

## Best Practices
- Implement with IntersectionObserver, fallback to scroll event for unsupported environments
- Always add `data-spy` or ID to section elements
- Optimize scroll event processing with Debounce or throttle

## Considerations
- High-frequency scroll events affect performance, so optimize
- Recalculate on resize if section height changes dynamically
- Adjust offset to detect correct position if header is fixed

## Related Technologies
- IntersectionObserver
- RxJS throttleTime
- Router fragment
