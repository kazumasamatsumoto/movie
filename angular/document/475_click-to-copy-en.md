# #475 "Click to Copy"

## Overview
Click to copy implementation detects click with HostListener, calls Clipboard API to copy text. Can easily provide copy functionality by applying to buttons or icons.

## Learning Objectives
- Understand coordination between click event and copy processing
- Learn Promise processing when using Clipboard API
- Grasp how to design UI feedback after copy

## Technical Points
- Capture click with HostListener
- `navigator.clipboard.writeText`
- Notify success/failure with Output

## 📺 On-Screen Code (for video)
```html
<button appCopyToClipboard="https://example.com" (copied)="notify($event)">Copy link</button>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-copy-button',
  standalone: true,
  imports: [CommonModule, CopyToClipboardDirective],
  template: `
    <button appCopyToClipboard="https://angular.dev" (copied)="notify($event)">Copy URL</button>
    <span *ngIf="lastResult === true">Copied</span>
    <span *ngIf="lastResult === false">Copy failed</span>
  `
})
export class CopyButtonComponent {
  protected lastResult: boolean | null = null;
  protected notify(result: boolean): void {
    this.lastResult = result;
  }
}
```

## Best Practices
- Communicate result with Tooltip or Snackbar on copy success
- Accept copy string via Input, don't embed secure values in button
- Consider state reset when same button is clicked consecutively

## Considerations
- Clipboard API must be called within user operation context
- Exception occurs on failure, so always implement error handling
- Handle carefully when copying sensitive information to clipboard

## Related Technologies
- Clipboard API
- Toast/Snackbar
- Feedback by Tooltips
