## File: 181.txt

# #181 「toFixed()メソッド」台本

## 📺 画面表示用コード

```typescript
// toFixed()メソッド
let num: number = 3.14159;

let fixed1: string = num.toFixed(2); // "3.14"
let fixed2: string = num.toFixed(4); // "3.1416"
let fixed3: string = num.toFixed(0); // "3"

// 実用的な例
let price: number = 1500.99;
let displayPrice: string = price.toFixed(2); // "1500.99"

let userAge: number = 25.5;
let displayAge: string = userAge.toFixed(0); // "26"
```

## File: 182.txt

# #182 「toPrecision()メソッド」台本

## 📺 画面表示用コード

```typescript
// toPrecision()メソッド
let num: number = 3.14159;

let precision1: string = num.toPrecision(3); // "3.14"
let precision2: string = num.toPrecision(5); // "3.1416"
let precision3: string = num.toPrecision(2); // "3.1"

// 実用的な例
let largeNumber: number = 123456.789;
let display1: string = largeNumber.toPrecision(4); // "1.235e+5"
let display2: string = largeNumber.toPrecision(8); // "123456.79"
```

## File: 183.txt

# #183 「イプシロン比較」台本

## 📺 画面表示用コード

```typescript
// イプシロン比較
function epsilonEqual(a: number, b: number, epsilon: number = 1e-10): boolean {
  return Math.abs(a - b) < epsilon;
}

// 実用的な例
let num1: number = 0.1 + 0.2;
let num2: number = 0.3;

console.log(num1 === num2); // false
console.log(epsilonEqual(num1, num2)); // true

// 実用的な例
let price1: number = 100.50;
let price2: number = 100.50;
console.log(epsilonEqual(price1, price2)); // true
```

## File: 184.txt

# #184 「Math.absを使った比較」台本

## 📺 画面表示用コード

```typescript
// Math.absを使った比較
function isEqual(a: number, b: number, tolerance: number = 1e-10): boolean {
  return Math.abs(a - b) < tolerance;
}

// 実用的な例
let num1: number = 0.1 + 0.2;
let num2: number = 0.3;

console.log(num1 === num2); // false
console.log(isEqual(num1, num2)); // true

// 実用的な例
let price1: number = 100.50;
let price2: number = 100.50;
console.log(isEqual(price1, price2)); // true
```

## File: 185.txt

# #185 「金銭計算の注意点」台本

## 📺 画面表示用コード

```typescript
// 金銭計算の注意点
function calculatePrice(price: number, tax: number): number {
  // 整数演算で精度を保つ
  const factor = 100;
  const priceInt = Math.round(price * factor);
  const taxInt = Math.round(tax * factor);
  const totalInt = priceInt + taxInt;
  
  return totalInt / factor;
}

// 実用的な例
let productPrice: number = 100.50;
let tax: number = 8.25;
let total: number = calculatePrice(productPrice, tax);

console.log(total); // 108.75
console.log(total.toFixed(2)); // "108.75"
```

## File: 186.txt

# #186 「BigIntの紹介」台本

## 📺 画面表示用コード

```typescript
// BigIntの紹介
let bigInt1: bigint = 123456789012345678901234567890n;
let bigInt2: bigint = BigInt("123456789012345678901234567890");

// 演算
let sum: bigint = bigInt1 + bigInt2;
let product: bigint = bigInt1 * bigInt2;

// 実用的な例
let largeId: bigint = 1234567890123456789n;
let userId: bigint = BigInt("9876543210987654321");

console.log(largeId.toString());
console.log(userId.toString());
```

## File: 187.txt

# #187 「BigIntとnumberの違い」台本

## 📺 画面表示用コード

```typescript
// BigIntとnumberの違い
let numberValue: number = 1234567890123456789;
let bigIntValue: bigint = 1234567890123456789n;

// 精度の違い
console.log(numberValue); // 1234567890123456800 (精度が失われる)
console.log(bigIntValue); // 1234567890123456789n (精度が保たれる)

// 型の違い
console.log(typeof numberValue); // "number"
console.log(typeof bigIntValue); // "bigint"

// 実用的な例
let userId: bigint = 1234567890123456789n;
let userAge: number = 25;
```

## File: 188.txt

# #188 「BigIntの使用例」台本

## 📺 画面表示用コード

```typescript
// BigIntの使用例
let userId: bigint = 1234567890123456789n;
let transactionId: bigint = BigInt("9876543210987654321");

// 演算
let newId: bigint = userId + 1n;
let multiplied: bigint = userId * 2n;

// 実用的な例
function generateId(): bigint {
  return BigInt(Date.now()) * 1000n + BigInt(Math.floor(Math.random() * 1000));
}

let newUserId: bigint = generateId();
console.log(newUserId.toString());
```

## File: 189.txt

# #189 「浮動小数点のベストプラクティス」台本

## 📺 画面表示用コード

