# #370 "Comparison with Traditional Syntax"

## Overview
Comparing traditional `*ngIf`/`*ngFor`/`*ngSwitch` with new Control Flow syntax reveals differences in readability, optimization, and API.

## Learning Objectives
- Understand differences and compatibility between new and old syntax
- Consider migration strategies for projects
- Be able to select consistent template style

## Technical Points
- New syntax uses block notation, old syntax is attribute-based
- Control Flow syntax recommends track clause by default for advanced optimization
- Old syntax continues to be supported and can coexist

## 📺 Screen Display Code (For Video)
```html
<!-- Traditional -->
<li *ngFor="let item of items">{{ item }}</li>
<!-- New syntax -->
@for (item of items) { <li>{{ item }}</li> }
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
@Component({
  selector: 'app-control-flow-compare',
  standalone: true,
  imports: [CommonModule],
  template: `
    <!-- Traditional syntax -->
    <ul>
      <li *ngFor="let item of legacy">{{ item }}</li>
    </ul>

    <!-- New syntax -->
    <ul>
      @for (item of modern; track item) {
        <li>{{ item }}</li>
      }
    </ul>
  `
})
export class ControlFlowCompareComponent {
  protected legacy = ['A', 'B', 'C'];
  protected modern = ['A', 'B', 'C'];
}
```

## Best Practices
- Create guidelines when adopting new syntax and document migration plan
- Migrate existing templates gradually to avoid risks from bulk replacement
- Control in reviews to avoid mixing new and old per component

## Cautions
- Verify build configuration and toolchain support when introducing new syntax
- Omitting track clause in Control Flow syntax may produce warnings
- Thoroughly communicate new notation through documentation and team education

## Related Technologies
- Angular Upgrade Guides
- Control Flow RFC
- Team Coding Guidelines
