# #053 「バナナインボックス構文の仕組み」

## 概要
角括弧と丸括弧を組み合わせた「バナナインボックス」構文がどのようにプロパティバインディングとイベントバインディングを同時に扱い、双方向データフローを実現しているかを理解します。

## 学習目標
- バナナインボックス構文の内部動作を説明できるようになる
- カスタムコンポーネントで`valueChange`イベントを実装し双方向化する
- `(propChange)`と`[prop]`の明示的な書き方との違いを理解する

## 技術ポイント
- **構文糖衣**: `[(prop)]`は`[prop]`と`(propChange)`の省略表現
- **命名規約**: `propChange`という@Outputを用意するとテンプレートで`[(prop)]`が利用できる
- **双方向バインディング**: コンポーネント側で値を更新すると親へ通知される

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```html
<input [ngModel]="name" (ngModelChange)="name = $event" />
```

```html
<input [(ngModel)]="name" />
```

```html
<app-toggle [(value)]="enabled"></app-toggle>
```

## 💻 詳細実装例（学習用）
```typescript
// toggle.component.ts
import { Component, EventEmitter, Input, Output, Signal, signal } from '@angular/core';

@Component({
  selector: 'app-toggle',
  standalone: true,
  templateUrl: './toggle.component.html',
})
export class ToggleComponent {
  @Input() value = false;
  @Output() valueChange = new EventEmitter<boolean>();
  protected hover = signal(false);

  toggle(): void {
    const next = !this.value;
    this.value = next;
    this.valueChange.emit(next);
  }

  setHover(state: boolean): void {
    this.hover.set(state);
  }
}
```

```html
<!-- toggle.component.html -->
<button
  type="button"
  (click)="toggle()"
  (mouseenter)="setHover(true)"
  (mouseleave)="setHover(false)"
  [class.active]="value"
>
  {{ value ? 'ON' : 'OFF' }}
</button>
<small *ngIf="hover()">クリックで切り替え</small>
```

```typescript
// host.component.ts
import { Component, signal } from '@angular/core';
import { ToggleComponent } from './toggle.component';

@Component({
  selector: 'app-host',
  standalone: true,
  imports: [ToggleComponent],
  templateUrl: './host.component.html',
})
export class HostComponent {
  darkMode = signal(false);
}
```

```html
<!-- host.component.html -->
<h3>ダークモード: {{ darkMode() ? 'ON' : 'OFF' }}</h3>
<app-toggle [(value)]="darkMode"></app-toggle>
```

## ベストプラクティス
- カスタムコンポーネントで双方向化する場合は`propChange`イベントを提供し、イベントの型を厳密にする
- テンプレート側で`[(prop)]`を使う箇所は数を絞り、ロジックはコンポーネントクラスへ寄せる
- SignalsなどのリアクティブAPIと組み合わせる際は、イベントで受け取った値を`signal.set()`に委譲する

## 注意点
- Output名は`propChange`に揃える必要があり、命名を変えると構文が機能しない
- 双方向バインディングは状態の責務が曖昧になる可能性があるため、片方向データフローと比較して検討する
- イベントを多重に発火させると親コンポーネントの変更検知が増えるため注意する

## 関連技術
- Template-driven Forms と `ngModelChange`
- Signalsと`ModelSignal`による双方向同期
- ControlValueAccessorによるフォーム要素拡張
