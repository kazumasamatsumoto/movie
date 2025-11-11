# #314 "Configuration Method - tsconfig.json"

Shikoku Metan「Let's learn about how to configure strictNullChecks!」
Zundamon「Do you configure it in tsconfig.json?」
Shikoku Metan「Yes. You can enable it by setting strictNullChecks to true in compilerOptions.」
Zundamon「There's a method to configure individually and a method to configure all at once!」
Shikoku Metan「Exactly. When you set strict: true, all strict options including strictNullChecks are enabled.」
Zundamon「Which one is recommended?」
Shikoku Metan「Yes. Using strict: true is recommended. You can write safer code.」
Zundamon「You can check the configuration with tsc --showConfig!」

---

## 📺 Code for Display

```typescript
/** Example 1: Individual configuration */
// tsconfig.json
{
  "compilerOptions": {
    "strictNullChecks": true
  }
}

/** Example 2: strict configuration (recommended) */
{
  "compilerOptions": {
    "strict": true  // strictNullChecks is also included
  }
}

/** Example 3: Verification method */
tsc --showConfig
// Check the value of strictNullChecks
```
