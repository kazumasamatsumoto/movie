# #111 「@Input() + @Output() の組み合わせ」

## 概要
@Input()で親から値を受け取り、@Output()で変更を通知する基本的な親子通信パターンを解説します。

## 学習目標
- 親が状態を保持し、子がイベントで更新要求を返すフローを理解する
- 双方向データフローを手動で構築する手順を学ぶ
- Input/Outputの命名を揃えることで可読性を高める

## 技術ポイント
- **@Input() value**: 親からの初期値を受け取る
- **@Output() valueChange**: 変更をイベントで通知する
- **親の責務**: 状態の真の所有者が親になる


```typescript
@Input() value = '';
@Output() valueChange = new EventEmitter<string>();
```

```html
<input [value]="value" (input)="onInput($event)" />
```

```html
<app-input
  [value]="name"
  (valueChange)="name = $event"
></app-input>
```

## 💻 詳細実装例（学習用）
```typescript
// text-input.component.ts
import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-text-input',
  standalone: true,
  templateUrl: './text-input.component.html',
})
export class TextInputComponent {
  @Input() value = '';
  @Output() valueChange = new EventEmitter<string>();

  onInput(event: Event): void {
    const target = event.target as HTMLInputElement;
    this.valueChange.emit(target.value);
  }
}
```

```html
<!-- text-input.component.html -->
<label>
  <span><ng-content /></span>
  <input
    [value]="value"
    (input)="onInput($event)"
  />
}</label>
```

```typescript
// parent.component.ts
import { Component } from '@angular/core';
import { TextInputComponent } from './text-input.component';

@Component({
  selector: 'app-profile-editor',
  standalone: true,
  imports: [TextInputComponent],
  templateUrl: './profile-editor.component.html',
})
export class ProfileEditorComponent {
  name = '四国めたん';
}
```

```html
<!-- profile-editor.component.html -->
<app-text-input [(value)]="name">お名前</app-text-input>
<p>入力値: {{ name }}</p>
```

## ベストプラクティス
- プロパティ名とイベント名を`value`/`valueChange`のように揃えると`[(value)]`構文が利用できる
- 子コンポーネントはできるだけステートレスにし、親が状態を持つことでテストしやすくする
- イベントハンドラで直接代入する場合でもバリデーションや変換ロジックを検討する

## 注意点
- 子で@Input()の値を変更しても親には伝わらないため、必ずvalueChangeで通知する
- バリデーション失敗時はイベントをemitせず、エラーメッセージを表示するなどの設計が必要
- 複雑なフォームではReactive FormsとControlValueAccessorの利用を検討する

## 関連技術
- バナナインボックス構文 `[(...)]`
- Angular Forms（Template-driven, Reactive）
- ControlValueAccessorによるフォーム連携
