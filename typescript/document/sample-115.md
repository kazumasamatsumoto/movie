# #115 「16進数リテラル - 0xFF」

## 概要
TypeScript v5.9の16進数リテラルについて学習します。0xで始まる16進数の記述方法を理解します。

## 学習目標
- 16進数リテラルの基本を理解する
- 0x記法の使用方法を理解する
- 実用的な使用例を理解する

## 画面表示用コード

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
```

## 重要なポイント
1. **0x記法**: 0xの後に0-9とA-Fを書く
2. **16進数**: 0-9とA-Fの文字を使用
3. **実用性**: 色の値やメモリアドレスに活用

## 次のステップ
次回は、科学的記数法について学習します。