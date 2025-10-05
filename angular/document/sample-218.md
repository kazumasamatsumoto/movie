# #218 「コンテンツ投影のベストプラクティス」

## 概要
Angular v20のコンテンツ投影におけるベストプラクティスと推奨される実装方法を学習します。

## 学習目標
- コンテンツ投影のベストプラクティスを理解する
- 推奨される実装パターンを習得する
- 保守性の高いコンテンツ投影設計を実現できるようになる

## 技術ポイント
- ベストプラクティス
- 設計パターン
- 保守性

## 📺 画面表示用コード

```html
<!-- 推奨される実装パターン -->
<app-well-designed-component>
  <!-- 明確なセレクターを使用 -->
  <div class="component-header">
    <h2>ヘッダー</h2>
  </div>
  <div class="component-body">
    <p>ボディコンテンツ</p>
  </div>
  <div class="component-footer">
    <button>アクション</button>
  </div>
</app-well-designed-component>
```

```html
<!-- 子コンポーネント（推奨実装） -->
<div class="well-designed-container">
  <!-- デフォルトコンテンツを提供 -->
  <header class="component-header">
    <ng-content select=".component-header">
      <h2>デフォルトヘッダー</h2>
    </ng-content>
  </header>
  
  <main class="component-body">
    <ng-content select=".component-body">
      <p>デフォルトコンテンツ</p>
    </ng-content>
  </main>
  
  <footer class="component-footer">
    <ng-content select=".component-footer">
      <button>デフォルトアクション</button>
    </ng-content>
  </footer>
</div>
```

```typescript
// 推奨されるコンポーネントクラス
@Component({
  selector: 'app-well-designed-component',
  template: `...`,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class WellDesignedComponent implements OnInit {
  // 明確なプロパティ定義
  @Input() title = '';
  @Input() disabled = false;
  
  // 適切なライフサイクル管理
  ngOnInit() {
    this.validateInputs();
  }
  
  private validateInputs(): void {
    if (!this.title) {
      console.warn('title プロパティが設定されていません');
    }
  }
}
```

## 実践的な活用例

```html
<!-- アクセシビリティを考慮した実装 -->
<app-accessible-card [ariaLabel]="'ユーザー情報カード'">
  <div class="card-header" role="banner">
    <h3 id="user-title">ユーザー名</h3>
  </div>
  <div class="card-body" role="main" [attr.aria-labelledby]="'user-title'">
    <p>ユーザーの詳細情報</p>
  </div>
  <div class="card-footer" role="contentinfo">
    <button aria-label="ユーザーを編集">編集</button>
  </div>
</app-accessible-card>
```

## ベストプラクティス
- 明確で意味のあるセレクターを使用する
- デフォルトコンテンツを提供する
- 適切なドキュメント化を行う
- アクセシビリティを考慮する
- パフォーマンスを最適化する

## 注意点
- セレクターの複雑さを避ける
- 過度な投影を避ける
- ネストの深さを制限する

## 関連技術
- Component Design
- Accessibility
- Performance Optimization
