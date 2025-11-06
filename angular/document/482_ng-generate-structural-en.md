# #482 "ng generate directive --structural"

## Overview
The `--structural` option of the `ng generate directive` command generates a template for structural directive and automatically injects TemplateRef and ViewContainerRef.

## Learning Objectives
- Understand how to generate structural directive template with CLI command
- Grasp generated files and injected dependencies
- Learn configuration to use as Standalone directive

## Technical Points
- `ng g directive directives/unless --standalone --structural`
- TemplateRef/ViewContainerRef automatically injected into constructor
- spec file also generated with test preparation ready

## 📺 On-Screen Code (for video)
```bash
ng g directive directives/unless --standalone --structural
```

## 💻 Detailed Implementation Example (for learning)
```bash
# Execution example
ng g directive shared/unless --standalone --structural

# Generated template
@Directive({
  selector: '[appUnless]',
  standalone: true
})
export class UnlessDirective {
  constructor(private tpl: TemplateRef<unknown>, private vc: ViewContainerRef) {}
}
```

## Best Practices
- Use with `--standalone` for structure not dependent on modules
- Adjust selector and Input names to match project conventions right after generation
- Utilize spec file to verify behavior early

## Considerations
- Option names may change depending on CLI version, so check documentation
- Declaration in using module needed if not Standalone
- Template is minimal code, so add logic and tests carefully

## Related Technologies
- Angular CLI
- TemplateRef / ViewContainerRef
- Standalone configuration
