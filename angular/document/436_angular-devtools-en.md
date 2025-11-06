# #436 "Verification with Angular DevTools"

## Overview
Angular DevTools is a browser extension that visualizes component/directive hierarchy and state, allowing verification of whether directives are properly applied.

## Learning Objectives
- Understand basic operations of Angular DevTools
- Learn how to check Directive state and HostBinding values
- Understand procedures for using performance profile

## Technical Points
- Check directive list and Input/Output in Elements tab
- Visualize Change Detection cost in Profiler tab
- Track state changes with Signals support

## 📺 On-Screen Code (for video)
```text
Angular DevTools → Elements → Directives
```

## 💻 Detailed Implementation Example (for learning)
```text
1. Install Chrome extension Angular DevTools
2. Open app and DevTools → Angular → Elements
3. Select element and check applied Directive and HostBinding
```

## Best Practices
- When debugging, check current Input/Output values in DevTools for early detection of unexpected changes
- Check rendering frequency with Profiler to visualize performance issues
- Track dependencies in Signals tab when using Signals

## Considerations
- Difficult to track in production builds without source maps
- Browser extensions cannot be used with SSR, so prepare alternative means
- Elements can be hard to find in large apps due to volume, so devise naming

## Related Technologies
- Chrome DevTools
- Angular Profiler
- Signals debugging
