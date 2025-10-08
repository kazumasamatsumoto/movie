# #062 「ngOnChanges - 入力プロパティ変更時」

## 概要
@Inputで受け取った値が変化したタイミングで呼び出される`ngOnChanges`フックの基本的な使い方を学びます。

## 学習目標
- `ngOnChanges`の実行タイミングを理解する
- 変更された@Inputプロパティを検知して処理を実行する
- 初期化時の呼び出しも考慮したロジックを書く

## 技術ポイント
- **OnChangesインターフェース**: `ngOnChanges(changes: SimpleChanges)`を実装
- **初回実行**: 初期Input代入時にも呼ばれる
- **差分検出**: どのプロパティが更新されたか`SimpleChanges`で判断

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
@Input() userId!: string;
```

```typescript
ngOnChanges(): void {
  console.log('userIdが変わりました');
}
```

```html
<p>現在のユーザー: {{ userId }}</p>
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, Input, OnChanges, SimpleChanges, computed, signal } from '@angular/core';

@Component({
  selector: 'app-user-badge',
  standalone: true,
  templateUrl: './user-badge.component.html',
})
export class UserBadgeComponent implements OnChanges {
  @Input({ required: true }) userId!: string;
  private readonly history = signal<string[]>([]);

  readonly latest = computed(() => this.history().at(-1) ?? '---');

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['userId']) {
      this.history.update((list) => [...list, changes['userId'].currentValue]);
    }
  }
}
```

```html
<h4>User Badge</h4>
<p>現在: {{ latest() }}</p>
<ul>
  <li @for (item of history(); track item)>{{ item }}</li>
</ul>
```

## ベストプラクティス
- 必要な@Inputのみ`ngOnChanges`で条件分岐し、差分がないときは何もしない
- 変更履歴が不要ならSignalやプロパティへの直接代入にとどめ、余分な配列生成を避ける
- 初回呼び出しで初期化したい場合は`changes['prop'].firstChange`を確認する

## 注意点
- `ngOnChanges`は`@Input`が更新されたときのみ呼ばれ、内部state更新では発火しない
- オブジェクト参照が変わらない場合は変更と認識されないので、immutableに扱う
- `SimpleChanges`は読み取り専用であり、値を書き換えないこと

## 関連技術
- `SimpleChanges` / `SimpleChange`の型定義
- `OnPush`戦略と入力プロパティ管理
- Signalsの`input()`デコレータとの比較
