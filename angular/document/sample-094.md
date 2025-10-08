# #094 「@Input() デフォルト値の設定」

## 概要
親から値が渡されなかった場合に備えて、@Input()プロパティへデフォルト値を設定する手法を学びます。初期値を持たせることで安全にレンダリングできます。

## 学習目標
- @Input()プロパティへの初期化の書き方を理解する
- getter/setterでフォールバック処理を行うパターンを把握する
- null合体演算子などで描画時の落ち込みを防ぐ

## 技術ポイント
- **初期値代入**: `@Input() color = 'primary';`
- **setter活用**: `set color(value: string) { this._color = value ?? 'primary'; }`
- **テンプレートガード**: `{{ label || '未設定' }}`でフォールバック

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
@Input() label = '未設定';
```

```typescript
private _type = 'info';
@Input()
set type(value: string) {
  this._type = value ?? 'info';
}
```

```html
<span>{{ label }}</span>
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, Input } from '@angular/core';

type AlertType = 'info' | 'success' | 'warning' | 'error';

@Component({
  selector: 'app-alert',
  standalone: true,
  templateUrl: './alert.component.html',
  styleUrls: ['./alert.component.css'],
})
export class AlertComponent {
  @Input() title = 'お知らせ';
  @Input() dismissible = false;

  private _type: AlertType = 'info';

  @Input()
  set type(value: AlertType | undefined) {
    this._type = value ?? 'info';
  }
  get type(): AlertType {
    return this._type;
  }
}
```

```html
<!-- alert.component.html -->
<article class="alert" [class]="'alert-' + type">
  <strong>{{ title }}</strong>
  <ng-content></ng-content>
  <button *ngIf="dismissible" type="button" aria-label="閉じる">×</button>
</article>
```

```typescript
// parent.component.ts
import { Component } from '@angular/core';
import { AlertComponent } from './alert.component';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [AlertComponent],
  templateUrl: './dashboard.component.html',
})
export class DashboardComponent {
  showAlert = true;
}
```

```html
<!-- dashboard.component.html -->
<app-alert type="success">デフォルト値があるので安心です。</app-alert>
<app-alert
  *ngIf="showAlert"
  [dismissible]="true"
>
  タイトルを省略すると「お知らせ」が表示されます。
</app-alert>
```

## ベストプラクティス
- デフォルト値には意味のあるUI文言を設定し、未指定でも自然な表示にする
- setterでフォールバックを実装する場合は、外部からアクセスできるgetterも用意して整合性を保つ
- オプショナルなプロパティには`| undefined`を明示し、nullish coalescingで補完する

## 注意点
- デフォルト値は初期化時にのみ適用されるので、親からundefinedを明示的に渡すと再評価される点に注意
- setterで重い処理を行うと変更検知の度に実行されるため軽量に保つ
- `!`で初期化なしにする場合はデフォルトが効かないのでどちらを使うか事前に決める

## 関連技術
- TypeScriptのnullish coalescing (`??`)
- Getter/Setter構文
- Angular ESLint `no-inputs-metadata-property`
