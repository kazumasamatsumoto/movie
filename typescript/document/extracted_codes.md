## File: 001.txt

# #001 「string型とは - 文字列を扱う最も基本的な型」台本

```

## 📺 画面表示用コード

```typescript
// string型の基本
let name: string = "Alice";
let message: string = "Hello, World!";
let description: string = "TypeScript学習中";

// 型安全性の例
let result: string = name + " " + message; // OK
// let error: number = name + message; // エラー

// 実用的な例
let userName: string = "ずんだもん";
let greeting: string = `こんにちは、${userName}さん！`;
```

```

## File: 002.txt

# #002 「string型の宣言 - let name: string」台本

```

## 📺 画面表示用コード

```typescript
// string型の宣言
let name: string;
let email: string;
let address: string;

// 後で値を代入
name = "Alice";
email = "alice@example.com";
address = "東京都渋谷区";

// 初期化と同時に宣言
let userName: string = "Bob";
let userEmail: string = "bob@example.com";
let fullName: string = userName + " Smith";
```

```

## File: 003.txt

# #003 「string型への代入 - name = "Hello"」台本

```

## 📺 画面表示用コード

```typescript
// string型への代入
let message: string;

// 文字列の代入
message = "Hello";        // OK
message = "World";        // OK
message = "こんにちは";    // OK

// 型エラーの例
// message = 123;         // エラー: Type 'number' is not assignable to type 'string'
// message = true;        // エラー: Type 'boolean' is not assignable to type 'string'

// 再代入
message = "Hello";
message = "Goodbye";
```

```

## File: 004.txt

# #004 「string型の初期化 - let name: string = "Alice"」台本

```

## 📺 画面表示用コード

```typescript
// string型の初期化
let name: string = "Alice";
let email: string = "alice@example.com";
let description: string = "TypeScript学習中";
let emptyString: string = "";

// 実用的な例
let componentTitle: string = "ユーザー管理";
let defaultMessage: string = "データを読み込み中...";
let apiEndpoint: string = "https://api.example.com/users";

// 条件による初期化
let status: string = "active";
let displayText: string = status === "active" ? "アクティブ" : "非アクティブ";
```

```

## File: 005.txt

# #005 「型推論でstring型 - let name = "Bob"」台本

```

## 📺 画面表示用コード

```typescript
// 型推論の例
let name = "Bob";           // string型と推論
let email = "bob@example.com"; // string型と推論
let message = "Hello";      // string型と推論

// 型安全性は保たれる
// name = 123; // エラー: Type 'number' is not assignable to type 'string'

// 明示的型注釈との比較
let explicit: string = "Alice";  // 明示的
let inferred = "Bob";            // 推論

// 実用的な例
let userName = "ずんだもん";
let greeting = `こんにちは、${userName}さん！`;
```

```

## File: 006.txt

# #006 「constでstring型 - const name = "Charlie"」台本

```

## 📺 画面表示用コード

```typescript
// constでの定数宣言
const API_URL = "https://api.example.com";
const APP_NAME = "TypeScript学習アプリ";
const VERSION = "1.0.0";

// 再代入はエラー
// API_URL = "https://new-api.com"; // エラー: Cannot assign to 'API_URL' because it is a constant

// 型推論でstring型
console.log(typeof API_URL); // "string"

// 実用的な例
const DEFAULT_MESSAGE = "データを読み込み中...";
const ERROR_MESSAGE = "エラーが発生しました";
const SUCCESS_MESSAGE = "処理が完了しました";
```

```

## File: 007.txt

# #007 「string型とリテラル型の違い - "hello" vs string」台本

```

## 📺 画面表示用コード

```typescript
// string型 - 任意の文字列
let message: string = "Hello";
message = "World"; // OK
message = "こんにちは"; // OK

// リテラル型 - 特定の文字列のみ
let status: "active" | "inactive" = "active";
// status = "pending"; // エラー: Type '"pending"' is not assignable to type '"active" | "inactive"'

// 実用的な例
let theme: "light" | "dark" = "light";
let language: "ja" | "en" = "ja";
let userRole: "admin" | "user" | "guest" = "user";
```

```

## File: 008.txt

# #008 「string型の変数宣言 - varは使わない理由」台本

```

## 📺 画面表示用コード

```typescript
// var（非推奨）
// var oldStyle: string = "古いスタイル";

// let（推奨）- 再代入可能
let modernStyle: string = "モダンスタイル";
modernStyle = "更新された値"; // OK

// const（推奨）- 再代入不可
const constantValue: string = "定数値";
// constantValue = "新しい値"; // エラー

// 実用的な例
let userName: string = "初期値";
const API_ENDPOINT: string = "https://api.example.com";
```

```

## File: 009.txt

# #009 「string型とundefined - 初期化前のアクセス」台本

```

## 📺 画面表示用コード

```typescript
// 初期化前のアクセス
let name: string;
// console.log(name); // undefined

// 安全な初期化
let userName: string = "初期値";
console.log(userName); // "初期値"

// undefinedチェック
let optionalName: string | undefined;
if (optionalName !== undefined) {
  console.log(optionalName.toUpperCase());
}

// 実用的な例
let componentTitle: string = "";
let apiResponse: string | undefined;
```

```

## File: 010.txt

# #010 「string型のスコープ - ブロックスコープ」台本

```

## 📺 画面表示用コード

```typescript
// ブロックスコープの例
{
  let blockScoped: string = "ブロック内";
  const blockConstant: string = "ブロック定数";
  // このブロック内でのみ有効
}

// console.log(blockScoped); // エラー: Cannot find name 'blockScoped'

// 実用的な例
function processData() {
  let localData: string = "ローカルデータ";
  
  if (true) {
    let conditionalData: string = "条件付きデータ";
    // このブロック内でのみ有効
  }
  
  return localData;
}
```

```

## File: 011.txt

# #011 「ダブルクォート文字列 - "hello"」台本

```

## 📺 画面表示用コード

```typescript
// ダブルクォート文字列
let message: string = "Hello, World!";
let name: string = "Alice";
let description: string = "TypeScript学習中";

// 実用的な例
let apiUrl: string = "https://api.example.com";
let errorMessage: string = "エラーが発生しました";
let successMessage: string = "処理が完了しました";

// 文字列の結合
let greeting: string = "こんにちは、" + name + "さん！";
let fullMessage: string = message + " " + description;
``````

## File: 012.txt

# #012 「シングルクォート文字列 - 'hello'」台本

```

## 📺 画面表示用コード

```typescript
// シングルクォート文字列
let message: string = 'Hello, World!';
let name: string = 'Alice';
let description: string = 'TypeScript学習中';

// 実用的な例
let apiUrl: string = 'https://api.example.com';
let errorMessage: string = 'エラーが発生しました';
let successMessage: string = '処理が完了しました';

// 文字列の結合
let greeting: string = 'こんにちは、' + name + 'さん！';
let fullMessage: string = message + ' ' + description;
``````

## File: 013.txt

# #013 「ダブルとシングルの使い分け」台本

```

## 📺 画面表示用コード

```typescript
// プロジェクト内での統一例
// シングルクォート統一スタイル
let message: string = 'Hello, World!';
let name: string = 'Alice';

// HTML属性内ではダブルクォート
let htmlTemplate: string = '<div class="container">Hello</div>';

// 実用的な例
let componentTemplate: string = '<h1>{{title}}</h1>';
let cssClass: string = 'btn btn-primary';
let apiEndpoint: string = '/api/users';

// 一貫性の重要性
let userMessage: string = 'ユーザー登録完了';
let systemMessage: string = 'システムエラー';
``````

## File: 014.txt

# #014 「エスケープシーケンス - \"と\'」台本

```

## 📺 画面表示用コード

```typescript
// エスケープシーケンスの例
let message1: string = "He said \"Hello\" to me";
let message2: string = 'It\'s a beautiful day';
let message3: string = "Path: C:\\Users\\Documents";

// 実用的な例
let jsonString: string = "{\"name\": \"Alice\", \"age\": 30}";
let htmlContent: string = "<div class=\"container\">Content</div>";
let filePath: string = "C:\\Program Files\\MyApp\\config.json";

// 複数のエスケープ
let complexMessage: string = "Line 1\nLine 2\tTabbed content";
``````

## File: 015.txt

# #015 「バックスラッシュのエスケープ - \\」台本

```

## 📺 画面表示用コード

```typescript
// バックスラッシュのエスケープ
let windowsPath: string = "C:\\Users\\Documents\\file.txt";
let unixPath: string = "/home/user/documents/file.txt";
let regexPattern: string = "\\d+\\s+\\w+";

// 実用的な例
let configPath: string = "C:\\Program Files\\MyApp\\config.json";
let logPath: string = "D:\\Logs\\application.log";
let assetPath: string = "assets\\images\\logo.png";

// 正規表現での使用
let phonePattern: string = "\\d{3}-\\d{4}-\\d{4}";
let emailPattern: string = "\\w+@\\w+\\.\\w+";
``````

## File: 016.txt

# #016 「改行のエスケープ - \n」台本

```

## 📺 画面表示用コード

```typescript
// 改行のエスケープ
let multiLineMessage: string = "Line 1\nLine 2\nLine 3";
let errorMessage: string = "エラーが発生しました\n詳細: ファイルが見つかりません";
let logMessage: string = "INFO: 処理開始\nDEBUG: データ読み込み中\nINFO: 処理完了";

// 実用的な例
let userInstructions: string = "手順:\n1. ファイルを選択\n2. アップロードボタンをクリック\n3. 完了を確認";
let systemMessage: string = "システムメンテナンス中\n復旧予定: 2024年1月1日 10:00";

// コンソール出力での確認
console.log(multiLineMessage);
``````

## File: 017.txt

# #017 「タブのエスケープ - \t」台本

```

## 📺 画面表示用コード

```typescript
// タブのエスケープ
let tabbedData: string = "Name\tAge\tCity\nAlice\t30\tTokyo\nBob\t25\tOsaka";
let indentedText: string = "Level 1\n\tLevel 2\n\t\tLevel 3";
let logFormat: string = "INFO\t2024-01-01\tUser login successful";

// 実用的な例
let csvHeader: string = "ID\tName\tEmail\tStatus";
let csvData: string = "1\tAlice\talice@example.com\tActive\n2\tBob\tbob@example.com\tInactive";
let debugOutput: string = "Function: processData\n\tInput: userData\n\tOutput: processedData";

// コンソール出力での確認
console.log(tabbedData);
``````

## File: 018.txt

# #018 「Unicode文字 - \u0041」台本

```

## 📺 画面表示用コード

```typescript
// Unicode文字の例
let unicodeA: string = "\u0041"; // A
let unicodeHeart: string = "\u2764"; // ❤
let unicodeStar: string = "\u2605"; // ★
let unicodeCheck: string = "\u2713"; // ✓

// 実用的な例
let successIcon: string = "\u2713 成功";
let errorIcon: string = "\u2717 エラー";
let warningIcon: string = "\u26A0 警告";
let infoIcon: string = "\u2139 情報";

// 多言語文字
let japanese: string = "\u65E5\u672C\u8A9E"; // 日本語
let chinese: string = "\u4E2D\u6587"; // 中文
``````

## File: 019.txt

# #019 「空文字列 - ""と''」台本

```

## 📺 画面表示用コード

```typescript
// 空文字列の例
let emptyString1: string = "";
let emptyString2: string = '';
let name: string = "";
let description: string = '';

// 実用的な例
let userInput: string = "";
let searchQuery: string = '';
let errorMessage: string = "";
let successMessage: string = '';

// 条件判定での使用
if (userInput === "") {
  console.log("入力が空です");
}

if (searchQuery.length === 0) {
  console.log("検索クエリが設定されていません");
}
``````

## File: 020.txt

# #020 「文字列リテラルの型推論」台本

```

## 📺 画面表示用コード

```typescript
// letでの型推論 - string型
let message = "Hello"; // string型と推論
let name = "Alice";    // string型と推論

// constでの型推論 - リテラル型
const API_URL = "https://api.example.com"; // "https://api.example.com"型と推論
const VERSION = "1.0.0"; // "1.0.0"型と推論

// 実用的な例
let userName = "ずんだもん"; // string型
const APP_NAME = "TypeScript学習アプリ"; // "TypeScript学習アプリ"型

// 型の違い
// message = "World"; // OK (string型)
// API_URL = "https://new-api.com"; // エラー (リテラル型)
``````

## File: 021.txt

# #021 「テンプレートリテラルとは - バッククォート`」台本

```

## 📺 画面表示用コード

```typescript
// テンプレートリテラルの基本
let name: string = "Alice";
let age: number = 30;

// バッククォートで囲む
let message: string = `Hello, ${name}!`;
let info: string = `${name} is ${age} years old`;

// 従来の文字列結合との比較
let oldWay: string = "Hello, " + name + "!";
let newWay: string = `Hello, ${name}!`;

// 実用的な例
let userName: string = "ずんだもん";
let greeting: string = `こんにちは、${userName}さん！`;
``````

## File: 022.txt

# #022 「基本構文 - `Hello, ${name}`」台本

```

## 📺 画面表示用コード

```typescript
// 基本構文の例
let name: string = "Alice";
let age: number = 30;
let isActive: boolean = true;

// 変数の埋め込み
let greeting: string = `Hello, ${name}!`;
let ageInfo: string = `Age: ${age}`;
let status: string = `Status: ${isActive ? "Active" : "Inactive"}`;

// 実用的な例
let userName: string = "Bob";
let userRole: string = "admin";
let welcomeMessage: string = `Welcome, ${userName}! Your role is ${userRole}.`;
``````

## File: 023.txt

# #023 「変数の埋め込み - ${variable}」台本

```

## 📺 画面表示用コード

```typescript
// 変数埋め込みの例
let firstName: string = "Alice";
let lastName: string = "Smith";
let age: number = 30;
let isVip: boolean = true;

// 文字列変数の埋め込み
let fullName: string = `${firstName} ${lastName}`;
let ageMessage: string = `Age: ${age}`;
let vipStatus: string = `VIP: ${isVip}`;

