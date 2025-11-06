# #467 "Drag & Drop Integration"

## Overview
To integrate drag and drop, structure so drag side holds and sends data while drop side receives and processes it, and manage state with shared service if needed.

## Learning Objectives
- Understand the flow of data passing between drag and drop
- Learn how to share information with EventEmitter or service
- Design integration with multiple drop zones

## Technical Points
- DragDirective sets data, DropDirective gets
- Service holds currently dragging data
- Notify drop result externally with Output event

## 📺 On-Screen Code (for video)
```typescript
@Injectable({ providedIn: 'root' })
export class DragDataService { data?: unknown; }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Injectable({ providedIn: 'root' })
export class DragContextService {
  data?: unknown;
}

@Directive({
  selector: '[appDragSource]',
  standalone: true
})
export class DragSourceDirective {
  @Input() dragData?: unknown;

  constructor(private readonly context: DragContextService) {}

  @HostListener('dragstart', ['$event'])
  onDragStart(event: DragEvent): void {
    event.dataTransfer?.setData('text/plain', JSON.stringify(this.dragData));
    this.context.data = this.dragData;
  }
}

@Directive({
  selector: '[appDropTarget]',
  standalone: true
})
export class DropTargetDirective {
  @Output() dropped = new EventEmitter<unknown>();

  constructor(private readonly context: DragContextService) {}

  @HostListener('drop', ['$event'])
  onDrop(event: DragEvent): void {
    event.preventDefault();
    const data = this.context.data ?? event.dataTransfer?.getData('text/plain');
    this.dropped.emit(data);
    this.context.data = undefined;
  }
}
```

## Best Practices
- Share data during drag with service to make it available for different drop targets
- Notify with Output on Drop, letting user side execute necessary processing
- Validate data for security and handle invalid input

## Considerations
- DataTransfer only supports strings, so JSONify objects
- When using DragContextService, consider parallel dragging (identify by ID)
- HTML5 Drag & Drop may not work on mobile in some cases

## Related Technologies
- DragContextService
- HTML5 Drag & Drop
- EventEmitter
