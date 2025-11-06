# #479 "Navigation Activation"

## Overview
Coordinating with ScrollSpy, receive currently displayed section ID and add active class to navigation links to show position to user.

## Learning Objectives
- Understand how to receive events from ScrollSpy and update navigation
- Learn active class assignment and hash update
- Grasp coordination with smooth scroll etc.

## Technical Points
- Match received ID from Output event with nav links
- Display active state with HostBinding or ngClass
- Use `Location.replaceState` etc. for hash update

## 📺 On-Screen Code (for video)
```html
<nav [appScrollSpy]="sections" (sectionChange)="active = $event">
  <a [class.is-active]="active === 'section-1'" href="#section-1">Section 1</a>
</nav>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-scrollspy-nav',
  standalone: true,
  imports: [CommonModule, ScrollSpyDirective],
  template: `
    <nav appScrollSpy [spyTargets]="sections" (sectionChange)="setActive($event)">
      <a *ngFor="let section of sections" [class.is-active]="active === section.id" [href]="'#' + section.id">
        {{ section.label }}
      </a>
    </nav>
  `
})
export class ScrollSpyNavComponent implements AfterViewInit {
  protected sections = [
    { id: 'section-1', label: 'Overview' },
    { id: 'section-2', label: 'Details' },
    { id: 'section-3', label: 'Examples' }
  ];
  protected active = this.sections[0].id;

  constructor(private readonly location: Location) {}

  protected setActive(id: string): void {
    this.active = id;
    this.location.replaceState(`#${id}`);
  }
}
```

## Best Practices
- Express navigation active state with class and visualize with CSS
- Update hash so same position is restored on page reload
- Be mindful that hash update occurs browser-side in SSG/SSR environments

## Considerations
- `replaceState` doesn't add entry to browser history, so use appropriately
- Adjust offset to section if scroll position is inaccurate
- Improves UX to implement smooth scroll when navigation links are clicked

## Related Technologies
- ScrollSpyDirective
- Router fragment
- Smooth Scroll API
