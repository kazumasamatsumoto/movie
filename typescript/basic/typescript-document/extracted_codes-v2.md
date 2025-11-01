## File: 281.txt

# #281「null型とは」

 

```typescript
// null型の基本
let value: null = null;
let name: string | null = null;
```

```typescript
// strictNullChecks有効時
let id: number = null; // エラー
let id: number | null = null; // OK
```

```typescript
// 関数の戻り値とオプショナル
function findUser(id: number): User | null {
  return users.find(u => u.id === id) ?? null;
}
interface User {
  email: string | null; // 明示的null許容
}
```

## File: 282.txt

# #282「nullの宣言」

 

```typescript
// null型の宣言
let value: null = null;
let name: string | null = null;
let age: number | null = 25;
```

```typescript
// 複数の型とnull
let data: string | number | null = null;
let items: string[] | null = null;
```

```typescript
// tsconfig.json
{
  "compilerOptions": {
    "strictNullChecks": true  // null安全性
  }
}
```

## File: 283.txt

# #283「nullの代入」

 

```typescript
// nullの代入
let name: string | null = null;
name = "Alice";  // OK
name = null;     // OK
```

```typescript
// strictNullChecks有効時
let id: number = null;  // エラー
let id: number | null = null;  // OK
```

```typescript
// 関数パラメータとオブジェクト
function setUser(user: User | null): void {
  currentUser = user;
}
interface Config {
  cache: CacheService | null;
}
```

## File: 284.txt

# #284「nullの使用例」

 

```typescript
// データ検索とキャッシュ管理
function findUser(id: number): User | null {
  return users.find(u => u.id === id) ?? null;
}
class CacheService {
  private cache: Map<string, any> | null = null;
}
```

```typescript
// APIレスポンス
interface ApiResponse<T> {
  data: T | null;
  error: string | null;
}
```

```typescript
// Angular DI
@Injectable()
class UserService {
  private currentUser: User | null = null;
  setUser(user: User | null): void {
    this.currentUser = user;
  }
}
```

## File: 285.txt

# #285「nullの型」

 

```typescript
// null型とtypeof
let value: null = null;
type NullType = null;
typeof null; // "object" (JavaScript仕様)
```

```typescript
// strictNullChecks: true
let str: string = null;  // エラー
let str: string | null = null;  // OK
```

```typescript
// NonNullable<T>で除外
type Result = string | number | null;
type NonNull = NonNullable<Result>;
// → string | number
```

## File: 286.txt

# #286「nullとundefinedの違い」

 

```typescript
// nullとundefinedの違い
let a: null = null;          // 明示的な空
let b: undefined = undefined; // 未定義
typeof null;      // "object"
typeof undefined; // "undefined"
```

```typescript
// オプショナルとnullの使い分け
interface User {
  name?: string;        // string | undefined
  email: string | null; // 明示的null
}
```

```typescript
// Nullish Coalescing
const value1 = null ?? "default";      // "default"
const value2 = undefined ?? "default"; // "default"
```

## File: 287.txt

# #287「nullの使い分け」

 

```typescript
// null: 明示的な空値
let currentUser: User | null = null;
function findById(id: number): User | null {
  return null;
}
```

```typescript
// undefined: オプショナル
interface Config {
  timeout?: number;  // number | undefined
}
function process(data?: string) {}
```

```typescript
// JSON互換性の違い
JSON.stringify({ value: null });      // {"value":null}
JSON.stringify({ value: undefined }); // {}
```

## File: 288.txt

# #288「nullチェック」

 

```typescript
// 厳密等価演算子と型ガード
if (user === null) {
  console.log("User is null");
}
function isNotNull<T>(value: T | null): value is T {
  return value !== null;
}
```

```typescript
// オプショナルチェーン
const name = user?.name;
const zip = user?.address?.zipCode;
```

```typescript
// Nullish Coalescing
const displayName = user ?? "Guest";
const port = config.port ?? 3000;
```

## File: 289.txt

# #289「nullish演算子 - ??」

 

```typescript
// Nullish Coalescing
const name = userName ?? "Guest";
const port = config.port ?? 3000;
```

```typescript
// ||演算子との違い
const count1 = 0 || 10;  // 10 (0はfalsy)
const count2 = 0 ?? 10;  // 0  (0はnullでない)
```

```typescript
// ??=代入演算子とオプショナルチェーン
config.timeout ??= 5000;
const zip = user?.address?.zipCode ?? "N/A";
```

## File: 290.txt

# #290「nullとfalseの違い」

 

```typescript
// 型の違い
let a: null = null;     // null型
let b: boolean = false; // boolean型
null === false;  // false
```

```typescript
// Nullish Coalescingの動作
const v1 = null ?? "default";  // "default"
const v2 = false ?? "default"; // false
```

```typescript
// 型安全性
let flag: boolean = null;  // エラー
let flag: boolean | null = null;  // OK
```

## File: 291.txt

# #291「nullと0の違い」

 

```typescript
// 型の違い
let a: null = null;   // null型
let b: number = 0;    // number型
null === 0;  // false
```

```typescript
// Nullish Coalescingの動作
const count1 = null ?? 10;  // 10
const count2 = 0 ?? 10;     // 0 (0は有効値)
```

```typescript
// 型安全性
let num: number = null;  // エラー
let num: number | null = null;  // OK
```

## File: 292.txt

# #292「nullと空文字列」

 

```typescript
// 型の違い
let a: null = null;     // null型
let b: string = "";     // string型
null === "";  // false
```

```typescript
// Nullish Coalescingの動作
const name1 = null ?? "Guest";  // "Guest"
const name2 = "" ?? "Guest";    // "" (空文字列は有効値)
```

```typescript
// 型安全性
let str: string = null;  // エラー
let str: string | null = null;  // OK
```

## File: 293.txt

# #293「nullのJSON表現」

 

```typescript
// nullのJSON表現
JSON.stringify({ value: null });
// → '{"value":null}'
JSON.stringify({ a: null, b: undefined });
// → '{"a":null}'
```

```typescript
// APIレスポンス型定義
interface ApiResponse {
  user: User | null;  // JSON互換
  metadata?: object;  // 省略可能
}
```

```typescript
// JSONパース
const data = JSON.parse('{"name":null}');
// → { name: null }
```

## File: 294.txt

# #294「nullのパターン」

 

```typescript
// Repository パターン
class UserRepository {
  findById(id: number): User | null {
    return this.users.find(u => u.id === id) ?? null;
  }
}
```

```typescript
// Option型パターン
type Option<T> = T | null;
function safeDivide(a: number, b: number): Option<number> {
  return b !== 0 ? a / b : null;
}
```

```typescript
// Null Objectパターン
const user = findUser(id) ?? createGuestUser();
if (user !== null) {
  console.log(user.name);
}
```

## File: 295.txt

# #295「null型まとめ」

 

```typescript
// null型の基本
let value: string | null = null;
if (value !== null) {
  value.toUpperCase(); // string型
}
```

```typescript
// Nullish Coalescing
const name = userName ?? "Guest";
const config = settings?.timeout ?? 5000;
```

```typescript
// 実践パターン
function findUser(id: number): User | null {
  return users.find(u => u.id === id) ?? null;
}
```

## File: 296.txt

# #296「undefined型とは」

 

```typescript
// undefined型の基本
let value: undefined = undefined;
let name: string | undefined;
```

```typescript
// オプショナルプロパティ
interface User {
  name?: string;  // string | undefined
  age?: number;   // number | undefined
}
```

```typescript
// strictNullChecks有効時
let id: number = undefined; // エラー
let id: number | undefined = undefined; // OK
```

## File: 297.txt

# #297「undefinedの宣言」

 

```typescript
// undefined型の宣言
let value: undefined = undefined;
let name: string | undefined;
```

```typescript
// オプショナルプロパティ
interface User {
  name?: string;  // string | undefined
  age?: number;   // number | undefined
}
```

```typescript
// 関数パラメータ
function greet(name?: string): void {
  console.log(name ?? "Guest");
}
```

## File: 298.txt

# #298「undefinedの代入」

 

```typescript
// undefinedの代入
let name: string | undefined = undefined;
name = "Alice";  // OK
name = undefined; // OK
```

```typescript
// strictNullChecks有効時
let id: number = undefined;  // エラー
let id: number | undefined = undefined;  // OK
```

```typescript
// オプショナルプロパティ
const user: User = {
  name: "Alice",
  age: undefined  // オプショナルなので省略可能
};
```

## File: 299.txt

# #299「初期化されていない変数」

 

```typescript
// 初期化されていない変数
let name: string | undefined;
console.log(name); // undefined
```

```typescript
// strictモードでのエラー
let id: number; // エラー: 初期化が必要
id = 42;  // OK
```

```typescript
// 明示的なundefined
let value: string | undefined = undefined;
if (value !== undefined) {
  console.log(value.toUpperCase());
}
```

## File: 300.txt

# #300「関数の戻り値なし」

 

```typescript
// void型: 戻り値を使わない
function log(message: string): void {
  console.log(message);
  // return undefined; が暗黙的
}
```

```typescript
// undefined型: 明示的にundefinedを返す
function find(): User | undefined {
  return undefined;
}
```

```typescript
// 暗黙的なundefined
function noReturn() {
  // 何もreturnしない
}
const result = noReturn(); // undefined
```

## File: 301.txt

# #301「存在しないプロパティ」

 

```typescript
// 存在しないプロパティ
const user = { name: "Alice" };
user.age;  // エラー: プロパティ'age'は存在しない
```

```typescript
// オプショナルチェーン
const age = user?.profile?.age;
// profileが存在しない場合はundefined
```

```typescript
// 型定義で安全に
interface User {
  name: string;
  age?: number;  // オプショナル
}
const user: User = { name: "Alice" };
user.age;  // number | undefined
```

## File: 302.txt

# #302「存在しない配列要素」

 

```typescript
// 配列の範囲外アクセス
const arr = [1, 2, 3];
const value = arr[10];  // undefined
```

```typescript
// noUncheckedIndexedAccess
// tsconfig: "noUncheckedIndexedAccess": true
const arr: number[] = [1, 2, 3];
const value = arr[0];  // number | undefined
```

```typescript
// 安全なアクセス
const arr = [1, 2, 3];
if (arr[10] !== undefined) {
  console.log(arr[10].toFixed());
}
```

## File: 303.txt

# #303「undefinedの型」

 

```typescript
// undefined型
let value: undefined = undefined;
type UndefinedType = undefined;
typeof undefined; // "undefined"
```

```typescript
// strictNullChecks: true
let str: string = undefined;  // エラー
let str: string | undefined = undefined;  // OK
```

```typescript
// NonNullable<T>で除外
type Result = string | number | undefined;
type NonUndef = NonNullable<Result>;
// → string | number
```

## File: 304.txt

# #304「undefinedチェック」

 

```typescript
// 厳密等価演算子と型ガード
if (value === undefined) {
  console.log("undefined");
}
function isDefined<T>(value: T | undefined): value is T {
  return value !== undefined;
}
```

```typescript
// Nullish Coalescing
const name = userName ?? "Guest";
const config = settings?.timeout ?? 5000;
```

```typescript
// オプショナルチェーン
const zip = user?.address?.zipCode;
// userまたはaddressがundefinedならundefined
```

## File: 305.txt

# #305「typeof undefined」

 

```typescript
// typeof undefined
typeof undefined; // "undefined"
typeof null;      // "object"
```

```typescript
// typeof でチェック
if (typeof value === "undefined") {
  console.log("undefined");
}
```

```typescript
// 未宣言の変数も安全
typeof undeclaredVar === "undefined"; // true (エラーなし)
undeclaredVar === undefined; // ReferenceError
```

## File: 306.txt

# #306「undefinedとvoidの違い」

 

```typescript
// void型: 戻り値を使わない
function log(msg: string): void {
  console.log(msg);
}
log("Hello"); // 戻り値は使えない
```

```typescript
// undefined型: 明示的にundefined
function find(): User | undefined {
  return undefined;
}
const user = find(); // undefined
```

```typescript
// voidはundefinedを返す
function noReturn(): void { }
const result = noReturn(); // undefined (型はvoid)
```

## File: 307.txt

# #307「undefinedのJSON表現」

 

```typescript
// undefinedのJSON表現
JSON.stringify({ value: undefined });
// → '{}'  (undefinedは省略)
JSON.stringify({ value: null });
// → '{"value":null}'
```

```typescript
// 配列内のundefined
JSON.stringify([1, undefined, 3]);
// → '[1,null,3]'  (配列ではnullに変換)
```

```typescript
// オプショナルプロパティ
interface User {
  name: string;
  age?: number;  // undefined可能
}
JSON.stringify({ name: "Alice" });
// → '{"name":"Alice"}'
```

## File: 308.txt

# #308「undefinedの自動挿入」

 

```typescript
// オプショナルパラメータ
function greet(name?: string) {
  console.log(name ?? "Guest"); // nameはundefined可能
}
greet(); // name = undefined
```

```typescript
// 暗黙的なreturn
function noReturn() {
  // return文がない
}
const result = noReturn(); // undefined
```

```typescript
// オプショナルプロパティ
interface User {
  name: string;
  age?: number;  // 省略時はundefined
}
const user: User = { name: "Alice" };
// user.age は undefined
```

## File: 309.txt

# #309「undefinedのパターン」

 

```typescript
// Option型パターン
type Option<T> = T | undefined;
function divide(a: number, b: number): Option<number> {
  return b !== 0 ? a / b : undefined;
}
```

```typescript
// デフォルト値パターン
function greet(name?: string): void {
  const displayName = name ?? "Guest";
  console.log(`Hello, ${displayName}`);
}
```

```typescript
// Partial型パターン
interface User {
  name: string;
  age: number;
}
type PartialUser = Partial<User>;
// { name?: string; age?: number }
```

## File: 310.txt

# #310「undefined型まとめ」

 

```typescript
// undefined型の基本
let value: string | undefined;
interface User {
  name: string;
  age?: number;  // オプショナル
}
```

```typescript
// undefinedチェック
if (value !== undefined) {
  value.toUpperCase(); // string型
}
const name = userName ?? "Guest";
```

```typescript
// 実践パターン
function greet(name?: string): void {
  console.log(name ?? "Guest");
}
type Option<T> = T | undefined;
```

## File: 311.txt

# #311「strictNullChecksとは」

 

```typescript
// strictNullChecks: false (無効)
let name: string = null; // OK (エラーなし)
let age: number = undefined; // OK
```

```typescript
// strictNullChecks: true (有効)
let name: string = null; // エラー
let name: string | null = null; // OK
```

```typescript
// tsconfig.json
{
  "compilerOptions": {
    "strictNullChecks": true
  }
}
```

## File: 312.txt

# #312「無効時の挙動」

 

```typescript
// strictNullChecks: false
let name: string = null; // OK
name.toUpperCase(); // 実行時エラー!
```

```typescript
// すべての型にnull/undefinedが含まれる
function greet(name: string) {
  // nameがnullかもしれない
  return name.toUpperCase(); // 危険
}
greet(null); // エラーなし
```

```typescript
// 型チェックが不十分
interface User {
  name: string;
}
const user: User = { name: null }; // OK
```

## File: 313.txt

# #313「有効時の挙動」

 

```typescript
// strictNullChecks: true
let name: string = null; // エラー
let name: string | null = null; // OK
```

```typescript
// nullチェックが必須
function greet(name: string | null) {
  if (name !== null) {
    return name.toUpperCase(); // 安全
  }
  return "Guest";
}
```

```typescript
// オプショナルプロパティ
interface User {
  name: string;
  age?: number; // number | undefined
}
```

## File: 314.txt

# #314「設定方法 - tsconfig.json」

 

```typescript
// tsconfig.json - 個別設定
{
  "compilerOptions": {
    "strictNullChecks": true
  }
}
```

```typescript
// tsconfig.json - strict設定（推奨）
{
  "compilerOptions": {
    "strict": true  // strictNullChecksも含まれる
  }
}
```

```typescript
// 確認方法
tsc --showConfig
// strictNullChecksの値を確認
```

## File: 315.txt

# #315「有効にすべき理由」

 

```typescript
// nullポインタ例外を防ぐ
function getLength(str: string | null): number {
  if (str === null) return 0;
  return str.length; // 安全
}
```

```typescript
// エディタ補完の改善
const user: User | null = getUser();
if (user !== null) {
  user.name; // 補完が効く
}
```

```typescript
// バグの早期発見
function process(data: string) {
  return data.toUpperCase();
}
process(null); // コンパイルエラー
```

## File: 316.txt

# #316「null代入エラー」

 

```typescript
// strictNullChecks: true
let name: string = null; // エラー
// Type 'null' is not assignable to type 'string'
```

```typescript
// 修正方法1: Union型
let name: string | null = null; // OK
name = "Alice"; // OK
```

```typescript
// 修正方法2: Non-Null Assertion (非推奨)
let name: string = null!; // OK (型チェック回避)
// 実行時エラーのリスクあり
```

## File: 317.txt

# #317「undefined代入エラー」

 

```typescript
// strictNullChecks: true
let name: string = undefined; // エラー
// Type 'undefined' is not assignable to type 'string'
```

```typescript
// 修正方法1: Union型
let name: string | undefined = undefined; // OK
name = "Alice"; // OK
```

```typescript
// 修正方法2: オプショナル
interface User {
  name?: string; // string | undefined
}
function greet(name?: string) {}
```

## File: 318.txt

# #318「型安全性の向上」

 

```typescript
// 型ガードで安全にアクセス
function getLength(str: string | null): number {
  if (str !== null) {
    return str.length; // string型
  }
  return 0;
}
```

```typescript
// 制御フロー分析
let value: string | null = getValue();
if (value === null) return;
value.toUpperCase(); // string型に絞り込み
```

```typescript
// オプショナルチェーン
const user: User | null = getUser();
const name = user?.name; // string | undefined
```

## File: 319.txt

# #319「段階的導入」

 

```typescript
// ファイル単位で有効化
// @ts-check
// strictNullChecks有効として扱う
```

```typescript
// tsconfig.json - 段階的設定
{
  "compilerOptions": {
    "strictNullChecks": false
  },
  "files": ["src/new-module.ts"]
}
```

```typescript
// エラー数を確認
tsc --noEmit
// エラーをリスト化して優先順位付け
```

## File: 320.txt

# #320「レガシーコード対応」

 

```typescript
// Non-Null Assertion (一時的)
const user = getUser()!; // null/undefinedでないと保証
user.name; // OK
```

```typescript
// 型アサーション (一時的)
const data = response as User;
// TODO: 適切なnullチェックに修正
```

```typescript
// 段階的修正
function legacyFunc(value: any) {
  // TODO: strictNullChecks対応
  return value.toString();
}
```

## File: 321.txt

# #321「マイグレーション」

 

```typescript
// マイグレーション手順
// 1. strictNullChecks有効化
{
  "compilerOptions": {
    "strictNullChecks": true
  }
}
```

```typescript
// 2. 型定義の追加
interface User {
  name: string;
  email: string | null; // null許容を明示
}
```

```typescript
// 3. nullチェックの実装
function getUser(id: number): User | null {
  const user = findUser(id);
  if (!user) return null;
  return user;
}
```

## File: 322.txt

# #322「サードパーティライブラリ」

 

```typescript
// 型定義ファイル作成
// types/legacy-lib.d.ts
declare module 'legacy-lib' {
  export function getData(): string | null;
}
```

```typescript
// skipLibCheck (一時的)
{
  "compilerOptions": {
    "strictNullChecks": true,
    "skipLibCheck": true
  }
}
```

```typescript
// 型アサーションで対応
import { getData } from 'legacy-lib';
const data = getData() as string | null;
```

## File: 323.txt

# #323「デバッグ方法」

 

```typescript
// エラーメッセージを読む
let name: string = getValue();
// Error: Type 'string | null' is not assignable to type 'string'
```

```typescript
// 型ガードで修正
const value = getValue();
if (value !== null) {
  const name: string = value; // OK
}
```

```typescript
// 型チェックのみ実行
tsc --noEmit
// コンパイルせず型エラーだけ確認
```

## File: 324.txt

# #324「ベストプラクティス」

 

```typescript
// ベストプラクティス1: 明示的な型定義
function getUser(id: number): User | null {
  return users.find(u => u.id === id) ?? null;
}
```

```typescript
// ベストプラクティス2: 型ガード
if (user !== null) {
  console.log(user.name); // 安全
}
```

```typescript
// ベストプラクティス3: Nullish Coalescing
const name = user?.name ?? "Guest";
const port = config.port ?? 3000;
```

## File: 325.txt

# #325「strictNullChecksまとめ」

 

```typescript
// 必須設定
{
  "compilerOptions": {
    "strict": true  // strictNullChecksも有効
  }
}
```

```typescript
// 型安全なコード
function process(value: string | null): string {
  if (value === null) return "default";
  return value.toUpperCase();
}
```

```typescript
// 実践パターン
const user = getUser();
const name = user?.name ?? "Guest";
if (user !== null) {
  console.log(user.email);
}
```

