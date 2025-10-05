# #184 「SCSS/SASS の使用」

## 概要
Angular v20におけるSCSS/SASSの使用方法。変数、ネスト、ミックスイン、関数などの機能を活用し、より強力で保守性の高いスタイル開発を実現する。

## 学習目標
- SCSS/SASSの基本的な使い方を理解する
- 主要な機能を学ぶ
- 効率的なスタイル開発を把握する

## 技術ポイント
- SCSS/SASSの設定
- 変数の活用
- ネスト機能
- ミックスインと関数

## 📺 画面表示用コード

### SCSSの基本的な使用
```scss
// variables.scss
$primary-color: #007bff;
$secondary-color: #6c757d;
$success-color: #28a745;
$border-radius: 8px;
$spacing-unit: 16px;

// mixins.scss
@mixin button-style($bg-color, $text-color: white) {
  background-color: $bg-color;
  color: $text-color;
  border: none;
  border-radius: $border-radius;
  padding: $spacing-unit / 2 $spacing-unit;
  cursor: pointer;
  transition: all 0.3s ease;
  
  &:hover {
    background-color: darken($bg-color, 10%);
    transform: translateY(-2px);
  }
}

@mixin card-style {
  background: white;
  border-radius: $border-radius;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  padding: $spacing-unit;
  margin: $spacing-unit / 2 0;
}

// main.scss
.component-container {
  padding: $spacing-unit * 2;
  max-width: 800px;
  margin: 0 auto;
  
  .header {
    color: $primary-color;
    margin-bottom: $spacing-unit;
    
    h1 {
      font-size: 2rem;
      font-weight: bold;
    }
  }
  
  .card {
    @include card-style;
    
    .card-title {
      color: $primary-color;
      margin-bottom: $spacing-unit / 2;
    }
    
    .card-content {
      color: #666;
      line-height: 1.6;
    }
    
    .card-actions {
      margin-top: $spacing-unit;
      display: flex;
      gap: $spacing-unit / 2;
      
      .btn-primary {
        @include button-style($primary-color);
      }
      
      .btn-secondary {
        @include button-style($secondary-color);
      }
      
      .btn-success {
        @include button-style($success-color);
      }
    }
  }
  
  .form-group {
    margin-bottom: $spacing-unit;
    
    label {
      display: block;
      margin-bottom: $spacing-unit / 4;
      font-weight: 500;
      color: #333;
    }
    
    input, textarea {
      width: 100%;
      padding: $spacing-unit / 2;
      border: 1px solid #ddd;
      border-radius: $border-radius / 2;
      font-size: 1rem;
      
      &:focus {
        outline: none;
        border-color: $primary-color;
        box-shadow: 0 0 0 3px rgba($primary-color, 0.1);
      }
    }
  }
}
```

### TypeScriptコンポーネント
```typescript
@Component({
  selector: 'app-scss-example',
  template: `
    <div class="component-container">
      <div class="header">
        <h1>SCSS/SASS の活用</h1>
      </div>
      
      <div class="card">
        <div class="card-title">カードタイトル</div>
        <div class="card-content">
          SCSS/SASSを使用したスタイリング例です。
          変数、ネスト、ミックスインが活用されています。
        </div>
        <div class="card-actions">
          <button class="btn-primary">プライマリ</button>
          <button class="btn-secondary">セカンダリ</button>
          <button class="btn-success">成功</button>
        </div>
      </div>
      
      <div class="form-group">
        <label>名前</label>
        <input type="text" placeholder="名前を入力してください">
      </div>
      
      <div class="form-group">
        <label>メッセージ</label>
        <textarea placeholder="メッセージを入力してください"></textarea>
      </div>
    </div>
  `,
  styleUrls: ['./scss-example.component.scss']
})
export class ScssExampleComponent {}
```

## 実践的な活用例
- 大規模なスタイル管理
- テーマシステムの構築
- 再利用可能なスタイル

## ベストプラクティス
- 適切な変数設計
- ミックスインの活用
- ネストの適度な使用

## 注意点
- ネストの深さ管理
- パフォーマンスの考慮
- 学習コスト

## 関連技術
- SCSS/SASS
- 変数とミックスイン
- 効率的なスタイル開発
