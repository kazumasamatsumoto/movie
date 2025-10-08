# #055 「テンプレート式のベストプラクティス」

## 概要
テンプレート式を読みやすく保ち、メンテナンスしやすいコードへ導くためのベストプラクティスを整理します。

## 学習目標
- テンプレート式に書いてよい内容と避けるべき内容を把握する
- コンポーネントプロパティやcomputedを活用して式を短く保つ
- 再利用可能なロジックをパイプやメソッドへ切り出す判断基準を身につける

## 技術ポイント
- **シンプルな式**: テンプレート式は副作用のない短い計算に限定する
- **派生値の準備**: 複雑な計算はコンポーネントプロパティやSignalのcomputedで事前に用意
- **再利用**: 同じ変換が複数箇所で必要ならカスタムパイプを検討

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
<p>{{ fullName }}</p>
```

```html
<p>{{ priceWithTax }} 円</p>
```

```html
<span>{{ dueDate | date: 'yyyy/MM/dd' }}</span>
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, computed, signal } from '@angular/core';
import { DatePipe, NgIf } from '@angular/common';

@Component({
  selector: 'app-template-best-practice',
  standalone: true,
  imports: [DatePipe, NgIf],
  templateUrl: './template-best-practice.component.html',
})
export class TemplateBestPracticeComponent {
  firstName = signal('四国');
  lastName = signal('めたん');
  price = signal(1200);
  taxRate = signal(0.1);
  dueDate = signal(new Date('2024-08-01'));

  fullName = computed(() => `${this.lastName()} ${this.firstName()}`);
  priceWithTax = computed(() => Math.round(this.price() * (1 + this.taxRate())));
  isOverdue = computed(() => this.dueDate().getTime() < Date.now());
}
```

```html
<h2>{{ fullName() }}</h2>
<p>お支払い予定額: {{ priceWithTax() }} 円</p>
<p>
  期日:
  <span>{{ dueDate() | date: 'yyyy/MM/dd' }}</span>
  <span *ngIf="isOverdue()">（遅延しています）</span>
</p>
```

## ベストプラクティス
- テンプレート式は1行で読み切れる長さを目安にし、複雑な条件はcomputedやgetterにする
- `DatePipe`や`CurrencyPipe`など組み込みパイプを活用してロジックをテンプレート外へ委譲する
- 再利用する`class`や`style`の判定ロジックはプロパティ化して重複を減らす

## 注意点
- 長い式をそのままテンプレートに書くと変更検知のたびに計算され、可読性も下がる
- computed内で非同期処理を行わず、純粋な計算に限定する
- getterを使う場合も重い処理を入れないようにし、Signalでメモ化を検討する

## 関連技術
- Angular Signalsによる派生値管理
- カスタムパイプの作成
- Templateのパフォーマンスチューニング