## File: 326.txt

# #326「nullable型とは - T | null」

 

```typescript
// nullable型の基本
type Nullable<T> = T | null;
let name: Nullable<string> = null;
let age: number | null = 25;
```

```typescript
// 関数の戻り値
function findUser(id: number): User | null {
  return users.find(u => u.id === id) ?? null;
}
```

```typescript
// プロパティ
interface Config {
  cache: CacheService | null;
  logger: Logger | null;
}
```

## File: 327.txt

# #327「nullable型の宣言」

 

```typescript
// 直接宣言
let name: string | null = null;
let age: number | null = null;
```

```typescript
// 型エイリアス
type Nullable<T> = T | null;
let user: Nullable<User> = null;
let config: Nullable<Config> = null;
```

```typescript
// インターフェース
interface ApiResponse<T> {
  data: T | null;
  error: string | null;
}
```

## File: 328.txt

# #328「値の代入」

 

```typescript
// 値の代入
let name: string | null = "Alice";
name = null; // OK
name = "Bob"; // OK
```

```typescript
// オブジェクトの代入
let user: User | null = { name: "Alice", age: 25 };
user = null; // OK
```

```typescript
// 配列の代入
let items: string[] | null = ["a", "b"];
items = null; // OK
items = ["c", "d"]; // OK
```

## File: 329.txt

# #329「nullの代入」

 

```typescript
// null代入
let user: User | null = getUser();
user = null; // OK
```

```typescript
// 初期値としてのnull
let cache: Cache | null = null;
function init() {
  cache = new Cache();
}
```

```typescript
// リセット時のnull
let currentUser: User | null = loginUser;
function logout() {
  currentUser = null;
}
```

## File: 330.txt

# #330「nullableチェック」

 

```typescript
// 厳密等価演算子
if (user === null) {
  return "No user";
}
console.log(user.name); // User型
```

```typescript
// 型ガード
function isNotNull<T>(value: T | null): value is T {
  return value !== null;
}
if (isNotNull(user)) {
  user.name; // T型
}
```

```typescript
// Nullish Coalescing
const name = user ?? createGuestUser();
const port = config ?? 3000;
```

## File: 331.txt

# #331「Optional Chaining - x?.property」

 

```typescript
// Optional Chaining
const user: User | null = getUser();
const name = user?.name; // string | undefined
```

```typescript
// ネストしたプロパティ
const city = user?.address?.city;
const zip = user?.address?.zipCode ?? "N/A";
```

```typescript
// 配列要素とメソッド
const firstItem = array?.[0];
const result = obj?.method?.();
```

## File: 332.txt

# #332「Nullish Coalescing - x ?? default」

 

```typescript
// Nullish Coalescing
const name = userName ?? "Guest";
const port = config.port ?? 3000;
```

```typescript
// || との違い
const count1 = 0 || 10;  // 10 (0はfalsy)
const count2 = 0 ?? 10;  // 0  (0は有効値)
```

```typescript
// Optional Chainingと組み合わせ
const city = user?.address?.city ?? "Unknown";
const age = user?.age ?? 18;
```

## File: 333.txt

# #333「nullable配列」

 

```typescript
// 要素がnullable
const users: (User | null)[] = [user1, null, user2];
const names = users.filter(u => u !== null);
```

```typescript
// 型ガードでフィルタ
function isNotNull<T>(value: T | null): value is T {
  return value !== null;
}
const validUsers = users.filter(isNotNull);
```

```typescript
// map処理
const userNames = users.map(u => u?.name ?? "Unknown");
```

## File: 334.txt

# #334「配列がnullable」

 

```typescript
// 配列がnullable
let items: string[] | null = null;
items = ["a", "b", "c"]; // OK
```

```typescript
// nullチェック後の操作
if (items !== null) {
  items.forEach(item => console.log(item));
}
```

```typescript
// Optional Chainingで安全にアクセス
const length = items?.length ?? 0;
const first = items?.[0];
```

## File: 335.txt

# #335「nullableオブジェクト」

 

```typescript
// nullableオブジェクト
function findUser(id: number): User | null {
  return users.find(u => u.id === id) ?? null;
}
```

```typescript
// Optional Chainingでアクセス
const user = findUser(1);
const name = user?.name;
const age = user?.age ?? 0;
```

```typescript
// 型ガードで安全に
if (user !== null) {
  console.log(user.name); // User型
  console.log(user.age);
}
```

## File: 336.txt

# #336「関数引数のnullable」

 

```typescript
// nullable引数
function greet(user: User | null): string {
  if (user === null) {
    return "Hello, Guest";
  }
  return `Hello, ${user.name}`;
}
```

```typescript
// オプショナルとの違い
function process1(data: string | null) {
  // nullを明示的に渡す必要あり
}
function process2(data?: string) {
  // 省略可能
}
```

```typescript
// デフォルト値との組み合わせ
function log(message: string | null = null) {
  console.log(message ?? "No message");
}
```

## File: 337.txt

# #337「関数戻り値のnullable」

 

```typescript
// nullable戻り値
function findUser(id: number): User | null {
  const user = users.find(u => u.id === id);
  return user ?? null;
}
```

```typescript
// 呼び出し側の処理
const user = findUser(1);
if (user !== null) {
  console.log(user.name);
}
```

```typescript
// Nullish Coalescingで簡潔に
const user = findUser(1) ?? createGuestUser();
const name = findUser(1)?.name ?? "Unknown";
```

## File: 338.txt

# #338「nullable型の型ガード」

 

```typescript
// 型ガード関数
function isNotNull<T>(value: T | null): value is T {
  return value !== null;
}
```

```typescript
// 使用例
const user: User | null = getUser();
if (isNotNull(user)) {
  user.name; // User型として扱える
}
```

```typescript
// 配列のfilterと組み合わせ
const users: (User | null)[] = [user1, null, user2];
const validUsers: User[] = users.filter(isNotNull);
```

## File: 339.txt

# #339「ベストプラクティス」

 

```typescript
// ベストプラクティス1: 型エイリアス
type Nullable<T> = T | null;
function findUser(id: number): Nullable<User> {
  return users.find(u => u.id === id) ?? null;
}
```

```typescript
// ベストプラクティス2: 型ガード
if (user !== null) {
  console.log(user.name); // 安全
}
```

```typescript
// ベストプラクティス3: Optional Chaining
const name = user?.name ?? "Guest";
const city = user?.address?.city;
```

## File: 340.txt

# #340「nullable型まとめ」

 

```typescript
// nullable型の基本
type Nullable<T> = T | null;
function findUser(id: number): Nullable<User> {
  return users.find(u => u.id === id) ?? null;
}
```

```typescript
// 安全なアクセス
const user = findUser(1);
const name = user?.name ?? "Guest";
if (user !== null) {
  console.log(user.email);
}
```

```typescript
// 実践パターン
const users = getUsers();
const validUsers = users.filter(isNotNull);
const names = validUsers.map(u => u.name);
```

## File: 341.txt

# #341「undefinedable型 - T | undefined」

 

```typescript
// undefinedable型の基本
type Undefinedable<T> = T | undefined;
let name: string | undefined;
name = "Alice";
name = undefined;
```

```typescript
// 関数引数での利用
function greet(name: string | undefined) {
  if (name !== undefined) {
    console.log(`Hello, ${name}`);
  }
}
```

```typescript
// オプショナルとの関係
interface User {
  name: string;
  age: number | undefined;  // 明示的undefinedable
  email?: string;           // オプショナル(= string | undefined)
}
```

## File: 342.txt

# #342「undefinedable型の宣言」

 

```typescript
// 基本的な宣言
let value: string | undefined;
let count: number | undefined = undefined;
let flag: boolean | undefined;
```

```typescript
// 型エイリアスでの再利用
type Undefinedable<T> = T | undefined;
let name: Undefinedable<string>;
let age: Undefinedable<number>;
```

```typescript
// インターフェースでの利用
interface Config {
  timeout: number | undefined;
  maxRetries: number | undefined;
  callback: ((data: string) => void) | undefined;
}
```

## File: 343.txt

# #343「オプショナルプロパティ - prop?」

 

```typescript
// オプショナルプロパティの基本
interface User {
  name: string;
  age?: number;       // 省略可能
  email?: string;     // 省略可能
}
```

```typescript
// オブジェクトリテラルでの省略
const user1: User = { name: "Alice", age: 30 };
const user2: User = { name: "Bob" }; // ageとemailは省略
```

```typescript
// 型エイリアスでの利用
type Config = {
  host: string;
  port?: number;      // デフォルト値を使う想定
  ssl?: boolean;
};
```

## File: 344.txt

# #344「オプショナルプロパティの型」

 

```typescript
// オプショナルとundefinedableの等価性
interface User1 {
  age?: number;              // number | undefined
}
interface User2 {
  age: number | undefined;   // 同じ型
}
```

```typescript
// アクセス時のチェック
const user: User1 = { age: 30 };
if (user.age !== undefined) {
  console.log(user.age + 1);
}
```

```typescript
// Optional Chainingでの安全なアクセス
const age = user.age?.toString();
const doubled = user.age ? user.age * 2 : 0;
```

## File: 345.txt

# #345「オプショナル引数」

 

```typescript
// オプショナル引数の基本
function greet(name: string, age?: number) {
  if (age !== undefined) {
    console.log(`${name} is ${age} years old`);
  } else {
    console.log(`Hello, ${name}`);
  }
}
```

```typescript
// 呼び出し時の省略
greet("Alice", 30);  // 引数2つ
greet("Bob");        // ageは省略
```

```typescript
// デフォルト値との組み合わせ
function createUser(name: string, role: string = "user") {
  return { name, role };
}
```

## File: 346.txt

# #346「オプショナル引数の型」

 

```typescript
// オプショナル引数とundefinedable
function log1(msg?: string) {
  // msg: string | undefined
  console.log(msg ?? "No message");
}
```

```typescript
// デフォルト引数との違い
function log2(msg: string = "default") {
  // msg: string (undefinedにならない)
  console.log(msg);
}
```

```typescript
// 型推論との組み合わせ
function process(data: number, options?: { verbose: boolean }) {
  if (options !== undefined) {
    console.log(options.verbose);
  }
}
```

## File: 347.txt

# #347「undefinedableチェック」

 

```typescript
// 基本的なチェック
function process(value: string | undefined) {
  if (value !== undefined) {
    console.log(value.toUpperCase());
  }
}
```

```typescript
// typeof演算子でのチェック
if (typeof value === "string") {
  console.log(value.length);
}
```

```typescript
// Optional Chainingとデフォルト値
const length = value?.length ?? 0;
const upper = value?.toUpperCase();
```

## File: 348.txt

# #348「Optional Chainingの活用」

 

```typescript
// プロパティアクセス
const user: { name?: string } = {};
const name = user.name?.toUpperCase();
const length = user.name?.length;
```

```typescript
// メソッド呼び出し
const callback: (() => void) | undefined = getCallback();
callback?.();
```

```typescript
// ネストしたアクセスとデフォルト値
const city = user?.address?.city ?? "Unknown";
const phone = user?.contact?.phone?.trim();
```

## File: 349.txt

# #349「ベストプラクティス」

 

```typescript
// ベストプラクティス1: オプショナルの活用
interface Config {
  host: string;
  port?: number;        // オプショナル
  timeout?: number;     // オプショナル
}
```

```typescript
// ベストプラクティス2: デフォルト値
function connect(config: Config) {
  const port = config.port ?? 8080;
  const timeout = config.timeout ?? 3000;
}
```

```typescript
// ベストプラクティス3: Optional Chaining
const result = data?.process()?.value ?? defaultValue;
```

## File: 350.txt

# #350「undefinedable型まとめ」

 

```typescript
// undefinedable型の基本
type Undefinedable<T> = T | undefined;
interface User {
  name: string;
  age?: number;  // オプショナル
}
```

```typescript
// 安全なアクセス
function greet(user?: User) {
  const name = user?.name ?? "Guest";
  console.log(`Hello, ${name}`);
}
```

```typescript
// 実践パターン
const config: Config = {
  host: "localhost",
  port: options?.port ?? 8080,
  timeout: options?.timeout ?? 3000,
};
```

## File: 351.txt

# #351「nullish型 - T | null | undefined」

 

```typescript
// nullish型の基本
type Nullish<T> = T | null | undefined;
let value: string | null | undefined;
value = "hello";
value = null;
value = undefined;
```

```typescript
// 実践的な使用例
interface User {
  name: string;
  email: string | null | undefined;
  age?: number | null;
}
```

```typescript
// 関数の戻り値
function findUser(id: number): User | null | undefined {
  if (id < 0) return undefined;  // 無効なID
  const user = database.find(id);
  return user ?? null;           // 見つからない場合
}
```

## File: 352.txt

# #352「nullish型の宣言」

 

```typescript
// 基本的な宣言
let name: string | null | undefined;
let count: number | null | undefined;
let flag: boolean | null | undefined;
```

```typescript
// 型エイリアスでの再利用
type Nullish<T> = T | null | undefined;
let value: Nullish<string>;
let data: Nullish<number[]>;
```

```typescript
// インターフェースでの利用
interface ApiResponse {
  data: User | null | undefined;
  error: Error | null | undefined;
  timestamp: number;
}
```

## File: 353.txt

# #353「nullish型の使用例」

 

```typescript
// APIレスポンスの型定義
interface ApiResponse<T> {
  data: T | null | undefined;
  error: string | null | undefined;
  status: number;
}
```

```typescript
// データベースクエリの結果
async function getUser(id: number): Promise<User | null | undefined> {
  try {
    return await db.users.findById(id);
  } catch {
    return undefined;
  }
}
```

```typescript
// フォーム入力の処理
interface FormData {
  name: string;
  email: string | null | undefined;
  phone: string | null | undefined;
}
```

## File: 354.txt

# #354「nullishチェック - x != null」

 

```typescript
// nullishチェックの基本
function process(value: string | null | undefined) {
  if (value != null) {
    // value: string
    console.log(value.toUpperCase());
  }
}
```

```typescript
// 厳密等価との違い
if (value !== null && value !== undefined) {
  // 冗長
}
if (value != null) {
  // 簡潔で推奨
}
```

```typescript
// 型ガードとして機能
const data: number | null | undefined = getData();
if (data != null) {
  const doubled = data * 2;  // number型として扱える
}
```

## File: 355.txt

# #355「Nullish Coalescing - ??」

 

```typescript
// Nullish Coalescingの基本
const value1 = null ?? "default";      // "default"
const value2 = undefined ?? "default"; // "default"
const value3 = "hello" ?? "default";   // "hello"
```

```typescript
// 実用的な使用例
function greet(name: string | null | undefined) {
  const displayName = name ?? "Guest";
  console.log(`Hello, ${displayName}`);
}
```

```typescript
// 設定値のデフォルト処理
const config = {
  port: options?.port ?? 8080,
  timeout: options?.timeout ?? 3000,
  retries: options?.retries ?? 3,
};
```

## File: 356.txt

# #356「??と||の違い」

 

```typescript
// ?? と || の違い
const count1 = 0 || 10;   // 10 (0はfalsy)
const count2 = 0 ?? 10;   // 0  (0はnullishではない)

const text1 = "" || "default";   // "default"
const text2 = "" ?? "default";   // ""
```

```typescript
// 数値のデフォルト値
function setVolume(volume: number | null | undefined) {
  const vol = volume ?? 50;  // 0も有効な音量
  console.log(`Volume: ${vol}`);
}
```

```typescript
// 真偽値のデフォルト値
const enabled = config.enabled ?? true;  // falseも有効
const verbose = options.verbose ?? false;
```

## File: 357.txt

# #357「??の使用例」

 

```typescript
// 設定値のデフォルト処理
const config = {
  host: env.HOST ?? "localhost",
  port: env.PORT ?? 8080,
  timeout: env.TIMEOUT ?? 3000,
};
```

```typescript
// Optional Chainingとの組み合わせ
const userName = user?.name ?? "Anonymous";
const city = user?.address?.city ?? "Unknown";
const email = user?.contacts?.[0]?.email ?? "no-email";
```

```typescript
// 関数の引数処理
function createUser(name: string, age?: number | null) {
  return {
    name,
    age: age ?? 0,
    status: "active",
  };
}
```

## File: 358.txt

# #358「Optional Chaining - ?.」

 

```typescript
// プロパティアクセス
const user: User | null | undefined = getUser();
const name = user?.name;
const email = user?.email;
```

```typescript
// メソッド呼び出し
const result = obj?.method?.();
const length = str?.toUpperCase()?.length;
```

```typescript
// 配列アクセスとネスト
const firstItem = array?.[0];
const city = user?.address?.city;
const phone = user?.contacts?.[0]?.phone;
```

## File: 359.txt

# #359「?.の使用例」

 

```typescript
// APIレスポンスの処理
const response = await fetchUser(id);
const userName = response?.data?.name ?? "Unknown";
const avatar = response?.data?.profile?.avatar;
```

```typescript
// イベントハンドラ
element?.addEventListener("click", () => {
  console.log(element?.dataset?.id);
});
```

```typescript
// 複雑なデータ構造のアクセス
const price = product?.variants?.[0]?.pricing?.amount ?? 0;
const rating = reviews?.[0]?.rating?.average?.toFixed(1);
```

## File: 360.txt

# #360「nullish型まとめ」

 

```typescript
// nullish型の基本
type Nullish<T> = T | null | undefined;
const value: string | null | undefined = getValue();
```

```typescript
// 安全な操作
const displayName = user?.name ?? "Guest";
const age = user?.age ?? 0;
if (value != null) {
  console.log(value);
}
```

```typescript
// 実践パターン
const config = {
  host: env?.HOST ?? "localhost",
  port: env?.PORT ?? 8080,
  data: response?.data ?? [],
};
```

## File: 361.txt

# #361「Non-null Assertionとは - !」

 

```typescript
// Non-null Assertionの基本
const element = document.getElementById("app")!;
// HTMLElement型として扱える(null可能性を無視)
element.innerHTML = "Hello";
```

```typescript
// nullable型での使用
function getUser(): User | null {
  return { name: "Alice", age: 30 };
}
const user = getUser()!;  // User型として扱う
console.log(user.name);
```

```typescript
// undefinedableでの使用
let value: string | undefined = "hello";
const length = value!.length;  // stringとして扱う
```

## File: 362.txt

# #362「!演算子の構文」

 

```typescript
// 変数での使用
let value: string | null = getValue();
const length = value!.length;
```

```typescript
// プロパティアクセスでの使用
const user: { name?: string } = getUser();
const name = user.name!.toUpperCase();
```

```typescript
// 関数呼び出しでの使用
const element = document.getElementById("app")!;
const firstChild = element.firstChild!;
const data = array.find(x => x.id === 1)!;
```

## File: 363.txt

# #363「!演算子の意味」

 

```typescript
// 型の変換
const value: string | null = getValue();
// value!: string (nullが除去される)
const upper = value!.toUpperCase();
```

```typescript
// 実行時コードは変わらない
// TypeScript
const length = value!.length;
// JavaScript (トランスパイル後)
const length = value.length;
```

```typescript
// 複数のnullish型から除去
const data: number | null | undefined = getData();
const doubled = data! * 2;  // number型として扱う
```

## File: 364.txt

# #364「!演算子の危険性」

 

```typescript
// 危険な使用例
const element = document.getElementById("app")!;
element.innerHTML = "Hello";  // elementがnullならエラー
```

```typescript
// 実行時エラーの例
const user = users.find(u => u.id === 999)!;
console.log(user.name);  // Cannot read property 'name' of undefined
```

```typescript
// 安全な代替手段
const element = document.getElementById("app");
if (element !== null) {
  element.innerHTML = "Hello";  // 安全
}
```

## File: 365.txt

# #365「代替手段」

 

```typescript
// 型ガードを使う
const element = document.getElementById("app");
if (element !== null) {
  element.innerHTML = "Hello";
}
```

```typescript
// Optional Chainingを使う
const user = findUser(id);
const name = user?.name ?? "Unknown";
user?.greet();
```

```typescript
// 型ガード関数を使う
function isNotNull<T>(value: T | null): value is T {
  return value !== null;
}
const validUsers = users.filter(isNotNull);
```

## File: 366.txt

# #366「間違い(1) - 混同」

 

```typescript
// 混同しやすい例
const value: boolean | null = getValue();
const result1 = !value;   // 論理否定 (boolean)
const result2 = value!;   // Non-null Assertion (boolean)
```

```typescript
// 間違った使用
if (!user!) {  // 混乱しやすい
  // ...
}
```

```typescript
// 正しい書き方
if (user === null) {  // 明確
  // ...
}
if (!user) {  // truthyチェック
  // ...
}
```

## File: 367.txt

# #367「間違い(2) - チェック漏れ」

 

```typescript
// チェック漏れの例
function processUser(id: number) {
  const user = findUser(id)!;  // nullの可能性を無視
  console.log(user.name);      // 実行時エラーの可能性
}
```

