# #466 "Dropzone Implementation"

## Overview
Dropzone visualizes droppable areas, changes style during drag to provide user feedback, and processes received data in drop event.

## Learning Objectives
- Understand visual representation and event processing of dropzone
- Learn state reflection using HostBinding
- Grasp how to retrieve data from drop event and process on user side

## Technical Points
- Toggle class with `dragenter`/`dragleave`
- `dataTransfer.getData` in `drop`
- Pass received data externally with Output event

## 📺 On-Screen Code (for video)
```typescript
@HostBinding('class.is-over') over = false;
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-dropzone',
  standalone: true,
  imports: [CommonModule, DropDirective],
  template: `
    <div class="dropzone" appDrop (dropped)="handleDrop($event)">
      <p>Drop here</p>
    </div>
  `
})
export class DropZoneComponent {
  protected handleDrop(data: string): void {
    console.log('dropped', data);
  }
}
```

CSS example:
```css
.dropzone { border: 2px dashed #94a3b8; padding: 2rem; text-align: center; transition: background .2s; }
.dropzone.is-over { background: #bfdbfe; border-color: #3b82f6; }
```

## Best Practices
- Indicate droppable state with style so users can operate intuitively
- Document accepted data formats and perform validation
- Consider integration with keyboard operations for accessibility

## Considerations
- `dragenter` event fires on child elements too, so control with `contains` check
- Validate dropped data as it cannot be trusted
- Drag & Drop is restricted on mobile, so provide alternative operations

## Related Technologies
- DropDirective
- HTML5 Drag & Drop
- CSS transitions