// 実用的な例
let productName: string = "TypeScript学習本";
let price: number = 2980;
let description: string = `${productName} - ¥${price}`;
``````

## File: 024.txt

# #024 「式の埋め込み - ${1 + 2}」台本

```

## 📺 画面表示用コード

```typescript
// 式埋め込みの例
let a: number = 10;
let b: number = 5;

// 算術演算
let sum: string = `Sum: ${a + b}`;
let product: string = `Product: ${a * b}`;
let average: string = `Average: ${(a + b) / 2}`;

// 比較演算
let comparison: string = `a > b: ${a > b}`;
let equality: string = `a === b: ${a === b}`;

// 実用的な例
let price: number = 1000;
let tax: number = 0.1;
let total: string = `Total: ¥${price * (1 + tax)}`;
``````

## File: 025.txt

# #025 「関数呼び出しの埋め込み - ${getName()}」台本

```

## 📺 画面表示用コード

```typescript
// 関数呼び出し埋め込みの例
function getName(): string {
  return "Alice";
}

function getAge(): number {
  return 30;
}

function isAdult(age: number): boolean {
  return age >= 18;
}

// 関数呼び出しの埋め込み
let greeting: string = `Hello, ${getName()}!`;
let ageInfo: string = `Age: ${getAge()}`;
let adultStatus: string = `Adult: ${isAdult(getAge())}`;

// 実用的な例
function formatPrice(price: number): string {
  return `¥${price.toLocaleString()}`;
}

let productPrice: string = `Price: ${formatPrice(2980)}`;
``````

## File: 026.txt

# #026 「オブジェクトプロパティ - ${user.name}」台本

```

## 📺 画面表示用コード

```typescript
// オブジェクトプロパティ埋め込みの例
let user = {
  name: "Alice",
  age: 30,
  email: "alice@example.com",
  isActive: true
};

// プロパティの埋め込み
let userInfo: string = `Name: ${user.name}`;
let userAge: string = `Age: ${user.age}`;
let userEmail: string = `Email: ${user.email}`;
let userStatus: string = `Status: ${user.isActive ? "Active" : "Inactive"}`;

// 実用的な例
let product = {
  name: "TypeScript学習本",
  price: 2980,
  category: "技術書"
};

let productInfo: string = `${product.name} (${product.category}) - ¥${product.price}`;
``````

## File: 027.txt

# #027 「配列要素の埋め込み - ${arr[0]}」台本

```

## 📺 画面表示用コード

```typescript
// 配列要素埋め込みの例
let fruits: string[] = ["apple", "banana", "orange"];
let numbers: number[] = [1, 2, 3, 4, 5];
let users: string[] = ["Alice", "Bob", "Charlie"];

// 配列要素の埋め込み
let firstFruit: string = `First fruit: ${fruits[0]}`;
let lastNumber: string = `Last number: ${numbers[numbers.length - 1]}`;
let secondUser: string = `Second user: ${users[1]}`;

// 実用的な例
let tags: string[] = ["TypeScript", "JavaScript", "Web開発"];
let firstTag: string = `Primary tag: ${tags[0]}`;
let allTags: string = `Tags: ${tags.join(", ")}`;
``````

## File: 028.txt

# #028 「複数の変数埋め込み - `${first} ${last}`」台本

```

## 📺 画面表示用コード

```typescript
// 複数変数埋め込みの例
let firstName: string = "Alice";
let lastName: string = "Smith";
let age: number = 30;
let city: string = "Tokyo";

// 複数の変数埋め込み
let fullInfo: string = `${firstName} ${lastName}, ${age} years old, from ${city}`;
let greeting: string = `Hello, ${firstName} ${lastName}! You are ${age} years old.`;

// 実用的な例
let productName: string = "TypeScript学習本";
let price: number = 2980;
let discount: number = 0.1;
let finalPrice: string = `${productName}: ¥${price} (${discount * 100}% off) = ¥${price * (1 - discount)}`;
``````

## File: 029.txt

# #029 「テンプレートリテラルの型 - string型」台本

```

## 📺 画面表示用コード

```typescript
// テンプレートリテラルの型
let name: string = "Alice";
let age: number = 30;
let isActive: boolean = true;

// すべてstring型になる
let message1: string = `Name: ${name}`;        // string型
let message2: string = `Age: ${age}`;          // string型
let message3: string = `Active: ${isActive}`;  // string型

// 型推論でもstring型
let inferred = `Hello, ${name}!`; // string型と推論

// 実用的な例
let userId: number = 12345;
let userName: string = "Bob";
let userInfo: string = `User ${userId}: ${userName}`;
``````

## File: 030.txt

# #030 「複数行のテンプレートリテラル」台本

```

## 📺 画面表示用コード

```typescript
// 複数行テンプレートリテラル
let userName: string = "Alice";
let userEmail: string = "alice@example.com";

// 複数行の文字列
let multiLineMessage: string = `
Hello, ${userName}!

Thank you for registering.
Your email: ${userEmail}

Best regards,
Support Team
`;

// 実用的な例
let htmlTemplate: string = `
<div class="user-card">
  <h2>${userName}</h2>
  <p>Email: ${userEmail}</p>
  <button>Edit Profile</button>
</div>
`;
``````

## File: 031.txt

# #031 「複数行文字列の実例 - HTMLテンプレート」台本

```

## 📺 画面表示用コード

```typescript
// HTMLテンプレートの例
let product = {
  name: "TypeScript学習本",
  price: 2980,
  description: "TypeScriptの基礎から応用まで"
};

// HTMLテンプレート
let productCard: string = `
<div class="product-card">
  <h3 class="product-title">${product.name}</h3>
  <p class="product-description">${product.description}</p>
  <div class="product-price">¥${product.price}</div>
  <button class="add-to-cart">カートに追加</button>
</div>
`;

// 実用的な例
let user = { name: "Alice", role: "admin" };
let userProfile: string = `
<div class="profile">
  <h2>${user.name}</h2>
  <span class="role-badge">${user.role}</span>
</div>
`;
``````

## File: 032.txt

# #032 「テンプレートリテラルのインデント」台本

```

## 📺 画面表示用コード

```typescript
// インデントの例
let userName: string = "Alice";

// インデントが保持される
let message: string = `
    Hello, ${userName}!
    Welcome to our service.
    Have a great day!
`;

// trim()で先頭の改行を削除
let trimmedMessage: string = `
    Hello, ${userName}!
    Welcome to our service.
`.trim();

// 実用的な例
let htmlTemplate: string = `
<div class="container">
    <h1>${userName}</h1>
    <p>Welcome!</p>
</div>
`.trim();
``````

## File: 033.txt

# #033 「バッククォートのエスケープ」台本

```

## 📺 画面表示用コード

```typescript
// バッククォートのエスケープ
let codeExample: string = `Here is some code: \`const name = "test"\``;
let templateExample: string = `Template: \`Hello, \${name}!\``;

// 実用的な例
let markdownCode: string = `
Here is a code block:
\`\`\`typescript
const greeting = \`Hello, \${name}!\`;
\`\`\`
`;

// 複数のエスケープ
let complexExample: string = `Use \`\${variable}\` for interpolation`;
``````

## File: 034.txt

# #034 「ネストは避ける」台本

```

## 📺 画面表示用コード

```typescript
// ネスト（非推奨）
let userName: string = "Alice";
let userRole: string = "admin";
// let nested: string = `User: \`${userName}\` with role \`${userRole}\``; // 複雑

// 推奨：シンプルな方法
let simple: string = `User: ${userName} with role ${userRole}`;

// 実用的な例
let productName: string = "TypeScript本";
let price: number = 2980;
let description: string = `${productName} - ¥${price}`; // シンプル

// 複雑な場合は分割
let part1: string = `Product: ${productName}`;
let part2: string = `Price: ¥${price}`;
let combined: string = `${part1} - ${part2}`;
``````

## File: 035.txt

# #035 「パフォーマンス考慮」台本

```

## 📺 画面表示用コード

```typescript
// パフォーマンス考慮の例
let users: string[] = ["Alice", "Bob", "Charlie"];

// 非効率：ループ内でテンプレートリテラル
// for (let user of users) {
//   console.log(`Hello, ${user}!`); // 毎回新しい文字列を作成
// }

// 効率的：事前に準備
let greetings: string[] = users.map(user => `Hello, ${user}!`);
greetings.forEach(greeting => console.log(greeting));

// 実用的な例
let productNames: string[] = ["本", "ペン", "ノート"];
let productList: string = productNames.map(name => `- ${name}`).join('\n');
``````

## File: 036.txt

# #036 「デバッグのコツ」台本

```

## 📺 画面表示用コード

```typescript
// デバッグのコツ
let userName: string = "Alice";
let userAge: number = 30;

// 1. 変数の確認
console.log("userName:", userName);
console.log("userAge:", userAge);

// 2. 段階的な構築
let part1: string = `Name: ${userName}`;
let part2: string = `Age: ${userAge}`;
let fullMessage: string = `${part1}, ${part2}`;

// 3. コンソール出力で確認
console.log("Full message:", fullMessage);

// 実用的な例
let product = { name: "本", price: 1000 };
let productInfo: string = `${product.name}: ¥${product.price}`;
console.log("Product info:", productInfo);
``````

## File: 037.txt

# #037 「よくある間違い(1)」台本

```

## 📺 画面表示用コード

```typescript
// よくある間違いの例

// 1. クォートの混在（間違い）
// let message = "Hello, ${name}!"; // ダブルクォートでは埋め込みされない

// 正しい方法
let name: string = "Alice";
let message: string = `Hello, ${name}!`; // バッククォートを使用

// 2. 未定義変数（間違い）
// let errorMessage = `Hello, ${undefinedVariable}!`; // エラー

// 正しい方法
let userName: string = "Bob";
let correctMessage: string = `Hello, ${userName}!`;

// 3. 型の不一致
let age: number = 30;
let ageMessage: string = `Age: ${age}`; // 数値も文字列に変換される
``````

## File: 038.txt

# #038 「よくある間違い(2)」台本

```

## 📺 画面表示用コード

```typescript
// よくある間違いの例（続き）

// 4. 複雑すぎる式（間違い）
// let complex = `Result: ${someFunction() + anotherFunction() * 2}`; // 読みにくい

// 正しい方法
let result1: number = someFunction();
let result2: number = anotherFunction() * 2;
let simple: string = `Result: ${result1 + result2}`;

// 5. エスケープの問題
let codeExample: string = `Code: \`const name = "test"\``; // 正しいエスケープ

// 6. パフォーマンスの問題
let items: string[] = ["a", "b", "c"];
// 非効率: ループ内でテンプレートリテラル
// 効率: 事前に準備
let itemList: string = items.map(item => `- ${item}`).join('\n');
``````

## File: 039.txt

# #039 「ベストプラクティス」台本

```

## 📺 画面表示用コード

```typescript
// ベストプラクティスの例

// 1. シンプルな構造
let userName: string = "Alice";
let userAge: number = 30;
let greeting: string = `Hello, ${userName}! You are ${userAge} years old.`;

// 2. 適切な命名
let productName: string = "TypeScript本";
let productPrice: number = 2980;
let productInfo: string = `${productName}: ¥${productPrice}`;

// 3. 複雑な場合は分割
let firstName: string = "Alice";
let lastName: string = "Smith";
let fullName: string = `${firstName} ${lastName}`;
let welcomeMessage: string = `Welcome, ${fullName}!`;

// 4. 型安全性の確保
let userId: number = 12345;
let userStatus: string = `User ID: ${userId}`;
``````

## File: 040.txt

# #040 「テンプレートリテラルまとめ」台本

```

## 📺 画面表示用コード

```typescript
// テンプレートリテラルの要点まとめ
let name: string = "Alice";
let age: number = 30;

// 1. 基本的な変数埋め込み
let greeting: string = `Hello, ${name}!`;

// 2. 複数変数の埋め込み
let info: string = `${name} is ${age} years old`;

// 3. 式の埋め込み
let calculation: string = `Next year: ${age + 1}`;

// 4. 複数行文字列
let multiLine: string = `
Hello, ${name}!
Age: ${age}
Welcome!
`;

// 5. 実用的な例
let user = { name: "Bob", role: "admin" };
let userInfo: string = `User: ${user.name} (${user.role})`;
``````

## File: 041.txt

# #041 「Stringとstringの基本的な違い」台本

```

## 📺 画面表示用コード

```typescript
// string型（推奨）- プリミティブ型
let name: string = "Alice";
let message: string = "Hello, World!";

// String型（非推奨）- オブジェクト型
// let nameObj: String = new String("Alice"); // 避けるべき

// 型の違い
console.log(typeof name);        // "string"
// console.log(typeof nameObj);  // "object"

// 実用的な例
let userName: string = "Bob";
let userEmail: string = "bob@example.com";
let userInfo: string = `${userName} (${userEmail})`;
``````

## File: 042.txt

# #042 「string型の宣言 - プリミティブ」台本

```

## 📺 画面表示用コード

```typescript
// string型の宣言（プリミティブ型）
let name: string = "Alice";
let email: string = "alice@example.com";
let description: string = "TypeScript学習中";

// 型推論でもstring型
let inferred = "Bob"; // string型と推論

// 実用的な例
let componentTitle: string = "ユーザー管理";
let apiEndpoint: string = "/api/users";
let errorMessage: string = "エラーが発生しました";

// プリミティブ型の特徴
console.log(typeof name); // "string"
``````

## File: 043.txt

# #043 「String型の宣言 - 避けるべき」台本

```

## 📺 画面表示用コード

```typescript
// String型（避けるべき）
// let nameObj: String = new String("Alice"); // 非推奨
// let messageObj: String = new String("Hello"); // 非推奨

// 正しい方法：string型を使用
let name: string = "Alice";
let message: string = "Hello";

// 型の違い
console.log(typeof name);        // "string"
// console.log(typeof nameObj);  // "object"

