# #31 「論理否定演算子 - !による型の扱い」台本

四国めたん「TypeScriptの論理否定演算子!について学びましょう！」
ずんだもん「!演算子って、どんな機能なの？」
四国めたん「真偽値を反転させる演算子です。内部的にはブール代数に基づいた型推論が行われています」
ずんだもん「型ガードとも関係があるの?」
四国めたん「はい！条件分岐と組み合わせることで、型の絞り込みができます。!!で明示的な真偽値変換も可能です」
ずんだもん「なるほど！null/undefinedチェックで活躍しそうだね！」
四国めたん「Angularのテンプレートやデコレータ、Nest.jsのバリデーションで型安全性が向上します」
ずんだもん「型推論と組み合わせて開発効率アップだよ！」

---

## 📺 画面表示用コード

```typescript
// 基本的な!演算子
const isActive: boolean = true;
const isInactive = !isActive; // false

const hasError: boolean = false;
const isValid = !hasError; // true
```

```typescript
// 型ガードとの組み合わせ
function processUser(user: User | null) {
  if (!user) {
    return; // user is null
  }
  // ここではuserはUser型に絞り込まれる
  console.log(user.name);
}
```

```typescript
// !!による真偽値変換
const value: string | undefined = "Hello";
const hasValue: boolean = !!value; // true

const empty: string | undefined = undefined;
const isEmpty: boolean = !!empty; // false
```

```typescript
// Angular: Optional Chainingと組み合わせ
@Component({...})
export class UserComponent {
  user?: User;
  
  get hasPermission(): boolean {
    return !!this.user?.permissions?.length;
  }
}
```

```typescript
// Nest.js: DTOバリデーション
export class CreateUserDto {
  @IsNotEmpty()
  name: string;
  
  get isValid(): boolean {
    return !!(this.name?.trim());
  }
}
```