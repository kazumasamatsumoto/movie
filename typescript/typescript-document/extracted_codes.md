## File: 246.txt

# #246 「大なり演算子 - >」 

 

```typescript
// 大なり演算子の使用例

// 数値の比較
console.log(10 > 5);   // true
console.log(5 > 10);   // false
console.log(5 > 5);    // false

// 型安全な比較関数
function isGreater(a: number, b: number): boolean {
  return a > b;
}

// 条件分岐での使用
const age: number = 20;
if (age > 18) {
  console.log('成人です');
}
```

## File: 247.txt

# #247 「大なり演算子の型」 

 

```typescript
// 大なり演算子の型別比較

// 数値の比較
const num1: number = 10;
const num2: number = 5;
console.log(num1 > num2); // true

// 文字列の比較（辞書順）
const str1: string = 'b';
const str2: string = 'a';
console.log(str1 > str2); // true

// Date型の比較
const date1: Date = new Date('2024-01-02');
const date2: Date = new Date('2024-01-01');
console.log(date1 > date2); // true
```

## File: 248.txt

# #248 「小なり演算子 - <」 

 

```typescript
// 小なり演算子の使用例

// 数値の比較
console.log(5 < 10);   // true
console.log(10 < 5);   // false
console.log(5 < 5);    // false

// 型安全な比較関数
function isLess(a: number, b: number): boolean {
  return a < b;
}

// 範囲チェック
const score: number = 75;
if (score < 80) {
  console.log('合格ラインです');
}
```

## File: 249.txt

# #249 「以上演算子 - >=」 

 

```typescript
// 以上演算子の使用例

// 数値の比較
console.log(10 >= 5);   // true
console.log(10 >= 10);  // true
console.log(5 >= 10);   // false

// 型安全な比較関数
function isGreaterOrEqual(a: number, b: number): boolean {
  return a >= b;
}

// 最小値チェック
const age: number = 18;
if (age >= 18) {
  console.log('成人です');
}
```

## File: 250.txt

# #250 「以下演算子 - <=」 

 

```typescript
// 以下演算子の使用例

// 数値の比較
console.log(5 <= 10);   // true
console.log(5 <= 5);    // true
console.log(10 <= 5);   // false

// 型安全な比較関数
function isLessOrEqual(a: number, b: number): boolean {
  return a <= b;
}

// 最大値チェック
const score: number = 100;
if (score <= 100) {
  console.log('有効なスコアです');
}
```

## File: 251.txt

# #251 「文字列の比較」 

 

```typescript
// 文字列の比較

// 辞書順の比較
console.log('apple' < 'banana'); // true
console.log('cat' > 'dog');      // false

// 大文字と小文字
console.log('A' < 'a');  // true
console.log('Z' < 'a');  // true

// 長さの異なる文字列
console.log('abc' < 'abcd'); // true

// 型安全な文字列比較
function compareStrings(a: string, b: string): number {
  return a === b ? 0 : a < b ? -1 : 1;
}
```

## File: 252.txt

# #252 「数値の比較」 

 

```typescript
// 数値の比較

// 整数の比較
console.log(10 > 5);    // true
console.log(10 === 10); // true

// 浮動小数点の問題
console.log(0.1 + 0.2 === 0.3); // false

// 許容誤差を使った比較
function isClose(a: number, b: number, epsilon = 1e-10): boolean {
  return Math.abs(a - b) < epsilon;
}

console.log(isClose(0.1 + 0.2, 0.3)); // true
```

## File: 253.txt

# #253 「booleanの比較」 

 

```typescript
// booleanの比較

// 厳密な比較
console.log(true === true);   // true
console.log(false === false); // true
console.log(true === false);  // false

// 型の違い
console.log(true === 1);  // false
console.log(true == 1);   // true

// 型安全な比較関数
function isSameBoolean(a: boolean, b: boolean): boolean {
  return a === b;
}
```

## File: 254.txt

# #254 「null/undefinedの比較」 

 

```typescript
// null/undefinedの比較

// ==による比較（型変換あり）
console.log(null == undefined);  // true

// ===による比較（厳密）
console.log(null === undefined); // false
console.log(null === null);      // true
console.log(undefined === undefined); // true

// 型安全なチェック
function isNull(value: unknown): value is null {
  return value === null;
}

function isUndefined(value: unknown): value is undefined {
  return value === undefined;
}
```

## File: 255.txt

# #255 「比較演算まとめ」 

 

