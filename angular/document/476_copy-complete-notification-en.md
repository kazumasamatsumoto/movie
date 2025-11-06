# #476 "Copy Complete Notification"

## Overview
Copy complete notification displays feedback using Tooltip, Snackbar, or Output event so users can immediately grasp success or failure of copy operation.

## Learning Objectives
- Understand how to get success/failure information from copy directive
- Learn UI feedback (message/icon) according to success or failure
- Grasp implementation considering notification display lifetime and accessibility

## Technical Points
- Receive success/failure with Output `(copied)` event
- Call Snackbar or Toast service
- Notify voice users with ARIA live region

## 📺 On-Screen Code (for video)
```html
<button appCopyToClipboard="text" (copied)="showToast($event)">Copy</button>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-copy-toast',
  standalone: true,
  imports: [CommonModule, CopyToClipboardDirective],
  template: `
    <button appCopyToClipboard="Angular Rocks!" (copied)="notify($event)">Copy</button>
    <div aria-live="polite">{{ message }}</div>
  `
})
export class CopyToastComponent {
  protected message = '';

  protected notify(success: boolean): void {
    this.message = success ? 'Copied ✅' : 'Copy failed ❌';
    setTimeout(() => (this.message = ''), 2000);
  }
}
```

## Best Practices
- Provide visual feedback using Snackbar/Toast component
- Notify screen readers with ARIA live region
- Clear message in short time or overwrite with re-copy

## Considerations
- Becomes unresponsive if both success/failure handling not implemented
- Manage so messages don't pile up when copying same element consecutively
- Excessive notifications harm UX, so adjust according to requirements

## Related Technologies
- CopyToClipboardDirective
- Snackbar/Toast service
- ARIA live region
