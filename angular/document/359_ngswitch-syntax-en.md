# #359 "Basic *ngSwitch Syntax"

## Overview
The basic syntax of `*ngSwitch` sets `[ngSwitch]` on a wrapper element and describes branching by combining `*ngSwitchCase` and `*ngSwitchDefault` inside.

## Learning Objectives
- Understand basic syntax and directive placement
- Learn value comparison methods and how to write cases
- Master template management per case

## Technical Points
- `ngSwitch` is property binding not a directive, cases are treated as structural directives
- Case values can be constants or expressions but align types
- Only one case with the same value is effective

## 📺 Screen Display Code (For Video)
```html
<div [ngSwitch]="mode">
  <p *ngSwitchCase="'preview'">Preview</p>
  <p *ngSwitchCase="'edit'">Edit mode</p>
  <p *ngSwitchDefault>Not selected</p>
</div>
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
type Mode = 'preview' | 'edit' | 'readonly';

@Component({
  selector: 'app-switch-syntax-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div [ngSwitch]="mode">
      <p *ngSwitchCase="'preview'">Preview display.</p>
      <p *ngSwitchCase="'edit'">Displaying editable form.</p>
      <p *ngSwitchCase="'readonly'">View only.</p>
      <p *ngSwitchDefault>Please select a mode.</p>
    </div>
  `
})
export class SwitchSyntaxDemoComponent {
  protected mode: Mode = 'preview';
}
```

## Best Practices
- Constrain mode values with types to prevent unexpected values
- Split templates to separate files or components when cases increase
- Display guidance message in default case to improve UX

## Cautions
- Values used in `*ngSwitchCase` are primitive comparisons, so objects aren't suitable
- Wrapper elements are necessary, so utilize `ng-container` when DOM structure increases
- Verify compatibility when using new syntax `@switch` together

## Related Technologies
- Union Types
- Template Composition
- @switch syntax
