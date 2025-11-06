# #465 "Drop Directive - Dropping"

## Overview
The Drop directive defines an area that accepts dragged elements, processing dragover/dragenter/drop events to handle drop data.

## Learning Objectives
- Understand basics of HTML5 Drag & Drop API
- Learn how to set events on drop zones
- Grasp data transfer and permission determination mechanisms

## Technical Points
- Make droppable with `event.preventDefault()` in `dragover`
- Get data from `event.dataTransfer` in `drop` event
- Change style during drop with HostBinding

## 📺 On-Screen Code (for video)
```typescript
@HostListener('dragover', ['$event']) onDragOver(event: DragEvent) { event.preventDefault(); }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appDrop]',
  standalone: true
})
export class DropDirective {
  @HostBinding('class.is-over') over = false;
  @Input() accept?: string[];
  @Output() dropped = new EventEmitter<string>();

  @HostListener('dragover', ['$event'])
  onDragOver(event: DragEvent): void {
    event.preventDefault();
  }

  @HostListener('dragenter', ['$event'])
  onDragEnter(event: DragEvent): void {
    event.preventDefault();
    this.over = true;
  }

  @HostListener('dragleave')
  onDragLeave(): void {
    this.over = false;
  }

  @HostListener('drop', ['$event'])
  onDrop(event: DragEvent): void {
    event.preventDefault();
    this.over = false;
    const data = event.dataTransfer?.getData('text/plain');
    if (!data) return;
    if (this.accept && !this.accept.includes(data)) return;
    this.dropped.emit(data);
  }
}
```

## Best Practices
- Call `preventDefault` in `dragover` to allow drop
- Change drop zone visual with HostBinding to provide user feedback
- Determine drop acceptability with Input for flexible control

## Considerations
- DataTransfer only supports strings, so JSONify complex data
- Additional processing needed to support drop via `files` for image files etc.
- Verify as event behavior differs between browsers

## Related Technologies
- Drag & Drop API
- EventEmitter
- Integration with DragDirective
