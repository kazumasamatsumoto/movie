# #020 「Component のデバッグ方法」台本

四国めたん「Component のデバッグ方法について学びましょう！」
ずんだもん「デバッグって何をするの？」
四国めたん「Componentの動作を確認し、問題を特定・修正する作業です」
ずんだもん「どんな方法があるの？」
四国めたん「Angular DevTools、コンソールログ、ブレークポイント、テストなどがあります」
ずんだもん「Angular DevToolsって何？」
四国めたん「Angular専用のブラウザ拡張機能で、Componentの状態やパフォーマンスを可視化できます」

---

## 📺 画面表示用コード

// 基本的なデバッグ方法
```typescript
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-debug-basic',
  standalone: true,
  template: `
    <div>
      <h2>デバッグの基本</h2>
      <p>カウント: {{count}}</p>
      <button (click)="increment()">増加</button>
    </div>
  `
})
export class DebugBasicComponent implements OnInit {
  count = 0;
  
  ngOnInit() {
    console.log('Componentが初期化されました');
    console.log('初期カウント:', this.count);
  }
  
  increment() {
    this.count++;
    console.log('カウントが増加:', this.count);
  }
}
```

// Angular DevToolsの活用
```typescript
import { Component, ChangeDetectorRef } from '@angular/core';

@Component({
  selector: 'app-devtools',
  standalone: true,
  template: `
    <div>
      <h2>Angular DevTools</h2>
      <p>ユーザー: {{user.name}}</p>
      <p>ステータス: {{status}}</p>
      <button (click)="updateUser()">ユーザー更新</button>
    </div>
  `
})
export class DevToolsComponent {
  user = { name: '田中太郎', age: 30 };
  status = 'active';
  
  constructor(private cdr: ChangeDetectorRef) {
    // DevToolsでComponentの状態を確認
    console.log('Component作成:', this);
  }
  
  updateUser() {
    this.user.name = '佐藤花子';
    this.status = 'inactive';
    
    // 変更検知を手動でトリガー
    this.cdr.detectChanges();
    
    console.log('ユーザー更新:', this.user);
  }
}
```

// コンソールログの活用
```typescript
import { Component, Input, OnChanges, SimpleChanges } from '@angular/core';

@Component({
  selector: 'app-console-log',
  standalone: true,
  template: `
    <div>
      <h2>コンソールログ</h2>
      <p>データ: {{data}}</p>
      <button (click)="processData()">データ処理</button>
    </div>
  `
})
export class ConsoleLogComponent implements OnChanges {
  @Input() data: any;
  
  ngOnChanges(changes: SimpleChanges) {
    console.log('入力データが変更されました:', changes);
    console.log('現在のデータ:', this.data);
  }
  
  processData() {
    console.group('データ処理開始');
    console.log('処理前のデータ:', this.data);
    
    try {
      // データ処理
      const processedData = this.data?.toUpperCase();
      console.log('処理後のデータ:', processedData);
      
      this.data = processedData;
      console.log('処理完了');
    } catch (error) {
      console.error('処理中にエラーが発生:', error);
    } finally {
      console.groupEnd();
    }
  }
}
```

// ブレークポイントの設定
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-breakpoint',
  standalone: true,
  template: `
    <div>
      <h2>ブレークポイント</h2>
      <input [(ngModel)]="searchTerm" placeholder="検索">
      <button (click)="search()">検索</button>
      <ul>
        <li *ngFor="let result of searchResults">{{result}}</li>
      </ul>
    </div>
  `
})
export class BreakpointComponent {
  searchTerm = '';
  searchResults: string[] = [];
  
  search() {
    // ブレークポイントをここに設定
    debugger;  // またはブラウザの開発者ツールでブレークポイントを設定
    
    console.log('検索開始:', this.searchTerm);
    
    // 検索ロジック
    const results = this.performSearch(this.searchTerm);
    
    this.searchResults = results;
    console.log('検索結果:', results);
  }
  
  private performSearch(term: string): string[] {
    // ブレークポイントをここに設定
    const data = ['田中太郎', '佐藤花子', '鈴木一郎'];
    
    return data.filter(item => 
      item.toLowerCase().includes(term.toLowerCase())
    );
  }
}
```

// エラーハンドリングとデバッグ
```typescript
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-error-debug',
  standalone: true,
  template: `
    <div>
      <h2>エラーデバッグ</h2>
      <div *ngIf="error; else content">
        <p class="error">エラー: {{error}}</p>
        <button (click)="retry()">再試行</button>
      </div>
      <ng-template #content>
        <p>データ: {{data}}</p>
      </ng-template>
    </div>
  `
})
export class ErrorDebugComponent implements OnInit {
  data: any = null;
  error: string | null = null;
  
