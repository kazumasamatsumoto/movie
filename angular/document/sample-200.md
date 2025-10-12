# #200 「デフォルトコンテンツの設定」

## 概要
親がコンテンツを渡さなかった場合に表示するデフォルトコンテンツを用意する方法を学び、コンポーネントの安全な挙動を確保します。

## 学習目標
- `ng-content`でデフォルトコンテンツを提供するパターンを理解する
- `ContentChild`を使って投影の有無を判定し、フォールバックを出し分ける方法を習得する
- 空状態（Empty State）の設計とUI/UX向上につなげる

## 技術ポイント
- **デフォルト挿入**: `ng-content`の後に通常のHTMLを置くと、マッチするコンテンツがない場合に表示される
- **条件付き**: `ContentChild`で投影を確認し、`ng-template`を使ってフォールバックを切り替える
- **Empty State**: ブランクメッセージやアイコンを用意してユーザーを導く

## 📺 画面表示用コード（動画用）

```html
<ng-content></ng-content>
<p *ngIf="!hasContent">デフォルトメッセージ</p>
```

```typescript
@ContentChild('content')
content?: ElementRef;
```

```html
<ng-container *ngIf="hasContent; else fallback">
  <ng-content></ng-content>
</ng-container>
<ng-template #fallback>...</ng-template>
```

## 💻 詳細実装例（学習用）
```typescript
// empty-state.component.ts
import { AfterContentInit, Component, ContentChild, TemplateRef } from '@angular/core';

@Component({
  selector: 'app-empty-state',
  standalone: true,
  templateUrl: './empty-state.component.html',
  styleUrls: ['./empty-state.component.scss'],
})
export class EmptyStateComponent implements AfterContentInit {
  @ContentChild('content')
  contentTemplate?: TemplateRef<unknown>;

  hasContent = false;

  ngAfterContentInit(): void {
    this.hasContent = !!this.contentTemplate;
  }
}
```

```html
<!-- empty-state.component.html -->
<section class="empty-state">
  <ng-container *ngIf="hasContent; else defaultContent">
    <ng-content select="[content]"></ng-content>
  </ng-container>
  <ng-template #defaultContent>
    <h3>表示する内容がありません</h3>
    <p>条件を変えるか、新しいデータを追加してください。</p>
  </ng-template>
</section>
```

```html
<!-- parent.component.html -->
<app-empty-state>
  <div content>
    <h3>データがありません</h3>
    <p>フィルターをリセットしてみてください。</p>
  </div>
</app-empty-state>

<app-empty-state></app-empty-state> <!-- デフォルトが表示される -->
```

## ベストプラクティス
- 空状態を想定したデフォルトメッセージやガイドを用意し、UXを向上させる
- ContentChildを使って投影の有無を判定し、フォールバックをロジックで切り替える
- ドキュメントで「投影しなかった場合の挙動」を明示し、利用者が安心して使えるようにする

## 注意点
- デフォルトコンテンツに重い処理やメディアを含めると、投影がある場合でも無駄にロードされる可能性がある
- `ng-content`以外の要素が先に描画されるとDOM順序が変わるため、フォールバックは最後に置く
- デフォルトコンテンツの多言語対応やアクセシビリティメッセージを忘れない

## 関連技術
- `ContentChild`での投影確認
- `ng-template`・`ngTemplateOutlet`による条件付きレンダリング
- Empty Stateデザインパターン


