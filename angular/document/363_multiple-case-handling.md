# #363 「複数 case の処理」

## 概要
同じUIを複数のケースで表示したい場合、`*ngSwitchCase`を複数定義して`ng-template`を共有すると重複を避けられる。

## 学習目標
- 複数ケースで同一テンプレートを再利用する方法を理解する
- テンプレート参照の活用とスコープを学ぶ
- 状態管理とUIの対応関係を設計する

## 技術ポイント
- `ng-template`に共通UIをまとめ、複数ケースから参照
- caseごとに追加処理が必要な場合は内部で分岐する
- 状態を分類してケースをグルーピングする

## 📺 画面表示用コード（動画用）
```html
<ng-template #reviewTpl><p>レビュー待ち</p></ng-template>
<ng-container *ngSwitchCase="'draft'">
  <ng-container *ngTemplateOutlet="reviewTpl"></ng-container>
</ng-container>
<ng-container *ngSwitchCase="'pending'">
  <ng-container *ngTemplateOutlet="reviewTpl"></ng-container>
</ng-container>
```

## 💻 詳細実装例（学習用）
```typescript
type ReviewState = 'draft' | 'pending' | 'approved' | 'rejected';

@Component({
  selector: 'app-multi-case-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <ng-template #reviewTpl>
      <p>レビュー中の状態です。</p>
    </ng-template>
    <section [ngSwitch]="state">
      <ng-container *ngSwitchCase="'draft'">
        <ng-container *ngTemplateOutlet="reviewTpl"></ng-container>
      </ng-container>
      <ng-container *ngSwitchCase="'pending'">
        <ng-container *ngTemplateOutlet="reviewTpl"></ng-container>
      </ng-container>
      <p *ngSwitchCase="'approved'">承認済みです。</p>
      <p *ngSwitchCase="'rejected'">差し戻しされました。</p>
      <p *ngSwitchDefault>未分類の状態です。</p>
    </section>
  `
})
export class MultiCaseDemoComponent {
  protected state: ReviewState = 'draft';
}
```

## ベストプラクティス
- 複数ケースで同じテンプレートを使う際は`ng-template`を活用し、DRY原則を守る
- 状態をまとめて別の列挙型に置き換えると更に整理できる
- テストで各状態の表示を確認し、共通テンプレートが正しく適用されるか検証する

## 注意点
- Angular v17未満では`ngSwitchCase`が複数値を直接受け取れないためテンプレート参照で共通化する
- 共通テンプレート内で状態固有の処理をしないよう責務を分離する
- ケースの追加・変更時に共通テンプレートが影響を受けるのでテストを更新する

## 関連技術
- ng-template
- DRY原則
- State Management
