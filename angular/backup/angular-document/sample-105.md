# #105 「@Output() の基本構文」

## 概要
@Output()の宣言からemitまでの基本構文を詳細に確認し、イベントハンドリングのベースを固めます。

## 学習目標
- EventEmitterの型パラメータの指定方法を理解する
- emitの呼び出しタイミングを意識する
- 親テンプレートで複数イベントをハンドリングする構文を学ぶ

## 技術ポイント
- **宣言**: `@Output() saved = new EventEmitter<string>();`
- **emit**: `this.saved.emit('complete');`
- **テンプレート**: `(saved)="onSaved($event)"`


```typescript
@Output() saved = new EventEmitter<string>();
```

```typescript
save() { this.saved.emit('success'); }
```

```html
<app-editor (saved)="showToast($event)"></app-editor>
```

## 💻 詳細実装例（学習用）
```typescript
// editor.component.ts
import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-editor',
  standalone: true,
  templateUrl: './editor.component.html',
})
export class EditorComponent {
  @Output() saved = new EventEmitter<string>();

  save(): void {
    // 保存処理...
    this.saved.emit('保存が完了しました');
  }
}
```

```html
<!-- editor.component.html -->
<button type="button" (click)="save()">保存</button>
```

```typescript
// parent.component.ts
import { Component } from '@angular/core';
import { EditorComponent } from './editor.component';

@Component({
  selector: 'app-editor-page',
  standalone: true,
  imports: [EditorComponent],
  template: `
    <app-editor (saved)="handleSaved($event)"></app-editor>
  `,
})
export class EditorPageComponent {
  message = '';

  handleSaved(result: string): void {
    this.message = result;
  }
}
```

```html
<!-- editor-page.component.html -->
<p>{{ message }}</p>
```

## ベストプラクティス
- EventEmitter型を明確にし、anyを避ける
- emit前に必要な前処理を完了させ、親側でのハンドラは反応するだけにする
- メッセージなど静的値をemitする場合でも定数化して保守性を高める

## 注意点
- EventEmitterをサービスなどで使うのは推奨されず、コンポーネント間通信専用とする
- emitを同期的に呼ぶため、親のハンドラでエラーが出ると子の処理にも影響する
- 親がイベントハンドラを未設定だと何も起きないが緊急ではないので設計上OKか確認する

## 関連技術
- EventEmitterとObservable互換性
- `@Output()` のエイリアス指定
- SignalOutputとの比較
