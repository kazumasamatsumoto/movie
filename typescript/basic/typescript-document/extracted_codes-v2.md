

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