```typescript
// 浮動小数点のベストプラクティス

// 1. 整数演算の使用
function addDecimals(a: number, b: number): number {
  const factor = 100;
  return (Math.round(a * factor) + Math.round(b * factor)) / factor;
}

// 2. 適切な比較
function isEqual(a: number, b: number): boolean {
  return Math.abs(a - b) < 1e-10;
}

// 3. 表示用のフォーマット
let price: number = 1500.99;
let displayPrice: string = price.toFixed(2);

// 実用的な例
let total: number = addDecimals(0.1, 0.2);
console.log(isEqual(total, 0.3)); // true
```

## File: 190.txt

# #190 「数値計算まとめ」台本

## 📺 画面表示用コード

```typescript
// 数値計算まとめ

// 1. 精度問題の理解
let num1: number = 0.1 + 0.2;
console.log(num1 === 0.3); // false

// 2. 回避方法
function addDecimals(a: number, b: number): number {
  const factor = 100;
  return (Math.round(a * factor) + Math.round(b * factor)) / factor;
}

// 3. 適切な比較
function isEqual(a: number, b: number): boolean {
  return Math.abs(a - b) < 1e-10;
}

// 4. BigIntの活用
let largeId: bigint = 1234567890123456789n;
```

## File: 191.txt

# #191 「Angularフォームでのnumber型」台本

## 📺 画面表示用コード

```typescript
// Angularフォームでのnumber型
import { FormControl, FormGroup } from '@angular/forms';

// FormControlでのnumber型
let ageControl = new FormControl<number>(25);
let priceControl = new FormControl<number>(1500);

// FormGroupでのnumber型
let userForm = new FormGroup({
  age: new FormControl<number>(25),
  price: new FormControl<number>(1500)
});

// 実用的な例
let productForm = new FormGroup({
  price: new FormControl<number>(0),
  quantity: new FormControl<number>(1)
});
```

## File: 192.txt

# #192 「数値バリデーション」台本

## 📺 画面表示用コード

```typescript
// 数値バリデーション
import { FormControl, Validators } from '@angular/forms';

// 基本的なバリデーション
let ageControl = new FormControl(25, [
  Validators.required,
  Validators.min(0),
  Validators.max(120)
]);

let priceControl = new FormControl(1500, [
  Validators.required,
  Validators.min(0)
]);

// 実用的な例
let productForm = new FormGroup({
  price: new FormControl(0, [
    Validators.required,
    Validators.min(1)
  ]),
  quantity: new FormControl(1, [
    Validators.required,
    Validators.min(1)
  ])
});
```

## File: 193.txt

# #193 「Nest.jsのDTOとnumber型」台本

## 📺 画面表示用コード

```typescript
// Nest.jsのDTOとnumber型
import { IsNumber, IsOptional, Min, Max } from 'class-validator';
import { Transform } from 'class-transformer';

export class CreateProductDto {
  @IsNumber()
  @Min(0)
  price: number;

  @IsNumber()
  @Min(1)
  quantity: number;

  @IsOptional()
  @IsNumber()
  @Min(0)
  @Max(100)
  discount?: number;
}

// 実用的な例
export class UpdateUserDto {
  @IsNumber()
  @Min(0)
  @Max(120)
  age: number;
}
```

## File: 194.txt

# #194 「@IsNumber()デコレータ」台本

## 📺 画面表示用コード

```typescript
// @IsNumber()デコレータ
import { IsNumber, IsOptional } from 'class-validator';

export class ProductDto {
  @IsNumber()
  id: number;

  @IsNumber()
  price: number;

  @IsOptional()
  @IsNumber()
  discount?: number;
}

// 実用的な例
export class UserDto {
  @IsNumber()
  age: number;

  @IsNumber()
  salary: number;

  @IsOptional()
  @IsNumber()
  bonus?: number;
}
```

## File: 195.txt

# #195 「数値範囲のバリデーション」台本

## 📺 画面表示用コード

```typescript
// 数値範囲のバリデーション
import { IsNumber, Min, Max, Range } from 'class-validator';

export class ProductDto {
  @IsNumber()
  @Min(0)
  @Max(1000000)
  price: number;

  @IsNumber()
  @Min(1)
  @Max(1000)
  quantity: number;

  @IsNumber()
  @Range(0, 100)
  discount: number;
}

// 実用的な例
export class UserDto {
  @IsNumber()
  @Min(0)
  @Max(120)
  age: number;

  @IsNumber()
  @Min(0)
  salary: number;
}
```

## File: 196.txt

# #196 「間違い(1) - 浮動小数点比較」台本

## 📺 画面表示用コード

```typescript
// 間違い(1) - 浮動小数点比較
let num1: number = 0.1 + 0.2;
let num2: number = 0.3;

// ❌ 間違い
console.log(num1 === num2); // false

// ✅ 正しい方法
function isEqual(a: number, b: number): boolean {
  return Math.abs(a - b) < 1e-10;
}

console.log(isEqual(num1, num2)); // true

// 実用的な例
let price1: number = 100.50;
let price2: number = 100.50;
console.log(isEqual(price1, price2)); // true
```

## File: 197.txt

# #197 「間違い(2) - NaNチェック」台本

## 📺 画面表示用コード