```typescript
// 正しいチェック
function processUser(id: number) {
  const user = findUser(id);
  if (user === null) {
    console.log("User not found");
    return;
  }
  console.log(user.name);  // 安全
}
```

```typescript
// Optional Chainingでの対処
function processUser(id: number) {
  const user = findUser(id);
  const name = user?.name ?? "Unknown";
  console.log(name);
}
```

## File: 368.txt

# #368「間違い(3) - !演算子乱用」

 

```typescript
// 乱用の例 (悪い例)
const data = response.data!.users!.find(u => u.id === id)!;
const name = data.profile!.name!.toUpperCase();
```

```typescript
// 適切な型ガード (良い例)
if (response.data?.users) {
  const user = response.data.users.find(u => u.id === id);
  if (user?.profile?.name) {
    const name = user.profile.name.toUpperCase();
  }
}
```

```typescript
// ESLintでの制限
// .eslintrc.json
{
  "rules": {
    "@typescript-eslint/no-non-null-assertion": "error"
  }
}
```

## File: 369.txt

# #369「ベストプラクティス」

 

```typescript
// ベストプラクティス1: 型ガードを優先
const element = document.getElementById("app");
if (element !== null) {
  element.innerHTML = "Hello";
}
```

```typescript
// ベストプラクティス2: Optional Chainingを活用
const name = user?.name ?? "Unknown";
const result = data?.process()?.value;
```

```typescript
// やむを得ず使う場合: コメントで理由を明記
// アプリ起動時に必ず存在することが保証されている
const rootElement = document.getElementById("root")!;
ReactDOM.render(<App />, rootElement);
```

## File: 370.txt

# #370「マスターチェック」

 

```typescript
// Non-null Assertionの基本
const element = document.getElementById("app")!;
// HTMLElement型 (nullの可能性を無視)
```

```typescript
// 推奨される代替手段
const element = document.getElementById("app");
if (element !== null) {
  element.innerHTML = "Hello";
}
const name = user?.name ?? "Unknown";
```

```typescript
// 使用を避けるべき例
const user = findUser(id)!;  // 危険
const data = response.data!.items!;  // 乱用
```

## File: 371.txt

# #371「void型とは」

 

```typescript
// void型の基本
function logMessage(msg: string): void {
  console.log(msg);
  // returnなし、または return; のみ
}
```

```typescript
// undefinedとの違い
function returnsVoid(): void {
  console.log("副作用のみ");
}
function returnsUndefined(): undefined {
  return undefined;  // 明示的にundefinedを返す
}
```

```typescript
// 実用例
function addEventListener(callback: () => void): void {
  // イベントリスナーの登録
}
```

## File: 372.txt

# #372「使用場面」

 

```typescript
// ログ出力
function log(message: string): void {
  console.log(`[LOG] ${message}`);
}
```

```typescript
// イベントハンドラ
button.addEventListener("click", (): void => {
  console.log("Clicked");
});
```

```typescript
// 非同期処理
async function saveData(data: Data): Promise<void> {
  await database.save(data);
  console.log("Saved");
}
```

## File: 373.txt

# #373「void型の宣言」

 

```typescript
// 関数宣言
function greet(name: string): void {
  console.log(`Hello, ${name}`);
}
```

```typescript
// アロー関数
const log = (msg: string): void => {
  console.log(msg);
};
```

```typescript
// 関数型の定義
type VoidFunction = () => void;
type Callback = (data: string) => void;
const handler: Callback = (data) => console.log(data);
```

## File: 374.txt

# #374「void型を返す関数」

 

```typescript
// return文なし
function log1(msg: string): void {
  console.log(msg);
}
```

```typescript
// 値を指定しないreturn
function log2(msg: string): void {
  if (!msg) return;
  console.log(msg);
}
```

```typescript
// undefinedを返す (許可される)
function log3(msg: string): void {
  console.log(msg);
  return undefined;
}
```

## File: 375.txt

# #375「return文」

 

```typescript
// 早期リターン
function validate(value: string): void {
  if (!value) return;  // 値なし
  if (value.length < 3) return;
  console.log(`Valid: ${value}`);
}
```

```typescript
// エラーになる例
function invalid(): void {
  return "string";  // エラー: Type 'string' is not assignable to type 'void'
}
```

```typescript
// undefinedは許可される
function allowed(): void {
  return undefined;  // OK
  return;            // OK (推奨)
}
```

## File: 376.txt

# #376「undefinedとの違い」

 

```typescript
// void: 戻り値を無視
function logMessage(msg: string): void {
  console.log(msg);
}
const result1 = logMessage("Hello");  // void型
```

```typescript
// undefined: undefined値を返す
function findItem(id: number): Item | undefined {
  return items.find(item => item.id === id);
}
const result2 = findItem(1);  // Item | undefined型
```

```typescript
// 使い分け
type Logger = (msg: string) => void;      // 副作用
type Finder = (id: number) => Item | undefined;  // 検索
```

## File: 377.txt

# #377「void型変数」

 

```typescript
// void型変数 (実用性は低い)
let value: void;
value = undefined;  // OK
// value = null;    // strictNullChecks有効時はエラー
```

```typescript
// 関数の戻り値として使うのが一般的
function execute(): void {
  console.log("Executed");
}
const result: void = execute();
```

```typescript
// 実用的な使用例
type VoidCallback = () => void;
const callbacks: VoidCallback[] = [];
callbacks.push(() => console.log("Done"));
```

## File: 378.txt

# #378「変数への代入」

 

```typescript
// 代入可能な値
let value: void;
value = undefined;  // OK
```

```typescript
// エラーになる代入
let value: void;
// value = null;       // strictNullChecks有効時はエラー
// value = 0;          // エラー
// value = "string";   // エラー
```

```typescript
// void型関数の戻り値
function doSomething(): void {
  console.log("Done");
}
const result: void = doSomething();  // undefined
```

## File: 379.txt

# #379「void型の意味」

 

```typescript
// 副作用のための関数
function updateUI(data: Data): void {
  // DOM操作など副作用のみ
  document.getElementById("app")!.innerHTML = data.html;
}
```

```typescript
// コールバック関数の型定義
function forEach<T>(
  array: T[],
  callback: (item: T) => void
): void {
  for (const item of array) {
    callback(item);
  }
}
```

```typescript
// 戻り値の無視を明示
type EventHandler = (event: Event) => void;
element.addEventListener("click", (e): void => {
  console.log("Clicked", e);
});
```

## File: 380.txt

# #380「設計思想」

 

```typescript
// 純粋関数: 値を返す
function add(a: number, b: number): number {
  return a + b;
}
```

```typescript
// 副作用関数: void
function logResult(result: number): void {
  console.log(`Result: ${result}`);
}
```

```typescript
// 設計の明確化
interface DataService {
  getData(): Data;        // 値を取得
  saveData(data: Data): void;  // 副作用のみ
  deleteData(id: number): void;  // 副作用のみ
}
```

## File: 381.txt

# #381「型推論」

 

```typescript
// 型推論されるvoid
function log1(msg: string) {
  console.log(msg);
  // 戻り値型: void (推論)
}
```

```typescript
// 明示的なvoid
function log2(msg: string): void {
  console.log(msg);
  // 意図が明確
}
```

```typescript
// 推論の活用
const handler = (e: Event) => {
  console.log(e);
};  // (e: Event) => void と推論
```

## File: 382.txt

# #382「明示的宣言」

 

```typescript
// 明示的宣言が推奨される場面
export function initialize(config: Config): void {
  // 公開API
}
interface Logger {
  log(message: string): void;  // インターフェース
}
```

```typescript
// 型推論でも良い場面
const logError = (err: Error) => {
  console.error(err);  // 内部関数
};
```

```typescript
// ESLintでの強制
// .eslintrc.json
{
  "rules": {
    "@typescript-eslint/explicit-function-return-type": "error"
  }
}
```

## File: 383.txt

# #383「ユースケース」

 

```typescript
// イベントハンドラ
button.addEventListener("click", (e: Event): void => {
  console.log("Clicked");
});
```

```typescript
// コールバック関数
array.forEach((item: string): void => {
  console.log(item);
});
```

```typescript
// ミドルウェア
type Middleware = (
  req: Request,
  res: Response,
  next: () => void
) => void;
```

## File: 384.txt

# #384「Promise<void>」

 

```typescript
// Promise<void>の基本
async function saveData(data: Data): Promise<void> {
  await database.save(data);
  console.log("Saved");
}
```

```typescript
// 型推論でPromise<void>
async function initialize() {
  await loadConfig();
  await connectDB();
  // Promise<void>と推論される
}
```

```typescript
// 実用例
async function processAll(items: Item[]): Promise<void> {
  await Promise.all(items.map(item => saveItem(item)));
  console.log("All items processed");
}
```

## File: 385.txt

# #385「基本まとめ」

 

```typescript
// void型の基本
function log(msg: string): void {
  console.log(msg);
}
```

```typescript
// Promise<void>
async function saveData(data: Data): Promise<void> {
  await database.save(data);
}
```

```typescript
// 実践パターン
type Callback = (data: string) => void;
const handler: Callback = (data) => {
  console.log(data);
};
```

## File: 386.txt

# #386「戻り値なし関数」

 

```typescript
// 戻り値なし関数
function greet(name: string): void {
  console.log(`Hello, ${name}`);
  // return文なし
}
```

```typescript
// 実行時はundefinedを返す
const result = greet("Alice");
console.log(result);  // undefined
// しかし型はvoid
```

```typescript
// 副作用のための関数
function updateCounter(): void {
  counter++;
  render();
}
```

## File: 387.txt

# #387「console.logの戻り値」

 

```typescript
// console.logの型定義
// console.log(message?: any, ...optionalParams: any[]): void
const result = console.log("Hello");
// result: void型
```

```typescript
// 戻り値を使うべきでない
function logAndReturn(msg: string): string {
  return console.log(msg);  // エラー: Type 'void' is not assignable to type 'string'
}
```

```typescript
// 正しい使い方
function process(data: Data): void {
  console.log("Processing:", data);
  // 副作用のみ
}
```

## File: 388.txt

# #388「return undefined」

 

```typescript
// return undefined は許可される
function log1(msg: string): void {
  console.log(msg);
  return undefined;  // OK
}
```

```typescript
// 推奨される書き方
function log2(msg: string): void {
  console.log(msg);
  return;  // より簡潔
}
function log3(msg: string): void {
  console.log(msg);
  // return文なし (最も簡潔)
}
```

```typescript
// 早期リターンでの使用
function validate(value: string): void {
  if (!value) return;  // 推奨
  console.log(value);
}
```

## File: 389.txt

# #389「明示的return」

 

```typescript
// 早期リターン
function processData(data: string | null): void {
  if (data === null) return;  // 早期終了
  console.log(data.toUpperCase());
}
```

```typescript
// 条件分岐での使用
function notify(user: User): void {
  if (!user.notifications) return;
  sendEmail(user.email);
  logNotification(user.id);
}
```

```typescript
// エラーになる例
function invalid(): void {
  return "value";  // エラー: Type 'string' is not assignable to type 'void'
}
```

## File: 390.txt

# #390「エラーハンドリング」

 

```typescript
// throw文の使用
function validateInput(input: string): void {
  if (input.length === 0) {
    throw new Error("Input is required");
  }
  console.log("Valid input:", input);
}
```

```typescript
// try-catchでのエラー処理
function processUser(user: User): void {
  try {
    validateUser(user);
    saveUser(user);
  } catch (error) {
    console.error("Failed to process user:", error);
  }
}
```

```typescript
// 早期リターンとthrowの組み合わせ
function process(data: Data | null): void {
  if (data === null) return;  // 正常な終了
  if (!data.isValid) throw new Error("Invalid data");  // エラー
  console.log(data);
}
```

## File: 391.txt

# #391「throw文」

 

```typescript
// throw文はvoid関数で使用可能
function assert(condition: boolean, message: string): void {
  if (!condition) {
    throw new Error(message);
  }
}
```

```typescript
// バリデーション関数
function validateAge(age: number): void {
  if (age < 0) throw new Error("Age cannot be negative");
  if (age > 150) throw new Error("Age is too large");
  console.log("Age is valid");
}
```

```typescript
// never型との関係
function throwError(message: string): never {
  throw new Error(message);
}
function process(): void {
  throwError("Error");  // OK: neverはvoidに代入可能
}
```

## File: 392.txt

# #392「コールバック関数」

 

```typescript
// コールバック関数の型定義
type Callback = (data: string) => void;
function processAsync(callback: Callback): void {
  setTimeout(() => callback("Done"), 1000);
}
```

```typescript
// 配列のforEach
const items = ["a", "b", "c"];
items.forEach((item: string): void => {
  console.log(item);
});
```

```typescript
// イベントリスナー
button.addEventListener("click", (e: Event): void => {
  console.log("Clicked");
});
```

## File: 393.txt

# #393「イベントハンドラ」

 

```typescript
// DOM イベントハンドラ
const button = document.getElementById("btn");
button?.addEventListener("click", (e: MouseEvent): void => {
  console.log("Clicked at:", e.clientX, e.clientY);
});
```

```typescript
// 型定義
type EventHandler = (event: Event) => void;
const handler: EventHandler = (e) => {
  e.preventDefault();
  console.log("Event handled");
};
```

```typescript
// React イベントハンドラ
const handleClick = (e: React.MouseEvent): void => {
  console.log("Button clicked");
};
<button onClick={handleClick}>Click</button>
```

## File: 394.txt

# #394「forEach()の戻り値」

 

```typescript
// forEach()の型定義
// forEach(callback: (value: T, index: number, array: T[]) => void): void
const items = [1, 2, 3];
const result = items.forEach(item => console.log(item));
console.log(result);  // undefined (void型)
```

```typescript
// コールバックの戻り値は無視される
items.forEach((item): void => {
  console.log(item * 2);
});
```

```typescript
// mapとの違い
const doubled = items.map(x => x * 2);  // 新しい配列を返す
items.forEach(x => console.log(x * 2));  // void、何も返さない
```

## File: 395.txt

# #395「メソッド定義」

 

```typescript
// オブジェクトリテラルのメソッド
const logger = {
  log(message: string): void {
    console.log(`[LOG] ${message}`);
  },
  error(message: string): void {
    console.error(`[ERROR] ${message}`);
  }
};
```

```typescript
// メソッド記法
const utils = {
  log: (msg: string): void => {
    console.log(msg);
  }
};
```

```typescript
// 型定義
type Logger = {
  log(message: string): void;
  warn(message: string): void;
};
```

## File: 396.txt

# #396「クラスメソッド」

 

```typescript
// クラスメソッド
class Counter {
  private count = 0;

  increment(): void {
    this.count++;
  }

  reset(): void {
    this.count = 0;
  }
}
```

```typescript
// 初期化と破棄
class Component {
  initialize(): void {
    console.log("Initializing...");
  }

  destroy(): void {
    console.log("Destroying...");
  }
}
```

```typescript
// イベント処理
class EventEmitter {
  emit(event: string): void {
    console.log(`Event: ${event}`);
  }
}
```

## File: 397.txt

# #397「インターフェースのメソッド」

 

```typescript
// インターフェースでのvoid
interface Lifecycle {
  init(): void;
  destroy(): void;
}
```

```typescript
// 実装クラス
class Component implements Lifecycle {
  init(): void {
    console.log("Initialized");
  }

  destroy(): void {
    console.log("Destroyed");
  }
}
```

```typescript
// イベントハンドラのインターフェース
interface EventListener {
  handleClick(event: MouseEvent): void;
  handleKeyPress(event: KeyboardEvent): void;
}
```

## File: 398.txt

# #398「オーバーロード」

 

```typescript
// オーバーロードでvoid
function process(data: string): string;
function process(data: number): void;
function process(data: string | number): string | void {
  if (typeof data === "string") return data.toUpperCase();
  console.log(data);
}
```

```typescript
// 実用例
function log(message: string): void;
function log(level: string, message: string): void;
function log(levelOrMsg: string, message?: string): void {
  if (message) {
    console.log(`[${levelOrMsg}] ${message}`);
  } else {
    console.log(levelOrMsg);
  }
}
```

```typescript
// コールバックのオーバーロード
function forEach(callback: (item: number) => void): void;
function forEach(start: number, callback: (item: number) => void): void;
function forEach(startOrCb: any, callback?: any): void {
  // 実装
}
```

## File: 399.txt

# #399「アロー関数」

 

```typescript
// アロー関数でのvoid
const log = (msg: string): void => {
  console.log(msg);
};
```

```typescript
// 型定義での使用
type VoidFunction = (x: number) => void;
const double: VoidFunction = (x) => {
  console.log(x * 2);
};
```

```typescript
// 配列メソッドでの使用
const items = [1, 2, 3];
items.forEach((item): void => {
  console.log(item);
});
```

## File: 400.txt

# #400「関数まとめ」

 

```typescript
// 基本的な使い方
function log(msg: string): void {
  console.log(msg);
}
const handler = (e: Event): void => {
  console.log(e);
};
```

```typescript
// クラスメソッド
class Logger {
  log(msg: string): void {
    console.log(msg);
  }
}
```

```typescript
// 実践パターン
async function saveData(data: Data): Promise<void> {
  await database.save(data);
}
type Callback = (result: string) => void;
```

## File: 401.txt

# #401「概念的違い」

 

```typescript
// void: 戻り値を無視
function logMessage(msg: string): void {
  console.log(msg);
  // 戻り値は重要でない
}
```

```typescript
// undefined: undefined値を返す
function findItem(id: number): Item | undefined {
  return items.find(item => item.id === id);
  // undefinedという値を返す可能性がある
}
```

```typescript
// 意図の違い
type Logger = () => void;          // 副作用のみ
type Finder = () => Item | undefined;  // 検索結果
```

## File: 402.txt

# #402「voidは「値を気にしない」」

 

```typescript
// void: 値を気にしない
function updateUI(): void {
  render();
  // 戻り値は使わない
}
```

```typescript
// 戻り値を使おうとするとエラー
function process(): void {
  console.log("Processing");
}
const result: string = process();  // エラー: Type 'void' is not assignable to type 'string'
```

```typescript
// コールバック: 戻り値を無視
type Callback = (data: string) => void;
const handler: Callback = (data) => {
  console.log(data);  // 処理のみ
};
```

## File: 403.txt

# #403「undefinedは「未定義の値」」

 

```typescript
// undefined: 未定義の値
function findUser(id: number): User | undefined {
  return users.find(u => u.id === id);
  // undefined値を返す可能性
}
```

```typescript
// 値として扱う
const user = findUser(1);
if (user !== undefined) {
  console.log(user.name);  // 値をチェック
}
```

```typescript
// オプショナルプロパティ
interface Config {
  timeout?: number;  // number | undefined
}
const config: Config = {};
console.log(config.timeout);  // undefined
```

## File: 404.txt

# #404「変数にundefined代入」

 

```typescript
// void型変数へのundefined代入
let value: void;
value = undefined;  // OK
// value = null;    // strictNullChecks有効時はエラー
// value = 0;       // エラー
```

```typescript
// undefined型変数への代入
let undef: undefined;
undef = undefined;  // OK
// undef = null;    // エラー
```

```typescript
// 実用的な使い方は関数の戻り値型
function doSomething(): void {
  console.log("Done");
}
const result: void = doSomething();  // undefined
```

## File: 405.txt

# #405「undefined型の変数に代入」

 

```typescript
// undefined型変数
let value: undefined;
value = undefined;  // OK
// value = null;    // エラー
// value = 0;       // エラー
```

```typescript
// 実用的な使い方: ユニオン型
let data: string | undefined;
data = "hello";
data = undefined;
```

```typescript
// 関数の戻り値型として
function getValue(): string | undefined {
  if (Math.random() > 0.5) {
    return "value";
  }
  return undefined;
}
```

## File: 406.txt

# #406「実際の戻り値」

 

```typescript
// 型はvoid、実行時はundefined
function log(msg: string): void {
  console.log(msg);
}
const result = log("Hello");
console.log(result);  // undefined
console.log(typeof result);  // "undefined"
```

```typescript
// 型システムではvoidとして扱う
const value: void = log("Test");
// const str: string = log("Test");  // エラー
```

```typescript
// JavaScriptレベルでは同じ
// TypeScript
function f1(): void { }
// JavaScript (トランスパイル後)
function f1() { }  // undefinedを返す
```

## File: 407.txt

# #407「戻り値型がundefined」

 

```typescript
// undefined戻り値型
function getOptionalValue(): number | undefined {
  if (Math.random() > 0.5) {
    return 42;
  }
  return undefined;  // 明示的にundefinedを返す
}
```

```typescript
// 値としてチェック
const value = getOptionalValue();
if (value !== undefined) {
  console.log(value * 2);
}
```

```typescript
// void型との違い
function voidFunc(): void {
  console.log("Done");
  // 戻り値を使うべきでない
}
function undefFunc(): undefined {
  return undefined;  // 値として返す
}
```

## File: 408.txt

# #408「strictNullChecks」

 

