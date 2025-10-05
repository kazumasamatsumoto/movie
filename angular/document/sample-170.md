# #170 「グローバルスタイルとの使い分け」

## 概要
Angular v20におけるコンポーネントスタイルとグローバルスタイルの適切な使い分け。用途に応じて最適なスタイル管理方法を選択し、保守性と再利用性の高いスタイル設計を実現する。

## 学習目標
- コンポーネントスタイルとグローバルスタイルの違いを理解する
- 適切な使い分けの基準を学ぶ
- 責任分離を考慮した設計を把握する

## 技術ポイント
- コンポーネント固有スタイルの適用範囲
- グローバルスタイルの適用範囲
- 責任分離の原則
- 再利用性の考慮

## 📺 画面表示用コード

### コンポーネントスタイルの使用場面
```typescript
@Component({
  selector: 'app-specific-component',
  template: `
    <div class="unique-card">
      <h3>固有のカードデザイン</h3>
      <p>このコンポーネント専用のスタイル</p>
    </div>
  `,
  styles: [`
    .unique-card {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      padding: 25px;
      border-radius: 15px;
      box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
      transform: rotate(-1deg);
    }
    
    .unique-card h3 {
      font-size: 24px;
      margin-bottom: 15px;
      text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .unique-card p {
      font-size: 16px;
      opacity: 0.9;
      line-height: 1.6;
    }
  `]
})
export class SpecificComponent {}
```

### グローバルスタイルの使用場面
```typescript
// グローバルスタイル（styles.css）
/*
.btn {
  padding: 12px 24px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 16px;
  transition: all 0.3s ease;
}

.btn-primary {
  background: #007bff;
  color: white;
}

.btn-primary:hover {
  background: #0056b3;
  transform: translateY(-2px);
}

.form-control {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

.form-control:focus {
  outline: none;
  border-color: #007bff;
  box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.1);
}
*/

@Component({
  selector: 'app-global-styles-usage',
  template: `
    <div class="form-container">
      <h2>グローバルスタイルの活用</h2>
      <form>
        <input type="text" class="form-control" placeholder="名前">
        <input type="email" class="form-control" placeholder="メール">
        <button type="submit" class="btn btn-primary">送信</button>
      </form>
    </div>
  `,
  styles: [`
    .form-container {
      max-width: 500px;
      margin: 0 auto;
      padding: 20px;
    }
    
    .form-container h2 {
      text-align: center;
      margin-bottom: 20px;
      color: #333;
    }
    
    .form-container form {
      display: flex;
      flex-direction: column;
      gap: 15px;
    }
  `]
})
export class GlobalStylesUsageComponent {}
```

### ハイブリッドアプローチ
```typescript
@Component({
  selector: 'app-hybrid-styling',
  template: `
    <div class="custom-container">
      <h2>ハイブリッドスタイリング</h2>
      <div class="content-section">
        <p class="description">グローバルスタイルとコンポーネントスタイルを組み合わせ</p>
        <button class="btn btn-primary custom-button">カスタムボタン</button>
      </div>
    </div>
  `,
  styles: [`
    .custom-container {
      background: #f8f9fa;
      padding: 30px;
      border-radius: 10px;
      margin: 20px 0;
    }
    
    .content-section {
      display: flex;
      flex-direction: column;
      gap: 20px;
      align-items: center;
    }
    
    .description {
      color: #666;
      text-align: center;
      font-size: 16px;
      line-height: 1.6;
    }
    
    /* グローバルスタイルの拡張 */
    .custom-button {
      background: linear-gradient(45deg, #ff6b6b, #4ecdc4) !important;
      border: none !important;
      padding: 15px 30px !important;
      font-size: 18px !important;
      border-radius: 25px !important;
    }
  `]
})
export class HybridStylingComponent {}
```

## 実践的な活用例
- コンポーネント固有デザインの実装
- 共通UI要素のスタイリング
- テーマシステムの構築

## ベストプラクティス
- 責任分離の原則に従う
- 再利用性を考慮した設計
- 一貫性のある命名規則

## 注意点
- スタイルの重複回避
- 競合の防止
- パフォーマンスの考慮

## 関連技術
- CSS 設計原則
- スタイル管理
- 責任分離