```typescript
// 間違い(2) - NaNチェック
let invalidNumber: number = Number("abc");

// ❌ 間違い
console.log(invalidNumber === NaN); // false

// ✅ 正しい方法
console.log(Number.isNaN(invalidNumber)); // true

// 実用的な例
function validateNumber(value: unknown): boolean {
  if (typeof value === "number") {
    return !Number.isNaN(value);
  }
  return false;
}

let userInput: unknown = "abc";
let converted: number = Number(userInput);
console.log(validateNumber(converted)); // false
```

## File: 198.txt

# #198 「間違い(3) - 文字列との混同」台本

## 📺 画面表示用コード

```typescript
// 間違い(3) - 文字列との混同
let userInput: string = "25";
let userAge: number = 25;

// ❌ 間違い
// let total: number = userInput + userAge; // "2525"

// ✅ 正しい方法
let total: number = Number(userInput) + userAge; // 50

// 実用的な例
let priceStr: string = "1500";
let price: number = 1500;

// 型安全な処理
let totalPrice: number = Number(priceStr) + price;
console.log(totalPrice); // 3000
```

## File: 199.txt

# #199 「ベストプラクティス」台本

## 📺 画面表示用コード

```typescript
// 数値のベストプラクティス

// 1. 型安全性
let userAge: number = 25;
// userAge = "25"; // エラー

// 2. 精度問題の回避
function addDecimals(a: number, b: number): number {
  const factor = 100;
  return (Math.round(a * factor) + Math.round(b * factor)) / factor;
}

// 3. 適切なバリデーション
function validateNumber(value: unknown): value is number {
  return typeof value === "number" && Number.isFinite(value);
}

// 4. 適切な比較
function isEqual(a: number, b: number): boolean {
  return Math.abs(a - b) < 1e-10;
}
```

## File: 200.txt

# #200 「マスターチェック」台本

## 📺 画面表示用コード

```typescript
// 数値のマスターチェック

// 1. 型の違い
let num: number = 30; // プリミティブ型
// let numObj: Number = new Number(30); // オブジェクト型（非推奨）

// 2. 精度問題
let sum: number = 0.1 + 0.2;
console.log(sum === 0.3); // false

// 3. 適切な比較
function isEqual(a: number, b: number): boolean {
  return Math.abs(a - b) < 1e-10;
}

// 4. バリデーション
function validateNumber(value: unknown): value is number {
  return typeof value === "number" && Number.isFinite(value);
}

// 5. 実用的な例
let userAge: number = 25;
let productPrice: number = 1500;
let total: number = userAge + productPrice;
```

## File: 201.txt

# #201 「boolean型とは」台本

## 📺 画面表示用コード

```typescript
// boolean型とは
let isActive: boolean = true;
let isCompleted: boolean = false;
let hasPermission: boolean = true;

// 実用的な例
let userLoggedIn: boolean = true;
let formValid: boolean = false;
let dataLoaded: boolean = true;

// 条件分岐での使用
if (isActive) {
  console.log("アクティブです");
}
```

## File: 202.txt

# #202 「boolean型の宣言」台本

## 📺 画面表示用コード

```typescript
// boolean型の宣言
let isActive: boolean;
let isCompleted: boolean;
let hasPermission: boolean;

// 後で値を代入
isActive = true;
isCompleted = false;
hasPermission = true;

// 実用的な例
let userLoggedIn: boolean = true;
let formValid: boolean = false;
let dataLoaded: boolean = true;
```

## File: 203.txt

# #203 「trueの代入」台本

## 📺 画面表示用コード

```typescript
// trueの代入
let isActive: boolean = true;
let isCompleted: boolean = true;
let hasPermission: boolean = true;

// 実用的な例
let userLoggedIn: boolean = true;
let formValid: boolean = true;
let dataLoaded: boolean = true;

// 条件分岐での使用
if (isActive) {
  console.log("アクティブです");
}
```

## File: 204.txt

# #204 「falseの代入」台本

## 📺 画面表示用コード

```typescript
// falseの代入
let isActive: boolean = false;
let isCompleted: boolean = false;
let hasPermission: boolean = false;

// 実用的な例
let userLoggedIn: boolean = false;
let formValid: boolean = false;
let dataLoaded: boolean = false;

// 条件分岐での使用
if (!isActive) {
  console.log("非アクティブです");
}
```

## File: 205.txt

# #205 「型推論でboolean型」台本

## 📺 画面表示用コード

```typescript
// 型推論でboolean型
let isActive = true;        // boolean型と推論
let isCompleted = false;    // boolean型と推論
let hasPermission = true;   // boolean型と推論

// 実用的な例
let userLoggedIn = true;    // boolean型と推論
let formValid = false;      // boolean型と推論
let dataLoaded = true;      // boolean型と推論

// 型注釈なしでも型安全
// isActive = "true"; // エラー: Type 'string' is not assignable to type 'boolean'
```

## File: 206.txt

# #206 「constでboolean型」台本

## 📺 画面表示用コード

```typescript
// constでboolean型
const isActive = true;        // boolean型と推論、変更不可
const isCompleted = false;    // boolean型と推論、変更不可
const hasPermission = true;   // boolean型と推論、変更不可

// 実用的な例
const userLoggedIn = true;    // boolean型と推論、変更不可
const formValid = false;      // boolean型と推論、変更不可
const dataLoaded = true;      // boolean型と推論、変更不可

// 変更不可
// isActive = false; // エラー: Cannot assign to 'isActive' because it is a constant
```