```typescript
// strictNullChecks: true
let voidValue: void;
voidValue = undefined;  // OK
// voidValue = null;    // エラー

let undefValue: undefined;
undefValue = undefined;  // OK
// undefValue = null;   // エラー
```

```typescript
// strictNullChecks: false (非推奨)
let value: void;
value = undefined;  // OK
value = null;       // OK (非推奨)
```

```typescript
// 関数の戻り値型
function f1(): void {
  // strictNullChecksに関わらずvoid
}
function f2(): undefined {
  return undefined;
}
```

## File: 409.txt

# #409「互換性」

 

```typescript
// voidにはundefinedを代入可能
let v: void = undefined;  // OK

// undefinedにはvoidを代入可能
let u: undefined = undefined;
let v2: void = u;  // OK
```

```typescript
// 関数の戻り値では違いがある
function returnsVoid(): void {
  return undefined;  // OK
}
function returnsUndefined(): undefined {
  return undefined;  // OK
}
```

```typescript
// 代入の互換性
const f1: () => void = (): undefined => undefined;  // OK
const f2: () => undefined = (): void => {};  // エラー (場合による)
```

## File: 410.txt

# #410「戻り値を使用」

 

```typescript
// void戻り値は使用できない
function log(msg: string): void {
  console.log(msg);
}
const result: string = log("Hello");  // エラー: Type 'void' is not assignable to type 'string'
```

```typescript
// void型変数にしか代入できない
const voidValue: void = log("Test");  // OK
// const strValue: string = log("Test");  // エラー
```

```typescript
// 実行時はundefinedだが型チェックで防げる
function process(): void {
  return;
}
const value = process();
console.log(value);  // undefined (実行時)
// しかし型はvoidなので誤用を防げる
```

## File: 411.txt

# #411「undefined戻り値使用」

 

```typescript
// undefined戻り値は使用可能
function findUser(id: number): User | undefined {
  return users.find(u => u.id === id);
}
const user = findUser(1);
```

```typescript
// 値としてチェック
if (user !== undefined) {
  console.log(user.name);  // User型として扱える
}
```

```typescript
// Optional ChainingとNullish Coalescing
const name = findUser(2)?.name ?? "Unknown";
const email = findUser(3)?.email;
```

## File: 412.txt

# #412「使い分け」

 

```typescript
// void: 副作用のための関数
function saveData(data: Data): void {
  database.save(data);
  // 戻り値を使わない
}
```

```typescript
// undefined: 値を返す可能性
function loadData(id: number): Data | undefined {
  return database.find(id);
  // undefinedという値を返す可能性
}
```

```typescript
// 実践的な使い分け
interface UserService {
  getUser(id: number): User | undefined;  // 検索
  deleteUser(id: number): void;           // 削除
  saveUser(user: User): void;             // 保存
}
```

## File: 413.txt

# #413「パフォーマンス」

 

```typescript
// TypeScript
function voidFunc(): void {
  console.log("void");
}
function undefFunc(): undefined {
  return undefined;
}
```

```typescript
// JavaScript (トランスパイル後は同じ)
function voidFunc() {
  console.log("void");
}
function undefFunc() {
  return undefined;
}
```

```typescript
// 実行時の動作は同じ
console.log(voidFunc());    // undefined
console.log(undefFunc());   // undefined
// パフォーマンス差はなし
```

## File: 414.txt

# #414「コンパイル結果」

 

```typescript
// TypeScript
function f1(): void {
  console.log("void");
}
function f2(): undefined {
  return undefined;
}
```

```typescript
// JavaScript (コンパイル結果)
function f1() {
  console.log("void");
}
function f2() {
  return undefined;
}
```

```typescript
// 型情報は完全に削除される
// TypeScript: function log(msg: string): void
// JavaScript: function log(msg)
```

## File: 415.txt

# #415「比較まとめ」

 

```typescript
// void: 戻り値を無視
function logMessage(msg: string): void {
  console.log(msg);
}
type Logger = (msg: string) => void;
```

```typescript
// undefined: undefined値を返す
function findItem(id: number): Item | undefined {
  return items.find(item => item.id === id);
}
```

```typescript
// 実行時の違い
console.log(logMessage("test"));  // undefined
console.log(findItem(1));         // Item | undefined
// 両方undefinedだが意図が異なる
```

## File: 416.txt

# #416「Promise<void>とは」

 

```typescript
// Promise<void>の基本
async function saveData(data: Data): Promise<void> {
  await database.save(data);
  console.log("Saved");
}
```

```typescript
// 型推論でPromise<void>
async function initialize() {
  await loadConfig();
  await connectDB();
  // Promise<void>と推論される
}
```

```typescript
// 使用例
async function main(): Promise<void> {
  await saveData({ id: 1, name: "Alice" });
  console.log("Complete");
}
```

## File: 417.txt

# #417「async関数のvoid型」

 

```typescript
// 正しい書き方
async function process(): Promise<void> {
  await doSomething();
  console.log("Done");
}
```

```typescript
// エラーになる書き方
// async function process(): void {  // エラー
//   await doSomething();
// }
```

```typescript
// 型推論を使う
async function load() {
  await fetch("/api/data");
  // Promise<void>と推論される
}
```

## File: 418.txt

# #418「return文なし」

 

```typescript
// return文なし
async function saveUser(user: User): Promise<void> {
  await database.save(user);
  console.log("User saved");
}
```

```typescript
// 早期リターン
async function validate(data: Data): Promise<void> {
  if (!data) return;  // 早期終了
  await processData(data);
}
```

```typescript
// return undefinedも許可される
async function log(msg: string): Promise<void> {
  console.log(msg);
  return undefined;  // OK だが不要
}
```

## File: 419.txt

# #419「使用例」

 

```typescript
// データ保存
async function saveData(data: Data): Promise<void> {
  await database.save(data);
  await logActivity("Data saved");
}
```

```typescript
// 初期化処理
async function initialize(): Promise<void> {
  await loadConfig();
  await connectDatabase();
  await startServer();
  console.log("Initialized");
}
```

```typescript
// クリーンアップ
async function cleanup(): Promise<void> {
  await closeConnections();
  await flushLogs();
  console.log("Cleanup complete");
}
```

## File: 420.txt

# #420「then() - 引数なし」

 

```typescript
// then()で完了を待つ
saveData(data).then(() => {
  console.log("Save complete");
});
```

```typescript
// 引数なしのコールバック
initialize().then(() => {
  console.log("Initialized");
}).catch((error) => {
  console.error("Failed:", error);
});
```

```typescript
// async/awaitの方が推奨
async function main() {
  await saveData(data);
  console.log("Save complete");
}
```

## File: 421.txt

# #421「await」

 

```typescript
// awaitで完了を待つ
async function process(): Promise<void> {
  await saveData(data);
  await logActivity("Saved");
  console.log("All done");
}
```

```typescript
// await式の型はvoid
async function example(): Promise<void> {
  const result: void = await initialize();
  // resultは使わない
}
```

```typescript
// 複数の処理を順次実行
async function sequence(): Promise<void> {
  await step1();
  await step2();
  await step3();
}
```

## File: 422.txt

# #422「await式の型」

 

```typescript
// await式の型
async function example(): Promise<void> {
  const result: void = await saveData(data);
  // resultはvoid型
}
```

```typescript
// Promise<T>との比較
async function compare(): Promise<void> {
  const num: number = await Promise.resolve(42);
  const v: void = await Promise.resolve();
}
```

```typescript
// 値として使えない
async function invalid(): Promise<void> {
  const result = await initialize();
  // const str: string = result;  // エラー
}
```

## File: 423.txt

# #423「Promise<void>の連鎖」

 

```typescript
// Promise<void>の連鎖
saveData(data)
  .then(() => logActivity("Saved"))
  .then(() => notify("Complete"))
  .catch((error) => console.error(error));
```

```typescript
// async/awaitで書き直し (推奨)
async function process(): Promise<void> {
  await saveData(data);
  await logActivity("Saved");
  await notify("Complete");
}
```

```typescript
// 連鎖の型
const promise: Promise<void> = initialize()
  .then(() => loadData())
  .then(() => render());
```

## File: 424.txt

# #424「エラーハンドリング」

 

```typescript
// try-catchでエラーハンドリング
async function process(): Promise<void> {
  try {
    await saveData(data);
    await notify("Success");
  } catch (error) {
    console.error("Failed:", error);
  }
}
```

```typescript
// catch()メソッド
saveData(data)
  .then(() => notify("Success"))
  .catch((error) => {
    console.error("Failed:", error);
  });
```

```typescript
// finallyも使える
async function withCleanup(): Promise<void> {
  try {
    await processData();
  } catch (error) {
    console.error(error);
  } finally {
    await cleanup();
  }
}
```

## File: 425.txt

# #425「finally()」

 

```typescript
// finally()メソッド
saveData(data)
  .then(() => console.log("Success"))
  .catch((error) => console.error(error))
  .finally(() => {
    console.log("Cleanup");
  });
```

```typescript
// async/awaitでのfinally
async function process(): Promise<void> {
  try {
    await saveData(data);
  } catch (error) {
    console.error(error);
  } finally {
    await cleanup();
  }
}
```

```typescript
// ローディング表示の例
async function loadData(): Promise<void> {
  showLoading();
  try {
    await fetchData();
  } finally {
    hideLoading();  // 必ず実行
  }
}
```

## File: 426.txt

# #426「並行実行」

 

```typescript
// Promise.all()で並行実行
async function processAll(): Promise<void> {
  await Promise.all([
    saveUser(user1),
    saveUser(user2),
    saveUser(user3)
  ]);
  console.log("All saved");
}
```

```typescript
// 複数の初期化を並行実行
async function initialize(): Promise<void> {
  await Promise.all([
    loadConfig(),
    connectDatabase(),
    startCache()
  ]);
}
```

```typescript
// エラーハンドリング
async function processWithError(): Promise<void> {
  try {
    await Promise.all([task1(), task2(), task3()]);
  } catch (error) {
    console.error("One of the tasks failed:", error);
  }
}
```

## File: 427.txt

# #427「Promise.all()」

 

```typescript
// Promise.all()の戻り値型
async function saveAll(): Promise<void> {
  const results: void[] = await Promise.all([
    saveData(data1),
    saveData(data2),
    saveData(data3)
  ]);
  // resultsは使わない (すべてundefined)
}
```

```typescript
// Promise.allSettled()
async function processAllSettled(): Promise<void> {
  const results = await Promise.allSettled([
    task1(),
    task2(),
    task3()
  ]);
  results.forEach((result) => {
    if (result.status === "rejected") {
      console.error(result.reason);
    }
  });
}
```

```typescript
// Promise.race()
async function timeout(): Promise<void> {
  await Promise.race([
    longTask(),
    delay(5000).then(() => { throw new Error("Timeout"); })
  ]);
}
```

## File: 428.txt

# #428「実践例」

 

```typescript
// API呼び出し
async function updateProfile(profile: Profile): Promise<void> {
  await fetch("/api/profile", {
    method: "PUT",
    body: JSON.stringify(profile)
  });
  console.log("Profile updated");
}
```

```typescript
// バッチ処理
async function processBatch(items: Item[]): Promise<void> {
  for (const item of items) {
    await processItem(item);
  }
  console.log("Batch complete");
}
```

```typescript
// アプリケーション初期化
async function initializeApp(): Promise<void> {
  await loadConfig();
  await connectDatabase();
  await startServices();
  console.log("App initialized");
}
```

## File: 429.txt

# #429「ベストプラクティス」

 

```typescript
// ベストプラクティス1: 明示的な型宣言
async function saveData(data: Data): Promise<void> {
  await database.save(data);
}
```

```typescript
// ベストプラクティス2: エラーハンドリング
async function process(): Promise<void> {
  try {
    await processData();
  } catch (error) {
    console.error("Failed:", error);
    throw error;
  } finally {
    await cleanup();
  }
}
```

```typescript
// ベストプラクティス3: 並行実行の活用
async function processAll(items: Item[]): Promise<void> {
  await Promise.all(items.map(item => saveItem(item)));
}
```

## File: 430.txt

# #430「非同期voidまとめ」

 

```typescript
// Promise<void>の基本
async function saveData(data: Data): Promise<void> {
  await database.save(data);
  console.log("Saved");
}
```

```typescript
// awaitで完了を待つ
async function process(): Promise<void> {
  await saveData(data);
  await logActivity("Complete");
}
```

```typescript
// 並行実行
async function processAll(): Promise<void> {
  await Promise.all([task1(), task2(), task3()]);
  console.log("All complete");
}
```

## File: 431.txt

# #431「ジェネリクスのvoid型」

 

```typescript
// ジェネリクスでvoid型
type Callback<T> = (value: T) => void;
const numberCallback: Callback<number> = (n) => {
  console.log(n);
};
```

```typescript
// Promise<T>でのvoid
async function saveData(): Promise<void> {
  await database.save();
}
```

```typescript
// 関数型のジェネリクス
type Handler<T> = (data: T) => void;
const userHandler: Handler<User> = (user) => {
  console.log(user.name);
};
```

## File: 432.txt

# #432「デフォルト型パラメータ」

 

```typescript
// デフォルト型パラメータ
type Callback<T = void> = (value: T) => void;
const voidCallback: Callback = (v) => {
  console.log("Callback called");
};
```

```typescript
// 型引数を指定
const numberCallback: Callback<number> = (n) => {
  console.log(n * 2);
};
```

```typescript
// 複数の型パラメータ
type Handler<TData = void, TResult = void> =
  (data: TData) => TResult;
const logger: Handler = () => {
  console.log("Log");
};
```

## File: 433.txt

# #433「Callback<void>」

 

```typescript
// Callback型の定義
type Callback<T> = (data: T) => void;
type VoidCallback = Callback<void>;
const onComplete: VoidCallback = () => {
  console.log("Complete");
};
```

```typescript
// イベントハンドラ
type EventHandler<T = void> = (event: T) => void;
const clickHandler: EventHandler<MouseEvent> = (e) => {
  console.log(e.clientX);
};
```

```typescript
// 非同期コールバック
type AsyncCallback<T> = (data: T) => Promise<void>;
const saveCallback: AsyncCallback<User> = async (user) => {
  await database.save(user);
};
```

## File: 434.txt

# #434「条件付き型」

 

```typescript
// 条件付き型でvoid判定
type IsVoid<T> = T extends void ? true : false;
type Test1 = IsVoid<void>;    // true
type Test2 = IsVoid<number>;  // false
```

```typescript
// 戻り値型による分岐
type ResultType<T> = T extends void
  ? { success: true }
  : { success: true; data: T };
```

```typescript
// 実用例
type AsyncResult<T> = T extends void
  ? Promise<void>
  : Promise<{ data: T }>;
async function fetch1(): AsyncResult<void> {
  return;
}
```

## File: 435.txt

# #435「Mapped Types」

 

```typescript
// すべてのメソッドをvoidにする
type VoidMethods<T> = {
  [K in keyof T]: T[K] extends (...args: any[]) => any
    ? (...args: Parameters<T[K]>) => void
    : T[K];
};
```

```typescript
// 実用例
interface Service {
  getData(): Promise<Data>;
  saveData(data: Data): Promise<void>;
}
type MockService = VoidMethods<Service>;
```

```typescript
// プロパティを関数に変換
type ToHandlers<T> = {
  [K in keyof T]: (value: T[K]) => void;
};
type UserHandlers = ToHandlers<User>;
```

## File: 436.txt

# #436「Utility Types」

 

```typescript
// ReturnTypeでvoid抽出
function log(msg: string): void {
  console.log(msg);
}
type LogReturn = ReturnType<typeof log>;  // void
```

```typescript
// Parametersとの組み合わせ
type VoidFunction<T extends any[]> =
  (...args: T) => void;
type Handler = VoidFunction<[string, number]>;
```

```typescript
// Record<K, void>
type EventMap = Record<string, () => void>;
const events: EventMap = {
  click: () => console.log("Click"),
  hover: () => console.log("Hover")
};
```

## File: 437.txt

# #437「型推論」

 

```typescript
// 型推論でvoid
function execute<T>(fn: () => T): T {
  return fn();
}
const result = execute(() => {
  console.log("Done");
});  // void と推論
```

```typescript
// Promiseの型推論
async function process() {
  await doSomething();
  // Promise<void>と推論される
}
```

```typescript
// 明示的な型指定
const result2 = execute<void>(() => {
  console.log("Done");
});
```

## File: 438.txt

# #438「エッジケース」

 

```typescript
// コールバックのvoidは柔軟
type Callback = () => void;
const cb: Callback = () => {
  return 42;  // OK (戻り値は無視される)
};
```

```typescript
// 関数宣言では厳密
function log(): void {
  // return 42;  // エラー: Type 'number' is not assignable to type 'void'
}
```

```typescript
// 実用例: forEachとmap
[1, 2, 3].forEach((x): void => {
  return x * 2;  // OK (戻り値は無視される)
});
```

## File: 439.txt

# #439「実例」

 

```typescript
// イベントエミッター
class EventEmitter<T = void> {
  private listeners: Array<(data: T) => void> = [];

  on(listener: (data: T) => void): void {
    this.listeners.push(listener);
  }

  emit(data: T): void {
    this.listeners.forEach(fn => fn(data));
  }
}
```

```typescript
// 使用例
const emitter = new EventEmitter<string>();
emitter.on((msg) => console.log(msg));
emitter.emit("Hello");
```

```typescript
// void型のエミッター
const voidEmitter = new EventEmitter();
voidEmitter.on(() => console.log("Event"));
voidEmitter.emit();
```

## File: 440.txt

# #440「ジェネリクスまとめ」

 

```typescript
// 基本的なジェネリクス
type Callback<T> = (data: T) => void;
const handler: Callback<User> = (user) => {
  console.log(user.name);
};
```

```typescript
// デフォルト型パラメータ
type Handler<T = void> = (data: T) => void;
const voidHandler: Handler = () => {
  console.log("Done");
};
```

```typescript
// 実践例
class EventEmitter<T = void> {
  on(listener: (data: T) => void): void {
    // イベント登録
  }
}
```

## File: 441.txt

# #441「Angularイベントハンドラ」

 

```typescript
// Angularコンポーネント
@Component({
  selector: 'app-user',
  template: '<button (click)="onClick()">Click</button>'
})
export class UserComponent {
  onClick(): void {
    console.log('Button clicked');
  }
}
```

```typescript
// フォーム送信
@Component({
  selector: 'app-form',
  template: '<form (submit)="onSubmit()">...</form>'
})
export class FormComponent {
  onSubmit(): void {
    console.log('Form submitted');
  }
}
```

```typescript
// 入力イベント
onInput(event: Event): void {
  const value = (event.target as HTMLInputElement).value;
  console.log('Input:', value);
}
```

## File: 442.txt

# #442「(click)="onClick()"」

 

```typescript
// 基本的なクリックハンドラ
@Component({
  selector: 'app-button',
  template: '<button (click)="handleClick()">Click</button>'
})
export class ButtonComponent {
  handleClick(): void {
    console.log('Clicked');
  }
}
```

```typescript
// イベントオブジェクトを受け取る
@Component({
  template: '<button (click)="onClick($event)">Click</button>'
})
export class Component {
  onClick(event: MouseEvent): void {
    console.log('Position:', event.clientX, event.clientY);
  }
}
```

```typescript
// 引数を渡す
@Component({
  template: '<button (click)="delete(user.id)">Delete</button>'
})
export class UserListComponent {
  delete(id: number): void {
    console.log('Deleting user:', id);
  }
}
```

## File: 443.txt

# #443「Observableとvoid型」

 

```typescript
// Observable<void>の基本
import { Observable, Subject } from 'rxjs';

class Service {
  private saveComplete$ = new Subject<void>();

  save(data: Data): void {
    database.save(data);
    this.saveComplete$.next();
  }

  onSaveComplete(): Observable<void> {
    return this.saveComplete$.asObservable();
  }
}
```

```typescript
// 購読
service.onSaveComplete().subscribe(() => {
  console.log('Save completed');
});
```

```typescript
// tap()演算子
data$.pipe(
  tap((): void => {
    console.log('Data received');
  })
).subscribe();
```

## File: 444.txt

# #444「Observable<void>」

 

```typescript
// Subject<void>の作成
import { Subject } from 'rxjs';

const click$ = new Subject<void>();
click$.subscribe(() => {
  console.log('Clicked');
});
click$.next();  // イベント発火
```

```typescript
// fromEventでの使用
import { fromEvent } from 'rxjs';

const button = document.getElementById('btn');
const clicks$: Observable<void> = fromEvent(button!, 'click')
  .pipe(map(() => undefined));
```

```typescript
// finalize()との組み合わせ
import { finalize } from 'rxjs/operators';

operation$.pipe(
  finalize((): void => {
    console.log('Cleanup');
  })
).subscribe();
```

## File: 445.txt

# #445「RxJSオペレータ」

 

```typescript
// tap()オペレータ
import { tap } from 'rxjs/operators';

data$.pipe(
  tap((data): void => {
    console.log('Data:', data);
  }),
  tap((): void => {
    console.log('Processing');
  })
).subscribe();
```

