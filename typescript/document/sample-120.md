# #120 「数値リテラルまとめ」

## 概要
TypeScript v5.9の数値リテラルまとめについて学習します。数値リテラルの要点と重要な機能を総括します。

## 学習目標
- 数値リテラルの要点を理解する
- 主要な機能を整理する
- 実用的な使用例を理解する

## 画面表示用コード

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
```

## 重要なポイント
1. **10進数**: 通常の数値記述
2. **2進数**: 0b記法でビット演算
3. **8進数**: 0o記法で権限設定
4. **16進数**: 0x記法で色やアドレス
5. **科学的記数法**: e記法で大きな数値
6. **アンダースコア区切り**: 可読性向上

## 次のステップ
次回は、boolean型について学習します。