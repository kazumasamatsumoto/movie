# #004 「string型の初期化 - let name: string = "Alice"」

## 概要
TypeScript v5.9のstring型初期化について学習します。宣言と同時に初期値を設定する効率的な方法を理解します。

## 学習目標
- 変数の初期化の基本構文を理解する
- 初期化の利点を理解する
- 適切な初期化方法を習得する

## 画面表示用コード

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

## 重要なポイント
1. **一行で完結**: 宣言、型指定、初期化を同時に実行
2. **未定義回避**: 初期化によりundefined状態を避けられる
3. **意図の明確化**: コードの意図が明確になる

## 次のステップ
次回は、型推論でstring型について学習します。