// 実用的な例
let userName: string = "Bob";
let userRole: string = "admin";
let userInfo: string = `${userName} (${userRole})`;
``````

## File: 044.txt

# #044 「Stringコンストラクタ - new String()」台本

```

## 📺 画面表示用コード

```typescript
// Stringコンストラクタ（避けるべき）
// let strObj = new String("Hello"); // 非推奨

// 正しい方法：文字列リテラル
let str: string = "Hello";

// 型の違い
console.log(typeof str);        // "string"
// console.log(typeof strObj);  // "object"

// 比較の問題
let str1: string = "Hello";
let str2: string = "Hello";
console.log(str1 === str2); // true

// let obj1 = new String("Hello");
// let obj2 = new String("Hello");
// console.log(obj1 === obj2); // false
``````

## File: 045.txt

# #045 「Stringオブジェクトの問題点」台本

```

## 📺 画面表示用コード

```typescript
// Stringオブジェクトの問題点

// 1. 型の不一致
// let strObj: String = new String("Hello");
// let str: string = "Hello";
// console.log(strObj === str); // false

// 2. オブジェクト比較の問題
// let obj1 = new String("Hello");
// let obj2 = new String("Hello");
// console.log(obj1 === obj2); // false（異なるオブジェクト）

// 正しい方法
let str1: string = "Hello";
let str2: string = "Hello";
console.log(str1 === str2); // true

// 実用的な例
let userName: string = "Alice";
let userInput: string = "Alice";
console.log(userName === userInput); // true
``````

## File: 046.txt

# #046 「Stringからstringへ - valueOf()」台本

```

## 📺 画面表示用コード

```typescript
// Stringからstringへの変換

// 1. valueOf()メソッド
// let strObj = new String("Hello");
// let str: string = strObj.valueOf(); // string型に変換

// 2. String()関数
// let strObj = new String("Hello");
// let str: string = String(strObj); // string型に変換

// 3. 文字列リテラル（推奨）
let str: string = "Hello"; // 最初からstring型

// 実用的な例
let userData = {
  name: "Alice",
  email: "alice@example.com"
};

let userName: string = String(userData.name);
let userEmail: string = String(userData.email);
``````

## File: 047.txt

# #047 「自動ボックス化」台本

```

## 📺 画面表示用コード

```typescript
// 自動ボックス化の例
let str: string = "Hello";

// メソッド呼び出し時に自動ボックス化
let upperStr: string = str.toUpperCase(); // 自動的にStringオブジェクトに変換
let lowerStr: string = str.toLowerCase(); // 自動的にStringオブジェクトに変換

// プロパティアクセス時も自動ボックス化
let length: number = str.length; // 自動的にStringオブジェクトに変換

// 実用的な例
let userName: string = "Alice";
let userNameUpper: string = userName.toUpperCase();
let userNameLength: number = userName.length;
let userNameFirst: string = userName.charAt(0);
``````

## File: 048.txt

# #048 「==と===での比較」台本

```

## 📺 画面表示用コード

```typescript
// ==と===での比較

// string型同士の比較
let str1: string = "Hello";
let str2: string = "Hello";
console.log(str1 === str2); // true
console.log(str1 == str2);  // true

// Stringオブジェクトとの比較
// let strObj = new String("Hello");
// console.log(str1 === strObj); // false（型が異なる）
// console.log(str1 == strObj);  // true（型変換される）

// 実用的な例
let userName: string = "Alice";
let userInput: string = "Alice";
console.log(userName === userInput); // true

// 型安全な比較
if (userName === userInput) {
  console.log("ユーザー名が一致します");
}
``````

## File: 049.txt

# #049 「なぜstringを使うべきか」台本

```

## 📺 画面表示用コード

```typescript
// string型を使うべき理由

// 1. 型安全性
let userName: string = "Alice";
// userName = 123; // エラー: Type 'number' is not assignable to type 'string'

// 2. パフォーマンス
let message: string = "Hello, World!"; // 軽量なプリミティブ型

// 3. 一貫性
let userData = {
  name: "Bob",
  email: "bob@example.com"
};
let userInfo: string = `${userData.name} (${userData.email})`;

// 4. 予測可能な動作
let str1: string = "Hello";
let str2: string = "Hello";
console.log(str1 === str2); // 常にtrue
``````

## File: 050.txt

# #050 「String型使用禁止ルール」台本

```

## 📺 画面表示用コード

```typescript
// String型使用禁止ルール

// ❌ 禁止：String型の使用
// let name: String = new String("Alice");
// let message: String = new String("Hello");

// ✅ 推奨：string型の使用
let name: string = "Alice";
let message: string = "Hello";

// ✅ 推奨：型推論の活用
let userName = "Bob"; // string型と推論
let userEmail = "bob@example.com"; // string型と推論

// 実用的な例
let componentProps = {
  title: "ユーザー管理",
  description: "ユーザー情報の管理画面"
};
let pageTitle: string = componentProps.title;
``````

## File: 051.txt

# #051 「toUpperCase() - 大文字化」台本

```

## 📺 画面表示用コード

```typescript
// toUpperCase()の使用例
let name: string = "alice";
let email: string = "alice@example.com";
let message: string = "hello, world!";

// 大文字化
let upperName: string = name.toUpperCase(); // "ALICE"
let upperEmail: string = email.toUpperCase(); // "ALICE@EXAMPLE.COM"
let upperMessage: string = message.toUpperCase(); // "HELLO, WORLD!"

// 実用的な例
let userName: string = "bob";
let userRole: string = "admin";
let displayName: string = userName.toUpperCase();
let roleDisplay: string = userRole.toUpperCase();
``````

## File: 052.txt

# #052 「toUpperCase()の型」台本

```

## 📺 画面表示用コード

```typescript
// toUpperCase()の型
let name: string = "alice";
let result: string = name.toUpperCase(); // string型

// 型推論でもstring型
let inferred = "hello".toUpperCase(); // string型と推論

// 実用的な例
let userInput: string = "john doe";
let normalizedInput: string = userInput.toUpperCase(); // "JOHN DOE"

let productName: string = "typescript book";
let displayName: string = productName.toUpperCase(); // "TYPESCRIPT BOOK"

// 型チェック
console.log(typeof normalizedInput); // "string"
``````

## File: 053.txt

# #053 「toLowerCase() - 小文字化」台本

```

## 📺 画面表示用コード

```typescript
// toLowerCase()の使用例
let name: string = "ALICE";
let email: string = "ALICE@EXAMPLE.COM";
let message: string = "HELLO, WORLD!";

// 小文字化
let lowerName: string = name.toLowerCase(); // "alice"
let lowerEmail: string = email.toLowerCase(); // "alice@example.com"
let lowerMessage: string = message.toLowerCase(); // "hello, world!"

// 実用的な例
let userName: string = "BOB";
let userRole: string = "ADMIN";
let normalizedName: string = userName.toLowerCase();
let normalizedRole: string = userRole.toLowerCase();
``````

## File: 054.txt

# #054 「toLowerCase()の実例」台本

```

## 📺 画面表示用コード

```typescript
// toLowerCase()の実例

// 1. データの正規化
let userInput: string = "  ALICE  ";
let normalizedInput: string = userInput.trim().toLowerCase(); // "alice"

// 2. 比較処理
let storedName: string = "alice";
let inputName: string = "ALICE";
let isMatch: boolean = storedName === inputName.toLowerCase(); // true

// 3. 検索処理
let searchTerm: string = "TYPESCRIPT";
let content: string = "Learn TypeScript programming";
let isFound: boolean = content.toLowerCase().includes(searchTerm.toLowerCase());

// 実用的な例
let email: string = "USER@EXAMPLE.COM";
let normalizedEmail: string = email.toLowerCase(); // "user@example.com"
``````

## File: 055.txt

# #055 「charAt(index) - 文字取得」台本

```

## 📺 画面表示用コード

```typescript
// charAt()の使用例
let name: string = "Alice";
let message: string = "Hello, World!";

// 文字の取得
let firstChar: string = name.charAt(0); // "A"
let secondChar: string = name.charAt(1); // "l"
let lastChar: string = name.charAt(name.length - 1); // "e"

// 実用的な例
let userName: string = "Bob";
let userInitial: string = userName.charAt(0); // "B"

let productCode: string = "ABC123";
let category: string = productCode.charAt(0); // "A"
let subCategory: string = productCode.charAt(1); // "B"
``````

## File: 056.txt

# #056 「charAt()の型」台本

```

## 📺 画面表示用コード

```typescript
// charAt()の型
let name: string = "Alice";
let result: string = name.charAt(0); // string型

// 型推論でもstring型
let inferred = "Hello".charAt(1); // string型と推論

// 範囲外アクセス
let emptyResult: string = name.charAt(10); // ""（空文字列）

// 実用的な例
let userInput: string = "TypeScript";
let firstChar: string = userInput.charAt(0); // "T"
let lastChar: string = userInput.charAt(userInput.length - 1); // "t"

// 型チェック
console.log(typeof firstChar); // "string"
``````

## File: 057.txt

# #057 「charAt()範囲外アクセス」台本

```

## 📺 画面表示用コード

```typescript
// charAt()範囲外アクセス
let name: string = "Alice"; // 長さ5

// 範囲内アクセス
let validChar: string = name.charAt(0); // "A"
let validChar2: string = name.charAt(4); // "e"

// 範囲外アクセス
let invalidChar: string = name.charAt(5); // ""（空文字列）
let invalidChar2: string = name.charAt(-1); // ""（空文字列）
let invalidChar3: string = name.charAt(10); // ""（空文字列）

// 実用的な例
let userInput: string = "Hello";
let safeChar: string = userInput.charAt(userInput.length); // ""（安全）
``````

## File: 058.txt

# #058 「charCodeAt(index)」台本

```

## 📺 画面表示用コード

```typescript
// charCodeAt()の使用例
let name: string = "Alice";
let message: string = "Hello";

// Unicodeコードポイントの取得
let codeA: number = name.charCodeAt(0); // 65 (Aのコードポイント)
let codeL: number = name.charCodeAt(1); // 108 (lのコードポイント)
let codeH: number = message.charCodeAt(0); // 72 (Hのコードポイント)

// 実用的な例
let userInput: string = "ABC";
let codeA: number = userInput.charCodeAt(0); // 65
let codeB: number = userInput.charCodeAt(1); // 66
let codeC: number = userInput.charCodeAt(2); // 67

// 範囲外アクセス
let invalidCode: number = name.charCodeAt(10); // NaN
``````

## File: 059.txt

# #059 「indexOf(searchString)」台本

```

## 📺 画面表示用コード

```typescript
// indexOf()の使用例
let message: string = "Hello, World!";
let text: string = "TypeScript is great";

// 文字列の検索
let index1: number = message.indexOf("World"); // 7
let index2: number = message.indexOf("Hello"); // 0
let index3: number = text.indexOf("Script"); // 4

// 実用的な例
let userEmail: string = "alice@example.com";
let atIndex: number = userEmail.indexOf("@"); // 5
let domainStart: number = userEmail.indexOf("example"); // 6

let productName: string = "TypeScript Handbook";
let bookIndex: number = productName.indexOf("Book"); // -1（見つからない）
``````

## File: 060.txt

# #060 「indexOf()の戻り値」台本

```

## 📺 画面表示用コード

```typescript
// indexOf()の戻り値
let message: string = "Hello, World!";

// 見つかった場合
let foundIndex: number = message.indexOf("World"); // 7
let foundIndex2: number = message.indexOf("Hello"); // 0

// 見つからない場合
let notFoundIndex: number = message.indexOf("TypeScript"); // -1

// 型チェック
console.log(typeof foundIndex); // "number"
console.log(typeof notFoundIndex); // "number"

// 実用的な例
let userInput: string = "alice@example.com";
let atIndex: number = userInput.indexOf("@");
if (atIndex !== -1) {
  console.log("メールアドレス形式です");
}
``````

## File: 061.txt

# #061 「indexOf()で存在チェック」台本

```

## 📺 画面表示用コード

```typescript
// indexOf()で存在チェック
let message: string = "Hello, World!";
let userEmail: string = "alice@example.com";

// 存在チェック
let hasWorld: boolean = message.indexOf("World") !== -1; // true
let hasTypeScript: boolean = message.indexOf("TypeScript") !== -1; // false

// 実用的な例
let hasAtSymbol: boolean = userEmail.indexOf("@") !== -1; // true
let hasDomain: boolean = userEmail.indexOf(".com") !== -1; // true

// 条件分岐での使用
if (userEmail.indexOf("@") !== -1) {
  console.log("有効なメールアドレス形式です");
} else {
  console.log("無効なメールアドレス形式です");
}
``````

## File: 062.txt

# #062 「lastIndexOf()」台本

```

## 📺 画面表示用コード

```typescript
// lastIndexOf()の使用例
let message: string = "Hello, World! Hello, TypeScript!";
let text: string = "apple, banana, apple, orange";

// 最後の出現位置
let lastHello: number = message.lastIndexOf("Hello"); // 14
let lastApple: number = text.lastIndexOf("apple"); // 15

// 実用的な例
let filePath: string = "/home/user/documents/file.txt";
let lastSlash: number = filePath.lastIndexOf("/"); // 20
let fileName: string = filePath.substring(lastSlash + 1); // "file.txt"

let userEmail: string = "user.name@example.com";
let lastDot: number = userEmail.lastIndexOf("."); // 18
let extension: string = userEmail.substring(lastDot + 1); // "com"
``````

## File: 063.txt

# #063 「includes(searchString)」台本

```

## 📺 画面表示用コード

```typescript
// includes()の使用例
let message: string = "Hello, World!";
let text: string = "TypeScript is great";

// 包含チェック
let hasWorld: boolean = message.includes("World"); // true
let hasHello: boolean = message.includes("Hello"); // true
let hasTypeScript: boolean = text.includes("Script"); // true

// 実用的な例
let userEmail: string = "alice@example.com";
let hasAtSymbol: boolean = userEmail.includes("@"); // true
let hasDomain: boolean = userEmail.includes(".com"); // true

