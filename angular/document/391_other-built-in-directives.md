# #391 「その他の組み込み Directive」

## 概要
Angularには`ngClass`や`ngStyle`以外にも多様なAttribute Directiveが存在し、テンプレート表現力を高めたり動的レンダリングを支援する。

## 学習目標
- 主要な組み込みAttribute Directiveの種類を把握する
- 用途ごとに適切なディレクティブを選択できるようになる
- カスタムディレクティブとの併用をイメージする

## 技術ポイント
- `ngNonBindable`, `ngPlural`, `ngTemplateOutlet`, `ngComponentOutlet`など
- 特殊用途ディレクティブは`CommonModule`や`RouterModule`に含まれる
- 利用時はスタンドアロンコンポーネントに対応する`imports`設定が必要

## 📺 画面表示用コード（動画用）
```html
<ng-container [ngTemplateOutlet]="itemTpl" [ngTemplateOutletContext]="{ $implicit: item }"></ng-container>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-builtins-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <p ngNonBindable>{{ おまじない }}</p>
    <ng-container [ngTemplateOutlet]="cardTpl" [ngTemplateOutletContext]="{ $implicit: 'Angular' }"></ng-container>
    <ng-template #cardTpl let-name>
      <article class="card">Hello {{ name }}</article>
    </ng-template>
  `
})
export class BuiltinsDemoComponent {}
```

## ベストプラクティス
- 組み込みディレクティブをカタログ化し、適切な用途をチームで共有する
- スタンドアロン環境では必要なディレクティブを`imports`に明示的に追加する
- カスタムディレクティブと衝突しないよう命名規則を整える

## 注意点
- モジュールによってエクスポートされるディレクティブが異なるため、依存関係を確認する
- 動的レンダリング系ディレクティブはパフォーマンスに影響する場合があるためプロファイルを取る
- SSRで対応しているか公式ドキュメントで確認する

## 関連技術
- CommonModule
- RouterModule
- Angular Materialのディレクティブ群