```typescript
// 比較演算のまとめ

// ✅ 推奨: ===の使用
if (value === 0) { }

// ✅ 浮動小数点の比較
function isClose(a: number, b: number): boolean {
  return Math.abs(a - b) < 1e-10;
}

// ✅ null/undefinedチェック
if (value === null) { }
if (value === undefined) { }

// ✅ 範囲チェック
if (score >= 60 && score <= 100) { }
```

## File: 256.txt

# #256 「型ガードとは」 

 

```typescript
// 型ガードとは

// Union型の例
function processValue(value: string | number) {
  if (typeof value === 'string') {
    // この中ではstring型として扱われる
    console.log(value.toUpperCase());
  } else {
    // この中ではnumber型として扱われる
    console.log(value.toFixed(2));
  }
}

// 型ガードの効果
type User = { name: string; age: number };
function isUser(obj: unknown): obj is User {
  return typeof obj === 'object' && obj !== null && 
    'name' in obj && 'age' in obj;
}
```

## File: 257.txt

# #257 「typeof型ガード」 

 

```typescript
// typeof型ガード

function processValue(value: string | number | boolean) {
  if (typeof value === 'string') {
    console.log(value.toUpperCase());
  } else if (typeof value === 'number') {
    console.log(value.toFixed(2));
  } else {
    console.log(!value);
  }
}

// 型安全な処理
function double(value: unknown): number | undefined {
  if (typeof value === 'number') {
    return value * 2;
  }
  return undefined;
}
```

## File: 258.txt

# #258 「typeof型ガードの戻り値」 

 

```typescript
// typeof型ガードの戻り値

console.log(typeof 'hello');     // 'string'
console.log(typeof 42);          // 'number'
console.log(typeof true);        // 'boolean'
console.log(typeof {});          // 'object'
console.log(typeof []);          // 'object' (配列もobject)
console.log(typeof null);        // 'object' (注意!)
console.log(typeof undefined);   // 'undefined'
console.log(typeof function(){}); // 'function'

// nullの正しいチェック
function isNull(value: unknown): value is null {
  return value === null;
}
```

## File: 259.txt

# #259 「instanceof型ガード」 

 

```typescript
// instanceof型ガード

function processValue(value: Date | string) {
  if (value instanceof Date) {
    console.log(value.getFullYear());
  } else {
    console.log(value.toUpperCase());
  }
}

// 複数のクラス
class User { name: string = ''; }
class Admin { role: string = ''; }

function processEntity(entity: User | Admin) {
  if (entity instanceof Admin) {
    console.log(entity.role);
  } else {
    console.log(entity.name);
  }
}
```

## File: 260.txt

# #260 「in型ガード」 

 

```typescript
// in型ガード

type Dog = { bark: () => void; };
type Cat = { meow: () => void; };

function makeSound(animal: Dog | Cat) {
  if ('bark' in animal) {
    animal.bark();
  } else {
    animal.meow();
  }
}

// 複雑な型の判別
type Success = { success: true; data: string };
type Error = { success: false; error: string };

function handle(result: Success | Error) {
  if ('data' in result) {
    console.log(result.data);
  }
}
```

## File: 261.txt

# #261 「Array.isArray()」 

 

```typescript
// Array.isArray()

function processValue(value: string[] | string) {
  if (Array.isArray(value)) {
    console.log(value.join(', '));
  } else {
    console.log(value.toUpperCase());
  }
}

// 配列かどうかの判定
console.log(Array.isArray([]));       // true
console.log(Array.isArray([1, 2]));   // true
console.log(Array.isArray('hello')); // false
console.log(Array.isArray({}));       // false
console.log(Array.isArray(null));     // false
```

## File: 262.txt

# #262 「null/undefinedチェック」 

 

```typescript
// null/undefinedチェック

// 厳密なチェック
function process(value: string | null | undefined) {
  if (value === null) {
    console.log('null');
  } else if (value === undefined) {
    console.log('undefined');
  } else {
    console.log(value.toUpperCase());
  }
}

// 両方をチェック
function handle(value: string | null | undefined) {
  if (value != null) {
    // nullでもundefinedでもない
    console.log(value.toUpperCase());
  }
}
```

## File: 263.txt

# #263 「truthyチェック」 

 

```typescript
// truthyチェック

function process(value: string | number | null) {
  if (value) {
    // truthyな値の場合
    console.log('値が存在します');
  }
}

// truthy値の例
console.log(Boolean(1));        // true
console.log(Boolean('hello'));  // true
console.log(Boolean([]));       // true
console.log(Boolean({}));       // true
console.log(Boolean(true));     // true
```

