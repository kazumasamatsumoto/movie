# #274 「YAGNI 原則の適用」

## 概要
YAGNI（You Aren't Gonna Need It）は、必要になるまで機能や拡張ポイントを追加しないことで、過剰な複雑さを避ける設計原則である。

## 学習目標
- YAGNIをコンポーネント開発に適用する判断基準を理解する
- 最小限のInput/Outputで構築する方法を学ぶ
- 要件発生時にリファクタリングで対応する手順を把握する

## 技術ポイント
- LeanなViewModel設計
- Signalの最小定義
- Backlogによる将来要件の追跡

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-simple-banner', standalone: true, template: `<section class="banner">{{ message }}</section>` })
export class SimpleBannerComponent {
  @Input({ required: true }) message = '';
}
```

```typescript
export type BannerVm = {
  readonly message: string;
};
```

```typescript
@Component({ selector: 'app-simple-banner-container', standalone: true, imports: [SimpleBannerComponent], template: `<app-simple-banner [message]="vm()"></app-simple-banner>` })
export class SimpleBannerContainerComponent {
  private readonly message = signal('ようこそ');
  readonly vm = this.message.asReadonly();
}
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-simple-banner-feature',
  standalone: true,
  imports: [SimpleBannerContainerComponent],
  template: `<app-simple-banner-container></app-simple-banner-container>`
})
export class SimpleBannerFeatureComponent {}
```

## ベストプラクティス
- Inputは実際に必要になった時点で追加し、初期段階では最小構成に留める
- 追加要望はBacklogで管理し、対応時に設計を見直す
- Signalやサービスも最小個数から始め、後から拡張する

## 注意点
- 最小構成でもアクセシビリティなど必須要件は満たす
- 将来機能を想定したコメントをコードに残しすぎない
- 拡張時はテストを追加し影響を局所化する

## 関連技術
- Lean開発
- Angular Signals
- Product Backlog管理
