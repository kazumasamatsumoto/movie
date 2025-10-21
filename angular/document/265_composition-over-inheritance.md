# #265 「Composition over Inheritance」

## 概要
Composition over Inheritanceは、共通機能を継承で共有するのではなく小さなコンポーネントやディレクティブを組み合わせて再利用する設計指針である。

## 学習目標
- コンポーネント構成で合成パターンを適用する
- ディレクティブやサービスによる機能共有を学ぶ
- 継承に頼らない拡張方法を理解する

## 技術ポイント
- Attributeディレクティブによる振る舞い注入
- Content Projectionでの構成
- サービス分離による疎結合化

## 📺 画面表示用コード（動画用）
```typescript
@Directive({
  selector: '[appElevated]',
  standalone: true,
  host: { class: 'elevated' }
})
export class ElevatedDirective {}
```

```typescript
@Component({
  selector: 'app-panel',
  standalone: true,
  template: `<section appElevated><ng-content></ng-content></section>`
})
export class PanelComponent {}
```

```typescript
@Component({
  selector: 'app-info-panel',
  standalone: true,
  imports: [PanelComponent],
  template: `<app-panel><p>{{ message }}</p></app-panel>`
})
export class InfoPanelComponent {
  @Input({ required: true }) message = '';
}
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-dashboard-panels',
  standalone: true,
  imports: [InfoPanelComponent, PanelComponent],
  template: `
    <app-panel><h3>{{ title }}</h3></app-panel>
    <app-info-panel [message]="description"></app-info-panel>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class DashboardPanelsComponent {
  @Input({ required: true }) title = '';
  @Input({ required: true }) description = '';
}
```

## ベストプラクティス
- 共通スタイルはディレクティブへ移し、必要に応じて組み合わせる
- コンポーネント構成でバリエーションを表現し、継承による強制的な依存を避ける
- Storybookで組み合わせパターンをドキュメント化する

## 注意点
- 合成対象が多すぎると階層が深くなるためレビュー時に確認する
- ディレクティブの副作用は最小限に抑える
- 継承を使う場合は明確な理由を記録する

## 関連技術
- Attributeディレクティブ
- Content Projection
- デザインシステム構成