## File: 264.txt

# #264 「falsyチェック」 

 

```typescript
// falsyチェック

function process(value: string | number | null) {
  if (!value) {
    // falsyな値の場合
    console.log('値が存在しないか、falsy値です');
  }
}

// falsy値の例
console.log(Boolean(false));    // false
console.log(Boolean(0));        // false
console.log(Boolean(''));       // false
console.log(Boolean(null));     // false
console.log(Boolean(undefined));// false
console.log(Boolean(NaN));      // false
```

## File: 265.txt

# #265 「falsyな値一覧」 

 

```typescript
// falsyな値一覧（全6つ）

console.log(Boolean(false));     // false
console.log(Boolean(0));         // false
console.log(Boolean(''));        // false
console.log(Boolean(null));      // false
console.log(Boolean(undefined)); // false
console.log(Boolean(NaN));       // false

// 注意: これらはtruthyです
console.log(Boolean('0'));       // true (文字列)
console.log(Boolean([]));        // true (空配列)
console.log(Boolean({}));        // true (空オブジェクト)
```

## File: 266.txt

# #266 「truthyな値」 

 

```typescript
// truthyな値の例

console.log(Boolean(true));      // true
console.log(Boolean(1));         // true
console.log(Boolean(-1));        // true
console.log(Boolean('hello'));   // true
console.log(Boolean('0'));       // true (文字列の'0')
console.log(Boolean([]));        // true (空配列)
console.log(Boolean({}));        // true (空オブジェクト)
console.log(Boolean(new Date())); // true
console.log(Boolean(function(){})); // true
```

## File: 267.txt

# #267 「明示的なboolean変換」 

 

```typescript
// 明示的なboolean変換

// Boolean()関数
const value1 = Boolean('hello'); // true
const value2 = Boolean(0);       // false

// !!演算子（二重否定）
const value3 = !!'hello';  // true
const value4 = !!0;        // false

// 型安全な変換
function toBoolean(value: unknown): boolean {
  return Boolean(value);
}

// 条件式での使用
const isValid = Boolean(userInput);
```

## File: 268.txt

# #268 「型述語関数 - x is Type」 

 

```typescript
// 型述語関数

function isString(value: unknown): value is string {
  return typeof value === 'string';
}

function isNumber(value: unknown): value is number {
  return typeof value === 'number';
}

// 使用例
function process(value: unknown) {
  if (isString(value)) {
    console.log(value.toUpperCase());
  } else if (isNumber(value)) {
    console.log(value.toFixed(2));
  }
}
```

## File: 269.txt

# #269 「型ガードのベストプラクティス」 

 

```typescript
// 型ガードのベストプラクティス

// ✅ 型述語関数の活用
function isUser(obj: unknown): obj is { name: string; age: number } {
  return typeof obj === 'object' && obj !== null &&
    'name' in obj && 'age' in obj;
}

// ✅ 早期リターン
function process(value: string | null) {
  if (value === null) return;
  console.log(value.toUpperCase());
}

// ✅ 明示的なnullチェック
if (value !== null && value !== undefined) {
  // 安全に使用
}
```

## File: 270.txt

# #270 「型ガードまとめ」 

 

```typescript
// 型ガードまとめ

// typeof - プリミティブ型
if (typeof value === 'string') { }

// instanceof - クラス
if (value instanceof Date) { }

// in - オブジェクトプロパティ
if ('name' in obj) { }

// Array.isArray - 配列
if (Array.isArray(value)) { }

// 型述語関数 - カスタム型ガード
function isUser(obj: unknown): obj is User {
  return typeof obj === 'object' && obj !== null && 'name' in obj;
}
```

## File: 271.txt

# #271 「Angularテンプレートでのboolean」 

 

```typescript
// Angularテンプレートでのboolean

// コンポーネント
@Component({
  selector: 'app-user',
  template: `
    <div *ngIf="isLoggedIn">ログイン済み</div>
    <button [disabled]="!isValid">送信</button>
  `
})
export class UserComponent {
  isLoggedIn: boolean = true;
  isValid: boolean = false;
  
  checkStatus(): void {
    if (this.isLoggedIn && this.isValid) {
      console.log('OK');
    }
  }
}
```

## File: 272.txt

# #272 「*ngIfディレクティブ」 

 

