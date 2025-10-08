# #125 「SignalOutput vs @Output() 比較」

## 概要
SignalOutputと従来の@Output()（EventEmitter）の違いを比較し、適切な選択基準を整理します。

## 学習目標
- SignalOutputの利点と制約を理解する
- EventEmitterを継続利用するケースを把握する
- プロジェクトでの段階的移行を考える

## 技術ポイント
- **Signalベース**: SignalOutputはSignal APIと統一される
- **EventEmitter互換**: 従来のライブラリやデコレータがEventEmitter前提
- **API成熟度**: SignalOutputは新しいAPIで安定性やドキュメントを確認する必要がある

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
readonly saved = output<string>(); // SignalOutput
```

```typescript
@Output() saved = new EventEmitter<string>(); // 従来
```

```typescript
// emitはどちらも saved.emit(value)
```

## 💻 詳細実装例（学習用）
```typescript
// signal-output.component.ts
import { Component, output } from '@angular/core';

@Component({
  selector: 'app-signal-output-demo',
  standalone: true,
  template: `<button type="button" (click)="save()">SignalOutput</button>`,
})
export class SignalOutputDemoComponent {
  readonly saved = output<string>();

  save(): void {
    this.saved.emit('signal-version');
  }
}
```

```typescript
// classic-output.component.ts
import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-classic-output-demo',
  standalone: true,
  template: `<button type="button" (click)="save()">EventEmitter</button>`,
})
export class ClassicOutputDemoComponent {
  @Output() saved = new EventEmitter<string>();

  save(): void {
    this.saved.emit('classic-version');
  }
}
```

```typescript
// compare.component.ts
import { Component } from '@angular/core';
import { SignalOutputDemoComponent } from './signal-output-demo.component';
import { ClassicOutputDemoComponent } from './classic-output-demo.component';

@Component({
  selector: 'app-output-compare',
  standalone: true,
  imports: [SignalOutputDemoComponent, ClassicOutputDemoComponent],
  template: `
    <app-signal-output-demo (saved)="log('signal', $event)"></app-signal-output-demo>
    <app-classic-output-demo (saved)="log('classic', $event)"></app-classic-output-demo>
  `,
})
export class OutputCompareComponent {
  log(type: string, value: string): void {
    console.log(type, value);
  }
}
```

## ベストプラクティス
- 新規コンポーネントではSignalOutputを検討し、SignalInputと統一して摩擦を減らす
- 従来のEventEmitterで十分な場合は無理に置き換えず、整合性を重視する
- チームにSignal APIの知識が浸透してから移行する。実験的に導入してフィードバックを得る

## 注意点
- SignalOutputはまだエコシステムやドキュメントが少ないため、安定性を確認する
- EventEmitter特有の`complete`や`error`を利用している場合は代替手段が必要
- テストやツールがEventEmitter前提の場合、SignalOutputへの移行に不具合がないか確認する

## 関連技術
- Angular Signals Roadmap
- EventEmitterとObservableの違い
- Signal-basedコンポーネント開発のベストプラクティス
