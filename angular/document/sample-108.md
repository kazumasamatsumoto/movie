# #108 「@Output() データ付きイベント」

## 概要
@Output()イベントでデータを添えて親へ通知する方法を学び、イベントペイロードの型安全性を確保します。

## 学習目標
- EventEmitterに型パラメータを付ける方法を理解する
- `$event`から渡されたデータを親で利用する流れを習得する
- イベントデータにスキーマを設け、契約を明確にする

## 技術ポイント
- **型付きEventEmitter**: `new EventEmitter<SaveResult>()`
- **イベントハンドラ**: `(saved)="handleSaved($event)"`
- **インターフェース定義**: ペイロードの構造を`type`や`interface`で表現

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
@Output() saved = new EventEmitter<{ id: string; status: string }>();
```

```typescript
this.saved.emit({ id, status: 'success' });
```

```html
<app-editor (saved)="handleSaved($event)"></app-editor>
```

## 💻 詳細実装例（学習用）
```typescript
// editor.component.ts
import { Component, EventEmitter, Output } from '@angular/core';

type SaveResult = {
  id: string;
  status: 'success' | 'error';
  message?: string;
};

@Component({
  selector: 'app-editor',
  standalone: true,
  templateUrl: './editor.component.html',
})
export class EditorComponent {
  @Output() saved = new EventEmitter<SaveResult>();

  async save(): Promise<void> {
    const id = crypto.randomUUID();
    await new Promise((resolve) => setTimeout(resolve, 200));
    this.saved.emit({ id, status: 'success' });
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
  templateUrl: './editor-page.component.html',
})
export class EditorPageComponent {
  lastMessage = '';

  handleSaved(result: { id: string; status: string }): void {
    this.lastMessage = `ID ${result.id} が ${result.status} で保存されました`;
  }
}
```

```html
<!-- editor-page.component.html -->
<app-editor (saved)="handleSaved($event)"></app-editor>
<p>{{ lastMessage }}</p>
```

## ベストプラクティス
- イベントデータのスキーマをtypeで定義し、親子間の契約を明確化する
- オプションのデータは`message?`のようにoptionalにして受け取り側で判定する
- イベント名とペイロードの意味が一致するよう命名する

## 注意点
- 大量のデータをイベントで渡すとシリアライズコストが増えるので必要最小限にする
- `any`型でイベントを扱うと意図しない値が流入する恐れがある
- 非同期処理中に複数回emitすると親側で想定外の挙動になる場合があるので制御フラグを使う

## 関連技術
- TypeScript型ガード
- RxJS Observableによるイベントストリーム
- SignalOutputとSignal-basedイベント
