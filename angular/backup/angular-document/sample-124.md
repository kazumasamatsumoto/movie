# #124 「SignalOutput - signal() ベース出力」

## 概要
SignalOutput APIを使ってSignalベースのイベントを定義し、従来のEventEmitterより表現力と型安全性を高める方法を学びます。

## 学習目標
- SignalOutputの基本構文を理解する
- `emit()` ではなく `.emit(value)`（同名）の挙動を把握する
- SignalInputと組み合わせてSignal中心の通信を構築する

## 技術ポイント
- **出力宣言**: `readonly saved = output<string>();`
- **発火**: `this.saved.emit('done');`
- **Observable互換**: SignalOutputはEventEmitter同様に購読可能

```typescript
import { output } from '@angular/core';
```

```typescript
readonly saved = output<string>();
```

```typescript
this.saved.emit('success');
```

## 💻 詳細実装例（学習用）
```typescript
// signal-output.component.ts
import { Component, output } from '@angular/core';

@Component({
  selector: 'app-signal-output',
  standalone: true,
  templateUrl: './signal-output.component.html',
})
export class SignalOutputComponent {
  readonly saved = output<string>();

  save(): void {
    this.saved.emit('signal-output');
  }
}
```

```html
<!-- signal-output.component.html -->
<button type="button" (click)="save()">SignalOutputで保存</button>
```

```typescript
// parent.component.ts
import { Component } from '@angular/core';
import { SignalOutputComponent } from './signal-output.component';

@Component({
  selector: 'app-output-page',
  standalone: true,
  imports: [SignalOutputComponent],
  template: `
    <app-signal-output (saved)="handleSaved($event)"></app-signal-output>
  `,
})
export class OutputPageComponent {
  handleSaved(message: string): void {
    console.log('SignalOutputイベント:', message);
  }
}
```

## ベストプラクティス
- SignalOutputを使うとSignalInputと同じAPIセットで統一でき、リアクティブ思考がしやすい
- emitsするデータ型をジェネリクスで明示し、呼び出し側と受信側の契約を保つ
- 従来のEventEmitter同様に親テンプレートでは`(saved)="..."`で受け取れる

## 注意点
- SignalOutputはAngular v17以降のプレビューAPIであり、安定版かどうかを確認した上で採用する
- EventEmitter特有の機能（complete/error）を使っていた場合は代替手段を検討する
- Signal中心の設計に切り替える場合、開発チームの理解とガイドライン整備が必要

## 関連技術
- SignalInput / SignalOutputセット
- `toObservable`, `toSignal`でSignalとObservableを橋渡し
- Angular Signals RFC
