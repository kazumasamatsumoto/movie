# #474 "CopyToClipboard Directive - Clipboard"

## Overview
The CopyToClipboard directive copies specified text to clipboard with operations like click, notifies completion event to give user feedback.

## Learning Objectives
- Understand copy processing using Clipboard API
- Learn implementation to detect click with HostListener and copy
- Grasp how to notify copy result with Output and reflect in UI

## Technical Points
- `navigator.clipboard.writeText(text)`
- Note that it only works in HTTPS environment
- Consider execCommand as Fallback

## 📺 On-Screen Code (for video)
```typescript
@HostListener('click') async copy(): Promise<void> { await navigator.clipboard.writeText(this.text); }
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Directive({
  selector: '[appCopyToClipboard]',
  standalone: true
})
export class CopyToClipboardDirective {
  @Input('appCopyToClipboard') text = '';
  @Output() copied = new EventEmitter<boolean>();

  @HostListener('click')
  async onClick(): Promise<void> {
    if (!this.text) return;
    try {
      await navigator.clipboard.writeText(this.text);
      this.copied.emit(true);
    } catch (error) {
      console.error('copy failed', error);
      this.copied.emit(false);
    }
  }
}
```

## Best Practices
- Notify copy success/failure with Output and display feedback to user
- Implement fallback or display warning for environments without Clipboard API support
- Accept copy string via Input to keep template concise

## Considerations
- Clipboard API only works on HTTPS or localhost
- Cannot be called synchronously as it's a Promise, so error handling is necessary
- Large text or binary copy has constraints per browser

## Related Technologies
- Clipboard API
- EventEmitter
- Notification by Toast/Tooltip
