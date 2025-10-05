# #185 「レスポンシブデザイン実装」

## 概要
Angular v20におけるレスポンシブデザインの実装方法。CSS Grid、Flexbox、メディアクエリを活用し、あらゆるデバイスサイズに対応したモダンなレスポンシブデザインを実現する。

## 学習目標
- レスポンシブデザインの基本を理解する
- ブレークポイントの設計を学ぶ
- モバイルファーストの実装を把握する

## 技術ポイント
- メディアクエリの活用
- CSS GridとFlexbox
- ブレークポイント設計
- モバイルファーストアプローチ

## 📺 画面表示用コード

### レスポンシブデザインの実装
```typescript
@Component({
  selector: 'app-responsive-design',
  template: `
    <div class="responsive-container">
      <header class="header">
        <h1>レスポンシブデザイン</h1>
        <nav class="navigation">
          <a href="#" class="nav-link">ホーム</a>
          <a href="#" class="nav-link">サービス</a>
          <a href="#" class="nav-link">お問い合わせ</a>
        </nav>
      </header>
      
      <main class="main-content">
        <section class="hero">
          <h2>メインコンテンツ</h2>
          <p>レスポンシブデザインの実装例</p>
        </section>
        
        <section class="features">
          <div class="feature-card" *ngFor="let feature of features">
            <h3>{{ feature.title }}</h3>
            <p>{{ feature.description }}</p>
          </div>
        </section>
      </main>
      
      <aside class="sidebar">
        <h3>サイドバー</h3>
        <div class="sidebar-content">
          <p>関連情報</p>
          <ul>
            <li>項目1</li>
            <li>項目2</li>
            <li>項目3</li>
          </ul>
        </div>
      </aside>
      
      <footer class="footer">
        <p>&copy; 2024 Angular v20 レスポンシブデザイン</p>
      </footer>
    </div>
  `,
  styles: [`
    /* モバイルファースト（デフォルト） */
    .responsive-container {
      display: grid;
      grid-template-areas: 
        "header"
        "main"
        "sidebar"
        "footer";
      grid-template-rows: auto 1fr auto auto;
      min-height: 100vh;
      gap: 1rem;
      padding: 1rem;
    }
    
    .header {
      grid-area: header;
      background: #007bff;
      color: white;
      padding: 1rem;
      border-radius: 8px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }
    
    .navigation {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      margin-top: 1rem;
      width: 100%;
    }
    
    .nav-link {
      color: white;
      text-decoration: none;
      padding: 0.5rem;
      border-radius: 4px;
      background: rgba(255,255,255,0.1);
      transition: background 0.3s ease;
    }
    
    .nav-link:hover {
      background: rgba(255,255,255,0.2);
    }
    
    .main-content {
      grid-area: main;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
    
    .hero {
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      padding: 2rem;
      border-radius: 8px;
      text-align: center;
    }
    
    .features {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1rem;
    }
    
    .feature-card {
      background: white;
      padding: 1.5rem;
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
      border-left: 4px solid #007bff;
    }
    
    .sidebar {
      grid-area: sidebar;
      background: #f8f9fa;
      padding: 1rem;
      border-radius: 8px;
    }
    
    .footer {
      grid-area: footer;
      background: #343a40;
      color: white;
      padding: 1rem;
      border-radius: 8px;
      text-align: center;
    }
    
    /* タブレット（768px以上） */
    @media (min-width: 768px) {
      .responsive-container {
        grid-template-areas: 
          "header header"
          "main sidebar"
          "footer footer";
        grid-template-columns: 2fr 1fr;
        grid-template-rows: auto 1fr auto;
      }
      
      .header {
        flex-direction: row;
        justify-content: space-between;
        text-align: left;
      }
      
      .navigation {
        flex-direction: row;
        margin-top: 0;
        width: auto;
      }
      
      .features {
        grid-template-columns: repeat(2, 1fr);
      }
    }
    
    /* デスクトップ（1024px以上） */
    @media (min-width: 1024px) {
      .responsive-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
      }
      
      .features {
        grid-template-columns: repeat(3, 1fr);
      }
      
      .hero {
        padding: 3rem;
      }
    }
    
    /* 大画面（1440px以上） */
    @media (min-width: 1440px) {
      .responsive-container {
        max-width: 1400px;
      }
      
      .features {
        grid-template-columns: repeat(4, 1fr);
      }
    }
  `]
})
export class ResponsiveDesignComponent {
  features = [
    { title: 'レスポンシブ', description: 'あらゆるデバイスに対応' },
    { title: 'モダン', description: '最新のWeb技術を活用' },
    { title: 'アクセシブル', description: '誰でも使いやすい設計' },
    { title: '高速', description: '最適化されたパフォーマンス' }
  ];
}
```

## 実践的な活用例
- モバイルアプリケーション
- レスポンシブWebサイト
- マルチデバイス対応

## ベストプラクティス
- モバイルファーストの設計
- 適切なブレークポイント
- フレキシブルなレイアウト

## 注意点
- パフォーマンスの考慮
- テストの重要性
- ユーザビリティ

## 関連技術
- レスポンシブデザイン
- メディアクエリ
- CSS Grid/Flexbox