let productName: string = "TypeScript Handbook";
let isBook: boolean = productName.includes("Book"); // false
``````

## File: 064.txt

# #064 「includes()の型」台本

```

## 📺 画面表示用コード

```typescript
// includes()の型
let message: string = "Hello, World!";
let result: boolean = message.includes("World"); // boolean型

// 型推論でもboolean型
let inferred = "TypeScript".includes("Script"); // boolean型と推論

// 真偽値の例
let hasHello: boolean = message.includes("Hello"); // true
let hasTypeScript: boolean = message.includes("TypeScript"); // false

// 実用的な例
let userInput: string = "alice@example.com";
let isValidEmail: boolean = userInput.includes("@") && userInput.includes(".");

// 型チェック
console.log(typeof isValidEmail); // "boolean"
``````

## File: 065.txt

# #065 「startsWith(prefix)」台本

```

## 📺 画面表示用コード

```typescript
// startsWith()の使用例
let url: string = "https://example.com";
let filePath: string = "/home/user/documents/file.txt";
let message: string = "Hello, World!";

// 接頭辞チェック
let isHttps: boolean = url.startsWith("https://"); // true
let isAbsolute: boolean = filePath.startsWith("/"); // true
let startsWithHello: boolean = message.startsWith("Hello"); // true

// 実用的な例
let userInput: string = "admin@example.com";
let isAdmin: boolean = userInput.startsWith("admin"); // true

let apiEndpoint: string = "/api/users";
let isApiRoute: boolean = apiEndpoint.startsWith("/api"); // true
``````

## File: 066.txt

# #066 「endsWith(suffix)」台本

```

## 📺 画面表示用コード

```typescript
// endsWith()の使用例
let fileName: string = "document.pdf";
let url: string = "https://example.com/page.html";
let message: string = "Hello, World!";

// 接尾辞チェック
let isPdf: boolean = fileName.endsWith(".pdf"); // true
let isHtml: boolean = url.endsWith(".html"); // true
let endsWithWorld: boolean = message.endsWith("World!"); // true

// 実用的な例
let userEmail: string = "alice@example.com";
let isComDomain: boolean = userEmail.endsWith(".com"); // true

let imageFile: string = "photo.jpg";
let isImage: boolean = imageFile.endsWith(".jpg") || imageFile.endsWith(".png");
``````

## File: 067.txt

# #067 「substring(start, end)」台本

```

## 📺 画面表示用コード

```typescript
// substring()の使用例
let message: string = "Hello, World!";
let text: string = "TypeScript is great";

// 部分文字列の抽出
let hello: string = message.substring(0, 5); // "Hello"
let world: string = message.substring(7, 12); // "World"
let script: string = text.substring(4, 10); // "Script"

// 実用的な例
let userEmail: string = "alice@example.com";
let username: string = userEmail.substring(0, 5); // "alice"
let domain: string = userEmail.substring(6); // "example.com"

let filePath: string = "/home/user/file.txt";
let fileName: string = filePath.substring(filePath.lastIndexOf("/") + 1); // "file.txt"
``````

## File: 068.txt

# #068 「substring()の型」台本

```

## 📺 画面表示用コード

```typescript
// substring()の型
let message: string = "Hello, World!";
let result: string = message.substring(0, 5); // string型

// 型推論でもstring型
let inferred = "TypeScript".substring(0, 4); // string型と推論

// 戻り値の例
let hello: string = message.substring(0, 5); // "Hello"
let empty: string = message.substring(10, 5); // ""（空文字列）

// 実用的な例
let userInput: string = "alice@example.com";
let username: string = userInput.substring(0, 5); // "alice"

// 型チェック
console.log(typeof username); // "string"
``````

## File: 069.txt

# #069 「slice(start, end)」台本

```

## 📺 画面表示用コード

```typescript
// slice()の使用例
let message: string = "Hello, World!";
let text: string = "TypeScript";

// 部分文字列の抽出
let hello: string = message.slice(0, 5); // "Hello"
let world: string = message.slice(7, 12); // "World"
let script: string = text.slice(4); // "Script"

// 負のインデックス
let lastChar: string = message.slice(-1); // "!"
let lastWord: string = message.slice(-6, -1); // "World"
``````

## File: 070.txt

# #070 「split(separator)」台本

```

## 📺 画面表示用コード

```typescript
// split()の使用例
let message: string = "Hello,World,TypeScript";
let csv: string = "Alice,30,Tokyo";
let words: string = "Hello World TypeScript";

// 文字列の分割
let parts: string[] = message.split(","); // ["Hello", "World", "TypeScript"]
let userData: string[] = csv.split(","); // ["Alice", "30", "Tokyo"]
let wordArray: string[] = words.split(" "); // ["Hello", "World", "TypeScript"]

// 実用的な例
let email: string = "alice@example.com";
let emailParts: string[] = email.split("@"); // ["alice", "example.com"]
``````

## File: 071.txt

# #071 「string[]型とは」台本

```

## 📺 画面表示用コード

```typescript
// string[]型の例
let names: string[] = ["Alice", "Bob", "Charlie"];
let emails: string[] = ["alice@example.com", "bob@example.com"];
let tags: string[] = ["TypeScript", "JavaScript", "Web開発"];

// 実用的な例
let userRoles: string[] = ["admin", "user", "guest"];
let productCategories: string[] = ["本", "ペン", "ノート"];
let apiEndpoints: string[] = ["/api/users", "/api/products"];
``````

## File: 072.txt

# #072 「string配列の宣言」台本

```

## 📺 画面表示用コード

```typescript
// string配列の宣言
let names: string[] = [];
let emails: string[] = [];
let tags: string[] = [];

// 後で値を代入
names = ["Alice", "Bob", "Charlie"];
emails = ["alice@example.com", "bob@example.com"];

// 実用的な例
let userList: string[] = [];
let productNames: string[] = [];
let errorMessages: string[] = [];
``````

## File: 073.txt

# #073 「Array<string>記法」台本

```

## 📺 画面表示用コード

```typescript
// Array<string>記法
let names: Array<string> = ["Alice", "Bob", "Charlie"];
let emails: Array<string> = ["alice@example.com", "bob@example.com"];
let tags: Array<string> = ["TypeScript", "JavaScript"];

// string[]記法との比較
let names1: string[] = ["Alice", "Bob"];
let names2: Array<string> = ["Alice", "Bob"];

// 実用的な例
let userRoles: Array<string> = ["admin", "user"];
let productCategories: Array<string> = ["本", "ペン"];
``````

## File: 074.txt

# #074 「string配列の初期化」台本

```

## 📺 画面表示用コード

```typescript
// string配列の初期化
let names: string[] = ["Alice", "Bob", "Charlie"];
let emails: string[] = ["alice@example.com", "bob@example.com"];
let emptyArray: string[] = [];

// 実用的な例
let userRoles: string[] = ["admin", "user", "guest"];
let productCategories: string[] = ["本", "ペン", "ノート"];
let errorMessages: string[] = ["エラー1", "エラー2"];

// 型推論でも配列型
let inferred = ["TypeScript", "JavaScript"]; // string[]型と推論
``````

## File: 075.txt

# #075 「配列への要素追加」台本

```

## 📺 画面表示用コード

```typescript
// 配列への要素追加
let names: string[] = ["Alice", "Bob"];

// 末尾に追加
names.push("Charlie"); // ["Alice", "Bob", "Charlie"]

// 先頭に追加
names.unshift("David"); // ["David", "Alice", "Bob", "Charlie"]

// 実用的な例
let userList: string[] = ["admin"];
userList.push("user");
userList.push("guest");

let productTags: string[] = ["本"];
productTags.push("技術書");
productTags.push("TypeScript");
``````

## File: 076.txt

# #076 「配列の要素アクセス」台本

```

## 📺 画面表示用コード

```typescript
// 配列の要素アクセス
let names: string[] = ["Alice", "Bob", "Charlie"];

// インデックスでアクセス
let first: string = names[0]; // "Alice"
let second: string = names[1]; // "Bob"
let last: string = names[names.length - 1]; // "Charlie"

// 実用的な例
let userRoles: string[] = ["admin", "user", "guest"];
let adminRole: string = userRoles[0]; // "admin"
let userRole: string = userRoles[1]; // "user"
``````

## File: 077.txt

# #077 「配列のループ - for...of」台本

```

## 📺 画面表示用コード

```typescript
// 配列のループ
let names: string[] = ["Alice", "Bob", "Charlie"];

// for...of文
for (let name of names) {
  console.log(name);
}

// 実用的な例
let userRoles: string[] = ["admin", "user", "guest"];
for (let role of userRoles) {
  console.log(`Role: ${role}`);
}

let productTags: string[] = ["本", "ペン", "ノート"];
for (let tag of productTags) {
  console.log(`Tag: ${tag}`);
}
``````

## File: 078.txt

# #078 「配列のmap」台本

```

## 📺 画面表示用コード

```typescript
// 配列のmap
let names: string[] = ["alice", "bob", "charlie"];

// 大文字に変換
let upperNames: string[] = names.map(name => name.toUpperCase());
// ["ALICE", "BOB", "CHARLIE"]

// 実用的な例
let userEmails: string[] = ["alice@example.com", "bob@example.com"];
let usernames: string[] = userEmails.map(email => email.split("@")[0]);
// ["alice", "bob"]

let productNames: string[] = ["本", "ペン", "ノート"];
let displayNames: string[] = productNames.map(name => `商品: ${name}`);
``````

## File: 079.txt

# #079 「配列のfilter」台本

```

## 📺 画面表示用コード

```typescript
// 配列のfilter
let names: string[] = ["Alice", "Bob", "Charlie", "David"];

// 長さが4文字以上の名前を抽出
let longNames: string[] = names.filter(name => name.length >= 4);
// ["Alice", "Charlie", "David"]

// 実用的な例
let userRoles: string[] = ["admin", "user", "guest", "moderator"];
let adminRoles: string[] = userRoles.filter(role => role.includes("admin"));
// ["admin"]

let productTags: string[] = ["本", "ペン", "ノート", "技術書"];
let bookTags: string[] = productTags.filter(tag => tag.includes("本"));
// ["本", "技術書"]
``````

## File: 080.txt

# #080 「配列のjoin」台本

```

## 📺 画面表示用コード

```typescript
// 配列のjoin
let names: string[] = ["Alice", "Bob", "Charlie"];

// カンマで結合
let joined: string = names.join(", "); // "Alice, Bob, Charlie"

// 実用的な例
let userRoles: string[] = ["admin", "user", "guest"];
let roleList: string = userRoles.join(" | "); // "admin | user | guest"

let productTags: string[] = ["本", "ペン", "ノート"];
let tagString: string = productTags.join(", "); // "本, ペン, ノート"

let errorMessages: string[] = ["エラー1", "エラー2"];
let errorText: string = errorMessages.join("\n"); // 改行で結合
``````

## File: 081.txt

# #081 「Angularコンポーネントのstring型」台本

```

## 📺 画面表示用コード

```typescript
// Angularコンポーネントのstring型
import { Component } from '@angular/core';

@Component({
  selector: 'app-user',
  template: `
    <h1>{{title}}</h1>
    <p>{{message}}</p>
    <span>{{userName}}</span>
  `
})
export class UserComponent {
  title: string = "ユーザー管理";
  message: string = "ユーザー情報を表示中";
  userName: string = "Alice";
}
``````

## File: 082.txt

# #082 「テンプレートバインディング」台本

```

## 📺 画面表示用コード

```typescript
// テンプレートバインディング
import { Component } from '@angular/core';

@Component({
  selector: 'app-product',
  template: `
    <h2>{{productName}}</h2>
    <p>{{description}}</p>
    <span>{{price}}</span>
    <div>{{status}}</div>
  `
})
export class ProductComponent {
  productName: string = "TypeScript学習本";
  description: string = "TypeScriptの基礎から応用まで";
  price: string = "¥2,980";
  status: string = "在庫あり";
}
``````

## File: 083.txt

# #083 「Nest.jsのDTOとstring型」台本

```

## 📺 画面表示用コード

```typescript
// Nest.jsのDTOとstring型
import { IsString, IsEmail } from 'class-validator';

export class CreateUserDto {
  @IsString()
  name: string;

  @IsEmail()
  email: string;

  @IsString()
  role: string;
}

export class UpdateUserDto {
  @IsString()
  name?: string;

  @IsString()
  role?: string;
}
``````

## File: 084.txt

# #084 「@IsString()デコレータ」台本

```

## 📺 画面表示用コード

```typescript
// @IsString()デコレータ
import { IsString, IsOptional } from 'class-validator';

export class UserDto {
  @IsString()
  name: string;

  @IsString()
  email: string;

  @IsString()
  @IsOptional()
  description?: string;
}

export class ProductDto {
  @IsString()
  name: string;

  @IsString()
  category: string;

  @IsString()
  @IsOptional()
  tags?: string;
}
``````

## File: 085.txt

# #085 「バリデーション実例」台本

```

## 📺 画面表示用コード

```typescript
// バリデーション実例
import { IsString, IsNotEmpty, Length, IsEmail } from 'class-validator';

export class CreateUserDto {
  @IsString()
  @IsNotEmpty()
  @Length(1, 50)
  name: string;

  @IsString()
  @IsEmail()
  email: string;

  @IsString()
  @IsNotEmpty()
  @Length(3, 20)
  username: string;
}

export class UpdateProfileDto {
  @IsString()
  @IsOptional()
  @Length(0, 200)
  bio?: string;
}
``````

## File: 086.txt

# #086 「間違い(1) - Stringを使う」台本

```

## 📺 画面表示用コード

```typescript
// 間違い(1) - Stringを使う

// ❌ 間違い：String型の使用
// let name: String = new String("Alice");
// let message: String = new String("Hello");

// ✅ 正しい：string型の使用
let name: string = "Alice";
let message: string = "Hello";

// 実用的な例
let userName: string = "Bob";
let userEmail: string = "bob@example.com";
let userInfo: string = `${userName} (${userEmail})`;
``````