```typescript
// *ngIfディレクティブ

@Component({
  selector: 'app-example',
  template: `
    <div *ngIf="isVisible">表示されます</div>
    
    <div *ngIf="isLoggedIn; else loginTemplate">
      ログイン済み
    </div>
    <ng-template #loginTemplate>
      未ログイン
    </ng-template>
  `
})
export class ExampleComponent {
  isVisible: boolean = true;
  isLoggedIn: boolean = false;
}
```

## File: 273.txt

# #273 「[disabled]属性」 

 

```typescript
// [disabled]属性

@Component({
  selector: 'app-form',
  template: `
    <button [disabled]="isSubmitting">送信</button>
    <input [disabled]="!isEditable" />
  `
})
export class FormComponent {
  isSubmitting: boolean = false;
  isEditable: boolean = true;
  
  submit(): void {
    this.isSubmitting = true;
    // API呼び出し処理
  }
}
```

## File: 274.txt

# #274 「Nest.jsのDTOとboolean」 

 

```typescript
// Nest.jsのDTOとboolean

import { IsBoolean, IsString } from 'class-validator';

export class CreateUserDto {
  @IsString()
  name: string;
  
  @IsBoolean()
  isActive: boolean;
  
  @IsBoolean()
  isAdmin: boolean;
}

@Controller('users')
export class UsersController {
  @Post()
  create(@Body() dto: CreateUserDto) {
    return { success: dto.isActive };
  }
}
```

## File: 275.txt

# #275 「@IsBoolean()デコレータ」 

 

```typescript
// @IsBoolean()デコレータ

import { IsBoolean, IsOptional } from 'class-validator';

export class UpdateSettingsDto {
  @IsBoolean()
  emailNotification: boolean;
  
  @IsBoolean()
  @IsOptional()
  pushNotification?: boolean;
}

// バリデーション成功例
const valid = { emailNotification: true };

// バリデーション失敗例
const invalid = { emailNotification: 'true' }; // エラー
```

## File: 276.txt

# #276 「間違い(1) - ==使用」 

 

```typescript
// ❌ 間違い: ==の使用

if (userInput == 0) {  // '0'や空文字列もtrue
  // 予期しない動作
}

if (value == null) {  // nullとundefinedを区別しない
  // 曖昧な処理
}

// ✅ 正しい: ===の使用

if (userInput === 0) {  // 数値の0のみtrue
  // 意図通りの動作
}

if (value === null) {  // nullのみ
  // 明確な処理
}
```

## File: 277.txt

# #277 「間違い(2) - truthyとの混同」 

 

```typescript
// ❌ 間違い: truthyとの混同

function process(count: number | null) {
  if (count) {  // 0もfalsyなので問題
    console.log(count);
  }
}

// ✅ 正しい: 明示的なチェック

function processCorrect(count: number | null) {
  if (count !== null && count !== undefined) {
    console.log(count);  // 0も正しく処理される
  }
}

// または
if (count != null) {
  console.log(count);
}
```

## File: 278.txt

# #278 「間違い(3) - 文字列"true"」 

 

```typescript
// ❌ 間違い: 文字列"true"の扱い

const value = "true";  // APIから取得
if (value === true) {  // false
  console.log('実行されない');
}

// ❌ truthyとして扱う（意図しない挙動）
if (value) {  // true（文字列はtruthy）
  console.log('実行される');
}

// ✅ 正しい: 明示的な変換
const boolValue = value === "true";
if (boolValue === true) {  // 正しく動作
  console.log('実行される');
}
```

## File: 279.txt

# #279 「ベストプラクティス」 

 

```typescript
// ベストプラクティス

// ✅ 厳密等価演算子の使用
if (value === null) { }

// ✅ 型ガードの活用
function isString(val: unknown): val is string {
  return typeof val === 'string';
}

// ✅ 明示的な型注釈
const isActive: boolean = true;

// ✅ strictNullChecksの有効化
// tsconfig.json
// "strictNullChecks": true

// ✅ ESLint設定
// "eqeqeq": ["error", "always"]
```

## File: 280.txt

# #280 「マスターチェック」 

 

```typescript
// マスターチェック

// ✅ 厳密等価演算子
if (value === null) { }

// ✅ 型ガード
function isUser(obj: unknown): obj is User {
  return typeof obj === 'object' && obj !== null && 'name' in obj;
}

// ✅ falsy値の理解
// false, 0, '', null, undefined, NaN

// ✅ Angular/Nest.jsでの実践
@IsBoolean() isActive: boolean;

// ✅ ベストプラクティス
// strictNullChecks + ESLint
```