## File: 207.txt

# #207 「if文での使用」台本

## 📺 画面表示用コード

```typescript
// if文での使用
let isActive: boolean = true;
let isCompleted: boolean = false;

// 基本的な使用
if (isActive) {
  console.log("アクティブです");
}

if (!isCompleted) {
  console.log("未完了です");
}

// 実用的な例
let userLoggedIn: boolean = true;
if (userLoggedIn) {
  console.log("ユーザーがログインしています");
}
```

## File: 208.txt

# #208 「while文での使用」台本

## 📺 画面表示用コード

```typescript
// while文での使用
let isActive: boolean = true;
let isCompleted: boolean = false;

// 基本的な使用
while (isActive) {
  console.log("アクティブです");
  isActive = false; // ループを終了
}

// 実用的な例
let dataLoading: boolean = true;
while (dataLoading) {
  console.log("データを読み込み中...");
  dataLoading = false; // ループを終了
}
```

## File: 209.txt

# #209 「三項演算子」台本

## 📺 画面表示用コード

```typescript
// 三項演算子での使用
let isActive: boolean = true;
let isCompleted: boolean = false;

// 基本的な使用
let status: string = isActive ? "アクティブ" : "非アクティブ";
let message: string = isCompleted ? "完了" : "未完了";

// 実用的な例
let userLoggedIn: boolean = true;
let displayText: string = userLoggedIn ? "ログイン中" : "ログアウト中";

console.log(status);    // "アクティブ"
console.log(message);   // "未完了"
console.log(displayText); // "ログイン中"
```

## File: 210.txt

# #210 「boolean配列」台本

## 📺 画面表示用コード

```typescript
// boolean配列
let flags: boolean[] = [true, false, true];
let states: boolean[] = [false, true, false];

// 配列の操作
flags.push(true);
flags[0] = false;

// 実用的な例
let userPermissions: boolean[] = [true, false, true, true];
let formValidations: boolean[] = [true, true, false];

// 配列の要素にアクセス
console.log(userPermissions[0]); // true
console.log(formValidations[2]); // false
```

## File: 211.txt

# #211 「booleanリテラル型」台本

## 📺 画面表示用コード

```typescript
// booleanリテラル型
let isActive: true = true;        // trueのみ許可
let isCompleted: false = false;   // falseのみ許可

// 実用的な例
let userLoggedIn: true = true;    // trueのみ許可
let formValid: false = false;     // falseのみ許可

// 型の制限
// isActive = false; // エラー: Type 'false' is not assignable to type 'true'
// isCompleted = true; // エラー: Type 'true' is not assignable to type 'false'
```

## File: 212.txt

# #212 「デフォルト値」台本

## 📺 画面表示用コード

```typescript
// boolean型のデフォルト値
let isActive: boolean = true;        // デフォルト値: true
let isCompleted: boolean = false;    // デフォルト値: false
let hasPermission: boolean = true;   // デフォルト値: true

// 実用的な例
let userLoggedIn: boolean = false;   // デフォルト値: false
let formValid: boolean = false;      // デフォルト値: false
let dataLoaded: boolean = false;     // デフォルト値: false

// デフォルト値の活用
if (isActive) {
  console.log("アクティブです");
}
```

## File: 213.txt

# #213 「初期化のベストプラクティス」台本

## 📺 画面表示用コード

```typescript
// 初期化のベストプラクティス

// 1. デフォルト値の設定
let isActive: boolean = false;  // 明示的なデフォルト値

// 2. 型推論の活用
let isCompleted = false;        // 型推論でboolean型

// 3. constの使用
const hasPermission = true;     // 変更不可の定数

// 実用的な例
let userLoggedIn = false;       // 型推論でboolean型
const isProduction = true;      // 変更不可の定数
```

## File: 214.txt

# #214 「boolean型の用途」台本

## 📺 画面表示用コード

```typescript
// boolean型の用途

// 1. 条件分岐
let isActive: boolean = true;
if (isActive) {
  console.log("アクティブです");
}

// 2. フラグ管理
let hasPermission: boolean = true;
let canEdit: boolean = false;

// 3. 状態管理
let userLoggedIn: boolean = true;
let formValid: boolean = false;

// 4. バリデーション
let isEmailValid: boolean = true;
let isPasswordValid: boolean = false;
```

## File: 215.txt

# #215 「基本まとめ」台本

## 📺 画面表示用コード

```typescript
// boolean型基本まとめ

// 1. 型宣言
let isActive: boolean = true;
let isCompleted: boolean = false;

// 2. 型推論
let userLoggedIn = true;    // boolean型と推論
let formValid = false;      // boolean型と推論

// 3. 条件分岐
if (isActive) {
  console.log("アクティブです");
}

// 4. 配列
let flags: boolean[] = [true, false, true];

// 5. 実用的な例
let userPermissions: boolean[] = [true, false, true];
```

## File: 216.txt

# #216 「trueリテラル型」台本

## 📺 画面表示用コード