## File: 087.txt

# #087 「間違い(2) - nullとの混同」台本

```

## 📺 画面表示用コード

```typescript
// 間違い(2) - nullとの混同

// ❌ 間違い：型の混同
// let name: string = null; // エラー

// ✅ 正しい：null許可型の使用
let name: string | null = null;
let message: string | null = "Hello";

// 実用的な例
let userName: string | null = null;
let userEmail: string | null = "alice@example.com";

// nullチェック
if (userName !== null) {
  console.log(userName.toUpperCase());
}
``````

## File: 088.txt

# #088 「間違い(3) - undefinedとの混同」台本

```

## 📺 画面表示用コード

```typescript
// 間違い(3) - undefinedとの混同

// ❌ 間違い：型の混同
// let name: string = undefined; // エラー

// ✅ 正しい：undefined許可型の使用
let name: string | undefined = undefined;
let message: string | undefined = "Hello";

// 実用的な例
let userName: string | undefined = undefined;
let userEmail: string | undefined = "alice@example.com";

// undefinedチェック
if (userName !== undefined) {
  console.log(userName.toUpperCase());
}
``````

## File: 089.txt

# #089 「デバッグ(1) - 型エラーの読み方」台本

```

## 📺 画面表示用コード

```typescript
// デバッグ(1) - 型エラーの読み方

// 型の不一致エラー
let name: string = "Alice";
// name = 123; // エラー: Type 'number' is not assignable to type 'string'

// 未定義変数エラー
// let message: string;
// console.log(message); // エラー: Variable 'message' is used before being assigned

// 正しい方法
let userName: string = "Bob";
let userMessage: string = "Hello, " + userName;
console.log(userMessage);
``````

## File: 090.txt

# #090 「デバッグ(2) - 実行時エラー」台本

```

## 📺 画面表示用コード

```typescript
// デバッグ(2) - 実行時エラー

// null参照エラーの回避
let name: string | null = null;
if (name !== null) {
  console.log(name.toUpperCase()); // 安全
}

// 未定義プロパティの回避
let user: { name?: string } = {};
if (user.name) {
  console.log(user.name.toUpperCase()); // 安全
}

// 型変換エラーの回避
let input: unknown = "Hello";
if (typeof input === "string") {
  console.log(input.toUpperCase()); // 安全
}
``````

## File: 091.txt

# #091 「パフォーマンス最適化(1)」台本

```

## 📺 画面表示用コード

```typescript
// パフォーマンス最適化(1)

// 効率的な文字列結合
let name: string = "Alice";
let age: number = 30;
let message: string = `Name: ${name}, Age: ${age}`; // テンプレートリテラル

// 非効率な結合
// let message: string = "Name: " + name + ", Age: " + age;

// 実用的な例
let userInfo: string = `User: ${name}`;
let productInfo: string = `Product: TypeScript Book`;
let apiResponse: string = `Status: Success`;
``````

## File: 092.txt

# #092 「パフォーマンス最適化(2)」台本

```

## 📺 画面表示用コード

```typescript
// パフォーマンス最適化(2)

// 効率的な型使用
let names: string[] = ["Alice", "Bob", "Charlie"];
let upperNames: string[] = names.map(name => name.toUpperCase());

// 非効率な方法
// let upperNames: string[] = [];
// for (let i = 0; i < names.length; i++) {
//   upperNames.push(names[i].toUpperCase());
// }

// 実用的な例
let userRoles: string[] = ["admin", "user", "guest"];
let filteredRoles: string[] = userRoles.filter(role => role !== "guest");
let roleString: string = filteredRoles.join(", ");
``````

## File: 093.txt

# #093 「セキュリティ - XSS対策」台本

```

## 📺 画面表示用コード

```typescript
// セキュリティ - XSS対策

// 入力値の検証
function sanitizeInput(input: string): string {
  return input.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '');
}

// 安全な文字列処理
let userInput: string = "<script>alert('XSS')</script>";
let safeInput: string = sanitizeInput(userInput);

// 実用的な例
let userName: string = "Alice";
let userMessage: string = "Hello, World!";
let displayText: string = `${userName}: ${userMessage}`;
``````

## File: 094.txt

# #094 「ベストプラクティス(1)」台本

```

## 📺 画面表示用コード

```typescript
// ベストプラクティス(1)

// 1. 型の一貫性
let userName: string = "Alice";
let userEmail: string = "alice@example.com";
let userRole: string = "admin";

// 2. 適切な命名
let productName: string = "TypeScript Book";
let productDescription: string = "Learn TypeScript";
let productPrice: string = "¥2,980";

// 3. 型安全性の確保
let apiEndpoint: string = "/api/users";
let errorMessage: string = "An error occurred";
let successMessage: string = "Operation completed";
``````

## File: 095.txt

# #095 「ベストプラクティス(2)」台本

```

## 📺 画面表示用コード

```typescript
// ベストプラクティス(2)

// 1. 定数の使用
const API_BASE_URL: string = "https://api.example.com";
const DEFAULT_MESSAGE: string = "Loading...";

// 2. テンプレートリテラル
let userName: string = "Alice";
let welcomeMessage: string = `Welcome, ${userName}!`;

// 3. 配列処理
let tags: string[] = ["TypeScript", "JavaScript", "Web"];
let tagString: string = tags.join(", ");
``````

## File: 096.txt

# #096 「ベストプラクティス(3)」台本

```

## 📺 画面表示用コード

```typescript
// ベストプラクティス(3)

// 1. 型ガード
function isString(value: unknown): value is string {
  return typeof value === "string";
}

// 2. ユニオン型
let status: "loading" | "success" | "error" = "loading";

// 3. オプショナル型
let userName: string | undefined = undefined;
let userEmail: string | null = null;

// 実用的な例
if (isString(userName)) {
  console.log(userName.toUpperCase());
}
``````

## File: 097.txt

# #097 「実践パターン(1)」台本

```

## 📺 画面表示用コード

```typescript
// 実践パターン(1)

// 1. フォーム処理
interface UserForm {
  name: string;
  email: string;
  message: string;
}

let formData: UserForm = {
  name: "Alice",
  email: "alice@example.com",
  message: "Hello, World!"
};

// 2. API通信
let apiUrl: string = "https://api.example.com/users";
let requestBody: string = JSON.stringify(formData);

// 3. データ変換
let userInfo: string = `${formData.name} (${formData.email})`;
``````

## File: 098.txt

# #098 「実践パターン(2)」台本

```

## 📺 画面表示用コード

```typescript
// 実践パターン(2)

// 1. バリデーション
function validateEmail(email: string): boolean {
  return email.includes("@") && email.includes(".");
}

// 2. エラーハンドリング
try {
  let userInput: string = "invalid input";
  if (!validateEmail(userInput)) {
    throw new Error("Invalid email format");
  }
} catch (error) {
  let errorMessage: string = `Error: ${error.message}`;
  console.log(errorMessage);
}

// 3. ログ出力
let logMessage: string = `User action: ${new Date().toISOString()}`;
console.log(logMessage);
``````

## File: 099.txt

# #099 「総まとめ」台本

```

## 📺 画面表示用コード

```typescript
// 総まとめ

// 1. 基本概念
let name: string = "Alice";
let message: string = "Hello, World!";

// 2. テンプレートリテラル
let greeting: string = `Hello, ${name}!`;

// 3. 文字列メソッド
let upperName: string = name.toUpperCase();
let lowerName: string = name.toLowerCase();
let nameLength: number = name.length;

// 4. 配列処理
let names: string[] = ["Alice", "Bob", "Charlie"];
let joinedNames: string = names.join(", ");
``````

## File: 100.txt

# #100 「マスターチェック」台本

```

## 📺 画面表示用コード

```typescript
// マスターチェック

// 1. 型の理解
let userName: string = "Alice";
let userEmail: string = "alice@example.com";

// 2. メソッドの使用
let upperName: string = userName.toUpperCase();
let emailDomain: string = userEmail.split("@")[1];

// 3. 実践的な応用
let userInfo: string = `${userName} (${userEmail})`;
let isValidEmail: boolean = userEmail.includes("@") && userEmail.includes(".");

// 4. 配列処理
let userRoles: string[] = ["admin", "user"];
let roleString: string = userRoles.join(" | ");
``````

## File: 101.txt

# #101 「number型とは - 数値を扱う型」台本

```

## 📺 画面表示用コード

```typescript
// number型の基本
let age: number = 30;
let price: number = 2980.50;
let count: number = -5;

// 実用的な例
let userAge: number = 25;
let productPrice: number = 1500;
let discountRate: number = 0.1;
let finalPrice: number = productPrice * (1 - discountRate);
``````

## File: 102.txt

# #102 「number型の宣言 - let age: number」台本

```

## 📺 画面表示用コード

```typescript
// number型の宣言
let age: number;
let price: number;
let count: number;

// 後で値を代入
age = 30;
price = 2980.50;
count = -5;

// 実用的な例
let userAge: number = 25;
let productPrice: number = 1500;
let itemCount: number = 10;
``````

## File: 103.txt

# #103 「number型への代入」台本

```

## 📺 画面表示用コード

```typescript
// number型への代入
let value: number;

// 数値の代入
value = 100;        // OK
value = 3.14;       // OK
value = -50;        // OK
value = 1e6;        // OK

// 型エラーの例
// value = "100";   // エラー: Type 'string' is not assignable to type 'number'
// value = true;    // エラー: Type 'boolean' is not assignable to type 'number'
``````

## File: 104.txt

# #104 「number型の初期化」台本

```

## 📺 画面表示用コード

```typescript
// number型の初期化
let age: number = 30;
let price: number = 2980.50;
let count: number = 0;
let result: number = 10 * 5 + 3;

// 実用的な例
let userAge: number = 25;
let productPrice: number = 1500;
let taxRate: number = 0.1;
let totalPrice: number = productPrice * (1 + taxRate);
``````

## File: 105.txt

# #105 「型推論でnumber型」台本

```

## 📺 画面表示用コード

```typescript
// 型推論の例
let age = 30;           // number型と推論
let price = 2980.50;    // number型と推論
let count = -5;         // number型と推論

// 型安全性は保たれる
// age = "30"; // エラー: Type 'string' is not assignable to type 'number'

// 実用的な例
let userAge = 25;       // number型
let productPrice = 1500; // number型
let discountRate = 0.1;  // number型
``````

## File: 106.txt

# #106 「constでnumber型」台本

```

## 📺 画面表示用コード

```typescript
// constでの定数宣言
const MAX_USERS = 1000;
const PI = 3.14159;
const TAX_RATE = 0.1;

// 再代入はエラー
// MAX_USERS = 2000; // エラー: Cannot assign to 'MAX_USERS' because it is a constant

// 実用的な例
const API_TIMEOUT = 5000;
const MAX_RETRY_COUNT = 3;
const DEFAULT_PAGE_SIZE = 20;
``````

## File: 107.txt

# #107 「number型とリテラル型」台本

```

## 📺 画面表示用コード

```typescript
// number型 - 任意の数値
let value: number = 100;
value = 200; // OK
value = 3.14; // OK

// リテラル型 - 特定の数値のみ
let status: 0 | 1 | 2 = 0;
// status = 3; // エラー: Type '3' is not assignable to type '0 | 1 | 2'

// 実用的な例
let httpStatus: 200 | 404 | 500 = 200;
let userLevel: 1 | 2 | 3 = 1;
``````

## File: 108.txt

# #108 「整数と小数の区別なし」台本

```

## 📺 画面表示用コード

```typescript
// 整数と小数の区別なし
let integer: number = 100;    // 整数
let decimal: number = 3.14;   // 小数
let negative: number = -50;   // 負数

// すべて同じnumber型
console.log(typeof integer);  // "number"
console.log(typeof decimal);  // "number"
console.log(typeof negative); // "number"

// 実用的な例
let userAge: number = 25;     // 整数
let productPrice: number = 2980.50; // 小数
let discountRate: number = 0.1;     // 小数
``````

## File: 109.txt

# #109 「number型の範囲 - MAX_VALUE」台本

```

## 📺 画面表示用コード

```typescript
// number型の範囲
let maxValue: number = Number.MAX_VALUE;
let minValue: number = Number.MIN_VALUE;

console.log(maxValue); // 1.7976931348623157e+308
console.log(minValue); // 5e-324

// 実用的な例
let largeNumber: number = 1e10;
let smallNumber: number = 1e-10;

// 範囲チェック
if (largeNumber < Number.MAX_VALUE) {
  console.log("安全な範囲内です");
}
``````

## File: 110.txt

# #110 「number型の最小値 - MIN_VALUE」台本

```

## 📺 画面表示用コード

```typescript
// number型の最小値
let minValue: number = Number.MIN_VALUE;
let maxValue: number = Number.MAX_VALUE;

console.log(minValue); // 5e-324
console.log(maxValue); // 1.7976931348623157e+308

// 実用的な例
let tinyNumber: number = 1e-100;
let normalNumber: number = 1e-10;

// 最小値チェック
if (tinyNumber > Number.MIN_VALUE) {
  console.log("最小値より大きいです");
}
``````

## File: 111.txt

# #111 「10進数リテラル」台本

```

## 📺 画面表示用コード

```typescript
// 10進数リテラル
let integer: number = 100;    // 整数
let decimal: number = 3.14;   // 小数
let negative: number = -50;   // 負数
let zero: number = 0;         // ゼロ

// 実用的な例
let userAge: number = 25;
let productPrice: number = 2980;
let discountRate: number = 0.1;
let taxRate: number = 0.08;
``````

## File: 112.txt

# #112 「2進数リテラル - 0b1010」台本

```

## 📺 画面表示用コード

```typescript
// 2進数リテラル
let binary1: number = 0b1010;  // 10
let binary2: number = 0b1111;  // 15
let binary3: number = 0b0001;  // 1

// 実用的な例
let flag1: number = 0b0001;    // フラグ1
let flag2: number = 0b0010;    // フラグ2
let flag3: number = 0b0100;    // フラグ3
let combined: number = flag1 | flag2; // フラグの組み合わせ
``````

