# #263 「Component の拡張性設計」

## 概要
拡張性を備えたコンポーネントは、将来的な要件追加やバリエーション変化に応じて柔軟に振る舞いを変えられるよう設計されたコンポーネントである。

## 学習目標
- 拡張ポイントをInput/Configで公開する方法を学ぶ
- Template Slotによる拡張パターンを理解する
- Signal設計で変更影響を局所化する

## 技術ポイント
- Configオブジェクトによる振る舞い制御
- Template Slot（ng-content, ngTemplateOutlet）
- computedで派生状態を管理

## 📺 画面表示用コード（動画用）
```typescript
export type BannerConfig = {
  readonly tone: 'info' | 'success' | 'warning';
  readonly dismissible?: boolean;
};
```

```typescript
@Component({
  selector: 'app-banner',
  standalone: true,
  template: `<section [class]="'banner '+config.tone"><ng-content></ng-content></section>`
})
export class BannerComponent {
  @Input({ required: true }) config!: Readonly<BannerConfig>;
}
```

```typescript
@Component({
  selector: 'app-banner-actions',
  standalone: true,
  template: `<button *ngIf="config.dismissible" (click)="close.emit()">閉じる</button>`
})
export class BannerActionsComponent {
  @Input({ required: true }) config!: Readonly<BannerConfig>;
  @Output() close = new EventEmitter<void>();
}
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-banner-shell',
  standalone: true,
  imports: [BannerComponent, BannerActionsComponent],
  template: `
    <app-banner [config]="config">
      <strong>{{ title }}</strong>
      <p>{{ message }}</p>
      <ng-content></ng-content>
    </app-banner>
    <app-banner-actions [config]="config" (close)="onClose()"></app-banner-actions>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class BannerShellComponent {
  @Input({ required: true }) config!: Readonly<BannerConfig>;
  @Input({ required: true }) title = '';
  @Input({ required: true }) message = '';
  @Output() dismissed = new EventEmitter<void>();

  onClose(): void {
    if (this.config.dismissible) {
      this.dismissed.emit();
    }
  }
}
```

## ベストプラクティス
- 拡張ポイントはConfigオブジェクトとSlotで提供し、if分岐を肥大化させない
- 必要なSignalだけWritableにし、派生情報はcomputedで生成する
- 拡張仕様をガイドとして残し、組織全体で統一する

## 注意点
- Configに過剰なオプションを追加しない
- Template Slotの数が多い場合は別コンポーネント化を検討する
- Config変更時の互換性を確認するためにテストを追加する

## 関連技術
- Configパターン
- Content Projection
- Angular Signals
