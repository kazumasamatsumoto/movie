# #187 「Flexbox レイアウト」

## 概要
Angular v20におけるFlexboxレイアウトの活用方法。一次元レイアウトの強力な制御機能を使用し、柔軟で効率的なレイアウト設計を実現する。

## 学習目標
- Flexboxの基本的な使い方を理解する
- レイアウトの制御方法を学ぶ
- レスポンシブデザインでの活用を把握する

## 技術ポイント
- Flexboxの基本プロパティ
- 方向と配置の制御
- サイズ調整の仕組み
- レスポンシブレイアウト

## 📺 画面表示用コード

### Flexboxの基本的な使用
```typescript
@Component({
  selector: 'app-flexbox-layout',
  template: `
    <div class="flexbox-container">
      <header class="header">
        <h1>Flexbox レイアウト</h1>
        <nav class="navigation">
          <a href="#" class="nav-item">ホーム</a>
          <a href="#" class="nav-item">サービス</a>
          <a href="#" class="nav-item">お問い合わせ</a>
        </nav>
      </header>
      
      <main class="main-content">
        <section class="hero-section">
          <h2>メインコンテンツ</h2>
          <p>Flexboxを使用したレイアウト例</p>
        </section>
        
        <section class="features-section">
          <h3>機能一覧</h3>
          <div class="features-grid">
            <div class="feature-card" *ngFor="let feature of features">
              <h4>{{ feature.title }}</h4>
              <p>{{ feature.description }}</p>
            </div>
          </div>
        </section>
        
        <section class="content-section">
          <div class="content-wrapper">
            <div class="content-block">
              <h3>コンテンツブロック1</h3>
              <p>Flexboxによる柔軟なレイアウト</p>
            </div>
            <div class="content-block">
              <h3>コンテンツブロック2</h3>
              <p>自動的なサイズ調整</p>
            </div>
            <div class="content-block">
              <h3>コンテンツブロック3</h3>
              <p>レスポンシブな配置</p>
            </div>
          </div>
        </section>
      </main>
      
      <footer class="footer">
        <div class="footer-content">
          <p>&copy; 2024 Angular v20 Flexbox</p>
        </div>
      </footer>
    </div>
  `,
  styles: [`
    .flexbox-container {
      display: flex;
      flex-direction: column;
      min-height: 100vh;
    }
    
    .header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      padding: 1rem 2rem;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .header h1 {
      margin: 0;
      font-size: 1.5rem;
    }
    
    .navigation {
      display: flex;
      gap: 1rem;
    }
    
    .nav-item {
      color: white;
      text-decoration: none;
      padding: 0.5rem 1rem;
      border-radius: 4px;
      transition: background 0.3s ease;
    }
    
    .nav-item:hover {
      background: rgba(255,255,255,0.1);
    }
    
    .main-content {
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 2rem;
      padding: 2rem;
    }
    
    .hero-section {
      background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
      color: white;
      padding: 3rem;
      border-radius: 8px;
      text-align: center;
    }
    
    .hero-section h2 {
      margin: 0 0 1rem 0;
      font-size: 2rem;
    }
    
    .features-section {
      background: white;
      padding: 2rem;
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .features-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      margin-top: 1rem;
    }
    
    .feature-card {
      flex: 1;
      min-width: 250px;
      background: #f8f9fa;
      padding: 1.5rem;
      border-radius: 8px;
      border-left: 4px solid #007bff;
    }
    
    .feature-card h4 {
      margin: 0 0 1rem 0;
      color: #007bff;
    }
    
    .content-section {
      background: white;
      padding: 2rem;
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .content-wrapper {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      margin-top: 1rem;
    }
    
    .content-block {
      flex: 1;
      min-width: 200px;
      background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
      color: white;
      padding: 1.5rem;
      border-radius: 8px;
      text-align: center;
    }
    
    .content-block h3 {
      margin: 0 0 1rem 0;
    }
    
    .footer {
      background: #343a40;
      color: white;
      padding: 1rem 2rem;
    }
    
    .footer-content {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    
    /* レスポンシブ対応 */
    @media (max-width: 768px) {
      .header {
        flex-direction: column;
        gap: 1rem;
        text-align: center;
      }
      
      .navigation {
        flex-wrap: wrap;
        justify-content: center;
      }
      
      .main-content {
        padding: 1rem;
      }
      
      .hero-section {
        padding: 2rem;
      }
      
      .features-grid {
        flex-direction: column;
      }
      
      .content-wrapper {
        flex-direction: column;
      }
    }
    
    @media (max-width: 480px) {
      .header {
        padding: 1rem;
      }
      
      .header h1 {
        font-size: 1.25rem;
      }
      
      .navigation {
        flex-direction: column;
        width: 100%;
      }
      
      .nav-item {
        text-align: center;
      }
    }
  `]
})
export class FlexboxLayoutComponent {
  features = [
    { title: '柔軟性', description: '柔軟なレイアウト制御' },
    { title: '効率性', description: '効率的な配置管理' },
    { title: 'レスポンシブ', description: '自動的なレスポンシブ対応' },
    { title: 'シンプル', description: '直感的な実装' }
  ];
}
```

## 実践的な活用例
- ナビゲーションレイアウト
- カードレイアウト
- フォームレイアウト

## ベストプラクティス
- 適切な方向の選択
- フレックスアイテムの制御
- レスポンシブ対応

## 注意点
- ブラウザサポート
- パフォーマンスの考慮
- レイアウトの複雑さ

## 関連技術
- Flexbox
- レスポンシブレイアウト
- CSS レイアウト