```typescript
// finalize()オペレータ
import { finalize } from 'rxjs/operators';

request$.pipe(
  finalize((): void => {
    console.log('Request complete');
    cleanup();
  })
).subscribe();
```

```typescript
// forEach()メソッド
users$.forEach((user): void => {
  console.log('User:', user.name);
});
```

## File: 446.txt

# #446「Nest.jsコントローラ」

 

```typescript
// Nest.jsコントローラ
import { Controller, Delete, HttpCode } from '@nestjs/common';

@Controller('users')
export class UsersController {
  @Delete(':id')
  @HttpCode(204)
  async delete(@Param('id') id: string): Promise<void> {
    await this.usersService.delete(id);
  }
}
```

```typescript
// POSTでのvoid
@Controller('notifications')
export class NotificationsController {
  @Post('send')
  @HttpCode(204)
  async send(@Body() dto: SendDto): Promise<void> {
    await this.notificationService.send(dto);
  }
}
```

```typescript
// PUTでの更新
@Put(':id')
@HttpCode(204)
async update(@Param('id') id: string, @Body() dto: UpdateDto): Promise<void> {
  await this.service.update(id, dto);
}
```

## File: 447.txt

# #447「ミドルウェア」

 

```typescript
// Nest.jsミドルウェア
import { Injectable, NestMiddleware } from '@nestjs/common';

@Injectable()
export class LoggerMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction): void {
    console.log(`${req.method} ${req.url}`);
    next();
  }
}
```

```typescript
// 認証ミドルウェア
@Injectable()
export class AuthMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction): void {
    if (!req.headers.authorization) {
      throw new UnauthorizedException();
    }
    next();
  }
}
```

```typescript
// 複数の処理
@Injectable()
export class CorsMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction): void {
    res.setHeader('Access-Control-Allow-Origin', '*');
    next();
  }
}
```

## File: 448.txt

# #448「API設計」

 

```typescript
// DELETE API
@Controller('posts')
export class PostsController {
  @Delete(':id')
  @HttpCode(204)
  async delete(@Param('id') id: string): Promise<void> {
    await this.postsService.delete(id);
  }
}
```

```typescript
// 通知送信API
@Controller('notifications')
export class NotificationsController {
  @Post('send')
  @HttpCode(204)
  async send(@Body() dto: NotificationDto): Promise<void> {
    await this.notificationService.send(dto);
  }
}
```

```typescript
// バッチ処理API
@Controller('batch')
export class BatchController {
  @Post('process')
  @HttpCode(202)
  async process(@Body() dto: BatchDto): Promise<void> {
    await this.batchService.enqueue(dto);
  }
}
```

## File: 449.txt

# #449「レスポンス」

 

```typescript
// 204 No Content (推奨)
@Delete(':id')
@HttpCode(204)
async delete(@Param('id') id: string): Promise<void> {
  await this.service.delete(id);
}
```

```typescript
// 202 Accepted (非同期処理)
@Post('process')
@HttpCode(202)
async process(@Body() dto: ProcessDto): Promise<void> {
  await this.queue.add(dto);
}
```

```typescript
// 200 OK (デフォルト)
@Put(':id')
async update(@Param('id') id: string, @Body() dto: UpdateDto): Promise<void> {
  await this.service.update(id, dto);
  // 200 OK、空のレスポンスボディ
}
```

## File: 450.txt

# #450「ベストプラクティス」

 

```typescript
// Angularコンポーネント
@Component({...})
export class UserComponent {
  onClick(): void {
    this.service.save(this.user);
  }
}
```

```typescript
// Nest.jsコントローラ
@Controller('users')
export class UsersController {
  @Delete(':id')
  @HttpCode(204)
  async delete(@Param('id') id: string): Promise<void> {
    await this.usersService.delete(id);
  }
}
```

```typescript
// RxJS Observable
private destroy$ = new Subject<void>();
ngOnDestroy(): void {
  this.destroy$.next();
  this.destroy$.complete();
}
```

## File: 451.txt

# #451「間違い(1) - 戻り値使用」

 

```typescript
// 間違い: void戻り値を使用
function log(msg: string): void {
  console.log(msg);
}
const result: string = log("Hello");  // エラー
```

```typescript
// 間違い: 計算に使用
function update(): void {
  count++;
}
const value = update() + 1;  // エラー
```

```typescript
// 正しい使い方
function process(): void {
  doSomething();
}
process();  // 戻り値を使わない
console.log("Done");
```

## File: 452.txt

# #452「間違い(2) - undefined混同」

 

```typescript
// 間違い: voidとundefinedを混同
function getValue(): void {  // 間違い
  return undefined;
}
const value = getValue();  // voidなので値として使えない
```

```typescript
// 正しい: undefinedを返す
function findItem(id: number): Item | undefined {
  return items.find(item => item.id === id);
}
const item = findItem(1);
if (item !== undefined) {
  console.log(item.name);
}
```

```typescript
// 正しい: voidは副作用用
function logMessage(msg: string): void {
  console.log(msg);
}
logMessage("Hello");  // 戻り値を使わない
```

## File: 453.txt

# #453「間違い(3) - return値」

 

```typescript
// 間違い: void関数で値を返す
function process(data: string): void {
  if (!data) {
    return false;  // エラー: Type 'boolean' is not assignable to type 'void'
  }
  console.log(data);
}
```

```typescript
// 正しい: 戻り値型を変更
function process(data: string): boolean {
  if (!data) {
    return false;
  }
  console.log(data);
  return true;
}
```

```typescript
// 正しい: voidのまま早期リターン
function process(data: string): void {
  if (!data) return;  // OK
  console.log(data);
}
```

## File: 454.txt

# #454「デバッグ(1)」

 

```typescript
// デバッグログの追加
function processData(data: Data): void {
  console.log('processData called with:', data);

  if (!data.isValid) {
    console.log('Invalid data, returning early');
    return;
  }

  console.log('Processing data...');
  doSomething(data);
  console.log('processData completed');
}
```

```typescript
// 条件分岐のデバッグ
function update(user: User): void {
  console.log('update start:', user.id);

  if (user.age < 18) {
    console.log('User is minor');
    return;
  }

  console.log('Updating adult user');
  database.update(user);
}
```

```typescript
// ブレークポイント用のコメント
function save(data: Data): void {
  // デバッグポイント: ここで停止
  validateData(data);
  database.save(data);
}
```

## File: 455.txt

# #455「デバッグ(2)」

 

```typescript
// スパイ関数でのテスト
import { jest } from '@jest/globals';

test('processData calls database.save', () => {
  const spy = jest.spyOn(database, 'save');
  processData(mockData);
  expect(spy).toHaveBeenCalledWith(mockData);
});
```

```typescript
// 副作用の検証
test('update increments counter', () => {
  let counter = 0;
  function increment(): void {
    counter++;
  }
  increment();
  expect(counter).toBe(1);
});
```

```typescript
// モックを使った検証
const mockLogger = {
  log: jest.fn()
};
function process(): void {
  mockLogger.log('Processing');
}
process();
expect(mockLogger.log).toHaveBeenCalledWith('Processing');
```

## File: 456.txt

# #456「リファクタリング」

 

```typescript
// リファクタリング前: 大きな関数
function processUser(user: User): void {
  validateUser(user);
  database.save(user);
  sendEmail(user.email);
  logActivity('User processed');
}
```

```typescript
// リファクタリング後: 分割
function processUser(user: User): void {
  validateAndSave(user);
  notifyUser(user);
  logUserActivity(user);
}

function validateAndSave(user: User): void {
  validateUser(user);
  database.save(user);
}

function notifyUser(user: User): void {
  sendEmail(user.email);
}
```

```typescript
// 単一責任の原則
function logUserActivity(user: User): void {
  logActivity(`User ${user.id} processed`);
}
```

## File: 457.txt

# #457「テスト」

 

```typescript
// 状態変化のテスト
test('increment increases counter', () => {
  let count = 0;
  function increment(): void {
    count++;
  }
  increment();
  expect(count).toBe(1);
});
```

```typescript
// 関数呼び出しのテスト
test('saveUser calls database.save', () => {
  const spy = jest.spyOn(database, 'save');
  saveUser(mockUser);
  expect(spy).toHaveBeenCalledWith(mockUser);
  expect(spy).toHaveBeenCalledTimes(1);
});
```

```typescript
// 例外のテスト
test('validate throws error for invalid data', () => {
  expect(() => {
    validate(invalidData);
  }).toThrow('Invalid data');
});
```

## File: 458.txt

# #458「ドキュメント」

 

```typescript
/**
 * ユーザーをデータベースに保存します
 * @param user 保存するユーザー
 * @returns void
 * @throws {ValidationError} ユーザーデータが無効な場合
 */
function saveUser(user: User): void {
  validateUser(user);
  database.save(user);
}
```

```typescript
/**
 * カウンターをインクリメントします
 * 副作用: グローバル変数 counter を +1 します
 * @returns void
 */
function increment(): void {
  counter++;
}
```

```typescript
/**
 * イベントリスナーを登録します
 * @param event イベント名
 * @param handler イベントハンドラ
 * @returns void
 * @example
 * addEventListener('click', () => console.log('Clicked'));
 */
function addEventListener(event: string, handler: () => void): void {
  listeners.push({ event, handler });
}
```

## File: 459.txt

# #459「ベストプラクティス」

 

```typescript
// ベストプラクティス1: 明示的な型宣言
function logMessage(msg: string): void {
  console.log(msg);
}
async function saveData(data: Data): Promise<void> {
  await database.save(data);
}
```

```typescript
// ベストプラクティス2: 副作用の分離
function calculateTotal(items: Item[]): number {
  return items.reduce((sum, item) => sum + item.price, 0);
}
function displayTotal(items: Item[]): void {
  const total = calculateTotal(items);
  console.log(`Total: ${total}`);
}
```

```typescript
// ベストプラクティス3: 小さな関数
function processUser(user: User): void {
  validate(user);
  save(user);
  notify(user);
}
```

## File: 460.txt

# #460「マスターチェック」

 

```typescript
// 基本的な使い方
function log(msg: string): void {
  console.log(msg);
}
async function save(data: Data): Promise<void> {
  await database.save(data);
}
```

```typescript
// ジェネリクスとの組み合わせ
type Callback<T> = (data: T) => void;
const handler: Callback<User> = (user) => {
  console.log(user.name);
};
```

```typescript
// Angular/Nest.jsでの使用
@Component({...})
class UserComponent {
  onClick(): void {
    this.service.save(this.user);
  }
}
```

## File: 461.txt

# #461「never型とは」

 

```typescript
// never型の基本
function throwError(message: string): never {
  throw new Error(message);
}
```

```typescript
// 無限ループ
function infiniteLoop(): never {
  while (true) {
    console.log("Running...");
  }
}
```

```typescript
// voidとの違い
function voidFunc(): void {
  console.log("Done");
  // 制御が戻る
}
function neverFunc(): never {
  throw new Error("Never returns");
  // 制御が戻らない
}
```

## File: 462.txt

# #462「never型の意味」

 

```typescript
// 例外を投げる: 制御が戻らない
function fail(message: string): never {
  throw new Error(message);
}
```

```typescript
// 無限ループ: 終了しない
function serve(): never {
  while (true) {
    handleRequest();
  }
}
```

```typescript
// 到達不可能性の表現
function process(value: string | number): string {
  if (typeof value === "string") {
    return value.toUpperCase();
  } else if (typeof value === "number") {
    return value.toString();
  }
  return fail("Unreachable");  // never型なので型エラーなし
}
```

## File: 463.txt

# #463「例外を投げる関数」

 

```typescript
// 例外を投げる関数
function throwError(message: string): never {
  throw new Error(message);
}
```

```typescript
// アサーション関数
function assert(condition: boolean, message: string): asserts condition {
  if (!condition) {
    throw new Error(message);
  }
}
```

```typescript
// 使用例
function divide(a: number, b: number): number {
  if (b === 0) {
    throwError("Division by zero");
  }
  return a / b;
}
```

## File: 464.txt

# #464「無限ループ」

 

```typescript
// 無限ループ
function runForever(): never {
  while (true) {
    console.log("Running...");
  }
}
```

```typescript
// サーバーのメインループ
function startServer(): never {
  while (true) {
    const request = waitForRequest();
    handleRequest(request);
  }
}
```

```typescript
// イベントループ
function eventLoop(): never {
  while (true) {
    const event = getNextEvent();
    processEvent(event);
  }
}
```

## File: 465.txt

# #465「never型の宣言」

 

```typescript
// 関数での宣言
function throwError(message: string): never {
  throw new Error(message);
}
```

```typescript
// 変数での宣言 (稀)
let neverValue: never;
// neverValue = 1;  // エラー: すべての値の代入がエラー
```

```typescript
// 型推論
function fail(msg: string) {
  throw new Error(msg);
  // never型と推論される
}
```

## File: 466.txt

# #466「関数の実装」

 

```typescript
// 正しい実装: throw文
function fail(message: string): never {
  throw new Error(message);
}
```

```typescript
// 正しい実装: 無限ループ
function loop(): never {
  while (true) {
    doWork();
  }
}
```

```typescript
// エラーになる実装
function invalid(): never {
  console.log("Error");
  // return;  // エラー: Type 'void' is not assignable to type 'never'
}
```

## File: 467.txt

# #467「return文 - 到達しない」

 

```typescript
// 到達不可能なreturn文
function fail(message: string): never {
  throw new Error(message);
  // return;  // 到達不可能 (書く意味がない)
}
```

```typescript
// 到達可能なreturnはエラー
function invalid(): never {
  if (Math.random() > 0.5) {
    throw new Error("Error");
  }
  // return;  // エラー: 到達可能
}
```

```typescript
// 正しい実装
function abort(message: string): never {
  console.error(message);
  throw new Error(message);
}
```

## File: 468.txt

# #468「変数宣言」

 

```typescript
// never型変数の宣言
let neverValue: never;
// neverValue = 1;        // エラー
// neverValue = "text";   // エラー
// neverValue = null;     // エラー
```

```typescript
// 条件付き型での使用
type NonNullable<T> = T extends null | undefined ? never : T;
type Result = NonNullable<string | null>;  // string
```

```typescript
// ユニオン型からの除外
type Exclude<T, U> = T extends U ? never : T;
type Numbers = Exclude<string | number, string>;  // number
```

## File: 469.txt

# #469「何も代入できない」

 

```typescript
// 何も代入できない
let value: never;
// value = 1;           // エラー
// value = "string";    // エラー
// value = true;        // エラー
// value = null;        // エラー
// value = undefined;   // エラー
```

```typescript
// never関数の戻り値は代入可能
function fail(): never {
  throw new Error("Failed");
}
const result: never = fail();  // OK (実行されない)
```

```typescript
// 型の絞り込み
function check(value: string | number): string {
  if (typeof value === "string") {
    return value;
  } else if (typeof value === "number") {
    return value.toString();
  }
  const exhaustive: never = value;  // 到達不可能
  return exhaustive;
}
```

## File: 470.txt

# #470「void型との違い」

 

```typescript
// void: 正常終了、制御が戻る
function voidFunc(): void {
  console.log("Done");
  // 正常終了
}
```

```typescript
// never: 例外、制御が戻らない
function neverFunc(): never {
  throw new Error("Never returns");
  // 例外で終了
}
```

```typescript
// 使用例での違い
function process(): void {
  voidFunc();      // OK: 次の行に進む
  console.log("After void");
}

function fail(): void {
  neverFunc();     // この後のコードは実行されない
  console.log("Never reached");  // 到達不可能
}
```

## File: 471.txt

# #471「型階層」

 

```typescript
// neverはすべての型に代入可能
function fail(): never {
  throw new Error("Failed");
}

const str: string = fail();      // OK
const num: number = fail();      // OK
const bool: boolean = fail();    // OK
```

```typescript
// 逆は不可能
let value: never;
// value = "string";  // エラー
// value = 123;       // エラー
```

```typescript
// ユニオン型でのnever
type Result = string | never;  // string (neverは消える)
type Empty = never | never;    // never
```

## File: 472.txt

# #472「特殊な性質」

 

```typescript
// ユニオン型での吸収
type Result1 = string | never;     // string
type Result2 = number | never;     // number
type Result3 = never | boolean;    // boolean
```

```typescript
// インターセクション型
type Result4 = string & never;     // never
type Result5 = number & never;     // never
```

```typescript
// 到達不可能性のチェック
function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled case: ${value}`);
}

type Color = "red" | "blue";
function getColor(color: Color): string {
  if (color === "red") return "#ff0000";
  if (color === "blue") return "#0000ff";
  return exhaustiveCheck(color);  // 型エラーで漏れを検出
}
```

## File: 473.txt

# #473「型推論」

 

```typescript
// 型推論でnever
function fail(message: string) {
  throw new Error(message);
  // never型と推論される
}
```

```typescript
// 明示的な型宣言
function abort(message: string): never {
  throw new Error(message);
  // 意図が明確
}
```

```typescript
// 条件分岐での推論
function process(value: string | number) {
  if (typeof value === "string") {
    return value.length;
  } else {
    return value * 2;
  }
  // ここは到達不可能 (never型と推論)
}
```

## File: 474.txt

# #474「ユースケース」

 

```typescript
// 網羅性チェック
function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled case: ${value}`);
}

type Status = "pending" | "success" | "error";
function handleStatus(status: Status): void {
  switch (status) {
    case "pending": return;
    case "success": return;
    case "error": return;
    default: exhaustiveCheck(status);  // すべてカバー
  }
}
```

```typescript
// エラー処理
function assertNonNull<T>(value: T | null): asserts value is T {
  if (value === null) {
    throw new Error("Value is null");
  }
}
```

```typescript
// 条件付き型
type NonNullable<T> = T extends null | undefined ? never : T;
```

## File: 475.txt

# #475「基本まとめ」

 

```typescript
// 例外を投げる
function fail(message: string): never {
  throw new Error(message);
}
```

```typescript
// 網羅性チェック
function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled: ${value}`);
}
```

```typescript
// voidとの違い
function voidFunc(): void {
  console.log("Done");  // 制御が戻る
}
function neverFunc(): never {
  throw new Error("Error");  // 制御が戻らない
}
```

## File: 476.txt

# #476「throw文を含む関数」

 

```typescript
// never型: 必ずthrow
function alwaysThrows(): never {
  throw new Error("Always fails");
}
```

```typescript
// void型: 条件付きthrow
function maybeThrows(condition: boolean): void {
  if (condition) {
    throw new Error("Failed");
  }
  console.log("Success");
}
```

```typescript
// never型: すべてのパスでthrow
function validate(value: unknown): never {
  if (typeof value === "string") {
    throw new Error("String not allowed");
  }
  throw new Error("Invalid type");
}
```

## File: 477.txt

# #477「型注釈」

 

```typescript
// 明示的な型注釈 (推奨)
function throwError(message: string): never {
  throw new Error(message);
}
```

```typescript
// 型推論に任せる
function fail(message: string) {
  throw new Error(message);
  // never型と推論される
}
```

```typescript
// 公開API: 明示的に書く
export function assertNever(value: never): never {
  throw new Error(`Unexpected value: ${value}`);
}
```

## File: 478.txt

# #478「Error型」

 

```typescript
// Error型の基本
function fail(message: string): never {
  throw new Error(message);
}
```

```typescript
// Errorのサブクラス
function invalidType(value: unknown): never {
  throw new TypeError(`Invalid type: ${typeof value}`);
}

function outOfRange(value: number): never {
  throw new RangeError(`Value ${value} is out of range`);
}
```

```typescript
// エラーメッセージとスタックトレース
function validate(data: unknown): never {
  const error = new Error("Validation failed");
  console.error(error.stack);
  throw error;
}
```

## File: 479.txt

# #479「カスタムエラー」

 

```typescript
// カスタムエラーの定義
class ValidationError extends Error {
  constructor(public field: string, message: string) {
    super(message);
    this.name = "ValidationError";
  }
}
```

```typescript
// カスタムエラーを投げる
function validateAge(age: number): never {
  throw new ValidationError("age", "Age must be positive");
}
```

```typescript
// 複数のカスタムエラー
class NotFoundError extends Error {
  constructor(public id: string) {
    super(`Resource ${id} not found`);
    this.name = "NotFoundError";
  }
}

function findUser(id: string): never {
  throw new NotFoundError(id);
}
```

## File: 480.txt

# #480「assertNever関数」

 

```typescript
// assertNever関数の定義
function assertNever(value: never): never {
  throw new Error(`Unexpected value: ${value}`);
}
```

```typescript
// 網羅性チェック
type Status = "pending" | "success" | "error";
function handleStatus(status: Status): void {
  switch (status) {
    case "pending":
      console.log("Pending");
      break;
    case "success":
      console.log("Success");
      break;
    case "error":
      console.log("Error");
      break;
    default:
      assertNever(status);  // すべてカバー
  }
}
```

```typescript
// 型追加時のエラー検出
type Color = "red" | "blue" | "green";
function getColor(color: Color): string {
  switch (color) {
    case "red": return "#ff0000";
    case "blue": return "#0000ff";
    default: return assertNever(color);  // greenが未処理で型エラー
  }
}
```

## File: 481.txt

# #481「使用例」

 

```typescript
// バリデーション
function validatePositive(value: number): void {
  if (value <= 0) {
    throwError("Value must be positive");
  }
}

