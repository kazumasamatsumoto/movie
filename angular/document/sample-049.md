# #049 「$event オブジェクトの活用」

## 概要
イベントバインディング式で参照できる`$event`オブジェクトを用い、DOMイベントの詳細情報を取得してUIロジックに活用する方法を学びます。

## 学習目標
- `$event` の正体と型を理解し、安全に扱う
- イベント位置や入力値など詳細プロパティを参照する方法を学ぶ
- 型ガードや型パラメータでコンポーネントロジックを堅牢にする

## 技術ポイント
- **$event参照**: イベントハンドラへ自動的に渡されるDOMイベントオブジェクト
- **型付け**: メソッド引数を`MouseEvent`や`InputEvent`など適切な型にする
- **プロパティ活用**: クライアント座標、キーコード、target要素などを条件分岐に利用

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
<button (click)="logPosition($event)">位置を表示</button>
```

```html
<input (input)="updateValue($event)" />
```

```html
<form (submit)="handleSubmit($event)">送信</form>
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, signal } from '@angular/core';

@Component({
  selector: 'app-event-object-demo',
  standalone: true,
  templateUrl: './event-object-demo.component.html',
})
export class EventObjectDemoComponent {
  coordinates = signal<{ x: number; y: number } | null>(null);
  latestInput = signal('');
  submitMessage = signal('');

  logPosition(event: MouseEvent): void {
    this.coordinates.set({ x: event.clientX, y: event.clientY });
  }

  updateValue(event: Event): void {
    const input = event.target as HTMLInputElement;
    this.latestInput.set(input.value);
  }

  handleSubmit(event: SubmitEvent): void {
    event.preventDefault();
    const form = event.target as HTMLFormElement;
    const formData = new FormData(form);
    this.submitMessage.set(`送信: ${formData.get('name') ?? ''}`);
  }
}
```

```html
<section>
  <button type="button" (click)="logPosition($event)">クリック位置を記録</button>
  <p *ngIf="coordinates()">
    X: {{ coordinates()!.x }}, Y: {{ coordinates()!.y }}
  </p>
</section>

<section>
  <input
    (input)="updateValue($event)"
    placeholder="ライブ更新"
    [value]="latestInput()"
  />
  <p>入力値: {{ latestInput() }}</p>
</section>

<form (submit)="handleSubmit($event)">
  <input name="name" placeholder="お名前" />
  <button type="submit">送信</button>
</form>
<p>{{ submitMessage() }}</p>
```

## ベストプラクティス
- メソッド引数に具体的なイベント型を宣言し、プロパティ参照を型安全にする
- `$event`をテンプレートで加工するより、コンポーネント側で処理する
- イベントオブジェクトは再利用されないので、必要情報をすぐコピーする

## 注意点
- `$event.target`が`null`になるケースがあるため防御的に扱う
- 非同期でイベントプロパティを読むと値がクリアされる場合がある
- 直接DOMを操作せず、AngularのバインディングやRenderer2を優先する

## 関連技術
- TypeScriptのDOM型定義（lib.dom.d.ts）
- Renderer2やElementRefによるDOM操作
- Angular Signals / RxJSでのイベントストリーム処理