## File: 113.txt

# #113 「2進数の型」台本

```

## 📺 画面表示用コード

```typescript
// 2進数の型
let binary: number = 0b1010;  // number型
let decimal: number = 10;     // number型

// 型は同じ
console.log(typeof binary);   // "number"
console.log(typeof decimal);  // "number"

// 値も同じ
console.log(binary === decimal); // true

// 実用的な例
let flag: number = 0b0001;
let value: number = 1;
console.log(flag === value); // true
``````

## File: 114.txt

# #114 「8進数リテラル - 0o777」台本

```

## 📺 画面表示用コード

```typescript
// 8進数リテラル
let octal1: number = 0o777;   // 511
let octal2: number = 0o644;   // 420
let octal3: number = 0o755;   // 493

// 実用的な例
let filePermission: number = 0o644;  // ファイル権限
let dirPermission: number = 0o755;   // ディレクトリ権限
let scriptPermission: number = 0o755; // スクリプト権限
``````

## File: 115.txt

# #115 「16進数リテラル - 0xFF」台本

```

## 📺 画面表示用コード

```typescript
// 16進数リテラル
let hex1: number = 0xFF;      // 255
let hex2: number = 0x10;      // 16
let hex3: number = 0xABCD;    // 43981

// 実用的な例
let redColor: number = 0xFF0000;    // 赤色
let greenColor: number = 0x00FF00;  // 緑色
let blueColor: number = 0x0000FF;   // 青色
let whiteColor: number = 0xFFFFFF;  // 白色
``````

## File: 116.txt

# #116 「科学的記数法 - 1e6」台本

```

## 📺 画面表示用コード

```typescript
// 科学的記数法
let large: number = 1e6;      // 1,000,000
let small: number = 1e-6;     // 0.000001
let veryLarge: number = 1e9;  // 1,000,000,000

// 実用的な例
let million: number = 1e6;    // 100万
let billion: number = 1e9;    // 10億
let microsecond: number = 1e-6; // マイクロ秒
let nanosecond: number = 1e-9;  // ナノ秒
``````

## File: 117.txt

# #117 「アンダースコア区切り - 1_000_000」台本

```

## 📺 画面表示用コード

```typescript
// アンダースコア区切り
let million: number = 1_000_000;
let billion: number = 1_000_000_000;
let price: number = 2_980_500;

// 実用的な例
let maxUsers: number = 10_000;
let apiTimeout: number = 30_000;  // 30秒
let fileSize: number = 1_024_000; // 1MB
let memoryLimit: number = 512_000_000; // 512MB
``````

## File: 118.txt

# #118 「数値リテラルの型推論」台本

```

## 📺 画面表示用コード

```typescript
// 数値リテラル型推論
let value = 100;        // number型と推論
let price = 2980.50;    // number型と推論

// constではリテラル型
const MAX_USERS = 1000; // 1000型と推論
const PI = 3.14159;     // 3.14159型と推論

// 実用的な例
let userAge = 25;       // number型
const API_TIMEOUT = 5000; // 5000型
``````

## File: 119.txt

# #119 「数値リテラルとconst」台本

```

## 📺 画面表示用コード

```typescript
// 数値リテラルとconst
const MAX_USERS = 1000;     // 1000型と推論
const PI = 3.14159;         // 3.14159型と推論
const TAX_RATE = 0.1;       // 0.1型と推論

// 型の違い
let value = 1000;           // number型
const constant = 1000;      // 1000型

// 実用的な例
const API_TIMEOUT = 5000;   // 5000型
const MAX_RETRY = 3;        // 3型
const DEFAULT_SIZE = 20;    // 20型
``````

## File: 120.txt

# #120 「数値リテラルまとめ」台本

```

## 📺 画面表示用コード

```typescript
// 数値リテラルまとめ
let decimal: number = 100;        // 10進数
let binary: number = 0b1010;      // 2進数
let octal: number = 0o777;        // 8進数
let hex: number = 0xFF;           // 16進数
let scientific: number = 1e6;     // 科学的記数法
let readable: number = 1_000_000; // アンダースコア区切り

// 実用的な例
let userAge: number = 25;
let productPrice: number = 2980.50;
let maxUsers: number = 10_000;
let apiTimeout: number = 30_000;
``````

## File: 121.txt

# #121 「Infinityとは」台本

```

## 📺 画面表示用コード

```typescript
// Infinityとは
let infinity: number = Infinity;
let negativeInfinity: number = -Infinity;

// 実用的な例
let maxValue: number = Infinity;
let minValue: number = -Infinity;

// 計算で生成される
let result1: number = 1 / 0; // Infinity
let result2: number = -1 / 0; // -Infinity

console.log(infinity); // Infinity
console.log(result1); // Infinity
``````

## File: 122.txt

# #122 「Infinityの型」台本

```

## 📺 画面表示用コード

```typescript
// Infinityの型
let infinity: number = Infinity;
let normalNumber: number = 100;

// 型は同じ
console.log(typeof infinity);    // "number"
console.log(typeof normalNumber); // "number"

// 実用的な例
let maxValue: number = Infinity;
let userAge: number = 25;

// 型チェック
console.log(typeof maxValue); // "number"
console.log(typeof userAge);  // "number"
``````

## File: 123.txt

# #123 「Infinityの生成 - 1/0」台本

```

## 📺 画面表示用コード

```typescript
// Infinityの生成
let result1: number = 1 / 0;        // Infinity
let result2: number = -1 / 0;       // -Infinity
let result3: number = Number.MAX_VALUE * 2; // Infinity

// 実用的な例
let division: number = 100 / 0;     // Infinity
let multiplication: number = Number.MAX_VALUE * 10; // Infinity

console.log(result1); // Infinity
console.log(result2); // -Infinity
console.log(division); // Infinity
``````

## File: 124.txt

# #124 「-Infinity」台本

```

## 📺 画面表示用コード

```typescript
// -Infinity
let negativeInfinity: number = -Infinity;
let positiveInfinity: number = Infinity;

// 実用的な例
let minValue: number = -Infinity;
let maxValue: number = Infinity;

// 計算で生成される
let result: number = -1 / 0; // -Infinity

console.log(negativeInfinity); // -Infinity
console.log(minValue); // -Infinity
console.log(result); // -Infinity
``````

## File: 125.txt

# #125 「NaNとは」台本

```

## 📺 画面表示用コード

```typescript
// NaNとは
let nan: number = NaN;
let invalidResult: number = 0 / 0;

// 実用的な例
let parseResult: number = parseInt("abc"); // NaN
let mathResult: number = Math.sqrt(-1); // NaN

console.log(nan); // NaN
console.log(invalidResult); // NaN
console.log(parseResult); // NaN
``````

## File: 126.txt

# #126 「NaNの型」台本

```

## 📺 画面表示用コード

```typescript
// NaNの型
let nan: number = NaN;
let normalNumber: number = 100;

// 型は同じ
console.log(typeof nan);        // "number"
console.log(typeof normalNumber); // "number"

// 実用的な例
let invalidResult: number = NaN;
let validResult: number = 42;

// 型チェック
console.log(typeof invalidResult); // "number"
console.log(typeof validResult);   // "number"
``````

## File: 127.txt

# #127 「NaNの生成 - 0/0」台本

```

## 📺 画面表示用コード

```typescript
// NaNの生成
let result1: number = 0 / 0;        // NaN
let result2: number = NaN + 1;      // NaN
let result3: number = Math.sqrt(-1); // NaN

// 実用的な例
let division: number = 0 / 0;       // NaN
let parseError: number = parseInt("abc"); // NaN
let invalidMath: number = Math.log(-1); // NaN

console.log(result1); // NaN
console.log(division); // NaN
console.log(parseError); // NaN
``````

## File: 128.txt

# #128 「isNaN()関数」台本

```

## 📺 画面表示用コード

```typescript
// isNaN()関数
let nan: number = NaN;
let normalNumber: number = 100;
let stringValue: string = "abc";

// NaN判定
let isNan1: boolean = isNaN(nan);        // true
let isNan2: boolean = isNaN(normalNumber); // false
let isNan3: boolean = isNaN(stringValue);  // true

// 実用的な例
let userInput: number = parseInt("123");
if (isNaN(userInput)) {
  console.log("無効な数値です");
} else {
  console.log("有効な数値です");
}
``````

## File: 129.txt

# #129 「Number.isNaN()の違い」台本

```

## 📺 画面表示用コード

```typescript
// Number.isNaN()の違い
let nan: number = NaN;
let stringValue: string = "abc";

// isNaN() - 型変換あり
let isNan1: boolean = isNaN(nan);        // true
let isNan2: boolean = isNaN(stringValue);  // true (型変換される)

// Number.isNaN() - 型変換なし
let isNan3: boolean = Number.isNaN(nan);        // true
let isNan4: boolean = Number.isNaN(stringValue);  // false (型変換されない)

// 実用的な例
let userInput: number = parseInt("abc");
if (Number.isNaN(userInput)) {
  console.log("数値ではありません");
}
``````

## File: 130.txt

# #130 「isFinite()関数」台本

```

## 📺 画面表示用コード

```typescript
// isFinite()関数
let normalNumber: number = 100;
let infinity: number = Infinity;
let nan: number = NaN;

// 有限数判定
let isFinite1: boolean = isFinite(normalNumber); // true
let isFinite2: boolean = isFinite(infinity);     // false
let isFinite3: boolean = isFinite(nan);          // false

// 実用的な例
let userInput: number = parseFloat("123.45");
if (isFinite(userInput)) {
  console.log("有効な数値です");
} else {
  console.log("無効な数値です");
}
``````

## File: 131.txt

# #131 「Number.isFinite()」台本

```

## 📺 画面表示用コード

```typescript
// Number.isFinite()
let normalNumber: number = 100;
let stringNumber: string = "123";

// isFinite() - 型変換あり
let isFinite1: boolean = isFinite(normalNumber); // true
let isFinite2: boolean = isFinite(stringNumber); // true (型変換される)

// Number.isFinite() - 型変換なし
let isFinite3: boolean = Number.isFinite(normalNumber); // true
let isFinite4: boolean = Number.isFinite(stringNumber); // false (型変換されない)

// 実用的な例
let userInput: number = 42;
if (Number.isFinite(userInput)) {
  console.log("有効な数値です");
}
``````

## File: 132.txt

# #132 「Number.isInteger()」台本

```

## 📺 画面表示用コード

```typescript
// Number.isInteger()
let integer: number = 42;
let decimal: number = 3.14;
let stringNumber: string = "123";

// 整数判定
let isInteger1: boolean = Number.isInteger(integer);     // true
let isInteger2: boolean = Number.isInteger(decimal);     // false
let isInteger3: boolean = Number.isInteger(stringNumber); // false

// 実用的な例
let userAge: number = 25;
if (Number.isInteger(userAge)) {
  console.log("整数の年齢です");
} else {
  console.log("小数の年齢は無効です");
}
``````

## File: 133.txt

# #133 「Number.isSafeInteger()」台本

```

## 📺 画面表示用コード

```typescript
// Number.isSafeInteger()
let safeInteger: number = 42;
let unsafeInteger: number = Number.MAX_SAFE_INTEGER + 1;

// 安全整数判定
let isSafe1: boolean = Number.isSafeInteger(safeInteger);   // true
let isSafe2: boolean = Number.isSafeInteger(unsafeInteger); // false

// 実用的な例
let userId: number = 12345;
if (Number.isSafeInteger(userId)) {
  console.log("安全な整数IDです");
} else {
  console.log("精度を失う可能性があります");
}
``````

## File: 134.txt

# #134 「特殊な数値のベストプラクティス」台本

```

## 📺 画面表示用コード

```typescript
// 特殊な数値のベストプラクティス

// 1. 適切な判定関数の使用
let value: number = parseFloat("abc");
if (Number.isNaN(value)) {
  console.log("無効な数値です");
}

// 2. 有限数チェック
let result: number = 1 / 0;
if (Number.isFinite(result)) {
  console.log("有効な数値です");
} else {
  console.log("無限大またはNaNです");
}

// 3. 安全整数チェック
let largeNumber: number = 9007199254740992;
if (Number.isSafeInteger(largeNumber)) {
  console.log("安全な整数です");
}
``````

## File: 135.txt

# #135 「特殊な数値まとめ」台本

```

## 📺 画面表示用コード

```typescript
// 特殊な数値まとめ

// 1. 特殊な数値
let infinity: number = Infinity;
let negativeInfinity: number = -Infinity;
let nan: number = NaN;

// 2. 判定関数
let isNan: boolean = Number.isNaN(nan);
let isFinite: boolean = Number.isFinite(infinity);
let isInteger: boolean = Number.isInteger(42);
let isSafe: boolean = Number.isSafeInteger(123);

// 3. 実用的な例
let userInput: number = parseFloat("123.45");
if (Number.isFinite(userInput) && Number.isSafeInteger(userInput)) {
  console.log("有効な整数です");
}
``````

## File: 136.txt

# #136 「加算演算子 - a + b」台本

```

## 📺 画面表示用コード

```typescript
// 加算演算子
let a: number = 10;
let b: number = 20;
let sum: number = a + b; // 30

// 実用的な例
let price: number = 1000;
let tax: number = 100;
let total: number = price + tax; // 1100

let userAge: number = 25;
let yearsToAdd: number = 5;
let futureAge: number = userAge + yearsToAdd; // 30
``````

## File: 137.txt

# #137 「加算の型推論」台本

```

## 📺 画面表示用コード

```typescript
// 加算の型推論
let a: number = 10;
let b: number = 20;
let sum = a + b; // number型と推論

// 型推論の例
let price = 1000;    // number型
let tax = 100;       // number型
let total = price + tax; // number型と推論

// 実用的な例
let userAge = 25;
let yearsToAdd = 5;
let futureAge = userAge + yearsToAdd; // number型
``````

## File: 138.txt

# #138 「減算演算子」台本