function throwError(message: string): never {
  throw new Error(message);
}
```

```typescript
// アサーション
function assertDefined<T>(value: T | undefined): asserts value is T {
  if (value === undefined) {
    throw new Error("Value is undefined");
  }
}
```

```typescript
// エラーハンドラ
function handleError(error: unknown): never {
  console.error("Fatal error:", error);
  process.exit(1);
}
```

## File: 482.txt

# #482「型安全なエラーハンドリング」

 

```typescript
// 型安全なエラー処理
function processData(data: string | null): string {
  if (data === null) {
    throwError("Data is null");
    // この後のコードは実行されない
  }
  return data.toUpperCase();  // data: string
}

function throwError(message: string): never {
  throw new Error(message);
}
```

```typescript
// カスタムエラーとの組み合わせ
class InvalidDataError extends Error {
  constructor(public data: unknown) {
    super("Invalid data");
  }
}

function validateData(data: unknown): never {
  throw new InvalidDataError(data);
}
```

```typescript
// 型の絞り込み
function ensure<T>(value: T | null, message: string): T {
  if (value === null) {
    throwError(message);
  }
  return value;  // T型として返せる
}
```

## File: 483.txt

# #483「try-catch」

 

```typescript
// never型関数のtry-catch
function riskyOperation(): never {
  throw new Error("Operation failed");
}

try {
  riskyOperation();
  console.log("Never reached");
} catch (error) {
  console.error("Caught:", error);
}
```

```typescript
// カスタムエラーのキャッチ
class ValidationError extends Error {}

function validate(data: unknown): never {
  throw new ValidationError("Invalid");
}

try {
  validate(data);
} catch (error) {
  if (error instanceof ValidationError) {
    console.error("Validation failed");
  }
}
```

```typescript
// エラーの型チェック
try {
  throwError("Error");
} catch (error) {
  if (error instanceof Error) {
    console.error(error.message);
  }
}
```

## File: 484.txt

# #484「スタックトレース」

 

```typescript
// スタックトレースの表示
function fail(message: string): never {
  const error = new Error(message);
  console.error(error.stack);
  throw error;
}
```

```typescript
// カスタムエラーのスタックトレース
class AppError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "AppError";
    Error.captureStackTrace(this, AppError);
  }
}

function throwAppError(): never {
  throw new AppError("Application error");
}
```

```typescript
// スタックトレースの利用
try {
  fail("Something went wrong");
} catch (error) {
  if (error instanceof Error) {
    console.error("Stack trace:", error.stack);
  }
}
```

## File: 485.txt

# #485「デバッグ」

 

```typescript
// デバッグログ付きエラー関数
function fail(message: string, context?: unknown): never {
  console.error("Error context:", context);
  console.error("Stack trace:");
  console.trace();
  throw new Error(message);
}
```

```typescript
// 条件付きデバッグ
const DEBUG = true;

function assertNever(value: never): never {
  if (DEBUG) {
    console.error("Unexpected value:", value);
    console.error("Type:", typeof value);
  }
  throw new Error(`Unhandled case: ${value}`);
}
```

```typescript
// デバッガでの停止
function throwError(message: string): never {
  debugger;  // ここで停止
  throw new Error(message);
}
```

## File: 486.txt

# #486「エラー関数設計」

 

```typescript
// 良い設計: 明確な名前とメッセージ
function throwValidationError(field: string, reason: string): never {
  throw new Error(`Validation failed for ${field}: ${reason}`);
}
```

```typescript
// コンテキスト情報を含む
function assertPositive(value: number, name: string): void {
  if (value <= 0) {
    throwError(`${name} must be positive, got ${value}`);
  }
}

function throwError(message: string): never {
  throw new Error(message);
}
```

```typescript
// 再利用可能な設計
function createError(type: string, message: string): never {
  throw new Error(`[${type}] ${message}`);
}

function validateUser(user: unknown): void {
  if (!user) {
    createError("VALIDATION", "User is required");
  }
}
```

## File: 487.txt

# #487「パターン」

 

```typescript
// パターン1: 網羅性チェック
function assertNever(value: never): never {
  throw new Error(`Unhandled case: ${value}`);
}

type Action = "create" | "update" | "delete";
function handle(action: Action): void {
  switch (action) {
    case "create": return;
    case "update": return;
    case "delete": return;
    default: assertNever(action);
  }
}
```

```typescript
// パターン2: アサーション
function assert(condition: boolean, message: string): asserts condition {
  if (!condition) throw new Error(message);
}
```

```typescript
// パターン3: エラーヘルパー
function notImplemented(feature: string): never {
  throw new Error(`${feature} is not implemented`);
}
```

## File: 488.txt

# #488「エラーバウンダリ」

 

```typescript
// エラーバウンダリの基本
function safeExecute<T>(fn: () => T, fallback: T): T {
  try {
    return fn();
  } catch (error) {
    console.error("Error caught:", error);
    return fallback;
  }
}
```

```typescript
// 非同期エラーバウンダリ
async function safeAsync<T>(
  fn: () => Promise<T>,
  fallback: T
): Promise<T> {
  try {
    return await fn();
  } catch (error) {
    console.error("Async error:", error);
    return fallback;
  }
}
```

```typescript
// Reactエラーバウンダリ
class ErrorBoundary extends React.Component {
  componentDidCatch(error: Error): void {
    console.error("Component error:", error);
  }
  render() {
    return this.props.children;
  }
}
```

## File: 489.txt

# #489「ベストプラクティス」

 

```typescript
// ベストプラクティス1: 明示的な型宣言
function throwError(message: string): never {
  throw new Error(message);
}

function assertNever(value: never): never {
  throw new Error(`Unexpected: ${value}`);
}
```

```typescript
// ベストプラクティス2: 詳細なエラー
class ValidationError extends Error {
  constructor(public field: string, message: string) {
    super(`${field}: ${message}`);
  }
}

function validate(field: string, value: unknown): never {
  throw new ValidationError(field, "Invalid value");
}
```

```typescript
// ベストプラクティス3: 網羅性チェック
type Status = "idle" | "loading" | "success" | "error";
function handleStatus(status: Status): void {
  switch (status) {
    case "idle": return;
    case "loading": return;
    case "success": return;
    case "error": return;
    default: assertNever(status);
  }
}
```

## File: 490.txt

# #490「例外まとめ」

 

```typescript
// 例外を投げる関数
function fail(message: string): never {
  throw new Error(message);
}
```

```typescript
// 網羅性チェック
function assertNever(value: never): never {
  throw new Error(`Unhandled: ${value}`);
}

type Action = "save" | "delete";
function handle(action: Action): void {
  switch (action) {
    case "save": return;
    case "delete": return;
    default: assertNever(action);
  }
}
```

```typescript
// カスタムエラーとtry-catch
class AppError extends Error {}

try {
  throw new AppError("Error");
} catch (error) {
  if (error instanceof AppError) {
    console.error(error.message);
  }
}
```

## File: 491.txt

# #491「無限ループ関数」

 

```typescript
// 無限ループ関数
function runForever(): never {
  while (true) {
    console.log("Running...");
    processTask();
  }
}
```

```typescript
// サーバーのメインループ
function startServer(): never {
  while (true) {
    const request = waitForRequest();
    handleRequest(request);
  }
}
```

```typescript
// イベントループ
function eventLoop(): never {
  while (true) {
    const event = getNextEvent();
    if (event) {
      processEvent(event);
    }
  }
}
```

## File: 492.txt

# #492「while(true)」

 

```typescript
// while(true)の基本
function loop(): never {
  while (true) {
    doWork();
  }
}
```

```typescript
// ポーリングループ
function poll(): never {
  while (true) {
    const data = fetchData();
    if (data) {
      process(data);
    }
    sleep(1000);
  }
}
```

```typescript
// 条件付き処理
function monitor(): never {
  while (true) {
    const status = checkStatus();
    if (status === "error") {
      handleError();
    }
    await delay(5000);
  }
}
```

## File: 493.txt

# #493「型注釈」

 

```typescript
// 明示的な型注釈 (推奨)
function startServer(): never {
  while (true) {
    handleRequest();
  }
}
```

```typescript
// 型推論に任せる
function loop() {
  while (true) {
    doWork();
  }
  // never型と推論される
}
```

```typescript
// 公開API: 明示的に書く
export function runEventLoop(): never {
  while (true) {
    const event = getEvent();
    processEvent(event);
  }
}
```

## File: 494.txt

# #494「使用例」

 

```typescript
// WebSocketサーバー
function runWebSocketServer(): never {
  const server = createServer();
  while (true) {
    const connection = server.accept();
    handleConnection(connection);
  }
}
```

```typescript
// タスクキュー処理
function processQueue(): never {
  while (true) {
    const task = queue.dequeue();
    if (task) {
      executeTask(task);
    } else {
      sleep(100);
    }
  }
}
```

```typescript
// 監視プロセス
function watchFiles(): never {
  while (true) {
    const changes = detectChanges();
    if (changes.length > 0) {
      handleChanges(changes);
    }
    await delay(1000);
  }
}
```

## File: 495.txt

# #495「イベントループ」

 

```typescript
// イベントループの基本
function eventLoop(): never {
  while (true) {
    const event = waitForEvent();
    dispatchEvent(event);
  }
}
```

```typescript
// 複数のイベントソース
function mainLoop(): never {
  while (true) {
    const events = pollEvents();
    for (const event of events) {
      handleEvent(event);
    }
  }
}
```

```typescript
// 優先度付きイベント処理
function priorityLoop(): never {
  while (true) {
    const event = getHighestPriorityEvent();
    if (event) {
      processEvent(event);
    } else {
      idle();
    }
  }
}
```

## File: 496.txt

# #496「サーバープロセス」

 

```typescript
// HTTPサーバーのメインループ
function startHttpServer(port: number): never {
  const server = createServer(port);
  while (true) {
    const request = server.accept();
    handleHttpRequest(request);
  }
}
```

```typescript
// TCPサーバー
function runTcpServer(): never {
  const listener = listen(8080);
  while (true) {
    const socket = listener.accept();
    processConnection(socket);
  }
}
```

```typescript
// ワーカープロセス
function workerProcess(): never {
  console.log("Worker started");
  while (true) {
    const job = fetchJob();
    if (job) {
      executeJob(job);
    } else {
      sleep(1000);
    }
  }
}
```

## File: 497.txt

# #497「型推論」

 

```typescript
// never型と推論される
function loop1() {
  while (true) {
    doWork();
  }
  // never型
}
```

```typescript
// void型と推論される
function loop2() {
  while (true) {
    doWork();
    if (shouldStop()) {
      break;  // 終了可能
    }
  }
  // void型
}
```

```typescript
// 条件次第で変わる
function loop3(forever: boolean) {
  while (true) {
    process();
    if (!forever) return;
  }
  // void型 (条件付き終了)
}
```

## File: 498.txt

# #498「リスク」

 

```typescript
// 悪い例: CPU を占有
function badLoop(): never {
  while (true) {
    // CPU 100%
  }
}
```

```typescript
// 良い例: 適切な待機
function goodLoop(): never {
  while (true) {
    doWork();
    sleep(100);  // CPU を解放
  }
}
```

```typescript
// 非同期での待機
async function asyncLoop(): never {
  while (true) {
    await processTask();
    await delay(1000);  // イベントループを解放
  }
}
```

## File: 499.txt

# #499「ベストプラクティス」

 

```typescript
// ベストプラクティス1: 明示的な型と待機
function serverLoop(): never {
  console.log("Server started");
  while (true) {
    const request = waitForRequest();
    handleRequest(request);
  }
}
```

```typescript
// ベストプラクティス2: エラーハンドリング
function safeLoop(): never {
  while (true) {
    try {
      processTask();
    } catch (error) {
      console.error("Error:", error);
    }
    await delay(1000);
  }
}
```

```typescript
// ベストプラクティス3: 終了シグナル
let shouldRun = true;
function gracefulLoop(): void {
  while (shouldRun) {
    doWork();
  }
  cleanup();
}
process.on('SIGTERM', () => { shouldRun = false; });
```

## File: 500.txt

# #500「無限ループまとめ」

 

```typescript
// 基本的な無限ループ
function eventLoop(): never {
  while (true) {
    const event = getEvent();
    processEvent(event);
  }
}
```

```typescript
// 適切な待機
function serverLoop(): never {
  while (true) {
    const request = waitForRequest();
    handleRequest(request);
    await delay(100);  // CPU解放
  }
}
```

```typescript
// エラーハンドリング
function safeLoop(): never {
  while (true) {
    try {
      processTask();
    } catch (error) {
      console.error(error);
    }
  }
}
```

## File: 501.txt

# #501「網羅性チェックとは」

 

```typescript
// 網羅性チェックの基本
type Status = "pending" | "success" | "error";

function handleStatus(status: Status): void {
  switch (status) {
    case "pending":
      console.log("Pending");
      break;
    case "success":
      console.log("Success");
      break;
    case "error":
      console.log("Error");
      break;
    default:
      const exhaustive: never = status;  // すべてカバー
  }
}
```

```typescript
// 処理漏れがある場合
function incomplete(status: Status): void {
  switch (status) {
    case "pending":
      return;
    case "success":
      return;
    // errorが未処理
    default:
      const exhaustive: never = status;  // 型エラー！
  }
}
```

```typescript
// 型追加時の検出
type Color = "red" | "blue" | "green";
function getHex(color: Color): string {
  switch (color) {
    case "red": return "#ff0000";
    case "blue": return "#0000ff";
    default: return assertNever(color);  // greenで型エラー
  }
}
```

## File: 502.txt

# #502「switch文の網羅性」

 

```typescript
// switch文の網羅性チェック
type Action = "create" | "update" | "delete";

function handleAction(action: Action): void {
  switch (action) {
    case "create":
      console.log("Creating");
      break;
    case "update":
      console.log("Updating");
      break;
    case "delete":
      console.log("Deleting");
      break;
    default:
      const exhaustive: never = action;
  }
}
```

```typescript
// 関数で再利用
function assertNever(value: never): never {
  throw new Error(`Unhandled case: ${value}`);
}

function process(action: Action): void {
  switch (action) {
    case "create": return;
    case "update": return;
    case "delete": return;
    default: assertNever(action);
  }
}
```

```typescript
// 型追加時の検出
type Status = "idle" | "loading" | "success";
function handle(status: Status): void {
  switch (status) {
    case "idle": return;
    case "loading": return;
    // successが未処理で型エラー
    default: assertNever(status);
  }
}
```

## File: 503.txt

# #503「exhaustive check関数」

 

```typescript
// exhaustive check関数の定義
function assertNever(value: never): never {
  throw new Error(`Unexpected value: ${value}`);
}
```

```typescript
// 使用例
type Shape = "circle" | "square" | "triangle";

function getArea(shape: Shape): number {
  switch (shape) {
    case "circle": return Math.PI;
    case "square": return 1;
    case "triangle": return 0.5;
    default: return assertNever(shape);
  }
}
```

```typescript
// カスタムエラーメッセージ
function exhaustiveCheck(value: never, message?: string): never {
  throw new Error(
    message || `Unhandled discriminated union member: ${JSON.stringify(value)}`
  );
}
```

## File: 504.txt

# #504「Union型の網羅性」

 

```typescript
// Union型の網羅性チェック
type Value = string | number | boolean;

function process(value: Value): string {
  if (typeof value === "string") {
    return value.toUpperCase();
  } else if (typeof value === "number") {
    return value.toString();
  } else if (typeof value === "boolean") {
    return value ? "true" : "false";
  }
  const exhaustive: never = value;
  return exhaustive;
}
```

```typescript
// クラスのUnion型
class Cat { meow() {} }
class Dog { bark() {} }
type Animal = Cat | Dog;

function makeSound(animal: Animal): void {
  if (animal instanceof Cat) {
    animal.meow();
  } else if (animal instanceof Dog) {
    animal.bark();
  } else {
    assertNever(animal);
  }
}
```

```typescript
// リテラル型のUnion
type Direction = "north" | "south" | "east" | "west";
function move(direction: Direction): void {
  if (direction === "north") return;
  if (direction === "south") return;
  if (direction === "east") return;
  if (direction === "west") return;
  assertNever(direction);
}
```

## File: 505.txt

# #505「判別Union型」

 

```typescript
// 判別Union型
type Circle = { kind: "circle"; radius: number };
type Square = { kind: "square"; size: number };
type Triangle = { kind: "triangle"; base: number; height: number };
type Shape = Circle | Square | Triangle;

function getArea(shape: Shape): number {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "square":
      return shape.size ** 2;
    case "triangle":
      return (shape.base * shape.height) / 2;
    default:
      return assertNever(shape);
  }
}
```

```typescript
// Reduxアクション
type Action =
  | { type: "increment" }
  | { type: "decrement" }
  | { type: "set"; payload: number };

function reducer(state: number, action: Action): number {
  switch (action.type) {
    case "increment": return state + 1;
    case "decrement": return state - 1;
    case "set": return action.payload;
    default: return assertNever(action);
  }
}
```

```typescript
// イベント
type Event =
  | { type: "click"; x: number; y: number }
  | { type: "keypress"; key: string };

function handleEvent(event: Event): void {
  switch (event.type) {
    case "click":
      console.log(`Clicked at ${event.x}, ${event.y}`);
      break;
    case "keypress":
      console.log(`Key: ${event.key}`);
      break;
    default:
      assertNever(event);
  }
}
```

## File: 506.txt

# #506 「if-else文の網羅性」

 

```typescript
type Status = 'pending' | 'success' | 'error';

function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled: ${value}`);
}
```

```typescript
function handleStatus(status: Status): string {
  if (status === 'pending') return '処理中';
  else if (status === 'success') return '成功';
  else if (status === 'error') return 'エラー';
  else return exhaustiveCheck(status); // never型でチェック
}
```

```typescript
// ケース漏れ時は型エラー
type Status = 'pending' | 'success' | 'error' | 'timeout';

function handle(status: Status) {
  if (status === 'pending') return '処理中';
  else return exhaustiveCheck(status); // エラー！
}
```

## File: 507.txt

# #507 「到達不可能コード検出」

 

```typescript
function process(value: string | number) {
  if (typeof value === 'string') return value.toUpperCase();
  else if (typeof value === 'number') return value * 2;
  else {
    value; // never型
    return 0; // 到達不可能コード
  }
}
```

```typescript
type Status = 'success' | 'error';

function handle(status: Status) {
  if (status === 'success') return 'OK';
  if (status === 'error') return 'NG';
  console.log(status); // 到達不可能（never型）
}
```

```typescript
function neverReturn(): never {
  throw new Error('Error');
}

function example() {
  neverReturn();
  console.log('到達不可能'); // エラー検出
}
```

## File: 508.txt

# #508 「never型での型エラー」

 

```typescript
type Action = 'create' | 'update' | 'delete';

function handleAction(action: Action) {
  if (action === 'create') return 'Created';
  if (action === 'update') return 'Updated';
  // deleteケースがない
  const check: never = action; // 型エラー！
}
```

```typescript
// ケース追加時の型エラー
type Action = 'create' | 'update' | 'delete' | 'archive';

function handle(action: Action) {
  if (action === 'create') return 'Created';
  const check: never = action; // 型エラー！
}
```

```typescript
// 正しい網羅的な実装
function handleAll(action: Action) {
  if (action === 'create') return 'Created';
  if (action === 'update') return 'Updated';
  if (action === 'delete') return 'Deleted';
  const check: never = action; // OK
}
```

## File: 509.txt

# #509 「実践例(1)」

 

```typescript
type Action =
  | { type: 'increment'; payload: number }
  | { type: 'decrement'; payload: number }
  | { type: 'reset' };
```

```typescript
function reducer(state: number, action: Action): number {
  if (action.type === 'increment') return state + action.payload;
  if (action.type === 'decrement') return state - action.payload;
  if (action.type === 'reset') return 0;
  const check: never = action; // 網羅性チェック
  return state;
}
```

```typescript
// アクション追加時
type Action =
  | { type: 'increment'; payload: number }
  | { type: 'multiply'; payload: number }; // 新規追加

// reducerで型エラーが発生し、実装漏れを検出
```

## File: 510.txt

# #510 「実践例(2)」

 

```typescript
type DomainEvent =
  | { type: 'UserCreated'; userId: string }
  | { type: 'UserUpdated'; userId: string; data: any }
  | { type: 'UserDeleted'; userId: string };
```

