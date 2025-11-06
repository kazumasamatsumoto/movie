# #402 "ng generate directive Command"

## Overview
`ng generate directive` is an Angular CLI command that creates directive scaffolding and can automate standalone conversion and test file generation.

## Learning Objectives
- Understand the syntax and options of the CLI command
- Learn the generated file structure
- Know the points to adjust after generation

## Technical Points
- `ng g directive path/name --standalone`
- Spec generation can be suppressed with `--skip-tests`
- Override selector prefix with `--prefix`

## 📺 On-Screen Code (for video)
```bash
ng g directive directives/hover --standalone --prefix=app
```

## 💻 Detailed Implementation Example (for learning)
```bash
# Directive generation
ng g directive shared/focus --standalone

# Generated files
# src/app/shared/focus.directive.ts
# src/app/shared/focus.directive.spec.ts

# focus.directive.ts (scaffolding)
@Directive({
  selector: '[appFocus]',
  standalone: true
})
export class FocusDirective {
  constructor() {}
}
```

## Best Practices
- Verify selector, prefix, and standalone settings immediately after generation
- Generally generate spec files to utilize testing
- Script commands and share with the team to maintain consistency

## Considerations
- If CLI prefix settings are not changed, `app` is automatically added
- Carefully choose the generation directory if overwriting existing files might occur
- Library projects require the `ng generate directive --project` option

## Related Technologies
- Angular CLI Schematics
- Standalone Components
- Workspace configuration (angular.json)
