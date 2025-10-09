# #041 「(event) イベントバインディング基礎」

## 概要
Angular v20のテンプレートでDOMイベントをコンポーネントのメソッドへ結び付ける(event)構文の基本を学びます。

## 学習目標
- (event)構文の役割と書き方を理解する
- イベントからコンポーネントメソッドを呼び出す方法を知る
- テンプレート式とTypeScriptコードの連携を整理する

## 技術ポイント
- **イベントバインディング**: `(eventName)="handler()"` でDOMイベントとメソッドを接続
- **テンプレート式**: Angular式でプロパティやメソッドを直接呼び出し可能
- **イベントオブジェクト**: `$event` を引数に渡して詳細情報を取得できる

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
<button (click)="increment()">カウント</button>
```

```html
<input (input)="updateName()" placeholder="お名前" />
```

```html
<div 
(mouseenter)="toggleHighlight(true)" 
(mouseleave)="toggleHighlight(false)"
>
  Hover me
</div>
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, signal } from '@angular/core';

@Component({
  selector: 'app-event-demo',
  standalone: true,
  templateUrl: './event-demo.component.html',
})
export class EventDemoComponent {
  count = signal(0);
  name = signal('');
  highlighted = signal(false);

  increment(): void {
    this.count.update((c) => c + 1);
  }

  updateName(): void {
    this.name.set('入力がありました');
  }

  toggleHighlight(state: boolean): void {
    this.highlighted.set(state);
  }
}
```

```html
<section>
  <p>クリック回数: {{ count() }}</p>
  <button (click)="increment()">+1</button>
</section>

<section>
  <input (input)="updateName()" placeholder="Your name" />
  <p>{{ name() }}</p>
</section>

<section [class.active]="highlighted()">
  <div
    (mouseenter)="toggleHighlight(true)"
    (mouseleave)="toggleHighlight(false)"
  >
    Hover to highlight
  </div>
</section>
```

## ベストプラクティス
- イベント名はDOM標準の小文字で記述し、メソッド名は動詞から始める
- テンプレート式は短く保ち、複雑な処理はコンポーネントクラスに委譲する
- SignalsなどリアクティブAPIと組み合わせてUI状態を明確に管理する

## 注意点
- イベント式内で重い処理を直接実行せず、メソッドを介して整理する
- `this` 参照はテンプレート内で不要なので書かない
- カスタムイベントの場合はOutputデコレーターやEventEmitterとの違いを意識する

## 関連技術
- Template式とPropertyバインディング
- Angular Signalsによる状態管理
- DOMイベントの基礎（EventTarget, Eventフェーズ）