```typescript
// trueリテラル型
let isActive: true = true;        // trueのみ許可
let isEnabled: true = true;       // trueのみ許可
let hasPermission: true = true;   // trueのみ許可

// 実用的な例
let userLoggedIn: true = true;    // trueのみ許可
let formValid: true = true;       // trueのみ許可
let dataLoaded: true = true;      // trueのみ許可

// 型の制限
// isActive = false; // エラー: Type 'false' is not assignable to type 'true'
```

## File: 217.txt

# #217 「trueリテラル型の宣言」台本

## 📺 画面表示用コード

```typescript
// trueリテラル型の宣言
let isActive: true;        // trueのみ許可
let isEnabled: true;       // trueのみ許可
let hasPermission: true;   // trueのみ許可

// 後で値を代入
isActive = true;           // OK
isEnabled = true;          // OK
hasPermission = true;      // OK

// 実用的な例
let userLoggedIn: true = true;    // 宣言時に初期化
let formValid: true = true;       // 宣言時に初期化
```

## File: 218.txt

# #218 「trueリテラル型の使用例」台本

## 📺 画面表示用コード

```typescript
// trueリテラル型の使用例

// 1. 定数フラグ
const isProduction: true = true;
const isDebugMode: true = true;

// 2. 設定値
const enableLogging: true = true;
const enableCaching: true = true;

// 3. 実用的な例
const userLoggedIn: true = true;
const formValid: true = true;

// 条件分岐での使用
if (isProduction) {
  console.log("本番環境です");
}
```

## File: 219.txt

# #219 「falseリテラル型」台本

## 📺 画面表示用コード

```typescript
// falseリテラル型
let isInactive: false = false;    // falseのみ許可
let isDisabled: false = false;    // falseのみ許可
let hasNoPermission: false = false; // falseのみ許可

// 実用的な例
let userLoggedOut: false = false; // falseのみ許可
let formInvalid: false = false;   // falseのみ許可
let dataNotLoaded: false = false; // falseのみ許可

// 型の制限
// isInactive = true; // エラー: Type 'true' is not assignable to type 'false'
```

## File: 220.txt

# #220 「falseリテラル型の宣言」台本

## 📺 画面表示用コード

```typescript
// falseリテラル型の宣言
let isInactive: false;        // falseのみ許可
let isDisabled: false;        // falseのみ許可
let hasNoPermission: false;   // falseのみ許可

// 後で値を代入
isInactive = false;           // OK
isDisabled = false;           // OK
hasNoPermission = false;      // OK

// 実用的な例
let userLoggedOut: false = false; // 宣言時に初期化
let formInvalid: false = false;   // 宣言時に初期化
```

## File: 221.txt

# #221 「falseリテラル型の使用例」台本

## 📺 画面表示用コード

```typescript
// falseリテラル型の使用例

// 1. 無効状態フラグ
const isInactive: false = false;
const isDisabled: false = false;

// 2. 無効設定値
const disableLogging: false = false;
const disableCaching: false = false;

// 3. 実用的な例
const userLoggedOut: false = false;
const formInvalid: false = false;

// 条件分岐での使用
if (!isInactive) {
  console.log("アクティブです");
}
```

## File: 222.txt

# #222 「リテラル型とboolean型の違い」台本

## 📺 画面表示用コード

```typescript
// リテラル型とboolean型の違い

// boolean型 - trueとfalse両方許可
let flag1: boolean = true;   // OK
let flag2: boolean = false;  // OK

// trueリテラル型 - trueのみ許可
let flag3: true = true;      // OK
// let flag4: true = false;  // エラー

// falseリテラル型 - falseのみ許可
let flag5: false = false;    // OK
// let flag6: false = true;  // エラー

// 実用的な例
let userLoggedIn: boolean = true;    // 変更可能
const isProduction: true = true;     // 変更不可、trueのみ
```

## File: 223.txt

# #223 「型推論 - const使用時」台本

## 📺 画面表示用コード

```typescript
// 型推論 - const使用時

// constでの型推論
const isActive = true;        // trueリテラル型と推論
const isDisabled = false;     // falseリテラル型と推論
const hasPermission = true;   // trueリテラル型と推論

// 実用的な例
const userLoggedIn = true;    // trueリテラル型と推論
const formValid = false;      // falseリテラル型と推論
const dataLoaded = true;      // trueリテラル型と推論

// 型の確認
// isActive = false; // エラー: Cannot assign to 'isActive' because it is a constant
```

## File: 224.txt

# #224 「ユースケース」台本

## 📺 画面表示用コード

```typescript
// リテラル型のユースケース

// 1. 定数フラグ
const isProduction: true = true;
const isDebugMode: false = false;

// 2. 設定値
const enableLogging: true = true;
const disableCaching: false = false;

// 3. 状態管理
const userLoggedIn: true = true;
const formValid: false = false;

// 4. 実用的な例
const config = {
  isProduction: true as const,
  enableLogging: false as const
};
```

## File: 225.txt

# #225 「リテラル型まとめ」台本

## 📺 画面表示用コード

