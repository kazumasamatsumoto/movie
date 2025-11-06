# #334 "Adding and Removing Structure"

## Overview
In Structural Directives, `ViewContainerRef` is used to insert and remove templates, dynamically controlling the DOM structure.

## Learning Objectives
- Understand the roles of `createEmbeddedView`/`clear`
- Learn view management with awareness of differential updates
- Grasp the timing of resource release

## Technical Points
- Insert views with `createEmbeddedView(template, context?)`
- Destroy unnecessary views with `remove()`/`clear()`
- Can also retain EmbeddedViewRef for reuse and updates

## 📺 On-Screen Code (for video)
```typescript
this.container.clear();
if (condition) this.container.createEmbeddedView(this.template);
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appToggleView]',
  standalone: true
})
export class ToggleViewDirective implements OnChanges, OnDestroy {
  @Input({ alias: 'appToggleView', required: true }) active!: boolean;
  private currentView?: EmbeddedViewRef<unknown>;

  constructor(private readonly container: ViewContainerRef, private readonly template: TemplateRef<unknown>) {}

  ngOnChanges(): void {
    if (this.active) {
      if (!this.currentView) {
        this.currentView = this.container.createEmbeddedView(this.template);
      }
    } else {
      this.container.clear();
      this.currentView = undefined;
    }
  }

  ngOnDestroy(): void {
    this.container.clear();
  }
}

@Component({
  selector: 'app-toggle-view-demo',
  standalone: true,
  imports: [CommonModule, ToggleViewDirective],
  template: `
    <label>
      <input type="checkbox" [(ngModel)]="checked" />
      Toggle display
    </label>
    <section *appToggleView="checked">Toggle target</section>
  `
})
export class ToggleViewDemoComponent {
  protected checked = false;
}
```

## Best Practices
- After view generation, retain a reference to avoid unnecessary regeneration
- Understand the difference between `clear` and `remove` to delete only specific indices
- Always destroy views in `ngOnDestroy` to prevent memory leaks

## Considerations
- Frequent generation/deletion affects performance, so suppress the frequency of conditional expression changes
- To avoid forgetting to destroy Observable subscriptions, utilize `onDestroy` within EmbeddedView
- In SSR, ViewContainerRef doesn't perform DOM operations, so limit side effects

## Related Technologies
- EmbeddedViewRef
- Lifecycle Hooks
- Angular Forms (used in examples)
