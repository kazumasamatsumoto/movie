# #056 「テンプレート式の制約事項」

## 概要
Angularのテンプレート式が安全で予測可能に動作するために設けられている制約を理解し、誤った記述を避ける方法を整理します。

## 学習目標
- テンプレート式で禁止されている操作を把握する
- 制約を回避するためにプロパティやメソッドへロジックを移す
- エラー発生時のメッセージを読み解き原因を特定する

## 技術ポイント
- **式のみ許可**: if文、for文、代入、new演算子などの文は利用できない
- **副作用禁止**: pushや++など状態を変える操作はテンプレートから排除する
- **テンプレート変数**: `let`宣言や関数宣言は使用できず、局所変数は構文ごとのシンタックスに従う

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
<p>{{ totalAmount }}</p>
```

```html
<!-- ❌ {{ totalAmount = totalAmount + 1 }} -->
```

```html
<!-- ❌ {{ items.push('new') }} -->
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, computed, signal } from '@angular/core';

@Component({
  selector: 'app-template-constraints',
  standalone: true,
  templateUrl: './template-constraints.component.html',
})
export class TemplateConstraintsComponent {
  items = signal([1200, 1800, 2200]);
  taxRate = signal(0.1);

  totalAmount = computed(() =>
    this.items().reduce((sum, price) => sum + price, 0),
  );

  totalWithTax = computed(() =>
    Math.round(this.totalAmount() * (1 + this.taxRate())),
  );

  addItem(price: number): void {
    this.items.update((list) => [...list, price]);
  }
}
```

```html
<p>小計: {{ totalAmount() }} 円</p>
<p>税込: {{ totalWithTax() }} 円</p>
<button type="button" (click)="addItem(1500)">アイテム追加</button>

<!-- テンプレート式内で代入しない -->
<!-- ❌ {{ totalAmount() = 0 }} -->
```

## ベストプラクティス
- 計算処理はコンポーネントのプロパティ（getterやcomputed）で準備し、テンプレートは読み取り専用にする
- 配列変更やロジック実行は明示的なハンドラメソッドに切り出してテストしやすくする
- ドキュメントの「Template expressions」ガイドに沿って記述ルールを定期的に確認する

## 注意点
- テンプレート式で副作用を起こすと予期しない挙動やAOTエラーにつながる
- strictTemplatesを有効にすると違反がコンパイル時に検出されるため、早期対応が可能
- カスタムディレクティブでもテンプレート式の制約は同じく適用される

## 関連技術
- Angular compilerのAOT制約
- strictTemplatesオプション
- Angularテンプレート構文ガイド
