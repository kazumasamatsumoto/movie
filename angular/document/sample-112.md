# #112 「双方向バインディングのカスタム実装」

## 概要
独自コンポーネントで`[(value)]`のような双方向バインディングを実現するために、@Input()と@Output()をペアで構成する方法を学びます。

## 学習目標
- `value`/`valueChange`ペアの命名規則を理解する
- バナナインボックス構文を利用できるようにする手順を習得する
- コンポーネントで値を更新したときのemitタイミングを管理する

## 技術ポイント
- **命名規約**: `[(prop)]`は`@Input() prop`と`@Output() propChange`
- **テンプレート**: `[prop]="..."` `(propChange)="..."`
- **双方向同期**: 子が変更をemitし、親が値を更新して再描画する

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
@Input() checked = false;
@Output() checkedChange = new EventEmitter<boolean>();
```

```html
<input
  type="checkbox"
  [checked]="checked"
  (change)="onToggle($event)"
/>{``}
```

```html
<app-toggle [(checked)]="enabled"></app-toggle>
```

## 💻 詳細実装例（学習用）
```typescript
// toggle.component.ts
import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-toggle',
  standalone: true,
  templateUrl: './toggle.component.html',
  styleUrls: ['./toggle.component.css'],
})
export class ToggleComponent {
  @Input() checked = false;
  @Output() checkedChange = new EventEmitter<boolean>();

  onToggle(event: Event): void {
    const target = event.target as HTMLInputElement;
    this.checkedChange.emit(target.checked);
  }
}
```

```html
<!-- toggle.component.html -->
<label class="toggle">
  <input
    type="checkbox"
    [checked]="checked"
    (change)="onToggle($event)"
  />
  <span>{{ checked ? 'ON' : 'OFF' }}</span>
</label>
```

```typescript
// parent.component.ts
import { Component } from '@angular/core';
import { ToggleComponent } from './toggle.component';

@Component({
  selector: 'app-preferences',
  standalone: true,
  imports: [ToggleComponent],
  templateUrl: './preferences.component.html',
})
export class PreferencesComponent {
  enabled = true;
}
```

```html
<!-- preferences.component.html -->
<app-toggle [(checked)]="enabled"></app-toggle>
<p>機能は: {{ enabled ? '有効' : '無効' }}</p>
```

## ベストプラクティス
- 双方向バインディングを提供する場合は、単方向でも利用できるように@Input()と@Output()をそのまま公開する
- イベントをemitする前に値が変わっているかを確認し、不要な更新を避ける
- 状態を内部に持たない(stateless)コンポーネントにするとテストが容易になる

## 注意点
- 双方向バインディングを多用するとデータの流れが追いにくくなるため、必要な箇所に限定する
- 入力値と出力値の型を一致させる（同じ型にしないとバインディングが破綻する）
- ControlValueAccessorを実装するとAngular Formsと連携しやすくなるが、今回のパターンとは別物

## 関連技術
- バナナインボックス `[(...)]`
- ControlValueAccessorとAngular Forms
- SignalInput/SignalOutputでの双方向同期