```typescript
// リテラル型まとめ

// 1. trueリテラル型
let isActive: true = true;        // trueのみ許可

// 2. falseリテラル型
let isDisabled: false = false;    // falseのみ許可

// 3. 型推論
const userLoggedIn = true;        // trueリテラル型と推論
const formValid = false;          // falseリテラル型と推論

// 4. 実用的な例
const config = {
  isProduction: true as const,
  enableLogging: false as const
};
```

## File: 226.txt

# #226 「論理積AND - &&」台本

## 📺 画面表示用コード

```typescript
// 論理積AND - &&
let isActive: boolean = true;
let hasPermission: boolean = true;
let isCompleted: boolean = false;

// 基本的な使用
let canProceed: boolean = isActive && hasPermission; // true
let canAccess: boolean = isActive && isCompleted;    // false

// 実用的な例
let userLoggedIn: boolean = true;
let formValid: boolean = false;
let canSubmit: boolean = userLoggedIn && formValid; // false

// 条件分岐での使用
if (isActive && hasPermission) {
  console.log("アクセス可能です");
}
```

## File: 227.txt

# #227 「ANDの型推論」台本

## 📺 画面表示用コード

```typescript
// ANDの型推論
let isActive: boolean = true;
let hasPermission: boolean = false;
let userName: string = "John";

// 型推論の例
let result1 = isActive && hasPermission; // boolean型
let result2 = isActive && userName;      // string型
let result3 = hasPermission && userName; // boolean型

// 実用的な例
let userLoggedIn: boolean = true;
let userData: string = "user123";
let displayData = userLoggedIn && userData; // string型
```

## File: 228.txt

# #228 「ANDの短絡評価」台本

## 📺 画面表示用コード

```typescript
// ANDの短絡評価
let isActive: boolean = false;
let hasPermission: boolean = true;

// 短絡評価の例
let result1 = isActive && hasPermission; // false（右側は評価されない）
let result2 = isActive && console.log("実行されない"); // false

// 実用的な例
let userLoggedIn: boolean = false;
let userData: string = "user123";

// 短絡評価を活用
let displayData = userLoggedIn && userData; // false（userDataは評価されない）
```

## File: 229.txt

# #229 「ANDと型の関係」台本

## 📺 画面表示用コード

```typescript
// ANDと型の関係
let isActive: boolean = true;
let hasPermission: boolean = false;
let userName: string = "John";
let userAge: number = 25;

// 型の関係
let result1: boolean = isActive && hasPermission; // boolean && boolean = boolean
let result2: string = isActive && userName;       // boolean && string = string
let result3: number = isActive && userAge;        // boolean && number = number

// 実用的な例
let userLoggedIn: boolean = true;
let userData: string = "user123";
let displayData: string = userLoggedIn && userData; // string型
```

## File: 230.txt

# #230 「論理和OR - ||」台本

## 📺 画面表示用コード

```typescript
// 論理和OR - ||
let isActive: boolean = true;
let hasPermission: boolean = false;
let isCompleted: boolean = false;

// 基本的な使用
let canProceed: boolean = isActive || hasPermission; // true
let canAccess: boolean = isCompleted || hasPermission; // false

// 実用的な例
let userLoggedIn: boolean = true;
let formValid: boolean = false;
let canAccess: boolean = userLoggedIn || formValid; // true

// 条件分岐での使用
if (isActive || hasPermission) {
  console.log("アクセス可能です");
}
```

## File: 231.txt

# #231 「ORの型推論」台本

## 📺 画面表示用コード

```typescript
// ORの型推論
let isActive: boolean = true;
let hasPermission: boolean = false;
let userName: string = "John";
let defaultName: string = "Guest";

// 型推論の例
let result1 = isActive || hasPermission; // boolean型
let result2 = userName || defaultName;   // string型
let result3 = hasPermission || userName; // string型

// 実用的な例
let userLoggedIn: boolean = true;
let userData: string = "user123";
let displayData = userLoggedIn || userData; // boolean型
```

## File: 232.txt

# #232 「ORの短絡評価」台本

## 📺 画面表示用コード

```typescript
// ORの短絡評価
let isActive: boolean = true;
let hasPermission: boolean = false;

// 短絡評価の例
let result1 = isActive || hasPermission; // true（右側は評価されない）
let result2 = isActive || console.log("実行されない"); // true

// 実用的な例
let userLoggedIn: boolean = true;
let defaultUser: string = "Guest";

// 短絡評価を活用
let displayUser = userLoggedIn || defaultUser; // true（defaultUserは評価されない）
```

## File: 233.txt

# #233 「ORとデフォルト値」台本

## 📺 画面表示用コード

```typescript
// ORとデフォルト値
let userName: string | null = null;
let userAge: number | undefined = undefined;
let isActive: boolean | null = null;

// デフォルト値の設定
let displayName: string = userName || "Guest";
let displayAge: number = userAge || 0;
let displayStatus: boolean = isActive || false;

// 実用的な例
let userInput: string = "";
let defaultText: string = "デフォルトテキスト";
let result: string = userInput || defaultText; // "デフォルトテキスト"
```

## File: 234.txt

# #234 「論理否定NOT - !」台本

## 📺 画面表示用コード

