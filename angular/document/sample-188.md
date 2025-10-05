# #188 「CSS Grid レイアウト」

## 概要
Angular v20におけるCSS Gridレイアウトの活用方法。二次元レイアウトの強力な制御機能を使用し、複雑で柔軟なレイアウト設計を実現する。

## 学習目標
- CSS Gridの基本的な使い方を理解する
- 二次元レイアウトの制御を学ぶ
- 複雑なレイアウト設計を把握する

## 技術ポイント
- CSS Gridの基本プロパティ
- グリッドエリアの定義
- レスポンシブグリッド
- 配置とサイズ制御

## 📺 画面表示用コード

### CSS Gridの基本的な使用
```typescript
@Component({
  selector: 'app-css-grid-layout',
  template: `
    <div class="grid-container">
      <header class="header">
        <h1>CSS Grid レイアウト</h1>
        <nav class="navigation">
          <a href="#" class="nav-link">ホーム</a>
          <a href="#" class="nav-link">サービス</a>
          <a href="#" class="nav-link">お問い合わせ</a>
        </nav>
      </header>
      
      <main class="main-content">
        <section class="hero">
          <h2>メインコンテンツ</h2>
          <p>CSS Gridによる二次元レイアウト</p>
        </section>
        
        <section class="content-grid">
          <div class="content-item" *ngFor="let item of contentItems">
            <h3>{{ item.title }}</h3>
            <p>{{ item.description }}</p>
          </div>
        </section>
      </main>
      
      <aside class="sidebar">
        <h3>サイドバー</h3>
        <div class="sidebar-content">
          <div class="sidebar-item" *ngFor="let item of sidebarItems">
            {{ item }}
          </div>
        </div>
      </aside>
      
      <footer class="footer">
        <div class="footer-grid">
          <div class="footer-section">
            <h4>会社情報</h4>
            <p>Angular v20で構築</p>
          </div>
          <div class="footer-section">
            <h4>リンク</h4>
            <ul>
              <li><a href="#">プライバシーポリシー</a></li>
              <li><a href="#">利用規約</a></li>
            </ul>
          </div>
          <div class="footer-section">
            <h4>お問い合わせ</h4>
            <p>info@example.com</p>
          </div>
        </div>
      </footer>
    </div>
  `,
  styles: [`
    .grid-container {
      display: grid;
      grid-template-areas: 
        "header header header"
        "main main sidebar"
        "footer footer footer";
      grid-template-columns: 1fr 1fr 250px;
      grid-template-rows: auto 1fr auto;
      min-height: 100vh;
      gap: 1rem;
      padding: 1rem;
    }
    
    .header {
      grid-area: header;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      padding: 2rem;
      border-radius: 8px;
      display: grid;
      grid-template-columns: 1fr auto;
      align-items: center;
      gap: 2rem;
    }
    
    .header h1 {
      margin: 0;
      font-size: 2rem;
    }
    
    .navigation {
      display: grid;
      grid-template-columns: repeat(3, auto);
      gap: 1rem;
    }
    
    .nav-link {
      color: white;
      text-decoration: none;
      padding: 0.5rem 1rem;
      border-radius: 4px;
      background: rgba(255,255,255,0.1);
      transition: background 0.3s ease;
    }
    
    .nav-link:hover {
      background: rgba(255,255,255,0.2);
    }
    
    .main-content {
      grid-area: main;
      display: grid;
      grid-template-rows: auto 1fr;
      gap: 2rem;
    }
    
    .hero {
      background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
      color: white;
      padding: 3rem;
      border-radius: 8px;
      text-align: center;
      display: grid;
      place-items: center;
    }
    
    .hero h2 {
      margin: 0 0 1rem 0;
      font-size: 2rem;
    }
    
    .content-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 1rem;
    }
    
    .content-item {
      background: white;
      padding: 2rem;
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
      border-left: 4px solid #007bff;
    }
    
    .content-item h3 {
      margin: 0 0 1rem 0;
      color: #007bff;
    }
    
    .sidebar {
      grid-area: sidebar;
      background: #f8f9fa;
      padding: 1.5rem;
      border-radius: 8px;
    }
    
    .sidebar h3 {
      margin: 0 0 1rem 0;
      color: #333;
    }
    
    .sidebar-content {
      display: grid;
      gap: 0.5rem;
    }
    
    .sidebar-item {
      background: white;
      padding: 1rem;
      border-radius: 4px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
      text-align: center;
    }
    
    .footer {
      grid-area: footer;
      background: #343a40;
      color: white;
      padding: 2rem;
      border-radius: 8px;
    }
    
    .footer-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 2rem;
    }
    
    .footer-section h4 {
      margin: 0 0 1rem 0;
      color: #007bff;
    }
    
    .footer-section ul {
      list-style: none;
      padding: 0;
      margin: 0;
    }
    
    .footer-section li {
      margin: 0.5rem 0;
    }
    
    .footer-section a {
      color: #ccc;
      text-decoration: none;
    }
    
    .footer-section a:hover {
      color: white;
    }
    
    /* レスポンシブ対応 */
    @media (max-width: 1024px) {
      .grid-container {
        grid-template-areas: 
          "header header"
          "main sidebar"
          "footer footer";
        grid-template-columns: 1fr 200px;
      }
    }
    
    @media (max-width: 768px) {
      .grid-container {
        grid-template-areas: 
          "header"
          "main"
          "sidebar"
          "footer";
        grid-template-columns: 1fr;
      }
      
      .header {
        grid-template-columns: 1fr;
        text-align: center;
        gap: 1rem;
      }
      
      .navigation {
        grid-template-columns: 1fr;
      }
      
      .content-grid {
        grid-template-columns: 1fr;
      }
      
      .footer-grid {
        grid-template-columns: 1fr;
        gap: 1rem;
      }
    }
    
    @media (max-width: 480px) {
      .grid-container {
        padding: 0.5rem;
        gap: 0.5rem;
      }
      
      .header {
        padding: 1rem;
      }
      
      .hero {
        padding: 2rem;
      }
      
      .content-item {
        padding: 1rem;
      }
    }
  `]
})
export class CssGridLayoutComponent {
  contentItems = [
    { title: 'Grid Area 1', description: 'CSS Gridの基本機能' },
    { title: 'Grid Area 2', description: '二次元レイアウト制御' },
    { title: 'Grid Area 3', description: 'レスポンシブグリッド' },
    { title: 'Grid Area 4', description: '柔軟な配置管理' }
  ];
  
  sidebarItems = [
    '関連リンク1',
    '関連リンク2',
    '関連リンク3',
    '関連リンク4'
  ];
}
```

## 実践的な活用例
- 複雑なレイアウト設計
- ダッシュボードレイアウト
- カードベースのレイアウト

## ベストプラクティス
- 適切なグリッドエリアの定義
- レスポンシブ対応
- セマンティックな構造

## 注意点
- ブラウザサポート
- パフォーマンスの考慮
- レイアウトの複雑さ

## 関連技術
- CSS Grid
- 二次元レイアウト
- レスポンシブデザイン
