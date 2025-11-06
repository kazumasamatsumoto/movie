# #477 "ScrollSpy Directive - Scroll Monitoring"

## Overview
The ScrollSpy directive identifies the currently displayed section according to scroll position and provides information to highlight navigation.

## Learning Objectives
- Understand basic structure of ScrollSpy
- Learn how to monitor sections with IntersectionObserver
- Grasp design of notifying active section with Output event

## Technical Points
- Register monitoring target sections with Input
- Detect visible section with IntersectionObserver
- Notify active ID with Output

## 📺 On-Screen Code (for video)
```typescript
@Output() sectionChange = new EventEmitter<string>();
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appScrollSpy]',
  standalone: true
})
export class ScrollSpyDirective implements OnInit, OnDestroy {
  @Input() spyTargets: NodeListOf<HTMLElement> | HTMLElement[] = [];
  @Output() sectionChange = new EventEmitter<string>();
  private observer?: IntersectionObserver;

  constructor(@Inject(PLATFORM_ID) private readonly platformId: Object) {}

  ngOnInit(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    this.observer = new IntersectionObserver(entries => {
      const visible = entries
        .filter(entry => entry.isIntersecting)
        .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
      if (visible?.target) {
        const id = (visible.target as HTMLElement).id;
        if (id) this.sectionChange.emit(id);
      }
    }, { rootMargin: '-50% 0px -50% 0px', threshold: [0, 0.25, 0.5, 0.75, 1] });

    const targets = Array.isArray(this.spyTargets) ? this.spyTargets : Array.from(this.spyTargets);
    targets.forEach(target => this.observer?.observe(target));
  }

  ngOnDestroy(): void {
    this.observer?.disconnect();
  }
}
```

## Best Practices
- Set rootMargin to switch active near section center
- Notify ID with Output and highlight in navigation component
- Improve UX by combining with hash update and scroll position sync

## Considerations
- Adjust threshold to increase detection accuracy when sections are short
- Cannot monitor in SSR, so perform browser detection
- Start monitoring after height is determined for elements with unstable height

## Related Technologies
- IntersectionObserver
- Router fragment/href
- Navigation component
