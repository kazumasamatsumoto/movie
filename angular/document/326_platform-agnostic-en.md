# #326 "Platform-Agnostic Implementation"

## Overview
Implementing directives in a platform-agnostic manner allows them to operate safely in non-browser environments (SSR or Web Workers).

## Learning Objectives
- Understand constraints for each platform
- Learn how to branch using `PLATFORM_ID` or `isPlatformBrowser`
- Switch environment-specific implementations via dependent services

## Technical Points
- Receive with `inject(PLATFORM_ID)` or through the constructor
- Abstract DOM-dependent code using Renderer2
- Delegate environment-specific strategies to services

## 📺 On-Screen Code (for video)
```typescript
@Directive({ selector: '[appPlatformSafe]', standalone: true })
export class PlatformSafeDirective implements OnInit {
  private readonly platformId = inject(PLATFORM_ID);
  constructor(private readonly el: ElementRef<HTMLElement>, private readonly r: Renderer2) {}
  ngOnInit(): void {
    if (!isPlatformBrowser(this.platformId)) return;
    this.r.setStyle(this.el.nativeElement, 'outline', '1px solid #0ea5e9');
  }
}
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Injectable({ providedIn: 'root' })
export class ClipboardPort {
  constructor(@Inject(PLATFORM_ID) private readonly platformId: Object) {}
  copy(text: string): Promise<void> {
    if (isPlatformBrowser(this.platformId)) {
      return navigator.clipboard.writeText(text);
    }
    return Promise.reject(new Error('Clipboard not available'));
  }
}

@Directive({
  selector: '[appClipboardButton]',
  standalone: true
})
export class ClipboardButtonDirective {
  @Input({ alias: 'appClipboardButton', required: true }) text!: string;
  private readonly platformId = inject(PLATFORM_ID);

  constructor(private readonly clipboard: ClipboardPort, private readonly el: ElementRef<HTMLButtonElement>) {}

  @HostListener('click')
  async handleClick(): Promise<void> {
    if (!isPlatformBrowser(this.platformId)) return;
    await this.clipboard.copy(this.text);
    this.el.nativeElement.setAttribute('data-copied', 'true');
  }
}
```

## Best Practices
- Check with `isPlatformBrowser` before calling browser-only APIs
- Prepare environment-specific implementations in the service layer and use only abstracted APIs from Directives
- Safely skip in non-browser environments and return explicit error messages

## Considerations
- Initializing during Hydration may cause DOM differences with SSR
- Avoid directly referencing `window` or `document`
- Renderer2 also operates in a limited way in Web Workers, so narrow down the methods used

## Related Technologies
- PLATFORM_ID
- isPlatformBrowser / isPlatformServer
- Angular Universal
