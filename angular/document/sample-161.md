# #161 「Component スタイルの基本」

## 概要
Angular v20におけるコンポーネントスタイルの基本的な実装方法。@Componentデコレータのstylesプロパティを使用して、コンポーネント固有のスタイルを定義し、カプセル化されたスタイリングを実現する。

## 学習目標
- コンポーネントスタイルの基本的な使い方を理解する
- stylesプロパティの実装方法を学ぶ
- スタイルのカプセル化を把握する

## 技術ポイント
- @Component デコレータのstylesプロパティ
- コンポーネント固有スタイルの定義
- スタイルのカプセル化
- 外部スタイルファイルの読み込み

## 📺 画面表示用コード

### インラインスタイルの定義
```typescript
@Component({
  selector: 'app-basic-styles',
  template: `
    <div class="container">
      <h1 class="title">コンポーネントスタイル</h1>
      <p class="content">このスタイルはコンポーネント固有です</p>
    </div>
  `,
  styles: [`
    .container {
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 8px;
      background-color: #f9f9f9;
    }
    
    .title {
      color: #333;
      font-size: 24px;
      margin-bottom: 16px;
    }
    
    .content {
      color: #666;
      line-height: 1.6;
    }
  `]
})
export class BasicStylesComponent {}
```

### 外部スタイルファイルの使用
```typescript
@Component({
  selector: 'app-external-styles',
  template: `
    <div class="card">
      <div class="card-header">カードタイトル</div>
      <div class="card-body">カード内容</div>
    </div>
  `,
  styleUrls: ['./card.component.css']
})
export class ExternalStylesComponent {}
```

## 実践的な活用例
- カードコンポーネントのスタイリング
- フォーム要素のデザイン
- ナビゲーションコンポーネント

## ベストプラクティス
- 適切なスタイル分離
- 意味のあるクラス名
- 保守性を考慮した設計

## 注意点
- スタイルの競合回避
- パフォーマンスの考慮
- レスポンシブデザインの実装

## 関連技術
- CSS
- コンポーネント設計
- スタイルカプセル化