```typescript
// 論理否定NOT - !
let isActive: boolean = true;
let hasPermission: boolean = false;
let isCompleted: boolean = true;

// 基本的な使用
let isInactive: boolean = !isActive;        // false
let hasNoPermission: boolean = !hasPermission; // true
let isNotCompleted: boolean = !isCompleted; // false

// 実用的な例
let userLoggedIn: boolean = true;
let formValid: boolean = false;
let userLoggedOut: boolean = !userLoggedIn; // false
let formInvalid: boolean = !formValid;      // true
```

## File: 235.txt

# #235 「NOTの型推論」台本

## 📺 画面表示用コード

```typescript
// NOTの型推論
let isActive: boolean = true;
let hasPermission: boolean = false;
let userName: string = "John";
let userAge: number = 25;

// 型推論の例
let result1: boolean = !isActive;        // boolean型
let result2: boolean = !hasPermission;   // boolean型
let result3: boolean = !userName;        // boolean型
let result4: boolean = !userAge;         // boolean型

// 実用的な例
let userLoggedIn: boolean = true;
let formValid: boolean = false;
let userLoggedOut: boolean = !userLoggedIn; // boolean型
```

## File: 236.txt

# #236 「二重否定 - !!」台本

## 📺 画面表示用コード

```typescript
// 二重否定 - !!
let userName: string = "John";
let userAge: number = 25;
let userData: object = {};
let nullValue: null = null;

// 二重否定の使用
let hasName: boolean = !!userName;        // true
let hasAge: boolean = !!userAge;          // true
let hasData: boolean = !!userData;        // true
let hasValue: boolean = !!nullValue;      // false

// 実用的な例
let userInput: string = "test";
let hasInput: boolean = !!userInput;      // true
```

## File: 237.txt

# #237 「二重否定での型変換」台本

## 📺 画面表示用コード

```typescript
// 二重否定での型変換
let str: string = "hello";
let num: number = 42;
let obj: object = {};
let arr: any[] = [];
let nullVal: null = null;
let undefinedVal: undefined = undefined;

// 型変換の例
let bool1: boolean = !!str;           // true
let bool2: boolean = !!num;           // true
let bool3: boolean = !!obj;           // true
let bool4: boolean = !!arr;           // true
let bool5: boolean = !!nullVal;       // false
let bool6: boolean = !!undefinedVal;  // false

// 実用的な例
let userInput: string = "test";
let hasInput: boolean = !!userInput;  // true
```

## File: 238.txt

# #238 「論理演算子の優先順位」台本

## 📺 画面表示用コード

```typescript
// 論理演算子の優先順位
let isActive: boolean = true;
let hasPermission: boolean = false;
let isCompleted: boolean = true;

// 優先順位の例
let result1 = !isActive && hasPermission;    // (!isActive) && hasPermission
let result2 = isActive || hasPermission && isCompleted; // isActive || (hasPermission && isCompleted)

// 実用的な例
let userLoggedIn: boolean = true;
let formValid: boolean = false;
let hasData: boolean = true;

// 優先順位を考慮した条件
let canSubmit = userLoggedIn && formValid || hasData; // (userLoggedIn && formValid) || hasData
```

## File: 239.txt

# #239 「論理演算子の組み合わせ」台本

## 📺 画面表示用コード

```typescript
// 論理演算子の組み合わせ
let isActive: boolean = true;
let hasPermission: boolean = false;
let isCompleted: boolean = true;
let hasData: boolean = false;

// 組み合わせの例
let result1 = (isActive && hasPermission) || isCompleted; // 括弧で優先順位を制御
let result2 = !(isActive && hasPermission) && hasData;    // 否定と組み合わせ
let result3 = isActive && (hasPermission || isCompleted); // ORとANDの組み合わせ

// 実用的な例
let userLoggedIn: boolean = true;
let formValid: boolean = false;
let hasPermission: boolean = true;
let canSubmit = userLoggedIn && (formValid || hasPermission); // 複雑な条件
```

## File: 240.txt

# #240 「論理演算まとめ」台本

## 📺 画面表示用コード

```typescript
// 論理演算まとめ

// 1. AND演算子（&&）
let isActive: boolean = true;
let hasPermission: boolean = false;
let canProceed: boolean = isActive && hasPermission; // false

// 2. OR演算子（||）
let canAccess: boolean = isActive || hasPermission; // true

// 3. NOT演算子（!）
let isInactive: boolean = !isActive; // false

// 4. 二重否定（!!）
let userName: string = "John";
let hasName: boolean = !!userName; // true

// 5. 実用的な例
let userLoggedIn: boolean = true;
let formValid: boolean = false;
let canSubmit: boolean = userLoggedIn && formValid; // false
```

## File: 241.txt

# #241 「等価演算子 - ==と===」台本

## 📺 画面表示用コード

```typescript
// 緩い比較（==）
1 == "1"     // true（型変換が発生）
0 == false   // true
null == undefined  // true

// 厳密比較（===）
1 === "1"    // false（型が異なる）
0 === false  // false
null === undefined  // false

// TypeScriptでは===を推奨
const value: number = 42;
if (value === 42) {  // 型安全
  console.log("正しい比較");
}
```

