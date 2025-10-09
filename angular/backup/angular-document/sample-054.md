# #054 「複数のバインディングを組み合わせる」

## 概要
同じHTML要素にプロパティ、イベント、クラス、スタイルなど複数のバインディングを組み合わせて、状態と見た目を一貫して制御するパターンを学びます。

## 学習目標
- プロパティバインディングとイベントバインディングを同一要素で併用する
- クラス／スタイルバインディングで状態に応じた表現を行う
- バインディングが多い要素でも可読性を保つ工夫を理解する

## 技術ポイント
- **宣言の自由度**: Angularは属性の順序に依存せず、それぞれ独立に評価される
- **クラス・スタイル制御**: `[class.active]`や`[style.opacity]`で条件付きスタイルを適用
- **イベント連携**: `(click)`や`(keydown)`で状態を更新し、描画へ反映

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
<button
  [disabled]="pending"
  [class.active]="selected"
  (click)="select()"
>
  選択
</button>
```

```html
<div
  [attr.aria-pressed]="selected"
  [style.opacity]="pending ? 0.5 : 1"
  (mouseenter)="hover = true"
  (mouseleave)="hover = false"
></div>
```

```html
<input
  [value]="keyword"
  (input)="onInput($event)"
  [attr.data-state]="state"
/>
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, computed, signal } from '@angular/core';

@Component({
  selector: 'app-binding-combo',
  standalone: true,
  templateUrl: './binding-combo.component.html',
  styleUrls: ['./binding-combo.component.css'],
})
export class BindingComboComponent {
  keyword = signal('');
  pending = signal(false);
  selectedId = signal<number | null>(null);
  hoverId = signal<number | null>(null);

  items = signal([
    { id: 1, name: 'Signals入門' },
    { id: 2, name: 'Control Flowガイド' },
    { id: 3, name: 'Standalone設計' },
  ]);

  filtered = computed(() =>
    this.items().filter((item) =>
      item.name.toLowerCase().includes(this.keyword().toLowerCase()),
    ),
  );

  onInput(event: Event): void {
    const target = event.target as HTMLInputElement;
    this.keyword.set(target.value);
  }

  select(id: number): void {
    this.pending.set(true);
    setTimeout(() => {
      this.selectedId.set(id);
      this.pending.set(false);
    }, 400);
  }
}
```

```html
<input
  [value]="keyword()"
  (input)="onInput($event)"
  placeholder="キーワードを入力"
/>

<ul>
  <li
    @for (item of filtered(); track item.id)
    [class.active]="selectedId() === item.id"
    [class.hover]="hoverId() === item.id"
    [attr.aria-selected]="selectedId() === item.id"
    [style.opacity]="pending() ? 0.6 : 1"
    (mouseenter)="hoverId.set(item.id)"
    (mouseleave)="hoverId.set(null)"
    (click)="select(item.id)"
  >
    {{ item.name }}
  </li>
</ul>

<p>選択中: {{ selectedId() ?? 'なし' }}</p>
<p>状態: {{ pending() ? '読み込み中' : '待機中' }}</p>
```

## ベストプラクティス
- 属性の種類ごとにブロックをまとめて記述し、可読性を高める
- クラスバインディングはBooleanを返すプロパティやcomputedを活用して簡潔にする
- イベントで状態を更新するときはSignalやstoreを利用し、副作用の範囲を限定する

## 注意点
- バインディング数が増えるときは共通コンポーネント化やディレクティブ化を検討する
- CSS側でも`.active`などのクラスを定義し、スタイルの責務を分離する
- イベントで非同期処理を行う場合は状態の競合が起きないように注意する

## 関連技術
- `[ngClass]`や`[ngStyle]`によるまとめ書き
- Control Flow（@if/@for）との組み合わせ
- Directiveでの状態カプセル化