```

## 📺 画面表示用コード

```typescript
// 減算演算子
let a: number = 30;
let b: number = 10;
let difference: number = a - b; // 20

// 実用的な例
let totalPrice: number = 1200;
let discount: number = 200;
let finalPrice: number = totalPrice - discount; // 1000

let currentYear: number = 2024;
let birthYear: number = 1990;
let age: number = currentYear - birthYear; // 34
``````

## File: 139.txt

# #139 「減算の型推論」台本

```

## 📺 画面表示用コード

```typescript
// 減算の型推論
let a: number = 30;
let b: number = 10;
let difference = a - b; // number型と推論

// 型推論の例
let totalPrice = 1200;  // number型
let discount = 200;     // number型
let finalPrice = totalPrice - discount; // number型と推論

// 実用的な例
let currentYear = 2024;
let birthYear = 1990;
let age = currentYear - birthYear; // number型
``````

## File: 140.txt

# #140 「乗算演算子」台本

```

## 📺 画面表示用コード

```typescript
// 乗算演算子
let a: number = 5;
let b: number = 6;
let product: number = a * b; // 30

// 実用的な例
let price: number = 1000;
let quantity: number = 3;
let total: number = price * quantity; // 3000

let rate: number = 0.1;
let amount: number = 5000;
let tax: number = amount * rate; // 500
```

```

## File: 141.txt

# #141 「乗算の型推論」台本

```

## 📺 画面表示用コード

```typescript
// 乗算の型推論
let a: number = 5;
let b: number = 6;
let product = a * b; // number型と推論

// 型推論の例
let price = 1000;    // number型
let quantity = 3;    // number型
let total = price * quantity; // number型と推論

// 実用的な例
let rate = 0.1;
let amount = 5000;
let tax = amount * rate; // number型
```

```

## File: 142.txt

# #142 「除算演算子」台本

```

## 📺 画面表示用コード

```typescript
// 除算演算子
let a: number = 20;
let b: number = 4;
let quotient: number = a / b; // 5

// 実用的な例
let totalAmount: number = 1200;
let people: number = 4;
let perPerson: number = totalAmount / people; // 300

let price: number = 1000;
let discountRate: number = 0.2;
let discountAmount: number = price * discountRate; // 200
```

```

## File: 143.txt

# #143 「除算の型推論」台本

```

## 📺 画面表示用コード

```typescript
// 除算の型推論
let a: number = 20;
let b: number = 4;
let quotient = a / b; // number型と推論

// 型推論の例
let totalAmount = 1200; // number型
let people = 4;         // number型
let perPerson = totalAmount / people; // number型と推論

// 実用的な例
let price = 1000;
let discountRate = 0.2;
let discountAmount = price * discountRate; // number型
```

```

## File: 144.txt

# #144 「剰余演算子」台本

```

## 📺 画面表示用コード

```typescript
// 剰余演算子
let a: number = 17;
let b: number = 5;
let remainder: number = a % b; // 2

// 実用的な例
let number: number = 42;
let isEven: boolean = number % 2 === 0; // true

let seconds: number = 125;
let minutes: number = Math.floor(seconds / 60);
let remainingSeconds: number = seconds % 60; // 5
```

```

## File: 145.txt

# #145 「剰余の型推論」台本

```

## 📺 画面表示用コード

```typescript
// 剰余の型推論
let a: number = 17;
let b: number = 5;
let remainder = a % b; // number型と推論

// 型推論の例
let number = 42;       // number型
let isEven = number % 2 === 0; // boolean型と推論

// 実用的な例
let seconds = 125;
let minutes = Math.floor(seconds / 60);
let remainingSeconds = seconds % 60; // number型
```

```

## File: 146.txt

# #146 「べき乗演算子 - a ** b」台本

```

## 📺 画面表示用コード

```typescript
// べき乗演算子
let base: number = 2;
let exponent: number = 3;
let result: number = base ** exponent; // 8

// 実用的な例
let side: number = 5;
let area: number = side ** 2; // 25 (正方形の面積)

let rate: number = 1.1;
let years: number = 3;
let finalAmount: number = 1000 * (rate ** years); // 複利計算
```

```

## File: 147.txt

# #147 「べき乗の型推論」台本

```

## 📺 画面表示用コード

```typescript
// べき乗の型推論
let base: number = 2;
let exponent: number = 3;
let result = base ** exponent; // number型と推論

// 型推論の例
let side = 5;          // number型
let area = side ** 2;  // number型と推論

// 実用的な例
let rate = 1.1;
let years = 3;
let finalAmount = 1000 * (rate ** years); // number型
```

```

## File: 148.txt

# #148 「インクリメント - ++i」台本

```

## 📺 画面表示用コード

```typescript
// インクリメント
let count: number = 5;
count++; // 6 (後置インクリメント)
++count; // 7 (前置インクリメント)

// 実用的な例
let index: number = 0;
index++; // 1

let score: number = 100;
++score; // 101

// ループでの使用
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```

```

## File: 149.txt

# #149 「デクリメント - --i」台本

```

## 📺 画面表示用コード

```typescript
// デクリメント
let count: number = 5;
count--; // 4 (後置デクリメント)
--count; // 3 (前置デクリメント)

// 実用的な例
let index: number = 10;
index--; // 9

let score: number = 100;
--score; // 99

// ループでの使用
for (let i = 5; i > 0; i--) {
  console.log(i);
}
```

```

## File: 150.txt

# #150 「単項プラス - +x」台本

```

## 📺 画面表示用コード

```typescript
// 単項プラス
let negative: number = -5;
let positive: number = +negative; // -5 (符号は変わらない)

// 型変換での使用
let stringNumber: string = "123";
let number: number = +stringNumber; // 123

// 実用的な例
let userInput: string = "42";
let numericValue: number = +userInput; // 42

let absoluteValue: number = +Math.abs(-10); // 10
```

```

## File: 151.txt

# #151 「単項マイナス - -x」台本

```

## 📺 画面表示用コード

```typescript
// 単項マイナス
let positive: number = 5;
let negative: number = -positive; // -5

let negative2: number = -10;
let positive2: number = -negative2; // 10

// 実用的な例
let price: number = 1000;
let discount: number = -price; // -1000

let temperature: number = 25;
let negativeTemp: number = -temperature; // -25
```

```

## File: 152.txt

# #152 「複合代入演算子」台本

```

## 📺 画面表示用コード

```typescript
// 複合代入演算子
let value: number = 10;

value += 5;  // value = value + 5; // 15
value -= 3;  // value = value - 3; // 12
value *= 2;  // value = value * 2; // 24
value /= 4;  // value = value / 4; // 6
value %= 5;  // value = value % 5; // 1

// 実用的な例
let total: number = 0;
total += 100; // 100
total += 200; // 300
total += 50;  // 350
```

```

## File: 153.txt

# #153 「ビット演算子」台本

```

## 📺 画面表示用コード

```typescript
// ビット演算子
let a: number = 5;  // 101
let b: number = 3;  // 011

let and: number = a & b;  // 001 (1)
let or: number = a | b;   // 111 (7)
let xor: number = a ^ b;  // 110 (6)
let not: number = ~a;     // -6

// 実用的な例
let flag1: number = 0b0001;
let flag2: number = 0b0010;
let combined: number = flag1 | flag2; // 0b0011
```

```

## File: 154.txt

# #154 「シフト演算子」台本

```

## 📺 画面表示用コード

```typescript
// シフト演算子
let value: number = 8;  // 1000

let leftShift: number = value << 1;   // 16 (10000)
let rightShift: number = value >> 1;  // 4 (0100)
let unsignedRightShift: number = value >>> 1; // 4

// 実用的な例
let number: number = 4;
let doubled: number = number << 1;    // 8 (2倍)
let halved: number = number >> 1;     // 2 (1/2倍)
```

```

## File: 155.txt

# #155 「数値演算まとめ」台本

```

## 📺 画面表示用コード

```typescript
// 数値演算まとめ

// 1. 四則演算
let a: number = 10;
let b: number = 3;
let sum: number = a + b;      // 13
let diff: number = a - b;     // 7
let prod: number = a * b;     // 30
let quot: number = a / b;     // 3.33...
let rem: number = a % b;      // 1

// 2. べき乗
let power: number = a ** 2;   // 100

// 3. インクリメント/デクリメント
let count: number = 5;
count++; // 6
count--; // 5

// 4. 複合代入
let value: number = 10;
value += 5; // 15
```

```

## File: 156.txt

# #156 「Numberとnumberの違い」台本

```

## 📺 画面表示用コード

```typescript
// number型（推奨）- プリミティブ型
let age: number = 30;
let price: number = 2980.50;

// Number型（非推奨）- オブジェクト型
// let ageObj: Number = new Number(30); // 避けるべき

// 型の違い
console.log(typeof age);        // "number"
// console.log(typeof ageObj);  // "object"

// 実用的な例
let userAge: number = 25;
let productPrice: number = 1500;
let totalPrice: number = userAge + productPrice;
```
```

## File: 157.txt

# #157 「number型の宣言」台本

```

## 📺 画面表示用コード

```typescript
// number型の宣言
let age: number;
let price: number;
let count: number;

// 後で値を代入
age = 30;
price = 2980.50;
count = -5;

// 実用的な例
let userAge: number = 25;
let productPrice: number = 1500;
let itemCount: number = 10;
```
```

## File: 158.txt

# #158 「Number型の宣言」台本

```

## 📺 画面表示用コード

```typescript
// Number型（避けるべき）
// let ageObj: Number = new Number(30); // 非推奨
// let priceObj: Number = new Number(2980.50); // 非推奨

// 正しい方法：number型を使用
let age: number = 30;
let price: number = 2980.50;

// 型の違い
console.log(typeof age);        // "number"
// console.log(typeof ageObj);  // "object"

// 実用的な例
let userAge: number = 25;
let productPrice: number = 1500;
let totalPrice: number = userAge + productPrice;
```
```

## File: 159.txt

# #159 「Numberコンストラクタ」台本

```

## 📺 画面表示用コード

```typescript
// Numberコンストラクタ（避けるべき）
// let numObj = new Number(30); // 非推奨

// 正しい方法：数値リテラル
let num: number = 30;

// 型の違い
console.log(typeof num);        // "number"
// console.log(typeof numObj);  // "object"

// 比較の問題
let num1: number = 30;
let num2: number = 30;
console.log(num1 === num2); // true

// let obj1 = new Number(30);
// let obj2 = new Number(30);
// console.log(obj1 === obj2); // false
```
```

## File: 160.txt

# #160 「Numberオブジェクトの問題」台本

```

## 📺 画面表示用コード

```typescript
// Numberオブジェクトの問題点

// 1. 型の不一致
// let numObj: Number = new Number(30);
// let num: number = 30;
// console.log(numObj === num); // false

// 2. オブジェクト比較の問題
// let obj1 = new Number(30);
// let obj2 = new Number(30);
// console.log(obj1 === obj2); // false（異なるオブジェクト）

// 正しい方法
let num1: number = 30;
let num2: number = 30;
console.log(num1 === num2); // true

// 実用的な例
let userAge: number = 25;
let productPrice: number = 1500;
console.log(userAge === 25); // true
```
```

## File: 161.txt

# #161 「Numberからnumberへ」台本

```

## 📺 画面表示用コード

```typescript
// Numberからnumberへの変換

// 1. valueOf()メソッド
// let numObj = new Number(30);
// let num: number = numObj.valueOf(); // number型に変換

// 2. Number()関数
// let numObj = new Number(30);
// let num: number = Number(numObj); // number型に変換

// 3. 数値リテラル（推奨）
let num: number = 30; // 最初からnumber型

// 実用的な例
let userData = {
  age: 25,
  price: 1500
};

let userAge: number = Number(userData.age);
let productPrice: number = Number(userData.price);
```
```

## File: 162.txt

# #162 「自動ボックス化」台本

```

## 📺 画面表示用コード

```typescript
// 自動ボックス化の例
let num: number = 30;

// メソッド呼び出し時に自動ボックス化
let numStr: string = num.toString(); // 自動的にNumberオブジェクトに変換
let numFixed: string = num.toFixed(2); // 自動的にNumberオブジェクトに変換

// プロパティアクセス時も自動ボックス化
let numStr2: string = num.toString(); // 自動的にNumberオブジェクトに変換

// 実用的な例
let userAge: number = 25;
let ageStr: string = userAge.toString();
let ageFixed: string = userAge.toFixed(0);
```
```

## File: 163.txt

# #163 「==と===での比較」台本

```

## 📺 画面表示用コード

```typescript
// ==と===での比較

// number型同士の比較
let num1: number = 30;
let num2: number = 30;
console.log(num1 === num2); // true
console.log(num1 == num2);  // true

// Numberオブジェクトとの比較
// let numObj = new Number(30);
// console.log(num1 === numObj); // false（型が異なる）
// console.log(num1 == numObj);  // true（型変換される）

// 実用的な例
let userAge: number = 25;
let expectedAge: number = 25;
console.log(userAge === expectedAge); // true

// 型安全な比較
if (userAge === expectedAge) {
  console.log("年齢が一致します");
}
```
```

## File: 164.txt

# #164 「なぜnumberを使うべきか」台本

```

## 📺 画面表示用コード

```typescript
// number型を使うべき理由

// 1. 型安全性
let userAge: number = 25;
// userAge = "25"; // エラー: Type 'string' is not assignable to type 'number'

// 2. パフォーマンス
let productPrice: number = 1500; // 軽量なプリミティブ型

// 3. 一貫性
let userData = {
  age: 25,
  price: 1500
};
let totalValue: number = userData.age + userData.price;

// 4. 予測可能な動作
let num1: number = 30;
let num2: number = 30;
console.log(num1 === num2); // 常にtrue
```
```

## File: 165.txt

# #165 「Number型使用禁止」台本

```

## 📺 画面表示用コード

```typescript
// Number型使用禁止ルール

// ❌ 禁止：Number型の使用
// let age: Number = new Number(25);
// let price: Number = new Number(1500);

