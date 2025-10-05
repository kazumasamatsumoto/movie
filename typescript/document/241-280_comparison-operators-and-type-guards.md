# TypeScript 比較演算子と型ガード 完全ガイド（241-280）

このガイドは、TypeScript v5.9における比較演算子と型ガードの完全な学習資料です。

## 目次

- [3-4: 比較演算子（241-255）](#3-4-比較演算子241-255)
- [3-5: 型ガード（256-270）](#3-5-型ガード256-270)
- [3-6: Angular/Nest.js実践（271-275）](#3-6-angularnestjs実践271-275)
- [3-7: よくある間違い（276-280）](#3-7-よくある間違い276-280)

---

## 3-4: 比較演算子（241-255）

### 等価演算子の基本

TypeScriptには厳密比較（===）と緩い比較（==）があります。型安全性を保つため、常に===を使用することが推奨されます。

```typescript
// 厳密比較（推奨）
1 === "1"    // false
1 === 1      // true

// 緩い比較（非推奨）
1 == "1"     // true（型変換が発生）
```

### 大小比較演算子

数値や文字列の比較に使用します。

```typescript
// 数値比較
5 > 3        // true
5 >= 5       // true

// 文字列比較（辞書順）
"apple" < "banana"  // true
```

---

## 3-5: 型ガード（256-270）

### 型ガードとは

型ガードは実行時に型を絞り込む仕組みです。

```typescript
function processValue(value: string | number) {
  if (typeof value === "string") {
    // value: string
    return value.toUpperCase();
  }
  // value: number
  return value.toFixed(2);
}
```

### 主要な型ガード

#### typeof型ガード
```typescript
typeof value === "string"
typeof value === "number"
```

#### instanceof型ガード
```typescript
if (error instanceof Error) {
  console.log(error.message);
}
```

#### in型ガード
```typescript
if ("email" in user) {
  console.log(user.email);
}
```

#### ユーザー定義型ガード
```typescript
function isString(value: unknown): value is string {
  return typeof value === "string";
}
```

---

## 3-6: Angular/Nest.js実践（271-275）

### Angularでの型ガード

```typescript
// テンプレートでの使用
@Component({
  template: `
    <div *ngIf="user">
      {{ user.name }}
    </div>
  `
})
export class UserComponent {
  user: User | null = null;
}
```

### Nest.jsでの型ガード

```typescript
// DTOバリデーション
@Injectable()
export class UserService {
  findUser(id: string | number): User {
    if (typeof id === "string") {
      return this.findByUsername(id);
    }
    return this.findById(id);
  }
}
```

---

## 3-7: よくある間違い（276-280）

### 間違い1: ==の使用
```typescript
// ❌ 悪い例
if (value == null) { }

// ✅ 良い例
if (value === null || value === undefined) { }
// または
if (value == null) { } // nullとundefinedの両方をチェックする場合のみOK
```

### 間違い2: truthyとの混同
```typescript
// ❌ 悪い例
if (value) { }  // 0や""もfalseになる

// ✅ 良い例
if (value !== null && value !== undefined) { }
```

### 間違い3: 文字列"true"との混同
```typescript
// ❌ 悪い例
const flag: boolean = "true" as any;

// ✅ 良い例
const flag: boolean = value === "true";
```

---

## まとめ

- 常に`===`を使用する
- 適切な型ガードで型安全性を確保する
- Angular/Nest.jsでも型ガードを活用する
- よくある間違いを避ける

このガイドを参考に、型安全なTypeScriptコードを書きましょう！