```typescript
class EventHandler {
  handle(event: DomainEvent): void {
    if (event.type === 'UserCreated') this.onCreate(event);
    else if (event.type === 'UserUpdated') this.onUpdate(event);
    else if (event.type === 'UserDeleted') this.onDelete(event);
    else this.exhaustiveCheck(event);
  }

  exhaustiveCheck(value: never): never {
    throw new Error(`Unhandled: ${value}`);
  }
}
```

```typescript
// Angular HTTPレスポンス処理
type ApiResponse<T> =
  | { status: 'success'; data: T }
  | { status: 'error'; error: string };

function process<T>(res: ApiResponse<T>) {
  if (res.status === 'success') return res.data;
  if (res.status === 'error') throw new Error(res.error);
  const check: never = res;
}
```

## File: 511.txt

# #511 「型ガード」

 

```typescript
type Shape =
  | { kind: 'circle'; radius: number }
  | { kind: 'square'; size: number }
  | { kind: 'rectangle'; width: number; height: number };
```

```typescript
function area(shape: Shape): number {
  if (shape.kind === 'circle') {
    return Math.PI * shape.radius ** 2;
  } else if (shape.kind === 'square') {
    return shape.size ** 2;
  } else if (shape.kind === 'rectangle') {
    return shape.width * shape.height;
  }
  const check: never = shape; // 網羅性チェック
  return 0;
}
```

```typescript
// カスタム型ガード
function isCircle(shape: Shape): shape is Extract<Shape, { kind: 'circle' }> {
  return shape.kind === 'circle';
}

function process(shape: Shape) {
  if (isCircle(shape)) return shape.radius;
  // 残りの型で処理
}
```

## File: 512.txt

# #512 「型の絞り込み」

 

```typescript
type Response =
  | { status: 200; data: string }
  | { status: 404; error: string }
  | { status: 500; error: string };
```

```typescript
function handle(res: Response) {
  if (res.status === 200) {
    console.log(res.data); // { status: 200; data: string }
  } else if (res.status === 404) {
    console.log(res.error); // { status: 404; error: string }
  } else if (res.status === 500) {
    console.log(res.error); // { status: 500; error: string }
  }
  const check: never = res; // 完全に絞り込まれた
}
```

```typescript
// 段階的な絞り込み
function process(value: string | number | boolean) {
  if (typeof value === 'string') {
    return value.toUpperCase(); // string型
  } else if (typeof value === 'number') {
    return value * 2; // number型
  } else {
    return !value; // boolean型
  }
}
```

## File: 513.txt

# #513 「else節」

 

```typescript
type State = 'idle' | 'loading' | 'success' | 'error';

function getLabel(state: State): string {
  if (state === 'idle') return '待機中';
  else if (state === 'loading') return '読込中';
  else if (state === 'success') return '成功';
  else if (state === 'error') return 'エラー';
  else {
    const check: never = state; // never型
    return check;
  }
}
```

```typescript
// else節での型エラー検出
type State = 'idle' | 'loading' | 'success' | 'error' | 'timeout';

function getLabel(state: State): string {
  if (state === 'idle') return '待機中';
  else {
    const check: never = state; // 型エラー！
    return '';
  }
}
```

```typescript
// 正しい実装
function getLabel(state: State): string {
  switch (state) {
    case 'idle': return '待機中';
    case 'loading': return '読込中';
    case 'success': return '成功';
    case 'error': return 'エラー';
    case 'timeout': return 'タイムアウト';
  }
}
```

## File: 514.txt

# #514 「default節」

 

```typescript
type Direction = 'north' | 'south' | 'east' | 'west';

function move(dir: Direction): [number, number] {
  switch (dir) {
    case 'north': return [0, 1];
    case 'south': return [0, -1];
    case 'east': return [1, 0];
    case 'west': return [-1, 0];
    default:
      const check: never = dir; // never型
      throw new Error(`Invalid: ${check}`);
  }
}
```

```typescript
// ケース漏れの検出
type Direction = 'north' | 'south' | 'east' | 'west' | 'center';

function move(dir: Direction) {
  switch (dir) {
    case 'north': return [0, 1];
    case 'south': return [0, -1];
    default:
      const check: never = dir; // 型エラー！
      throw new Error();
  }
}
```

```typescript
// exhaustiveCheck関数の利用
function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled: ${value}`);
}

function move(dir: Direction) {
  switch (dir) {
    case 'north': return [0, 1];
    default: return exhaustiveCheck(dir);
  }
}
```

## File: 515.txt

# #515 「コンパイラ最適化」

 

```typescript
// コンパイラが最適化可能
type Digit = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9;

function isEven(n: Digit): boolean {
  switch (n) {
    case 0: case 2: case 4: case 6: case 8:
      return true;
    case 1: case 3: case 5: case 7: case 9:
      return false;
    default:
      const check: never = n; // 最適化のヒント
      return false;
  }
}
```

```typescript
// 分岐予測の改善
type Priority = 'high' | 'medium' | 'low';

function getScore(p: Priority): number {
  if (p === 'high') return 3;
  if (p === 'medium') return 2;
  if (p === 'low') return 1;
  const check: never = p; // 到達不可能
  return 0; // デッドコード削除可能
}
```

```typescript
// インライン化の促進
type Bool = true | false;

function not(b: Bool): boolean {
  if (b === true) return false;
  if (b === false) return true;
  const check: never = b;
  throw new Error(); // 削除可能
}
```

## File: 516.txt

# #516 「静的解析」

 

```typescript
// 静的解析による網羅性検証
type HttpMethod = 'GET' | 'POST' | 'PUT' | 'DELETE';

function validate(method: HttpMethod): boolean {
  if (method === 'GET') return true;
  if (method === 'POST') return true;
  const check: never = method; // 静的に検出
  return false;
}
```

```typescript
// 制御フロー分析
function process(value: string | null): string {
  if (value === null) {
    return 'null';
  }
  return value.toUpperCase(); // nullチェック済みと解析
}
```

```typescript
// データフロー分析
type User = { name: string; age?: number };

function greet(user: User): string {
  if (user.age !== undefined) {
    return `${user.name} (${user.age})`;
  }
  return user.name; // ageはundefinedと解析
}
```

## File: 517.txt

# #517 「型安全性向上」

 

```typescript
// 型安全なステートマシン
type State = 'idle' | 'loading' | 'success' | 'error';
type Event = 'start' | 'complete' | 'fail' | 'reset';

function transition(state: State, event: Event): State {
  if (state === 'idle' && event === 'start') return 'loading';
  if (state === 'loading' && event === 'complete') return 'success';
  if (state === 'loading' && event === 'fail') return 'error';
  if (event === 'reset') return 'idle';
  return state;
}
```

```typescript
// 型安全なイベントハンドラ
type AppEvent =
  | { type: 'click'; x: number; y: number }
  | { type: 'keypress'; key: string }
  | { type: 'scroll'; delta: number };

function handle(event: AppEvent): void {
  if (event.type === 'click') console.log(event.x, event.y);
  else if (event.type === 'keypress') console.log(event.key);
  else if (event.type === 'scroll') console.log(event.delta);
  else {
    const check: never = event;
  }
}
```

```typescript
// 型安全なルーティング
type Route = '/home' | '/about' | '/contact';

function navigate(route: Route): void {
  if (route === '/home') loadHome();
  else if (route === '/about') loadAbout();
  else if (route === '/contact') loadContact();
  else {
    const check: never = route;
  }
}
```

## File: 518.txt

# #518 「ベストプラクティス」

 

```typescript
// ヘルパー関数の定義
function assertNever(value: never, message?: string): never {
  throw new Error(message ?? `Unexpected value: ${value}`);
}

function exhaustiveCheck(value: never): never {
  assertNever(value, 'Unhandled case');
}
```

```typescript
// 判別Union型の活用
type Result<T, E> =
  | { success: true; value: T }
  | { success: false; error: E };

function unwrap<T, E>(result: Result<T, E>): T {
  if (result.success) return result.value;
  else if (!result.success) throw result.error;
  else return exhaustiveCheck(result);
}
```

```typescript
// switch文での統一パターン
type Action = 'save' | 'load' | 'delete';

function execute(action: Action): void {
  switch (action) {
    case 'save': return save();
    case 'load': return load();
    case 'delete': return remove();
    default: return exhaustiveCheck(action);
  }
}
```

## File: 519.txt

# #519 「パターン集」

 

```typescript
// Reducerパターン
type CounterAction =
  | { type: 'increment'; by: number }
  | { type: 'decrement'; by: number }
  | { type: 'reset' };

function counterReducer(state: number, action: CounterAction): number {
  switch (action.type) {
    case 'increment': return state + action.by;
    case 'decrement': return state - action.by;
    case 'reset': return 0;
    default: return exhaustiveCheck(action);
  }
}
```

```typescript
// Commandパターン
interface Command<T = void> {
  execute(): T;
}

type AppCommand =
  | { kind: 'save'; data: string }
  | { kind: 'load'; id: number }
  | { kind: 'delete'; id: number };

function executeCommand(cmd: AppCommand): void {
  if (cmd.kind === 'save') save(cmd.data);
  else if (cmd.kind === 'load') load(cmd.id);
  else if (cmd.kind === 'delete') remove(cmd.id);
  else exhaustiveCheck(cmd);
}
```

```typescript
// Stateパターン
type ConnectionState =
  | { status: 'disconnected' }
  | { status: 'connecting'; attempt: number }
  | { status: 'connected'; sessionId: string };

function getLabel(state: ConnectionState): string {
  switch (state.status) {
    case 'disconnected': return '切断';
    case 'connecting': return `接続中(${state.attempt})`;
    case 'connected': return `接続済(${state.sessionId})`;
    default: return exhaustiveCheck(state);
  }
}
```

## File: 520.txt

# #520 「網羅性まとめ」

 

```typescript
// 網羅性チェックの基本形
type Status = 'pending' | 'success' | 'error';

function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled: ${value}`);
}

function handle(status: Status): string {
  if (status === 'pending') return '処理中';
  if (status === 'success') return '成功';
  if (status === 'error') return 'エラー';
  return exhaustiveCheck(status);
}
```

```typescript
// 判別Union型での活用
type Result<T, E> =
  | { ok: true; value: T }
  | { ok: false; error: E };

function process<T, E>(result: Result<T, E>): T {
  if (result.ok) return result.value;
  if (!result.ok) throw result.error;
  return exhaustiveCheck(result);
}
```

```typescript
// 実践的なパターン
type Event =
  | { type: 'click'; x: number; y: number }
  | { type: 'keypress'; key: string };

class EventHandler {
  handle(event: Event): void {
    switch (event.type) {
      case 'click':
        return this.onClick(event.x, event.y);
      case 'keypress':
        return this.onKey(event.key);
      default:
        return exhaustiveCheck(event);
    }
  }
}
```

## File: 521.txt

# #521 「Union型 - 消える」

 

```typescript
// Union型でnever型は消える
type A = string | never;        // string
type B = number | never;        // number
type C = boolean | never;       // boolean
type D = string | number | never;  // string | number
```

```typescript
// 実践例：条件付きフィルタリング
type NonNullable<T> = T extends null | undefined ? never : T;

type A = NonNullable<string | null>;  // string
type B = NonNullable<number | undefined>;  // number
type C = NonNullable<boolean | null | undefined>;  // boolean
```

```typescript
// 複数のnever型
type Complex =
  | string
  | never
  | number
  | never
  | boolean;  // string | number | boolean
```

## File: 522.txt

# #522 「string | never = string」

 

```typescript
// 基本的な等式
type Test1 = string | never;           // = string
type Test2 = number | never;           // = number
type Test3 = MyType | never;           // = MyType
type Test4 = (string | number) | never; // = string | number
```

```typescript
// Exclude型の実装原理
type Exclude<T, U> = T extends U ? never : T;

type Result1 = Exclude<'a' | 'b' | 'c', 'a'>;
// = never | 'b' | 'c'
// = 'b' | 'c'

type Result2 = Exclude<string | number, string>;
// = never | number
// = number
```

```typescript
// 実践例：関数の戻り値フィルタリング
type ReturnTypeFilter<T> =
  T extends (...args: any[]) => infer R
    ? R extends void ? never : R
    : never;

type A = ReturnTypeFilter<() => string>;  // string
type B = ReturnTypeFilter<() => void>;    // never
```

## File: 523.txt

# #523 「Intersection型」

 

```typescript
// Intersection型の基本
type A = { name: string } & { age: number };
// = { name: string; age: number }

type B = string & number;  // never（両立不可能）

type C = { x: string } & { x: number };  // never
```

```typescript
// never型とのIntersection
type Test1 = string & never;     // never
type Test2 = number & never;     // never
type Test3 = object & never;     // never
type Test4 = any & never;        // never
```

```typescript
// 実践例：型の絞り込み
type User = { role: 'admin' } | { role: 'user' };
type Admin = User & { role: 'admin' };
// = { role: 'admin' }

type InvalidRole = User & { role: 'guest' };
// = never（存在しない組み合わせ）
```

## File: 524.txt

# #524 「string & never = never」

 

```typescript
// 基本的な等式
type Test1 = string & never;    // = never
type Test2 = number & never;    // = never
type Test3 = boolean & never;   // = never
type Test4 = unknown & never;   // = never
type Test5 = any & never;       // = never
```

```typescript
// 矛盾する型の検出
type Contradiction = { type: 'A' } & { type: 'B' };
// = never（typeは同時にAとBにはなれない）

type Valid = { type: 'A' } & { value: number };
// = { type: 'A'; value: number }（矛盾なし）
```

```typescript
// Extract型の実装原理
type Extract<T, U> = T extends U ? T : never;

type Result = Extract<string | number, number>;
// = never | number
// = number（Union型でneverは消える）

type Keys = Extract<'a' | 'b' | 'c', 'a' | 'b'>;
// = 'a' | 'b'
```

## File: 525.txt

# #525 「分配法則」

 

```typescript
// 分配法則の基本
type ToArray<T> = T extends any ? T[] : never;

type Result = ToArray<string | number>;
// = ToArray<string> | ToArray<number>
// = string[] | number[]
```

```typescript
// Exclude型での分配
type Exclude<T, U> = T extends U ? never : T;

type Result = Exclude<'a' | 'b' | 'c', 'a'>;
// = Exclude<'a', 'a'> | Exclude<'b', 'a'> | Exclude<'c', 'a'>
// = never | 'b' | 'c'
// = 'b' | 'c'
```

```typescript
// 分配を防ぐ方法
type NoDistribute<T> = [T] extends [any] ? T[] : never;

type Result1 = NoDistribute<string | number>;
// = (string | number)[]

type Result2 = ToArray<string | number>;
// = string[] | number[]（分配される）
```

## File: 526.txt

# #526 「条件付き型」

 

```typescript
// 条件付き型の基本
type IsString<T> = T extends string ? true : false;

type A = IsString<string>;   // true
type B = IsString<number>;   // false
type C = IsString<'hello'>;  // true
```

```typescript
// neverを使ったフィルタリング
type Filter<T> = T extends string ? T : never;

type Result = Filter<string | number | boolean>;
// = Filter<string> | Filter<number> | Filter<boolean>
// = string | never | never
// = string
```

```typescript
// 実践例：関数型の抽出
type FunctionKeys<T> = {
  [K in keyof T]: T[K] extends Function ? K : never
}[keyof T];

type Methods = FunctionKeys<{
  name: string;
  getName(): string;
  age: number;
}>;  // = 'getName'
```

## File: 527.txt

# #527 「フィルタリング」

 

```typescript
// 文字列型のフィルタリング
type StringsOnly<T> = T extends string ? T : never;

type Result = StringsOnly<'a' | 'b' | 123 | true | 'c'>;
// = 'a' | 'b' | 'c'
```

```typescript
// 関数型のフィルタリング
type FunctionsOnly<T> = T extends (...args: any[]) => any ? T : never;

type Functions = FunctionsOnly<
  | string
  | ((x: number) => string)
  | number
  | ((y: string) => number)
>;
// = ((x: number) => string) | ((y: string) => number)
```

```typescript
// 実践例：nullableな型の除外
type NonNullable<T> = T extends null | undefined ? never : T;

type Clean = NonNullable<string | null | number | undefined>;
// = string | number
```

## File: 528.txt

# #528 「Exclude<T, never>」

 

```typescript
// Exclude<T, never>の挙動
type Exclude<T, U> = T extends U ? never : T;

type A = Exclude<string, never>;           // string
type B = Exclude<string | number, never>;  // string | number
type C = Exclude<never, never>;            // never
```

```typescript
// 比較：他のExclude
type D = Exclude<string | number, string>;  // number
type E = Exclude<'a' | 'b' | 'c', 'a'>;    // 'b' | 'c'

// never除外は無意味
type F = Exclude<string | never, never>;    // string
```

```typescript
// 実践例：型演算の最適化
type RemoveNever<T> = T extends never ? never : T;
// これはT自体と同じ（最適化で除去可能）

type Original = string | number | never;  // string | number
type Filtered = RemoveNever<Original>;    // string | number
```

## File: 529.txt

# #529 「Mapped Types」

 

```typescript
// Mapped Typesの基本
type Readonly<T> = {
  readonly [K in keyof T]: T[K];
};

type Partial<T> = {
  [K in keyof T]?: T[K];
};
```

```typescript
// never型での除外
type RemoveMethods<T> = {
  [K in keyof T]: T[K] extends Function ? never : T[K]
};

type Data = RemoveMethods<{
  name: string;
  age: number;
  getName(): string;
}>;
// = { name: string; age: number; getName: never }
```

```typescript
// Key Remappingでneverキーを削除
type OmitMethods<T> = {
  [K in keyof T as T[K] extends Function ? never : K]: T[K]
};

type Clean = OmitMethods<{
  name: string;
  getName(): string;
}>;
// = { name: string }
```

## File: 530.txt

# #530 「Key Remapping」

 

```typescript
// Key Remappingの基本
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K]
};

type User = { name: string; age: number };
type UserGetters = Getters<User>;
// = { getName: () => string; getAge: () => number }
```

```typescript
// neverでキーを削除
type OmitByType<T, U> = {
  [K in keyof T as T[K] extends U ? never : K]: T[K]
};

type Data = OmitByType<{
  name: string;
  age: number;
  active: boolean;
}, boolean>;
// = { name: string; age: number }
```

```typescript
// 実践例：プレフィックス付きキーの除外
type RemovePrefix<T, Prefix extends string> = {
  [K in keyof T as K extends `${Prefix}${infer _}` ? never : K]: T[K]
};

type Clean = RemovePrefix<{
  _id: string;
  _internal: number;
  name: string;
}, '_'>;
// = { name: string }
```

## File: 531.txt

# #531 「型レベルプログラミング」

 

```typescript
// 型レベルの条件分岐
type If<Cond extends boolean, True, False> =
  Cond extends true ? True : False;

type A = If<true, string, number>;   // string
type B = If<false, string, number>;  // number
```

```typescript
// 型レベルの再帰
type Reverse<T extends any[]> =
  T extends [infer First, ...infer Rest]
    ? [...Reverse<Rest>, First]
    : [];

type Result = Reverse<[1, 2, 3, 4]>;
// = [4, 3, 2, 1]
```

```typescript
// 型レベルの配列フィルタリング
type FilterNever<T extends any[]> =
  T extends [infer First, ...infer Rest]
    ? First extends never
      ? FilterNever<Rest>
      : [First, ...FilterNever<Rest>]
    : [];

type Clean = FilterNever<[string, never, number, never]>;
// = [string, number]
```

## File: 532.txt

# #532 「型演算パターン」

 

```typescript
// フィルタリングパターン
type Filter<T, Condition> =
  T extends Condition ? T : never;

type Strings = Filter<'a' | 'b' | 1 | 2, string>;
// = 'a' | 'b'
```

```typescript
// マッピングパターン
type MapToArray<T> = {
  [K in keyof T]: T[K][]
};

type Arrays = MapToArray<{ name: string; age: number }>;
// = { name: string[]; age: number[] }
```

```typescript
// パターンマッチング
type Match<T> =
  T extends string ? 'String'
  : T extends number ? 'Number'
  : T extends boolean ? 'Boolean'
  : 'Unknown';

type A = Match<'hello'>;  // 'String'
type B = Match<42>;       // 'Number'
type C = Match<object>;   // 'Unknown'
```

## File: 533.txt

# #533 「型変換」

 

```typescript
// Union型からの除外
type Without<T, U> = T extends U ? never : T;

type Numbers = Without<string | number | boolean, string | boolean>;
// = number
```

```typescript
// オブジェクト型の変換
type PickByType<T, ValueType> = {
  [K in keyof T as T[K] extends ValueType ? K : never]: T[K]
};

type StringProps = PickByType<{
  name: string;
  age: number;
  email: string;
}, string>;
// = { name: string; email: string }
```

```typescript
// 深いプロパティの変換
type DeepOmit<T, K extends string> = {
  [P in keyof T as P extends K ? never : P]:
    T[P] extends object ? DeepOmit<T[P], K> : T[P]
};

type Clean = DeepOmit<{
  _id: string;
  user: { _id: string; name: string }
}, '_id'>;
// = { user: { name: string } }
```

## File: 534.txt

