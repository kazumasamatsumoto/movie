# #376 "String Class Specification"

## Overview
Passing a string to `[ngClass]` allows splitting the string by spaces to apply classes. Merges with existing `class` attribute, making it suitable for simple toggles.

## Learning Objectives
- Understand string-format class specification method
- Grasp behavior when combining with class attribute
- Learn patterns for switching strings based on conditions

## Technical Points
- Strings are split by spaces and expanded to multiple classes
- Can switch using conditional operator in binding expression
- `DOMTokenList` eliminates duplicates when overlapping with existing class

## 📺 Screen Display Code (For Video)
```html
<p [ngClass]="isDark ? 'badge badge--dark' : 'badge'">Theme</p>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-ngclass-string-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <label>
      <input type="checkbox" [checked]="isDark" (change)="toggle()" />
      Dark mode
    </label>
    <p class="badge" [ngClass]="isDark ? 'badge--dark badge--outline' : 'badge--light'">
      Current: {{ isDark ? 'Dark' : 'Light' }}
    </p>
  `,
  styles: [`
    .badge { display: inline-block; padding: 0.25rem 0.75rem; border-radius: 9999px; }
    .badge--dark { background: #0f172a; color: #fff; }
    .badge--light { background: #e0f2fe; color: #0f172a; }
    .badge--outline { border: 1px solid currentColor; }
  `]
})
export class NgClassStringDemoComponent {
  protected isDark = false;

  protected toggle(): void {
    this.isDark = !this.isDark;
  }
}
```

## Best Practices
- Organize class names with space separation for readability, avoid overly complex expressions in templates
- Write string generation concisely with conditional operators rather than template literals
- Describe shared classes in advance in `class` attribute, focus binding side on conditional additions

## Cautions
- Trailing extra spaces generate empty classes
- Large numbers of conditional expressions with string concatenation become hard to read, so migrate to other formats
- Unreadable template literals in templates reduce maintainability

## Related Technologies
- class attribute
- Template expressions
- CSS Utilities
