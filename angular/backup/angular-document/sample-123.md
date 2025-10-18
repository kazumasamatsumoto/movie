# #123 「SignalInput vs @Input() 比較」

## 概要
従来の@Input()とSignalInputの挙動を比較し、移行のメリット・デメリットを整理します。

## 学習目標
- SignalInputの優位点（リアクティブ性、コード量削減）を理解する
- @Input()を継続利用するケースを把握する
- 移行時の注意点と段階的導入方法を学ぶ

## 技術ポイント
- **Signal API統一**: effectやcomputedとの親和性
- **互換性**: 既存ライブラリやバージョン制約で@Input()が必要なケース
- **テスト容易性**: Signals主体で副作用が減る

```typescript
readonly title = input<string>('initial');
```

```typescript
@Input() title = 'initial';
```

```typescript
readonly upper = computed(() => this.title().toUpperCase());
```

## 💻 詳細実装例（学習用）
```typescript
// signal-version.component.ts
import { Component, computed, input } from '@angular/core';

@Component({
  selector: 'app-signal-version',
  standalone: true,
  template: `
    <h3>Signal版: {{ upperTitle() }}</h3>
  `,
})
export class SignalVersionComponent {
  readonly title = input<string>('Signal Input');
  readonly upperTitle = computed(() => this.title().toUpperCase());
}
```

```typescript
// classic-version.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-classic-version',
  standalone: true,
  template: `
    <h3>従来版: {{ title.toUpperCase() }}</h3>
  `,
})
export class ClassicVersionComponent {
  @Input() title = 'Classic Input';
}
```

```typescript
// parent.component.ts
import { Component, signal } from '@angular/core';
import { SignalVersionComponent } from './signal-version.component';
import { ClassicVersionComponent } from './classic-version.component';

@Component({
  selector: 'app-compare',
  standalone: true,
  imports: [SignalVersionComponent, ClassicVersionComponent],
  templateUrl: './compare.component.html',
})
export class CompareComponent {
  readonly title = signal('Angular Input比較');
}
```

```html
<!-- compare.component.html -->
<app-signal-version [title]="title()"></app-signal-version>
<app-classic-version [title]="title()"></app-classic-version>
```

## ベストプラクティス
- 新規コンポーネントではSignalInputを優先し、既存コードは段階的に移行する
- SignalInputを使うとngOnChangesが不要になりコードが簡潔になる
- 共存シナリオでは整合性を保つため、Signal⇔従来Inputの同期ポイントを確認する

## 注意点
- SignalInputはAngular v17以降の機能であり、LTSや既存プロジェクトでは利用できない場合がある
- プロジェクト全体でAPIスタイルが混在すると混乱するため、ガイドラインを整備する
- カスタムデコレータや外部ライブラリが@Input()構文を前提にしていると互換性の問題が生じる

## 関連技術
- Angular Signalsドキュメント
- Angularアップグレードガイド
- ESLintルールでのSignal使用推奨設定
