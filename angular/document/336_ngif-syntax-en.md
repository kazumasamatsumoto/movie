# #336 "*ngIf Basic Syntax"

## Overview
`*ngIf="condition"` is the basic syntax that renders templates when the condition is true and doesn't generate views when false.

## Learning Objectives
- Understand the format and evaluation timing of `*ngIf`
- Learn how to write readable conditional expressions
- Gain design guidelines to avoid complex expressions

## Technical Points
- Angular judges conditions through truthy/falsy evaluation
- Component properties and methods can be referenced within expressions
- Keep conditional expressions lightweight to avoid excessive re-evaluation

## 📺 On-Screen Code (for video)
```html
<section *ngIf="userLoaded">User has been loaded.</section>
```

## 💻 Detailed Implementation Example (for learning)
```typescript
@Component({
  selector: 'app-ngif-syntax-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <button (click)="fetch()">Load user</button>
    <p *ngIf="isLoading">Loading...</p>
    <article *ngIf="user">
      <h3>{{ user.name }}</h3>
      <p>{{ user.email }}</p>
    </article>
  `
})
export class NgIfSyntaxDemoComponent {
  protected isLoading = false;
  protected user: { name: string; email: string } | null = null;

  protected fetch(): void {
    this.isLoading = true;
    setTimeout(() => {
      this.user = { name: 'Angular User', email: 'user@example.com' };
      this.isLoading = false;
    }, 800);
  }
}
```

## Best Practices
- Avoid writing method calls in conditional expressions as they will be executed each time
- Use variable names that represent state so the template's intent is conveyed
- Pre-calculate complex conditions with getters or Signals

## Considerations
- Understand the difference between `*ngIf` and `[hidden]`, using it only when DOM destruction is necessary
- Don't perform asynchronous processing directly in conditional expressions
- With strictTemplates, type safety is guaranteed, but using any types makes errors harder to detect

## Related Technologies
- Angular Signals
- Change Detection
- TypeScript strictTemplates
