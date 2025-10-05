# #167 「:host-context セレクタ - 祖先条件」

## 概要
Angular v20における:host-contextセレクタの使用方法。祖先要素の条件に基づいてスタイルを適用し、テーマ切り替えや条件付きスタイリングを実現する方法を学ぶ。

## 学習目標
- :host-contextセレクタの基本的な使い方を理解する
- 祖先要素の条件判定を学ぶ
- 動的なテーマ切り替えを把握する

## 技術ポイント
- :host-context() セレクタの使用
- 祖先要素の条件判定
- テーマ切り替えの実装
- 条件付きスタイル適用

## 📺 画面表示用コード

### :host-contextの基本的な使用
```typescript
@Component({
  selector: 'app-theme-component',
  template: `
    <div class="card">
      <h3>テーマ対応カード</h3>
      <p>祖先要素のクラスに応じてスタイルが変わります</p>
    </div>
  `,
  styles: [`
    .card {
      padding: 20px;
      border-radius: 10px;
      transition: all 0.3s ease;
    }
    
    /* ライトテーマ */
    :host-context(.light-theme) .card {
      background: white;
      color: #333;
      border: 1px solid #ddd;
    }
    
    /* ダークテーマ */
    :host-context(.dark-theme) .card {
      background: #2c3e50;
      color: white;
      border: 1px solid #34495e;
    }
    
    /* ハイコントラストテーマ */
    :host-context(.high-contrast) .card {
      background: #000;
      color: #fff;
      border: 3px solid #fff;
    }
  `]
})
export class ThemeComponent {}
```

### 複数条件の組み合わせ
```typescript
@Component({
  selector: 'app-conditional-styling',
  template: `
    <div class="message">
      <h4>条件付きスタイリング</h4>
      <p>複数の条件に応じてスタイルが適用されます</p>
    </div>
  `,
  styles: [`
    .message {
      padding: 15px;
      border-radius: 8px;
      margin: 10px 0;
    }
    
    /* エラー状態 */
    :host-context(.error) .message {
      background: #ffebee;
      color: #c62828;
      border-left: 4px solid #f44336;
    }
    
    /* 成功状態 */
    :host-context(.success) .message {
      background: #e8f5e8;
      color: #2e7d32;
      border-left: 4px solid #4caf50;
    }
    
    /* 警告状態 */
    :host-context(.warning) .message {
      background: #fff3e0;
      color: #ef6c00;
      border-left: 4px solid #ff9800;
    }
    
    /* コンパクトモード */
    :host-context(.compact) .message {
      padding: 10px;
      font-size: 14px;
    }
    
    /* モバイル表示 */
    :host-context(.mobile) .message {
      margin: 5px;
      border-radius: 4px;
    }
  `]
})
export class ConditionalStylingComponent {}
```

## 実践的な活用例
- テーマ切り替えシステム
- 条件付きスタイル適用
- レスポンシブデザイン
- 状態に応じたスタイリング

## ベストプラクティス
- 明確な条件設定
- 適切なクラス命名
- パフォーマンスの考慮

## 注意点
- 祖先要素の構造依存
- 条件の複雑さ管理
- デバッグの難しさ

## 関連技術
- CSS セレクタ
- 条件付きスタイリング
- テーマシステム
