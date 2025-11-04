# #302 "Three Types of Directives"

## Overview
Angular Directives are classified into three types: components, structural, and attribute. Their roles differ based on whether they render UI, control DOM structure, or adjust the behavior of existing elements.

## Learning Objectives
- Organize the main types and characteristics of Directives
- Determine placement and naming rules for projects
- Develop judgment criteria for selecting the appropriate type

## Technical Points
- Component Directives have templates
- Structural Directives handle `ViewContainerRef`/`TemplateRef`
- Attribute Directives adjust appearance using `ElementRef`/`Renderer2`

```typescript
@Component({ selector: 'app-card', template: `<ng-content></ng-content>` })
export class CardComponent {}

@Directive({ selector: '[appShowIf]' })
export class ShowIfDirective { /* Structural */ }

@Directive({ selector: '[appAccent]' })
export class AccentDirective { /* Attribute */ }
```

## 💻 Detailed Implementation Example (For Learning)
```typescript
export function classifyDirective(selector: string): 'component' | 'structural' | 'attribute' {
  if (!selector.includes('[') && !selector.includes('*') && !selector.startsWith('.')) return 'component';
  if (selector.startsWith('*')) return 'structural';
  return 'attribute';
}

console.log(classifyDirective('app-card')); // component
console.log(classifyDirective('*appIf'));   // structural
console.log(classifyDirective('[appAccent]')); // attribute
```

## Best Practices
- Organize by type with consistent folders or prefixes for easy discovery
- Minimize responsibilities for Structural Directives as they involve template transformation
- Use Renderer2 instead of direct DOM manipulation for Attribute Directives

## Cautions
- Even when using components for lightweight presentational purposes, templates are mandatory
- Be aware that Structural Directives can only be applied to a single element
- Mixing types without awareness reduces maintainability

## Related Technologies
- `@Directive`
- `ViewContainerRef`
- Renderer2
