# #189 「スタイリングのパフォーマンス」

## 概要
Angular v20におけるスタイリングのパフォーマンス最適化。OnPush戦略、CSS変数、効率的なセレクタなど、パフォーマンスを考慮したスタイリング手法を学ぶ。

## 学習目標
- スタイリングのパフォーマンス問題を理解する
- 最適化手法を学ぶ
- 効率的なスタイル実装を把握する

## 技術ポイント
- OnPushチェンジ検出戦略
- CSS変数の活用
- 効率的なセレクタ
- 不要な再レンダリングの回避

## 📺 画面表示用コード

### パフォーマンス最適化の実装
```typescript
@Component({
  selector: 'app-styling-performance',
  template: `
    <div class="performance-container">
      <header class="header">
        <h1>スタイリングパフォーマンス</h1>
        <div class="performance-info">
          <p>レンダリング回数: {{ renderCount }}</p>
          <p>FPS: {{ currentFPS }}</p>
        </div>
      </header>
      
      <main class="main-content">
        <section class="optimized-section">
          <h2>最適化されたスタイリング</h2>
          <div class="optimized-grid">
            <div class="optimized-item" 
                 *ngFor="let item of optimizedItems; trackBy: trackByFn"
                 [ngClass]="getItemClass(item)">
              <h3>{{ item.title }}</h3>
              <p>{{ item.description }}</p>
            </div>
          </div>
        </section>
        
        <section class="performance-controls">
          <h2>パフォーマンステスト</h2>
          <div class="controls">
            <button (click)="toggleOptimization()" 
                    [ngClass]="{'btn': true, 'optimized': isOptimized}">
              {{ isOptimized ? '最適化ON' : '最適化OFF' }}
            </button>
            <button (click)="updateItems()" class="btn">
              アイテム更新
            </button>
            <button (click)="startPerformanceTest()" class="btn">
              パフォーマンステスト開始
            </button>
          </div>
        </section>
        
        <section class="css-variables-section">
          <h2>CSS変数の活用</h2>
          <div class="variable-controls">
            <input type="range" [(ngModel)]="themeHue" 
                   (input)="updateTheme()" min="0" max="360">
            <input type="range" [(ngModel)]="spacingMultiplier" 
                   (input)="updateSpacing()" min="0.5" max="2" step="0.1">
          </div>
          <div class="variable-demo">
            <div class="demo-card" *ngFor="let card of demoCards">
              <h3>カード {{ card.id }}</h3>
              <p>CSS変数による動的スタイリング</p>
            </div>
          </div>
        </section>
      </main>
    </div>
  `,
  styles: [`
    :host {
      --theme-hue: 200;
      --spacing-multiplier: 1;
    }
    
    .performance-container {
      display: grid;
      grid-template-areas: "header" "main";
      grid-template-rows: auto 1fr;
      min-height: 100vh;
      gap: 1rem;
      padding: 1rem;
    }
    
    .header {
      grid-area: header;
      background: linear-gradient(135deg, hsl(var(--theme-hue), 70%, 60%) 0%, hsl(calc(var(--theme-hue) + 60), 70%, 60%) 100%);
      color: white;
      padding: calc(1rem * var(--spacing-multiplier));
      border-radius: 8px;
      display: grid;
      grid-template-columns: 1fr auto;
      align-items: center;
      gap: 2rem;
    }
    
    .header h1 {
      margin: 0;
    }
    
    .performance-info {
      background: rgba(255,255,255,0.1);
      padding: 1rem;
      border-radius: 4px;
      font-size: 0.9rem;
    }
    
    .main-content {
      grid-area: main;
      display: grid;
      grid-template-rows: auto auto auto;
      gap: calc(2rem * var(--spacing-multiplier));
    }
    
    .optimized-section {
      background: white;
      padding: calc(2rem * var(--spacing-multiplier));
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .optimized-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: calc(1rem * var(--spacing-multiplier));
      margin-top: 1rem;
    }
    
    .optimized-item {
      background: hsl(var(--theme-hue), 20%, 95%);
      padding: calc(1.5rem * var(--spacing-multiplier));
      border-radius: 8px;
      border-left: 4px solid hsl(var(--theme-hue), 70%, 50%);
      transition: transform 0.2s ease;
    }
    
    .optimized-item:hover {
      transform: translateY(-2px);
    }
    
    .optimized-item.priority-high {
      border-left-color: #dc3545;
    }
    
    .optimized-item.priority-medium {
      border-left-color: #ffc107;
    }
    
    .optimized-item.priority-low {
      border-left-color: #28a745;
    }
    
    .performance-controls {
      background: white;
      padding: calc(2rem * var(--spacing-multiplier));
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .controls {
      display: flex;
      gap: 1rem;
      margin-top: 1rem;
      flex-wrap: wrap;
    }
    
    .btn {
      padding: 0.75rem 1.5rem;
      border: none;
      border-radius: 4px;
      background: hsl(var(--theme-hue), 70%, 50%);
      color: white;
      cursor: pointer;
      transition: all 0.3s ease;
    }
    
    .btn:hover {
      background: hsl(var(--theme-hue), 70%, 40%);
    }
    
    .btn.optimized {
      background: #28a745;
    }
    
    .css-variables-section {
      background: white;
      padding: calc(2rem * var(--spacing-multiplier));
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .variable-controls {
      display: flex;
      gap: 2rem;
      margin: 1rem 0;
      align-items: center;
    }
    
    .variable-controls input[type="range"] {
      flex: 1;
      margin: 0 1rem;
    }
    
    .variable-demo {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: calc(1rem * var(--spacing-multiplier));
      margin-top: 1rem;
    }
    
    .demo-card {
      background: hsl(var(--theme-hue), 30%, 90%);
      padding: calc(1rem * var(--spacing-multiplier));
      border-radius: 8px;
      text-align: center;
      border: 2px solid hsl(var(--theme-hue), 70%, 50%);
    }
    
    .demo-card h3 {
      color: hsl(var(--theme-hue), 70%, 30%);
      margin: 0 0 0.5rem 0;
    }
    
    /* パフォーマンス最適化 */
    .optimized-item {
      will-change: transform;
    }
    
    /* プリロード用 */
    .optimized-item.priority-high {
      contain: layout style;
    }
  `],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class StylingPerformanceComponent implements OnInit {
  renderCount = 0;
  currentFPS = 60;
  isOptimized = true;
  themeHue = 200;
  spacingMultiplier = 1;
  
  optimizedItems = [
    { id: 1, title: '高優先度アイテム', description: '重要なコンテンツ', priority: 'high' },
    { id: 2, title: '中優先度アイテム', description: '標準的なコンテンツ', priority: 'medium' },
    { id: 3, title: '低優先度アイテム', description: '補助的なコンテンツ', priority: 'low' }
  ];
  
  demoCards = [
    { id: 1 }, { id: 2 }, { id: 3 }, { id: 4 }
  ];
  
  constructor(private cdr: ChangeDetectorRef) {}
  
  ngOnInit() {
    this.startFPSMonitoring();
  }
  
  trackByFn(index: number, item: any): number {
    return item.id;
  }
  
  getItemClass(item: any): string {
    return `priority-${item.priority}`;
  }
  
  toggleOptimization() {
    this.isOptimized = !this.isOptimized;
    this.updateItems();
  }
  
  updateItems() {
    if (this.isOptimized) {
      // 最適化された更新（trackByを使用）
      this.optimizedItems = [...this.optimizedItems];
    } else {
      // 非最適化の更新（全要素を再作成）
      this.optimizedItems = this.optimizedItems.map(item => ({ ...item }));
    }
    this.renderCount++;
  }
  
  updateTheme() {
    document.documentElement.style.setProperty('--theme-hue', this.themeHue.toString());
  }
  
  updateSpacing() {
    document.documentElement.style.setProperty('--spacing-multiplier', this.spacingMultiplier.toString());
  }
  
  startPerformanceTest() {
    // パフォーマンステストの実装
    console.log('パフォーマンステスト開始');
  }
  
  private startFPSMonitoring() {
    let lastTime = performance.now();
    let frameCount = 0;
    
    const measureFPS = () => {
      frameCount++;
      const currentTime = performance.now();
      
      if (currentTime - lastTime >= 1000) {
        this.currentFPS = Math.round((frameCount * 1000) / (currentTime - lastTime));
        frameCount = 0;
        lastTime = currentTime;
        
        if (this.isOptimized) {
          this.cdr.markForCheck();
        }
      }
      
      requestAnimationFrame(measureFPS);
    };
    
    measureFPS();
  }
}
```

## 実践的な活用例
- 大規模アプリケーションの最適化
- リアルタイムデータ表示
- パフォーマンスクリティカルなUI

## ベストプラクティス
- OnPush戦略の活用
- trackBy関数の使用
- CSS変数の活用

## 注意点
- 過度な最適化の回避
- メモリ使用量の管理
- 測定とプロファイリング

## 関連技術
- パフォーマンス最適化
- Change Detection
- CSS 変数