  ngOnInit() {
    this.loadData();
  }
  
  async loadData() {
    try {
      console.log('データ読み込み開始');
      
      // 非同期データ取得
      const response = await this.fetchData();
      
      console.log('データ取得成功:', response);
      this.data = response;
      this.error = null;
      
    } catch (error) {
      console.error('データ読み込みエラー:', error);
      this.error = 'データの読み込みに失敗しました';
      this.data = null;
    }
  }
  
  private async fetchData(): Promise<any> {
    // 模擬的なAPI呼び出し
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (Math.random() > 0.5) {
          resolve({ message: 'データ取得成功' });
        } else {
          reject(new Error('ネットワークエラー'));
        }
      }, 1000);
    });
  }
  
  retry() {
    console.log('再試行開始');
    this.loadData();
  }
}
```

// パフォーマンスデバッグ
```typescript
import { Component, OnInit, OnDestroy } from '@angular/core';

@Component({
  selector: 'app-performance-debug',
  standalone: true,
  template: `
    <div>
      <h2>パフォーマンスデバッグ</h2>
      <p>レンダリング回数: {{renderCount}}</p>
      <p>データ数: {{data.length}}</p>
      <button (click)="addData()">データ追加</button>
    </div>
  `
})
export class PerformanceDebugComponent implements OnInit, OnDestroy {
  data: any[] = [];
  renderCount = 0;
  private startTime = 0;
  
  ngOnInit() {
    this.startTime = performance.now();
    console.log('Component初期化開始:', this.startTime);
    
    // 初期データの生成
    this.generateData(1000);
  }
  
  ngOnDestroy() {
    const endTime = performance.now();
    const duration = endTime - this.startTime;
    console.log('Component生存時間:', duration, 'ms');
  }
  
  addData() {
    const startTime = performance.now();
    
    // データ追加
    this.generateData(100);
    
    const endTime = performance.now();
    const duration = endTime - startTime;
    
    console.log('データ追加時間:', duration, 'ms');
    console.log('現在のデータ数:', this.data.length);
  }
  
  private generateData(count: number) {
    for (let i = 0; i < count; i++) {
      this.data.push({
        id: this.data.length + i,
        name: `アイテム${this.data.length + i}`,
        value: Math.random()
      });
    }
  }
  
  // レンダリング回数をカウント
  ngAfterViewChecked() {
    this.renderCount++;
    if (this.renderCount % 10 === 0) {
      console.log('レンダリング回数:', this.renderCount);
    }
  }
}
```

// デバッグ用のユーティリティ
```typescript
// debug.util.ts
export class DebugUtil {
  static logComponent(component: any, message: string) {
    console.log(`[${component.constructor.name}] ${message}`, component);
  }
  
  static logPerformance(operation: string, startTime: number) {
    const endTime = performance.now();
    const duration = endTime - startTime;
    console.log(`[Performance] ${operation}: ${duration.toFixed(2)}ms`);
  }
  
  static logState(component: any, state: any) {
    console.log(`[State] ${component.constructor.name}:`, state);
  }
}

// 使用例
@Component({
  selector: 'app-debug-util',
  standalone: true,
  template: `
    <div>
      <h2>デバッグユーティリティ</h2>
      <button (click)="performOperation()">操作実行</button>
    </div>
  `
})
export class DebugUtilComponent {
  state = { count: 0, message: '初期状態' };
  
  performOperation() {
    const startTime = performance.now();
    
    // 操作実行
    this.state.count++;
    this.state.message = `カウント: ${this.state.count}`;
    
    // デバッグログ
    DebugUtil.logComponent(this, '操作実行');
    DebugUtil.logPerformance('操作実行', startTime);
    DebugUtil.logState(this, this.state);
  }
}
```

// デバッグのベストプラクティス
```typescript
@Component({
  selector: 'app-debug-best-practices',
  standalone: true,
  template: `
    <div>
      <h2>デバッグのベストプラクティス</h2>
      <ul>
        <li>Angular DevToolsを活用</li>
        <li>コンソールログを適切に使用</li>
        <li>ブレークポイントでステップ実行</li>
        <li>エラーハンドリングを実装</li>
        <li>パフォーマンスを測定</li>
        <li>テストを書く</li>
        <li>デバッグコードは本番環境で削除</li>
        <li>ログレベルを適切に設定</li>
      </ul>
    </div>
  `
})
export class DebugBestPracticesComponent {
  // デバッグを効率的に行うためのベストプラクティス
}
```
