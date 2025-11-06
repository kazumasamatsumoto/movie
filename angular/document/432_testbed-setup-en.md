# #432 "TestBed Configuration"

## Overview
In TestBed, register standalone directives in `imports` and host components in `declarations` or `imports` to build the test environment.

## Learning Objectives
- Understand TestBed configuration syntax
- Learn how to configure standalone directives
- Understand how to mock dependent modules and services

## Technical Points
- `TestBed.configureTestingModule({ imports: [HostComponent] })`
- Provide service mocks with `providers`
- Can replace dependent directives with `overrideDirective`

## 📺 On-Screen Code (for video)
```typescript
TestBed.configureTestingModule({ imports: [HostComponent] }).compileComponents();
```

## 💻 Detailed Implementation Example (for learning)
```typescript
beforeEach(async () => {
  await TestBed.configureTestingModule({
    imports: [HostComponent],
    providers: [{ provide: TooltipService, useClass: TooltipServiceMock }]
  }).compileComponents();
});
```

## Best Practices
- With standalone configuration, just register host component in `imports`
- Mock service dependencies in `providers` to maintain test independence
- Call `compileComponents()` only once in `beforeEach` to utilize cache

## Considerations
- List additionally in `imports` when depending on shared modules
- Consider if `resetTestingModule` is necessary as TestBed state is shared between tests
- Don't forget to register test modules like `NoopAnimationsModule`

## Related Technologies
- Angular TestBed
- Standalone Components
- Dependency Injection
