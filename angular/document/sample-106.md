# #106 「EventEmitter の使い方」

## 概要
`EventEmitter`の基礎挙動と注意点を整理し、@Output()でのイベント通知を安全に扱う方法を学びます。

## 学習目標
- EventEmitterがObservableを継承していることを理解する
- emit/subscribe/completeの役割を整理する
- UIイベント以外での使用を避ける理由を把握する

## 技術ポイント
- **Observable互換**: `saved`は`saved.subscribe(...)`で購読可能
- **emitの戻り値**: `emit`はvoid、例外は伝播する
- **complete/error**: UIイベントでは通常呼び出さない

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
@Output() saved = new EventEmitter<string>();
```

```typescript
const sub = this.saved.subscribe(console.log);
```

```typescript
this.saved.emit('done');
```

## 💻 詳細実装例（学習用）
```typescript
import { Component, EventEmitter, OnDestroy, Output } from '@angular/core';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-saver',
  standalone: true,
  templateUrl: './saver.component.html',
})
export class SaverComponent implements OnDestroy {
  @Output() saved = new EventEmitter<string>();
  private readonly sub: Subscription;

  constructor() {
    this.sub = this.saved.subscribe((message) =>
      console.log('Debug:', message),
    );
  }

  save(): void {
    this.saved.emit('保存しました');
  }

  ngOnDestroy(): void {
    this.sub.unsubscribe();
    this.saved.complete();
  }
}
```

```html
<!-- saver.component.html -->
<button type="button" (click)="save()">保存</button>
```

```typescript
// parent.component.ts
import { Component } from '@angular/core';
import { SaverComponent } from './saver.component';

@Component({
  selector: 'app-log-page',
  standalone: true,
  imports: [SaverComponent],
  template: `
    <app-saver (saved)="log($event)"></app-saver>
  `,
})
export class LogPageComponent {
  log(message: string): void {
    console.info('親で受信:', message);
  }
}
```

## ベストプラクティス
- `EventEmitter`はUIイベントの通知専用とし、サービスでの状態共有にはRxJS Subjectを使う
- `emit`に渡すデータ型を揃え、複数種類のデータを同じイベントで送らない
- デバッグ用にsubscribeする場合は`ngOnDestroy`で解除する

## 注意点
- `EventEmitter`はZone.js内で実行されるため、emitが重い処理を含むとUIが固まる
- `complete`や`error`を呼ぶと親のハンドラが以後呼ばれないので注意
- 多数のイベントをemitするときはスロットリングやバッチ処理を検討する

## 関連技術
- RxJS Subject/BehaviorSubject
- SignalOutput (Angular v17+)
- Zone.js と change detection
