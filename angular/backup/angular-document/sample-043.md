# #043 「(input) 入力イベント」

## 概要
入力要素の値が変わるたびに発火する(input)イベントで、リアルタイムにコンポーネント状態を反映させる方法を学びます。

## 学習目標
- (input) イベントの発火タイミングを理解する
- `$event.target.value` を安全に扱う方法を学ぶ
- 入力補助やライブプレビューの実装アイデアを身につける

## 技術ポイント
- **(input) イベント**: ユーザー入力のたびに発火し、最新値を取得できる
- **型アサーション**: `$event.target` を `HTMLInputElement` として扱う
- **リアクティブ更新**: SignalやFormControlと組み合わせてUIを即時更新

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
<input (input)="value = $any($event.target).value" />
```

```html
<textarea (input)="updatePreview($event)" rows="3"></textarea>
```

```html
<input (input)="filter($any($event.target).value)" placeholder="絞り込み" />
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, computed, signal } from '@angular/core';

@Component({
  selector: 'app-input-demo',
  standalone: true,
  templateUrl: './input-demo.component.html',
})
export class InputDemoComponent {
  keyword = signal('');
  preview = computed(() => this.keyword().toUpperCase());
  suggestions = computed(() =>
    this.sampleItems.filter((item) =>
      item.toLowerCase().includes(this.keyword().toLowerCase()),
    ),
  );

  private readonly sampleItems = ['Angular', 'React', 'Vue', 'Svelte'];

  onInput(event: Event): void {
    const target = event.target as HTMLInputElement;
    this.keyword.set(target.value);
  }

  clear(): void {
    this.keyword.set('');
  }
}
```

```html
<label>
  検索ワード
  <input (input)="onInput($event)" [value]="keyword()" />
</label>
<button type="button" (click)="clear()">クリア</button>

<section>
  <p>ライブプレビュー: {{ preview() }}</p>
  <ul>
    <li @for (item of suggestions(); track item)>{{ item }}</li>
  </ul>
</section>
```

## ベストプラクティス
- 入力頻度が高い場合はRxJSの`debounceTime`や`requestIdleCallback`で負荷を抑える
- `$event`から取り出した値は即座に型アサートして明示的に扱う
- SignalやフォームAPIへ値を流し込み、状態の単一ソースを維持する

## 注意点
- (input)は入力途中でも発火するため、確定値が欲しい場合は(change)を検討する
- 変換処理が重い場合は処理時間に注意し、ワーカや分割を検討する
- IME入力中の中間文字にも反応する点を考慮してUIを設計する

## 関連技術
- Angular Forms（Reactive FormsとTemplate-driven Forms）
- Signalsとcomputedによる派生値生成
- RxJSオペレーターでの入力補助
