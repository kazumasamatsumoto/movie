# #208 「while文での使用」

## 概要
TypeScript v5.9のwhile文でのboolean型使用について学習します。while文の条件式でboolean型の変数を使用する方法を理解します。

## 学習目標
- while文でのboolean型使用を理解する
- ループ制御を理解する
- 実用的な使用例を理解する

## 画面表示用コード

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

## 重要なポイント
1. **ループ制御**: while文の条件式で使用
2. **終了条件**: ループを終了する条件を設定
3. **実用性**: 繰り返し処理の制御に活用

## 次のステップ
次回は、三項演算子について学習します。
