# #110 「@Output() 複数イベントの管理」

## 概要
子コンポーネントから複数種類のイベントを発火させ、親がそれぞれをハンドリングする設計パターンを学びます。

## 学習目標
- 複数の@Output()を宣言する方法を理解する
- 親テンプレートでイベントごとに別ハンドラを割り当てる
- イベントの命名と責務分離を整理する

## 技術ポイント
- **複数イベント**: `@Output() saved`, `@Output() canceled`
- **ハンドラ分離**: `(saved)="onSaved()"`, `(canceled)="onCanceled()"`
- **状態管理**: イベントの種類ごとにロジックを明確化

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
@Output() saved = new EventEmitter<void>();
@Output() canceled = new EventEmitter<void>();
```

```html
<button (click)="save()">保存</button>
<button (click)="cancel()">キャンセル</button>
``>

```html
<app-dialog
  (saved)="handleSave()"
  (canceled)="handleCancel()"
></app-dialog>
```

## 💻 詳細実装例（学習用）
```typescript
// dialog.component.ts
import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-dialog',
  standalone: true,
  templateUrl: './dialog.component.html',
})
export class DialogComponent {
  @Output() saved = new EventEmitter<void>();
  @Output() canceled = new EventEmitter<void>();

  save(): void {
    this.saved.emit();
  }

  cancel(): void {
    this.canceled.emit();
  }
}
```

```html
<!-- dialog.component.html -->
<div class="dialog">
  <h3>設定を保存しますか？</h3>
  <button type="button" (click)="save()">保存</button>
  <button type="button" (click)="cancel()">キャンセル</button>
}</div>
```

```typescript
// parent.component.ts
import { Component } from '@angular/core';
import { DialogComponent } from './dialog.component';

@Component({
  selector: 'app-settings-page',
  standalone: true,
  imports: [DialogComponent],
  templateUrl: './settings-page.component.html',
})
export class SettingsPageComponent {
  lastAction = '';

  handleSave(): void {
    this.lastAction = 'saved';
  }

  handleCancel(): void {
    this.lastAction = 'canceled';
  }
}
```

```html
<!-- settings-page.component.html -->
<app-dialog
  (saved)="handleSave()"
  (canceled)="handleCancel()"
></app-dialog>
<p>直近の操作: {{ lastAction }}</p>
```

## ベストプラクティス
- イベント名は意味を明確にし、1イベント1責務にする
- 親でのハンドラは小さな関数に分けて読みやすく保つ
- イベント数が多くなったらコンポーネント分割やサービス化を検討する

## 注意点
- 同じイベントハンドラでswitch文を使うより、別々の@Output()で分離した方が明確な場合が多い
- イベントを増やしすぎるとAPIが複雑化するので必要最小限にとどめる
- EventEmitterは複数emitされても動くが、親側での副作用が重複しないように注意する

## 関連技術
- Angular Materialダイアログのイベント設計
- Signalsと組み合わせたイベント管理
- ReduxやNgRxでのイベント駆動アーキテクチャ