# #534 「型推論の関係」

 

```typescript
// 制御フロー分析による推論
function process(value: string | number) {
  if (typeof value === 'string') {
    return value.toUpperCase();
  } else if (typeof value === 'number') {
    return value * 2;
  }
  // ここでvalueはnever型と推論される
  const check: never = value;
}
```

```typescript
// 型ガードでの推論
type Shape = { kind: 'circle' } | { kind: 'square' };

function handle(shape: Shape) {
  if (shape.kind === 'circle') {
    // shape: { kind: 'circle' }
  } else {
    // shape: { kind: 'square' }
  }
  // すべて処理済みのため到達不可能
}
```

```typescript
// 条件付き型での推論
type InferReturnType<T> =
  T extends (...args: any[]) => infer R ? R : never;

type A = InferReturnType<() => string>;  // string
type B = InferReturnType<string>;        // never
```

## File: 535.txt

# #535 「型演算まとめ」

 

```typescript
// 型演算の基本法則
type Law1 = string | never;        // = string
type Law2 = string & never;        // = never
type Law3 = Exclude<T, never>;     // = T
type Law4 = Extract<never, T>;     // = never
```

```typescript
// 実践的な型ヘルパー
type NonNullable<T> = T extends null | undefined ? never : T;
type FunctionKeys<T> = {
  [K in keyof T]: T[K] extends Function ? K : never
}[keyof T];
type PickByType<T, U> = {
  [K in keyof T as T[K] extends U ? K : never]: T[K]
};
```

```typescript
// 複合的な型演算
type DeepPartial<T> = {
  [K in keyof T]?: T[K] extends object
    ? DeepPartial<T[K]>
    : T[K]
};

type Result<T, E> =
  | { ok: true; value: T }
  | { ok: false; error: E };
```

## File: 536.txt

# #536 「Angularガード」

 

```typescript
// Angular Guard with never型
type GuardResult = boolean | UrlTree | never;

@Injectable()
export class AuthGuard implements CanActivate {
  canActivate(route: ActivatedRouteSnapshot): Observable<GuardResult> {
    return this.authService.isAuthenticated$.pipe(
      map(isAuth => isAuth ? true : this.router.parseUrl('/login'))
    );
  }
}
```

```typescript
// 網羅的なガード実装
type AuthState = 'authenticated' | 'guest' | 'expired';

canActivate(state: AuthState): boolean | UrlTree {
  if (state === 'authenticated') return true;
  if (state === 'guest') return this.router.parseUrl('/login');
  if (state === 'expired') return this.router.parseUrl('/renew');
  const check: never = state;
  return false;
}
```

```typescript
// 型安全なリダイレクト
type RedirectResult =
  | { allow: true }
  | { allow: false; redirect: string };

function checkAccess(role: string): RedirectResult {
  if (role === 'admin') return { allow: true };
  return { allow: false, redirect: '/forbidden' };
}
```

## File: 537.txt

# #537 「ルートガード」

 

```typescript
// ルート状態の型定義
type RouteState =
  | { type: 'public' }
  | { type: 'protected'; requiredRole: string }
  | { type: 'admin' };

function canAccess(state: RouteState, userRole: string): boolean {
  if (state.type === 'public') return true;
  if (state.type === 'protected') return userRole === state.requiredRole;
  if (state.type === 'admin') return userRole === 'admin';
  const check: never = state;
  return false;
}
```

```typescript
// 複雑なガードロジック
type Permission = 'read' | 'write' | 'delete';
type GuardCheck =
  | { check: 'role'; role: string }
  | { check: 'permission'; permission: Permission };

function validateGuard(check: GuardCheck, user: User): boolean {
  if (check.check === 'role') return user.role === check.role;
  if (check.check === 'permission') return user.permissions.includes(check.permission);
  const exhaustive: never = check;
  return false;
}
```

```typescript
// CanActivateFn with 網羅性
export const authGuard: CanActivateFn = (route, state) => {
  const requiredAuth = route.data['auth'] as AuthType;

  if (requiredAuth === 'none') return true;
  if (requiredAuth === 'user') return checkUser();
  if (requiredAuth === 'admin') return checkAdmin();
  const check: never = requiredAuth;
  return false;
};
```

## File: 538.txt

# #538 「Nest.js例外フィルタ」

 

```typescript
// 例外タイプの定義
type AppException =
  | { type: 'validation'; errors: string[] }
  | { type: 'unauthorized'; message: string }
  | { type: 'notfound'; resource: string };

@Catch()
export class AllExceptionsFilter implements ExceptionFilter {
  catch(exception: AppException, host: ArgumentsHost) {
    if (exception.type === 'validation') return this.handleValidation(exception);
    if (exception.type === 'unauthorized') return this.handleUnauth(exception);
    if (exception.type === 'notfound') return this.handleNotFound(exception);
    const check: never = exception;
  }
}
```

```typescript
// HTTPステータスの網羅的処理
type HttpError = 400 | 401 | 403 | 404 | 500;

function getErrorMessage(status: HttpError): string {
  if (status === 400) return 'Bad Request';
  if (status === 401) return 'Unauthorized';
  if (status === 403) return 'Forbidden';
  if (status === 404) return 'Not Found';
  if (status === 500) return 'Internal Server Error';
  const check: never = status;
  return 'Unknown Error';
}
```

```typescript
// カスタム例外フィルタ
type DomainException =
  | { domain: 'user'; code: 'NOT_FOUND' | 'DUPLICATE' }
  | { domain: 'order'; code: 'INVALID' | 'EXPIRED' };

function handleException(ex: DomainException): HttpException {
  if (ex.domain === 'user') return new BadRequestException(ex.code);
  if (ex.domain === 'order') return new UnprocessableEntityException(ex.code);
  const check: never = ex;
  throw new InternalServerErrorException();
}
```

## File: 539.txt

# #539 「ミドルウェア」

 

```typescript
// ミドルウェアでのリクエストタイプ処理
type RequestType = 'json' | 'form' | 'multipart';

@Injectable()
export class RequestParserMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction) {
    const contentType = this.getRequestType(req);

    if (contentType === 'json') return this.parseJson(req, next);
    if (contentType === 'form') return this.parseForm(req, next);
    if (contentType === 'multipart') return this.parseMultipart(req, next);
    const check: never = contentType;
    next();
  }
}
```

```typescript
// 認証ミドルウェア
type AuthMethod = 'bearer' | 'basic' | 'apikey';

function authenticate(method: AuthMethod, req: Request): boolean {
  if (method === 'bearer') return validateBearer(req);
  if (method === 'basic') return validateBasic(req);
  if (method === 'apikey') return validateApiKey(req);
  const check: never = method;
  return false;
}
```

```typescript
// ロギングミドルウェア
type LogLevel = 'debug' | 'info' | 'warn' | 'error';

function logRequest(level: LogLevel, message: string) {
  if (level === 'debug') return logger.debug(message);
  if (level === 'info') return logger.info(message);
  if (level === 'warn') return logger.warn(message);
  if (level === 'error') return logger.error(message);
  const check: never = level;
}
```

## File: 540.txt

# #540 「API設計」

 

```typescript
// API レスポンス型
type ApiResponse<T> =
  | { status: 'success'; data: T }
  | { status: 'error'; error: { code: string; message: string } }
  | { status: 'loading' };

function handleResponse<T>(res: ApiResponse<T>): T | null {
  if (res.status === 'success') return res.data;
  if (res.status === 'error') throw new Error(res.error.message);
  if (res.status === 'loading') return null;
  const check: never = res;
  return null;
}
```

```typescript
// REST API エンドポイント型
type Endpoint =
  | { method: 'GET'; path: string }
  | { method: 'POST'; path: string; body: unknown }
  | { method: 'DELETE'; path: string };

async function request(endpoint: Endpoint): Promise<Response> {
  if (endpoint.method === 'GET') return fetch(endpoint.path);
  if (endpoint.method === 'POST') return fetch(endpoint.path, { method: 'POST', body: JSON.stringify(endpoint.body) });
  if (endpoint.method === 'DELETE') return fetch(endpoint.path, { method: 'DELETE' });
  const check: never = endpoint;
  throw new Error('Invalid endpoint');
}
```

```typescript
// GraphQL操作型
type GqlOperation =
  | { type: 'query'; query: string }
  | { type: 'mutation'; mutation: string }
  | { type: 'subscription'; subscription: string };

function executeGql(op: GqlOperation): Promise<any> {
  if (op.type === 'query') return client.query({ query: op.query });
  if (op.type === 'mutation') return client.mutate({ mutation: op.mutation });
  if (op.type === 'subscription') return client.subscribe({ query: op.subscription });
  const check: never = op;
}
```

## File: 541.txt

# #541 「型安全なエラーハンドリング」

 

```typescript
// Result型の定義
type Result<T, E> =
  | { ok: true; value: T }
  | { ok: false; error: E };

function divide(a: number, b: number): Result<number, string> {
  if (b === 0) return { ok: false, error: 'Division by zero' };
  return { ok: true, value: a / b };
}

function handleResult(result: Result<number, string>): number {
  if (result.ok) return result.value;
  if (!result.ok) throw new Error(result.error);
  const check: never = result;
}
```

```typescript
// Either型の実装
type Either<L, R> =
  | { type: 'left'; value: L }
  | { type: 'right'; value: R };

function parseJson<T>(json: string): Either<Error, T> {
  try {
    return { type: 'right', value: JSON.parse(json) };
  } catch (e) {
    return { type: 'left', value: e as Error };
  }
}
```

```typescript
// 複数のエラータイプ
type AppError =
  | { type: 'validation'; field: string }
  | { type: 'network'; code: number }
  | { type: 'business'; message: string };

function handleError(error: AppError): string {
  if (error.type === 'validation') return `Invalid: ${error.field}`;
  if (error.type === 'network') return `HTTP ${error.code}`;
  if (error.type === 'business') return error.message;
  const check: never = error;
  return 'Unknown error';
}
```

## File: 542.txt

# #542 「DTOバリデーション」

 

```typescript
// バリデーション結果型
type ValidationResult<T> =
  | { valid: true; data: T }
  | { valid: false; errors: ValidationError[] };

function validate<T>(dto: T): ValidationResult<T> {
  const errors = validateSync(dto);
  if (errors.length === 0) return { valid: true, data: dto };
  return { valid: false, errors };
}

function handleValidation<T>(result: ValidationResult<T>): T {
  if (result.valid) return result.data;
  if (!result.valid) throw new BadRequestException(result.errors);
  const check: never = result;
}
```

```typescript
// 型安全なDTO変換
type CreateUserDto = { name: string; email: string };
type UpdateUserDto = { name?: string; email?: string };
type DtoType = 'create' | 'update';

function transformDto(type: DtoType, data: any): CreateUserDto | UpdateUserDto {
  if (type === 'create') return plainToClass(CreateUserDto, data);
  if (type === 'update') return plainToClass(UpdateUserDto, data);
  const check: never = type;
  throw new Error('Invalid DTO type');
}
```

```typescript
// カスタムバリデータ
type ValidationRule =
  | { type: 'required'; field: string }
  | { type: 'email'; field: string }
  | { type: 'minLength'; field: string; min: number };

function applyRule(rule: ValidationRule, value: any): boolean {
  if (rule.type === 'required') return value != null;
  if (rule.type === 'email') return /\S+@\S+\.\S+/.test(value);
  if (rule.type === 'minLength') return value.length >= rule.min;
  const check: never = rule;
  return false;
}
```

## File: 543.txt

# #543 「レスポンス型」

 

```typescript
// 標準レスポンス型
type ApiResponse<T> =
  | { status: 'success'; data: T; timestamp: number }
  | { status: 'error'; error: { code: string; message: string } }
  | { status: 'loading' };

function handleResponse<T>(res: ApiResponse<T>): T | null {
  if (res.status === 'success') return res.data;
  if (res.status === 'error') {
    console.error(res.error);
    return null;
  }
  if (res.status === 'loading') return null;
  const check: never = res;
  return null;
}
```

```typescript
// ページネーション付きレスポンス
type PagedResponse<T> =
  | { hasData: true; items: T[]; total: number; page: number }
  | { hasData: false; reason: 'empty' | 'error' };

function processPage<T>(res: PagedResponse<T>): T[] {
  if (res.hasData) return res.items;
  if (!res.hasData && res.reason === 'empty') return [];
  if (!res.hasData && res.reason === 'error') throw new Error('Failed');
  const check: never = res;
  return [];
}
```

```typescript
// HTTPステータス付きレスポンス
type HttpResponse<T> =
  | { status: 200; data: T }
  | { status: 201; data: T; location: string }
  | { status: 204 }
  | { status: 400 | 404 | 500; error: string };

function handle<T>(res: HttpResponse<T>): T | null {
  if (res.status === 200) return res.data;
  if (res.status === 201) return res.data;
  if (res.status === 204) return null;
  if (res.status >= 400) throw new Error(res.error);
  const check: never = res;
}
```

## File: 544.txt

# #544 「実践パターン」

 

```typescript
// NgRx Reducerパターン
type UserAction =
  | { type: 'LOAD_USER'; id: string }
  | { type: 'UPDATE_USER'; user: User }
  | { type: 'DELETE_USER'; id: string };

function userReducer(state: UserState, action: UserAction): UserState {
  if (action.type === 'LOAD_USER') return { ...state, loading: true };
  if (action.type === 'UPDATE_USER') return { ...state, user: action.user };
  if (action.type === 'DELETE_USER') return { ...state, user: null };
  const check: never = action;
  return state;
}
```

```typescript
// HTTP Interceptorパターン
type InterceptorAction =
  | { type: 'add-auth'; token: string }
  | { type: 'retry'; maxRetries: number }
  | { type: 'log' };

intercept(req: HttpRequest<any>, next: HttpHandler, action: InterceptorAction) {
  if (action.type === 'add-auth') return next.handle(req.clone({ setHeaders: { Authorization: action.token } }));
  if (action.type === 'retry') return next.handle(req).pipe(retry(action.maxRetries));
  if (action.type === 'log') return next.handle(req).pipe(tap(res => console.log(res)));
  const check: never = action;
}
```

```typescript
// サービスレイヤーパターン
type ServiceResult<T> =
  | { success: true; data: T }
  | { success: false; error: ServiceError };

async function executeService<T>(result: ServiceResult<T>): Promise<T> {
  if (result.success) return result.data;
  if (!result.success) throw new ServiceException(result.error);
  const check: never = result;
}
```

## File: 545.txt

# #545 「ベストプラクティス」

 

```typescript
// 共通型定義（shared/types.ts）
export type Result<T, E = Error> =
  | { ok: true; value: T }
  | { ok: false; error: E };

export function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled case: ${JSON.stringify(value)}`);
}

export function assertNever(value: never, message?: string): never {
  throw new Error(message ?? `Unexpected: ${value}`);
}
```

```typescript
// サービス層での活用
@Injectable()
export class UserService {
  async getUser(id: string): Promise<Result<User, UserError>> {
    try {
      const user = await this.repository.findById(id);
      if (!user) return { ok: false, error: { type: 'notfound', id } };
      return { ok: true, value: user };
    } catch (e) {
      return { ok: false, error: { type: 'internal', message: e.message } };
    }
  }
}
```

```typescript
// コントローラー層での活用
@Controller('users')
export class UserController {
  @Get(':id')
  async getUser(@Param('id') id: string): Promise<UserDto> {
    const result = await this.service.getUser(id);

    if (result.ok) return this.toDto(result.value);
    if (!result.ok && result.error.type === 'notfound') throw new NotFoundException();
    if (!result.ok && result.error.type === 'internal') throw new InternalServerErrorException();
    return exhaustiveCheck(result);
  }
}
```

## File: 546.txt

# #546 「間違い(1) - void混同」

 

```typescript
// void型：正常終了する
function logMessage(msg: string): void {
  console.log(msg);
  // 関数は正常終了する
}

// never型：決して返らない
function throwError(msg: string): never {
  throw new Error(msg);
  // この後のコードは実行されない
}
```

```typescript
// 間違った例：voidをneverのように使う
function process(): void {
  throw new Error('Error');  // voidなのに例外を投げる
}

// 正しい例：never型を使う
function processCorrect(): never {
  throw new Error('Error');  // never型なので正しい
}
```

```typescript
// 戻り値の代入
const a: void = logMessage('Hello');     // OK: undefinedが代入される
const b: never = throwError('Error');    // 実行されない（例外が発生）

// void型はundefinedと互換性がある
const c: void = undefined;  // OK
const d: never = undefined; // エラー！
```

## File: 547.txt

# #547 「間違い(2) - 到達可能コード」

 

```typescript
// 間違い：never型の後にコード
function bad(value: string | number): string {
  if (typeof value === 'string') return value;
  const check: never = value;  // エラー！numberがneverに代入できない
  return 'default';  // 到達可能だが間違い
}

// 正しい実装
function good(value: string | number): string {
  if (typeof value === 'string') return value;
  if (typeof value === 'number') return value.toString();
  const check: never = value;  // OK
  return check;
}
```

```typescript
// 間違い：型ガード不足
type Status = 'active' | 'inactive' | 'pending';

function handle(status: Status): string {
  if (status === 'active') return 'Active';
  const check: never = status;  // エラー！'inactive' | 'pending'が残っている
  return '';
}
```

```typescript
// 間違い：Union型の除外漏れ
type Value = string | number | boolean;

function process(v: Value): string {
  if (typeof v === 'string') return v;
  // numberとbooleanが残っているのにneverチェック
  const check: never = v;  // エラー！
  return '';
}
```

## File: 548.txt

# #548 「デバッグ」

 

```typescript
// デバッグ手順1: 型エラーを確認
type Action = 'create' | 'update' | 'delete';

function handle(action: Action): string {
  if (action === 'create') return 'Created';
  const check: never = action;
  // エラー: Type '"update" | "delete"' is not assignable to type 'never'
  return '';
}
```

```typescript
// デバッグ手順2: 残りの型を確認
function handleFixed(action: Action): string {
  if (action === 'create') return 'Created';
  // VSCodeでactionにホバー → 型は 'update' | 'delete'
  if (action === 'update') return 'Updated';
  if (action === 'delete') return 'Deleted';
  const check: never = action;  // OK
  return check;
}
```

```typescript
// デバッグ手順3: ヘルパー関数でログ出力
function debugNever(value: never, context: string): never {
  console.error(`Unhandled case in ${context}:`, value);
  throw new Error(`Unhandled: ${JSON.stringify(value)}`);
}

function process(action: Action): string {
  if (action === 'create') return 'Created';
  return debugNever(action, 'process');  // ランタイムでデバッグ情報を出力
}
```

## File: 549.txt

# #549 「ベストプラクティス」

 

```typescript
// ベストプラクティス1: 共通ヘルパー
// utils/exhaustive.ts
export function exhaustiveCheck(value: never, context?: string): never {
  const msg = context
    ? `Unhandled case in ${context}: ${JSON.stringify(value)}`
    : `Unhandled case: ${JSON.stringify(value)}`;
  throw new Error(msg);
}

export function assertNever(value: never): never {
  throw new Error(`Unexpected value: ${value}`);
}
```

```typescript
// ベストプラクティス2: 判別Union型
type Result<T, E> =
  | { success: true; value: T }
  | { success: false; error: E };

type DomainEvent =
  | { type: 'UserCreated'; userId: string }
  | { type: 'UserUpdated'; userId: string; data: any };

// 必ず判別プロパティ（type, kind, success等）を持たせる
```

```typescript
// ベストプラクティス3: すべての分岐で網羅性チェック
function handleEvent(event: DomainEvent): void {
  switch (event.type) {
    case 'UserCreated':
      return this.onCreate(event);
    case 'UserUpdated':
      return this.onUpdate(event);
    default:
      return exhaustiveCheck(event, 'handleEvent');
  }
}
```

## File: 550.txt

# #550 「マスターチェック」

 

```typescript
// never型の基本法則
type Law1 = string | never;              // = string
type Law2 = string & never;              // = never
type Law3 = Exclude<string, never>;      // = string
type Law4 = Extract<never, string>;      // = never

function neverReturn(): never {
  throw new Error();
}

const unreachable: never = neverReturn(); // 実行されない
```

```typescript
// 網羅性チェックのマスターパターン
type Status = 'pending' | 'success' | 'error';

function exhaustiveCheck(value: never): never {
  throw new Error(`Unhandled: ${value}`);
}

function handle(status: Status): string {
  if (status === 'pending') return '処理中';
  if (status === 'success') return '成功';
  if (status === 'error') return 'エラー';
  return exhaustiveCheck(status);
}
```

```typescript
// 実践的な型安全パターン
type Result<T, E> =
  | { ok: true; value: T }
  | { ok: false; error: E };

type ApiResponse<T> =
  | { status: 'success'; data: T }
  | { status: 'error'; error: string };

function unwrap<T, E>(result: Result<T, E>): T {
  if (result.ok) return result.value;
  if (!result.ok) throw result.error;
  const check: never = result;
  return check;
}
```
```

