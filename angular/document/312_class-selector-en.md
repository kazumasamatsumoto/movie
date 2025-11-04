# #312 "Class Selector .xxx"

## Overview
Class selectors apply directives tied to CSS classes, useful when coordinating with existing class naming. However, naming collisions require caution.

## Learning Objectives
- Understand class selector syntax and application methods
- Learn how to coordinate dynamic class switching with directives
- Consider naming strategies across the project

## Technical Points
- Specify with dot like `selector: '.appDraggable'`
- Apply in templates with `class="appDraggable"` or `[class.appDraggable]="flag"`
- Assist class assignment with HostBinding to avoid collisions

## 📺 Display Code (For Video)
```typescript
@Directive({ selector: '.appDraggable', standalone: true })
export class DraggableDirective {
  constructor(private readonly el: ElementRef<HTMLElement>) {}
  ngOnInit(): void {
    this.el.nativeElement.setAttribute('draggable', 'true');
  }
}
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Directive({
  selector: '.appDraggable',
  standalone: true
})
export class DraggableDirective implements OnInit, OnDestroy {
  private removeListener?: () => void;

  constructor(private readonly el: ElementRef<HTMLElement>, private readonly renderer: Renderer2) {}

  ngOnInit(): void {
    const element = this.el.nativeElement;
    this.renderer.setAttribute(element, 'draggable', 'true');
    this.removeListener = this.renderer.listen(element, 'dragstart', event => {
      (event as DragEvent).dataTransfer?.setData('text/plain', element.id);
    });
  }

  ngOnDestroy(): void {
    this.removeListener?.();
    this.renderer.removeAttribute(this.el.nativeElement, 'draggable');
  }
}

@Component({
  selector: 'app-class-selector-demo',
  standalone: true,
  imports: [CommonModule, DraggableDirective],
  template: `
    <div class="appDraggable" id="drag-1">Draggable element</div>
    <div class="dropzone">Drop target</div>
  `,
  styles: [`
    .dropzone { margin-top: 1rem; padding: 1rem; border: 2px dashed #38bdf8; }
  `]
})
export class ClassSelectorDemoComponent {}
```

## Best Practices
- Adopt prefixed class names to avoid collisions with external libraries
- Control dynamic assignment with `[class.appDraggable]="condition"`, removing class when unnecessary
- Document specifications so other developers don't misuse naming

## Cautions
- Delegate styles to separate classes to avoid overlapping with CSS responsibilities
- Not subject to tree-shaking at compile time, so periodically check for unused items
- In SSR, drag events don't fire, so prepare fallbacks

## Related Technologies
- Renderer2
- Drag and Drop API
- BEM/utility class design
