# #046 「(keyup) キーボードイベント」

## 概要
キーボード入力時に処理を走らせる( keyup )イベントと、キー修飾子を使ったフィルタリング手法を学び、アクセシブルなショートカットを実装します。

## 学習目標
- (keyup) イベントの仕組みと発火タイミングを理解する
- `.enter`などキー修飾子を活用したテンプレート構文を習得する
- Signalやフィルタリング処理と組み合わせたライブ検索を実装する

## 技術ポイント
- **keyupイベント**: キーを離したタイミングで発火し、入力途中の反応を実現
- **キー修飾子**: `(keyup.enter)="..."` で特定キーのみ処理を実行
- **アクセシビリティ**: キーボード操作でも同等の体験を提供する設計が重要

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
<input (keyup)="onKey($event)" placeholder="タイプして検索" />
```

```html
<input (keyup.enter)="commit()" (keyup.escape)="reset()" />
```

```html
<button (keyup.space)="toggle()" tabindex="0">スペースで切替</button>
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, computed, signal } from '@angular/core';

@Component({
  selector: 'app-keyup-demo',
  standalone: true,
  templateUrl: './keyup-demo.component.html',
})
export class KeyupDemoComponent {
  keyword = signal('');
  onlyFavorites = signal(false);
  items = signal([
    { name: 'Angular', favorite: true },
    { name: 'React', favorite: false },
    { name: 'Vue', favorite: true },
    { name: 'Svelte', favorite: false },
  ]);

  filtered = computed(() =>
    this.items().filter((item) => {
      if (this.onlyFavorites() && !item.favorite) {
        return false;
      }
      return item.name.toLowerCase().includes(this.keyword().toLowerCase());
    }),
  );

  onKey(event: KeyboardEvent): void {
    const input = event.target as HTMLInputElement;
    this.keyword.set(input.value);
  }

  commit(): void {
    console.log('検索確定:', this.keyword());
  }

  reset(): void {
    this.keyword.set('');
  }

  toggle(): void {
    this.onlyFavorites.update((state) => !state);
  }
}
```

```html
<input
  (keyup)="onKey($event)"
  (keyup.enter)="commit()"
  (keyup.escape)="reset()"
  [value]="keyword()"
  placeholder="ライブラリを検索"
/>
<button type="button" (click)="toggle()" (keyup.space)="toggle()">
  お気に入りのみ: {{ onlyFavorites() ? 'ON' : 'OFF' }}
</button>

<ul>
  <li @for (item of filtered(); track item.name)>{{ item.name }}</li>
</ul>
```

## ベストプラクティス
- キーボードとポインタ操作で同じ機能を提供しアクセシビリティを確保する
- キー修飾子を活用し、テンプレートで意図を明示する
- 検索など負荷が高い処理には`debounce`やSignalの`effect`で最適化する

## 注意点
- 組み合わせたいキーが修飾子として用意されていない場合はコード側で判定する
- 入力欄の`value`をSignalと同期させるときは無限ループに注意する
- ショートカットはキーボードレイアウトやデバイス差を考慮して設計する

## 関連技術
- Angularのキーイベントプラグイン（KeyEventsPlugin）
- アクセシビリティ規格（WCAG）
- RxJSによる入力ストリーム処理