// ✅ 推奨：number型の使用
let age: number = 25;
let price: number = 1500;

// ✅ 推奨：型推論の活用
let userAge = 25; // number型と推論
let productPrice = 1500; // number型と推論

// 実用的な例
let componentProps = {
  age: 25,
  price: 1500
};
let userAge: number = componentProps.age;
```
```

## File: 166.txt

# #166 「Number()関数」台本

```

## 📺 画面表示用コード

```typescript
// Number()関数
let str: string = "123";
let bool: boolean = true;
let nullValue: null = null;

// 数値変換
let num1: number = Number(str);      // 123
let num2: number = Number(bool);     // 1
let num3: number = Number(nullValue); // 0

// 実用的な例
let userInput: string = "25";
let userAge: number = Number(userInput);

let isActive: boolean = true;
let activeValue: number = Number(isActive); // 1
```
```

## File: 167.txt

# #167 「parseInt()関数」台本

```

## 📺 画面表示用コード

```typescript
// parseInt()関数
let str1: string = "123";
let str2: string = "123.45";
let str3: string = "abc123";

// 整数変換
let int1: number = parseInt(str1);      // 123
let int2: number = parseInt(str2);      // 123
let int3: number = parseInt(str3);      // NaN

// 実用的な例
let userInput: string = "25";
let userAge: number = parseInt(userInput);

let priceStr: string = "1500円";
let price: number = parseInt(priceStr); // 1500
```
```

## File: 168.txt

# #168 「parseFloat()関数」台本

```

## 📺 画面表示用コード

```typescript
// parseFloat()関数
let str1: string = "123.45";
let str2: string = "123";
let str3: string = "abc123.45";

// 浮動小数点変換
let float1: number = parseFloat(str1);      // 123.45
let float2: number = parseFloat(str2);      // 123
let float3: number = parseFloat(str3);      // NaN

// 実用的な例
let userInput: string = "25.5";
let userAge: number = parseFloat(userInput);

let priceStr: string = "1500.99円";
let price: number = parseFloat(priceStr); // 1500.99
```
```

## File: 169.txt

# #169 「暗黙的な型変換」台本

```

## 📺 画面表示用コード

```typescript
// 暗黙的な型変換
let num: number = 10;
let str: string = "5";

// 演算での暗黙的変換
let result1: string = num + str;  // "105" (文字列結合)
let result2: number = num - str;  // 5 (数値演算)

// 実用的な例
let userAge: number = 25;
let ageStr: string = "歳";
let displayText: string = userAge + ageStr; // "25歳"

let price: number = 1000;
let discount: string = "100";
let finalPrice: number = price - discount; // 900
```
```

## File: 170.txt

# #170 「明示的な型変換」台本

```

## 📺 画面表示用コード

```typescript
// 明示的な型変換
let str: string = "123";
let bool: boolean = true;

// 明示的な変換
let num1: number = Number(str);      // 123
let num2: number = parseInt(str);    // 123
let num3: number = Number(bool);     // 1

// 実用的な例
let userInput: string = "25";
let userAge: number = Number(userInput); // 明示的に変換

let isActive: boolean = true;
let activeValue: number = Number(isActive); // 明示的に変換
```
```

## File: 171.txt

# #171 「変換失敗時 - NaN」台本

```

## 📺 画面表示用コード

```typescript
// 変換失敗時 - NaN
let invalidStr: string = "abc";
let emptyStr: string = "";

// 変換失敗
let result1: number = Number(invalidStr);  // NaN
let result2: number = parseInt(invalidStr); // NaN
let result3: number = parseFloat(emptyStr); // NaN

// 実用的な例
let userInput: string = "無効な値";
let userAge: number = Number(userInput);

if (Number.isNaN(userAge)) {
  console.log("無効な数値です");
} else {
  console.log("有効な数値です");
}
```
```

## File: 172.txt

# #172 「エラーハンドリング」台本

```

## 📺 画面表示用コード

```typescript
// エラーハンドリング
function safeNumberConversion(input: string): number | null {
  try {
    let result: number = Number(input);
    if (Number.isNaN(result)) {
      return null;
    }
    return result;
  } catch (error) {
    console.error("変換エラー:", error);
    return null;
  }
}

// 実用的な例
let userInput: string = "abc";
let userAge: number | null = safeNumberConversion(userInput);

if (userAge === null) {
  console.log("数値変換に失敗しました");
} else {
  console.log(`年齢: ${userAge}`);
}
```
```

## File: 173.txt

# #173 「数値バリデーション」台本

```

## 📺 画面表示用コード

```typescript
// 数値バリデーション
function validateNumber(value: number): boolean {
  return Number.isFinite(value) && !Number.isNaN(value);
}

function validateInteger(value: number): boolean {
  return Number.isInteger(value) && Number.isFinite(value);
}

// 実用的な例
let userAge: number = 25;
let productPrice: number = 1500;

if (validateNumber(userAge)) {
  console.log("有効な年齢です");
}

if (validateInteger(productPrice)) {
  console.log("有効な整数価格です");
}
```
```

## File: 174.txt

# #174 「型安全な変換」台本

```

## 📺 画面表示用コード

```typescript
// 型安全な変換
function isNumber(value: unknown): value is number {
  return typeof value === "number" && Number.isFinite(value);
}

function safeConvert(value: unknown): number | null {
  if (isNumber(value)) {
    return value;
  }
  
  if (typeof value === "string") {
    let converted = Number(value);
    return Number.isNaN(converted) ? null : converted;
  }
  
  return null;
}

// 実用的な例
let userInput: unknown = "25";
let userAge: number | null = safeConvert(userInput);

if (userAge !== null) {
  console.log(`年齢: ${userAge}`);
}
```
```

## File: 175.txt

# #175 「数値変換まとめ」台本

```

## 📺 画面表示用コード

```typescript
// 数値変換まとめ

// 1. 基本変換関数
let str: string = "123.45";
let num1: number = Number(str);      // 123.45
let num2: number = parseInt(str);    // 123
let num3: number = parseFloat(str);  // 123.45

// 2. バリデーション
let isValid: boolean = Number.isFinite(num1);
let isInteger: boolean = Number.isInteger(num2);

// 3. エラーハンドリング
let userInput: string = "abc";
let converted: number = Number(userInput);
if (Number.isNaN(converted)) {
  console.log("変換に失敗しました");
}
```
```

## File: 176.txt

# #176 「IEEE 754とは」台本

```

## 📺 画面表示用コード

```typescript
// IEEE 754の特徴
let num1: number = 0.1;
let num2: number = 0.2;
let sum: number = num1 + num2;

console.log(sum); // 0.30000000000000004

// 特殊な値
let infinity: number = Infinity;
let negativeInfinity: number = -Infinity;
let notANumber: number = NaN;

console.log(Number.isFinite(infinity)); // false
console.log(Number.isNaN(notANumber)); // true
```
```

## File: 177.txt

# #177 「精度問題 - 0.1 + 0.2」台本

```

## 📺 画面表示用コード

```typescript
// 精度問題の例
let num1: number = 0.1;
let num2: number = 0.2;
let sum: number = num1 + num2;

console.log(sum); // 0.30000000000000004
console.log(sum === 0.3); // false

// 実用的な例
let price1: number = 0.1;
let price2: number = 0.2;
let total: number = price1 + price2;

console.log(total); // 0.30000000000000004
console.log(total === 0.3); // false
```
```

## File: 178.txt

# #178 「丸め誤差」台本

```

## 📺 画面表示用コード

```typescript
// 丸め誤差の例
let num1: number = 0.1;
let num2: number = 0.2;
let sum: number = num1 + num2;

console.log(sum); // 0.30000000000000004

// 実用的な例
let userAge: number = 25.5;
let productPrice: number = 1500.99;
let total: number = userAge + productPrice;

console.log(total); // 1526.4899999999998
console.log(total.toFixed(2)); // "1526.49"
```
```

## File: 179.txt

# #179 「回避方法(1) - 整数演算」台本

```

## 📺 画面表示用コード

```typescript
// 整数演算による回避
function addDecimals(a: number, b: number): number {
  const factor = 100; // 小数点以下2桁
  return (Math.round(a * factor) + Math.round(b * factor)) / factor;
}

// 実用的な例
let price1: number = 0.1;
let price2: number = 0.2;
let total: number = addDecimals(price1, price2);

console.log(total); // 0.3
console.log(total === 0.3); // true

// 金銭計算の例
let yen1: number = 100.50;
let yen2: number = 200.25;
let totalYen: number = addDecimals(yen1, yen2);
```
```

## File: 180.txt

# #180 「回避方法(2) - ライブラリ」台本

```

## 📺 画面表示用コード

```typescript
// ライブラリによる回避（decimal.jsの例）
// npm install decimal.js
// import { Decimal } from 'decimal.js';

// const a = new Decimal(0.1);
// const b = new Decimal(0.2);
// const sum = a.plus(b);

// console.log(sum.toString()); // "0.3"

// 実用的な例
// const price1 = new Decimal(100.50);
// const price2 = new Decimal(200.25);
// const total = price1.plus(price2);

// console.log(total.toString()); // "300.75"
```
```

## File: 181.txt

# #181 「toFixed()メソッド」台本

```

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
```

## File: 182.txt

# #182 「toPrecision()メソッド」台本

```

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
```

## File: 183.txt

# #183 「イプシロン比較」台本

```

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
```

## File: 184.txt

# #184 「Math.absを使った比較」台本

```

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
```

## File: 185.txt

# #185 「金銭計算の注意点」台本

```

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
```

## File: 186.txt

# #186 「BigIntの紹介」台本

```

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
```

## File: 187.txt

# #187 「BigIntとnumberの違い」台本

```

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
```

## File: 188.txt

# #188 「BigIntの使用例」台本

```

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
```

## File: 189.txt

# #189 「浮動小数点のベストプラクティス」台本

```

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
```

## File: 190.txt

# #190 「数値計算まとめ」台本

```

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
```

## File: 191.txt

# #191 「Angularフォームでのnumber型」台本

```

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
```

## File: 192.txt

# #192 「数値バリデーション」台本

```

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
```

## File: 193.txt

# #193 「Nest.jsのDTOとnumber型」台本

```

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
```

## File: 194.txt

# #194 「@IsNumber()デコレータ」台本

```

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
```

## File: 195.txt

# #195 「数値範囲のバリデーション」台本

```

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
```

## File: 196.txt

# #196 「間違い(1) - 浮動小数点比較」台本

```

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
```

## File: 197.txt

# #197 「間違い(2) - NaNチェック」台本

```

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
```

## File: 198.txt

# #198 「間違い(3) - 文字列との混同」台本

```

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
```

## File: 199.txt

# #199 「ベストプラクティス」台本

```

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
```

## File: 200.txt

# #200 「マスターチェック」台本

```

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
```

## File: 201.txt

# #201 「boolean型とは」台本

```

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
```

## File: 202.txt

# #202 「boolean型の宣言」台本

```

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
```

## File: 203.txt

# #203 「trueの代入」台本

```

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
```

## File: 204.txt

# #204 「falseの代入」台本

```

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
```

## File: 205.txt

# #205 「型推論でboolean型」台本

```

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
```

## File: 206.txt

# #206 「constでboolean型」台本

```

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
```

## File: 207.txt

# #207 「if文での使用」台本

```

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
```

## File: 208.txt

# #208 「while文での使用」台本

```

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
```

## File: 209.txt

# #209 「三項演算子」台本

```

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
```

## File: 210.txt

# #210 「boolean配列」台本

```

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
```

## File: 211.txt

# #211 「booleanリテラル型」台本

```

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
```

## File: 212.txt

# #212 「デフォルト値」台本

```

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
```

## File: 213.txt

# #213 「初期化のベストプラクティス」台本

```

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
```

## File: 214.txt

# #214 「boolean型の用途」台本

```

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
```

## File: 215.txt

# #215 「基本まとめ」台本

```

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
```

## File: 216.txt

# #216 「trueリテラル型」台本

```

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
```

## File: 217.txt

# #217 「trueリテラル型の宣言」台本

```

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
```

## File: 218.txt

# #218 「trueリテラル型の使用例」台本

```

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
```

## File: 219.txt

# #219 「falseリテラル型」台本

```

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
```

## File: 220.txt

# #220 「falseリテラル型の宣言」台本

```

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
```

## File: 221.txt

# #221 「falseリテラル型の使用例」台本

```

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
```

## File: 222.txt

# #222 「リテラル型とboolean型の違い」台本

```

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
```

## File: 223.txt

# #223 「型推論 - const使用時」台本

```

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
```

## File: 224.txt

# #224 「ユースケース」台本

```

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
```

## File: 225.txt

# #225 「リテラル型まとめ」台本

```

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
```

## File: 226.txt

# #226 「論理積AND - &&」台本

```

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
```

## File: 227.txt

# #227 「ANDの型推論」台本

```

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
```

## File: 228.txt

# #228 「ANDの短絡評価」台本

```

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
```

## File: 229.txt

# #229 「ANDと型の関係」台本

```

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
```

## File: 230.txt

# #230 「論理和OR - ||」台本

```

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
```

## File: 231.txt

# #231 「ORの型推論」台本

```

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
```

## File: 232.txt

# #232 「ORの短絡評価」台本

```

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
```

## File: 233.txt

# #233 「ORとデフォルト値」台本

```

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
```

## File: 234.txt

# #234 「論理否定NOT - !」台本

```

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
```

## File: 235.txt

# #235 「NOTの型推論」台本

```

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
```

## File: 236.txt

# #236 「二重否定 - !!」台本

```

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
```

## File: 237.txt

# #237 「二重否定での型変換」台本

```

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
```

## File: 238.txt

# #238 「論理演算子の優先順位」台本

```

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
```

## File: 239.txt

# #239 「論理演算子の組み合わせ」台本

```

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
```

## File: 240.txt

# #240 「論理演算まとめ」台本

```

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
```

## File: 241.txt

# #241 「等価演算子 - ==と===」台本

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

```

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