## File: 242.txt

# #242 「==の型強制」台本

## 📺 画面表示用コード

```typescript
// ==の型強制の例

// 文字列→数値変換
console.log('5' == 5);     // true (文字列が数値に変換)
console.log('100' == 100); // true

// boolean→数値変換
console.log(true == 1);    // true (trueは1に変換)
console.log(false == 0);   // true (falseは0に変換)

// null/undefined
console.log(null == undefined); // true

// 予期しない結果
console.log(' ' == 0);     // true (空白が0に変換)
console.log('0' == false); // true
```

## File: 243.txt

# #243 「===の厳密比較」台本

## 📺 画面表示用コード

```typescript
// ===の厳密比較

// 型が異なる場合はfalse
console.log(5 === '5');    // false
console.log(true === 1);   // false
console.log(null === undefined); // false

// 型と値が一致する場合のみtrue
console.log(5 === 5);      // true
console.log('hello' === 'hello'); // true
console.log(true === true); // true

// 型安全な関数
function isEqual<T>(a: T, b: T): boolean {
  return a === b;
}
```

## File: 244.txt

# #244 「===を使うべき理由」台本

## 📺 画面表示用コード

```typescript
// ===を使うべき理由

// ❌ 悪い例: ==による予期しない挙動
if (userInput == 0) { // '0'や空文字列もtrue
  // 意図しない動作
}

// ✅ 良い例: ===で明確な比較
if (userInput === 0) { // 数値の0のみtrue
  // 意図通りの動作
}

// ESLint設定
// "eqeqeq": ["error", "always"]

// 型安全な比較関数
function compareValues<T>(a: T, b: T): boolean {
  return a === b;
}
```

## File: 245.txt

# #245 「不等価演算子 - !=と!==」台本

## 📺 画面表示用コード

```typescript
// 不等価演算子の違い

// != (型変換あり)
console.log(5 != '5');    // false (型変換後に比較)
console.log(0 != false);  // false
console.log(null != undefined); // false

// !== (型変換なし、厳密比較)
console.log(5 !== '5');   // true (型が異なる)
console.log(0 !== false); // true
console.log(null !== undefined); // true

// 推奨: !==を使用
function isNotEqual(a: number, b: number): boolean {
  return a !== b;
}
```

## File: 246.txt

# #246 「大なり演算子 - >」台本

## 📺 画面表示用コード

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

# #247 「大なり演算子の型」台本

## 📺 画面表示用コード

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

# #248 「小なり演算子 - <」台本

## 📺 画面表示用コード

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

# #249 「以上演算子 - >=」台本

## 📺 画面表示用コード

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

# #250 「以下演算子 - <=」台本

## 📺 画面表示用コード

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

# #251 「文字列の比較」台本

## 📺 画面表示用コード

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

# #252 「数値の比較」台本

## 📺 画面表示用コード

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

# #253 「booleanの比較」台本

## 📺 画面表示用コード

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

# #254 「null/undefinedの比較」台本

## 📺 画面表示用コード

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

# #255 「比較演算まとめ」台本

## 📺 画面表示用コード

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

# #256 「型ガードとは」台本

## 📺 画面表示用コード

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

# #257 「typeof型ガード」台本

## 📺 画面表示用コード

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

# #258 「typeof型ガードの戻り値」台本

## 📺 画面表示用コード

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

# #259 「instanceof型ガード」台本

## 📺 画面表示用コード

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

# #260 「in型ガード」台本

## 📺 画面表示用コード

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

# #261 「Array.isArray()」台本

## 📺 画面表示用コード

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

# #262 「null/undefinedチェック」台本

## 📺 画面表示用コード

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

# #263 「truthyチェック」台本

## 📺 画面表示用コード

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

# #264 「falsyチェック」台本

## 📺 画面表示用コード

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

# #265 「falsyな値一覧」台本

## 📺 画面表示用コード

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

# #266 「truthyな値」台本

## 📺 画面表示用コード

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

# #267 「明示的なboolean変換」台本

## 📺 画面表示用コード

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

# #268 「型述語関数 - x is Type」台本

## 📺 画面表示用コード

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

# #269 「型ガードのベストプラクティス」台本

## 📺 画面表示用コード

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

# #270 「型ガードまとめ」台本

## 📺 画面表示用コード

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

# #271 「Angularテンプレートでのboolean」台本

## 📺 画面表示用コード

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

# #272 「*ngIfディレクティブ」台本

## 📺 画面表示用コード

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

# #273 「[disabled]属性」台本

## 📺 画面表示用コード

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

# #274 「Nest.jsのDTOとboolean」台本

## 📺 画面表示用コード

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

# #275 「@IsBoolean()デコレータ」台本

## 📺 画面表示用コード

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

# #276 「間違い(1) - ==使用」台本

## 📺 画面表示用コード

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

# #277 「間違い(2) - truthyとの混同」台本

## 📺 画面表示用コード

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

# #278 「間違い(3) - 文字列"true"」台本

## 📺 画面表示用コード

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

# #279 「ベストプラクティス」台本

## 📺 画面表示用コード

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

# #280 「マスターチェック」台本

## 📺 画面表示用コード

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

