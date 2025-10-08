# #107 「@Output() カスタムイベント発火」

## 概要
ユーザー操作や非同期処理の完了など任意のタイミングで@Output()イベントを発火し、親へ通知するパターンを学びます。

## 学習目標
- カスタムイベントの命名と発火タイミングを理解する
- 非同期処理の完了後にemitする方法を習得する
- イベントを複数回発火させる場合の注意点を理解する

## 技術ポイント
- **emitのタイミング**: ボタンクリック、API完了、タイマーなど任意
- **Promise後処理**: `await service.save(); this.saved.emit();`
- **複数回発火**: イベントハンドラ側で影響を考慮する

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
@Output() completed = new EventEmitter<void>();
```

```typescript
async submit() {
  await this.api.save();
  this.completed.emit();
}
```

```html
<app-form (completed)="refresh()"></app-form>
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-upload-button',
  standalone: true,
  templateUrl: './upload-button.component.html',
})
export class UploadButtonComponent {
  @Output() uploaded = new EventEmitter<string>();
  uploading = false;

  async upload(): Promise<void> {
    if (this.uploading) return;
    this.uploading = true;
    await new Promise((resolve) => setTimeout(resolve, 400));
    this.uploading = false;
    this.uploaded.emit('upload-complete');
  }
}
```

```html
<!-- upload-button.component.html -->
<button type="button" (click)="upload()" [disabled]="uploading">
  {{ uploading ? 'アップロード中…' : 'アップロード' }}
</button>
```

```typescript
// parent.component.ts
import { Component } from '@angular/core';
import { UploadButtonComponent } from './upload-button.component';

@Component({
  selector: 'app-media-page',
  standalone: true,
  imports: [UploadButtonComponent],
  template: `
    <app-upload-button (uploaded)="handleUploaded($event)"></app-upload-button>
    <p>{{ message }}</p>
  `,
})
export class MediaPageComponent {
  message = '';

  handleUploaded(status: string): void {
    this.message = status;
  }
}
```

## ベストプラクティス
- 非同期処理の途中でボタン連打を防ぐためにフラグで制御する
- emitするデータはイベント名と整合するようにする（completedなら成功状態など）
- 親でのハンドラは副作用を最小限に保ち、必要ならサービスへ委譲する

## 注意点
- 非同期処理内で例外が発生した場合はemitされないので、try/catchでハンドリングする
- イベントを重複して発火させると親側で多重処理になるため、制御フラグを導入する
- イベントループ外でemitするとChangeDetectionが走らないことがあるのでZone外処理には注意

## 関連技術
- Angular HttpClientによる非同期処理
- RxJS `fromEvent`, `Subject`
- ChangeDetectorRefの利用
