# #169 「Component 固有スタイルの適用」

## 概要
Angular v20におけるコンポーネント固有スタイルの効率的な管理方法。stylesプロパティとstyleUrlsプロパティを使い分け、適切なスタイル分離と保守性の高いスタイル設計を実現する。

## 学習目標
- stylesとstyleUrlsの使い分けを理解する
- 適切なスタイル管理方法を学ぶ
- スタイルの分離戦略を把握する

## 技術ポイント
- styles プロパティでのインライン定義
- styleUrls プロパティでの外部ファイル読み込み
- スタイルの規模による使い分け
- 保守性を考慮した設計

## 📺 画面表示用コード

### インラインスタイル（小規模）
```typescript
@Component({
  selector: 'app-inline-styles',
  template: `
    <div class="simple-card">
      <h3>インラインスタイル</h3>
      <p>小規模なスタイルはインラインで定義</p>
    </div>
  `,
  styles: [`
    .simple-card {
      background: white;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
      margin: 10px 0;
    }
    
    .simple-card h3 {
      color: #333;
      margin-bottom: 10px;
      font-size: 18px;
    }
    
    .simple-card p {
      color: #666;
      line-height: 1.5;
    }
  `]
})
export class InlineStylesComponent {}
```

### 外部スタイルファイル（大規模）
```typescript
@Component({
  selector: 'app-external-styles',
  template: `
    <div class="complex-component">
      <header class="header">
        <h1>複雑なコンポーネント</h1>
        <nav class="navigation">
          <a href="#" class="nav-link">ホーム</a>
          <a href="#" class="nav-link">サービス</a>
          <a href="#" class="nav-link">お問い合わせ</a>
        </nav>
      </header>
      <main class="main-content">
        <section class="hero">
          <h2>メインコンテンツ</h2>
          <p>詳細なスタイルは外部ファイルで管理</p>
        </section>
      </main>
      <footer class="footer">
        <p>&copy; 2024 Angular v20</p>
      </footer>
    </div>
  `,
  styleUrls: ['./complex-component.component.css']
})
export class ExternalStylesComponent {}
```

### 複数スタイルファイルの使用
```typescript
@Component({
  selector: 'app-multiple-styles',
  template: `
    <div class="multi-style-component">
      <div class="base-styles">ベーススタイル</div>
      <div class="theme-styles">テーマスタイル</div>
      <div class="responsive-styles">レスポンシブスタイル</div>
    </div>
  `,
  styleUrls: [
    './base.component.css',
    './theme.component.css',
    './responsive.component.css'
  ]
})
export class MultipleStylesComponent {}
```

## 実践的な活用例
- 小規模コンポーネントのスタイリング
- 大規模コンポーネントのスタイル管理
- テーマとベーススタイルの分離

## ベストプラクティス
- スタイルの規模に応じた使い分け
- 適切なファイル分割
- 命名規則の統一

## 注意点
- ファイル数の管理
- スタイルの重複回避
- パフォーマンスの考慮

## 関連技術
- CSS ファイル管理
- スタイル分離
- 保守性設計
