# #186 「メディアクエリの活用」

## 概要
Angular v20におけるメディアクエリの活用方法。デバイスサイズ、向き、解像度などに応じたスタイル適用により、デバイス特性に最適化されたレスポンシブデザインを実現する。

## 学習目標
- メディアクエリの基本的な使い方を理解する
- デバイス特性に応じたスタイル適用を学ぶ
- レスポンシブデザインを把握する

## 技術ポイント
- メディアクエリの基本構文
- デバイス特性の検知
- ブレークポイントの設計
- 条件付きスタイル適用

## 📺 画面表示用コード

### メディアクエリの基本的な使用
```typescript
@Component({
  selector: 'app-media-queries',
  template: `
    <div class="media-container">
      <header class="header">
        <h1>メディアクエリの活用</h1>
        <div class="device-info">
          <p>現在のデバイス情報:</p>
          <ul>
            <li>画面幅: {{ screenWidth }}px</li>
            <li>デバイス向き: {{ deviceOrientation }}</li>
            <li>解像度: {{ devicePixelRatio }}</li>
          </ul>
        </div>
      </header>
      
      <main class="main-content">
        <section class="responsive-grid">
          <div class="grid-item" *ngFor="let item of gridItems">
            {{ item }}
          </div>
        </section>
        
        <section class="adaptive-layout">
          <div class="content-block">
            <h3>適応レイアウト</h3>
            <p>デバイスサイズに応じてレイアウトが変わります</p>
          </div>
        </section>
      </main>
      
      <aside class="sidebar">
        <h3>サイドバー</h3>
        <p>デスクトップでは表示、モバイルでは非表示</p>
      </aside>
    </div>
  `,
  styles: [`
    .media-container {
      display: grid;
      grid-template-areas: 
        "header"
        "main"
        "sidebar";
      gap: 1rem;
      padding: 1rem;
      min-height: 100vh;
    }
    
    .header {
      grid-area: header;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      padding: 2rem;
      border-radius: 8px;
      text-align: center;
    }
    
    .device-info {
      margin-top: 1rem;
      background: rgba(255,255,255,0.1);
      padding: 1rem;
      border-radius: 4px;
    }
    
    .device-info ul {
      list-style: none;
      padding: 0;
      margin: 0.5rem 0 0 0;
    }
    
    .device-info li {
      margin: 0.25rem 0;
    }
    
    .main-content {
      grid-area: main;
    }
    
    .responsive-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1rem;
      margin-bottom: 2rem;
    }
    
    .grid-item {
      background: white;
      padding: 1.5rem;
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
      text-align: center;
      border-left: 4px solid #007bff;
    }
    
    .adaptive-layout {
      background: white;
      padding: 2rem;
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .content-block {
      text-align: center;
    }
    
    .sidebar {
      grid-area: sidebar;
      background: #f8f9fa;
      padding: 1.5rem;
      border-radius: 8px;
      display: none;
    }
    
    /* タブレット（768px以上） */
    @media (min-width: 768px) {
      .media-container {
        grid-template-areas: 
          "header header"
          "main sidebar";
        grid-template-columns: 2fr 1fr;
      }
      
      .responsive-grid {
        grid-template-columns: repeat(2, 1fr);
      }
      
      .sidebar {
        display: block;
      }
    }
    
    /* デスクトップ（1024px以上） */
    @media (min-width: 1024px) {
      .responsive-grid {
        grid-template-columns: repeat(3, 1fr);
      }
      
      .adaptive-layout {
        padding: 3rem;
      }
    }
    
    /* 大画面（1440px以上） */
    @media (min-width: 1440px) {
      .media-container {
        max-width: 1400px;
        margin: 0 auto;
      }
      
      .responsive-grid {
        grid-template-columns: repeat(4, 1fr);
      }
    }
    
    /* 横向き（ランドスケープ） */
    @media (orientation: landscape) and (max-height: 600px) {
      .header {
        padding: 1rem;
      }
      
      .header h1 {
        font-size: 1.5rem;
      }
    }
    
    /* 高解像度ディスプレイ */
    @media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
      .grid-item {
        border-width: 2px;
      }
    }
    
    /* 印刷用スタイル */
    @media print {
      .sidebar {
        display: none;
      }
      
      .header {
        background: white;
        color: black;
        box-shadow: none;
      }
      
      .grid-item {
        box-shadow: none;
        border: 1px solid #ccc;
      }
    }
  `]
})
export class MediaQueriesComponent implements OnInit {
  screenWidth = 0;
  deviceOrientation = '';
  devicePixelRatio = 0;
  
  gridItems = [
    '項目1', '項目2', '項目3', '項目4', '項目5', '項目6'
  ];
  
  ngOnInit() {
    this.updateDeviceInfo();
    window.addEventListener('resize', () => this.updateDeviceInfo());
    window.addEventListener('orientationchange', () => this.updateDeviceInfo());
  }
  
  updateDeviceInfo() {
    this.screenWidth = window.innerWidth;
    this.deviceOrientation = window.innerWidth > window.innerHeight ? '横向き' : '縦向き';
    this.devicePixelRatio = window.devicePixelRatio;
  }
}
```

## 実践的な活用例
- レスポンシブWebサイト
- モバイルアプリケーション
- マルチデバイス対応

## ベストプラクティス
- モバイルファーストの設計
- 適切なブレークポイント
- デバイス特性の考慮

## 注意点
- パフォーマンスの考慮
- テストの重要性
- ブラウザサポート

## 関連技術
- メディアクエリ
- レスポンシブデザイン
- デバイス特性検知
