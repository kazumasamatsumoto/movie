# #021 「Angular DevTools で Component 確認」台本

四国めたん「Angular DevTools で Component 確認について解説します！」
ずんだもん「Angular DevToolsって何？」
四国めたん「Angular専用のブラウザ拡張機能で、Componentの状態やパフォーマンスを可視化できます」
ずんだもん「どんな機能があるの？」
四国めたん「Component Tree、Profiler、Router Tree、State Inspectorなどがあります」
ずんだもん「どうやって使うの？」
四国めたん「Chrome拡張機能をインストールし、開発者ツールでAngularタブを開きます」

---

## 📺 画面表示用コード

// Angular DevToolsで確認できるComponent
```typescript
import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-devtools-demo',
  standalone: true,
  template: `
    <div class="demo-container">
      <h2>Angular DevTools デモ</h2>
      <div class="user-info">
        <h3>{{user.name}}</h3>
        <p>年齢: {{user.age}}</p>
        <p>ステータス: {{user.status}}</p>
      </div>
      <div class="controls">
        <button (click)="updateUser()">ユーザー更新</button>
        <button (click)="toggleStatus()">ステータス切り替え</button>
      </div>
      <div class="child-components">
        <app-user-card [user]="user"></app-user-card>
        <app-user-actions [userId]="user.id" (action)="handleAction($event)"></app-user-actions>
      </div>
    </div>
  `,
  styles: [`
    .demo-container {
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 8px;
      margin: 20px;
    }
    .user-info {
      background-color: #f8f9fa;
      padding: 15px;
      border-radius: 4px;
      margin-bottom: 15px;
    }
    .controls {
      margin-bottom: 15px;
    }
    .controls button {
      margin-right: 10px;
      padding: 8px 16px;
    }
  `]
})
export class DevToolsDemoComponent {
  user = {
    id: 1,
    name: '田中太郎',
    age: 30,
    status: 'active'
  };
  
  updateUser() {
    this.user.name = '佐藤花子';
    this.user.age = 25;
    console.log('ユーザー情報を更新しました');
  }
  
  toggleStatus() {
    this.user.status = this.user.status === 'active' ? 'inactive' : 'active';
    console.log('ステータスを切り替えました:', this.user.status);
  }
  
  handleAction(action: string) {
    console.log('アクション実行:', action);
  }
}
```

// 子Component（DevToolsで確認）
```typescript
@Component({
  selector: 'app-user-card',
  standalone: true,
  template: `
    <div class="user-card">
      <h4>{{user.name}}</h4>
      <p>ID: {{user.id}}</p>
      <p>年齢: {{user.age}}</p>
      <span class="status" [class.active]="user.status === 'active'">
        {{user.status}}
      </span>
    </div>
  `,
  styles: [`
    .user-card {
      border: 1px solid #ddd;
      padding: 15px;
      border-radius: 4px;
      margin: 10px 0;
    }
    .status {
      padding: 4px 8px;
      border-radius: 12px;
      font-size: 12px;
    }
    .status.active {
      background-color: #d4edda;
      color: #155724;
    }
  `]
})
export class UserCardComponent {
  @Input() user: any;
}
```

// アクションComponent（DevToolsで確認）
```typescript
@Component({
  selector: 'app-user-actions',
  standalone: true,
  template: `
    <div class="actions">
      <button (click)="edit()">編集</button>
      <button (click)="delete()">削除</button>
      <button (click)="view()">詳細</button>
    </div>
  `,
  styles: [`
    .actions button {
      margin-right: 8px;
      padding: 6px 12px;
    }
  `]
})
export class UserActionsComponent {
  @Input() userId!: number;
  @Output() action = new EventEmitter<string>();
  
  edit() {
    this.action.emit('edit');
  }
  
  delete() {
    this.action.emit('delete');
  }
  
  view() {
    this.action.emit('view');
  }
}
```

// DevToolsで確認できる状態管理
```typescript
import { Component, OnInit, OnDestroy } from '@angular/core';
import { BehaviorSubject, interval, Subscription } from 'rxjs';

@Component({
  selector: 'app-state-demo',
  standalone: true,
  template: `
    <div class="state-demo">
      <h2>状態管理デモ</h2>
      <div class="counter">
        <p>カウンター: {{counter}}</p>
        <button (click)="increment()">増加</button>
        <button (click)="decrement()">減少</button>
      </div>
      <div class="timer">
        <p>タイマー: {{timer}}秒</p>
        <button (click)="toggleTimer()">{{isRunning ? '停止' : '開始'}}</button>
      </div>
      <div class="data">
        <p>データ: {{data | json}}</p>
        <button (click)="loadData()">データ読み込み</button>
      </div>
    </div>
  `,
  styles: [`
    .state-demo {
      padding: 20px;
      border: 1px solid #007bff;
      border-radius: 8px;
      margin: 20px;
    }
    .counter, .timer, .data {
      margin-bottom: 15px;
      padding: 10px;
      background-color: #f8f9fa;
      border-radius: 4px;
    }
  `]
})
export class StateDemoComponent implements OnInit, OnDestroy {
  counter = 0;
  timer = 0;
  isRunning = false;
  data: any = null;
  
  private timerSubscription?: Subscription;
  private dataSubject = new BehaviorSubject<any>(null);
  
  ngOnInit() {
    // DevToolsでObservableの状態を確認
    this.dataSubject.subscribe(data => {
      this.data = data;
      console.log('データ更新:', data);
    });
  }
  
  ngOnDestroy() {
    if (this.timerSubscription) {
      this.timerSubscription.unsubscribe();
    }
  }
  
  increment() {
    this.counter++;
    console.log('カウンター増加:', this.counter);
  }
  
  decrement() {
    this.counter--;
    console.log('カウンター減少:', this.counter);
  }
  
  toggleTimer() {
    if (this.isRunning) {
      this.stopTimer();
    } else {
      this.startTimer();
    }
  }
  
  private startTimer() {
    this.isRunning = true;
    this.timerSubscription = interval(1000).subscribe(() => {
      this.timer++;
      console.log('タイマー:', this.timer);
    });
  }
  
  private stopTimer() {
    this.isRunning = false;
    if (this.timerSubscription) {
      this.timerSubscription.unsubscribe();
    }
  }
  
  loadData() {
    // 模擬的なデータ読み込み
    setTimeout(() => {
      const newData = {
        id: Math.random(),
        timestamp: new Date().toISOString(),
        value: Math.random() * 100
      };
      this.dataSubject.next(newData);
    }, 1000);
  }
}
```

// DevToolsの機能説明
```typescript
@Component({
  selector: 'app-devtools-features',
  standalone: true,
  template: `
    <div class="features">
      <h2>Angular DevTools の機能</h2>
      <div class="feature-list">
        <div class="feature">
          <h3>Component Tree</h3>
          <p>Componentの階層構造を可視化</p>
          <ul>
            <li>Componentの親子関係</li>
            <li>Componentの状態</li>
            <li>Input/Outputの値</li>
          </ul>
        </div>
        <div class="feature">
          <h3>Profiler</h3>
          <p>パフォーマンスの分析</p>
          <ul>
            <li>変更検知の回数</li>
            <li>レンダリング時間</li>
            <li>メモリ使用量</li>
          </ul>
        </div>
        <div class="feature">
          <h3>Router Tree</h3>
          <p>ルーティングの状態</p>
          <ul>
            <li>現在のルート</li>
            <li>ルートパラメータ</li>
            <li>ナビゲーション履歴</li>
          </ul>
        </div>
        <div class="feature">
          <h3>State Inspector</h3>
          <p>アプリケーションの状態</p>
          <ul>
            <li>Serviceの状態</li>
            <li>Storeの状態</li>
            <li>Observableの値</li>
          </ul>
        </div>
      </div>
    </div>
  `,
  styles: [`
    .features {
      padding: 20px;
      max-width: 800px;
      margin: 0 auto;
    }
    .feature-list {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 20px;
      margin-top: 20px;
    }
    .feature {
      border: 1px solid #ddd;
      padding: 15px;
      border-radius: 8px;
      background-color: #f8f9fa;
    }
    .feature h3 {
      color: #007bff;
      margin-top: 0;
    }
    .feature ul {
      margin-bottom: 0;
    }
  `]
})
export class DevToolsFeaturesComponent {
  // Angular DevToolsの機能を説明
}
```

// DevToolsのインストール方法
```typescript
@Component({
  selector: 'app-devtools-install',
  standalone: true,
  template: `
    <div class="install-guide">
      <h2>Angular DevTools インストール方法</h2>
      <div class="steps">
        <div class="step">
          <h3>1. Chrome拡張機能をインストール</h3>
          <p>Chrome Web Storeで「Angular DevTools」を検索してインストール</p>
        </div>
        <div class="step">
          <h3>2. 開発者ツールを開く</h3>
          <p>F12キーまたは右クリック→「検証」で開発者ツールを開く</p>
        </div>
        <div class="step">
          <h3>3. Angularタブを選択</h3>
          <p>開発者ツールのタブ一覧から「Angular」を選択</p>
        </div>
        <div class="step">
          <h3>4. Component Treeを確認</h3>
          <p>左側のComponent TreeでComponentの階層を確認</p>
        </div>
      </div>
    </div>
  `,
  styles: [`
    .install-guide {
      padding: 20px;
      max-width: 600px;
      margin: 0 auto;
    }
    .steps {
      margin-top: 20px;
    }
    .step {
      margin-bottom: 20px;
      padding: 15px;
      border-left: 4px solid #007bff;
      background-color: #f8f9fa;
    }
    .step h3 {
      margin-top: 0;
      color: #007bff;
    }
  `]
})
export class DevToolsInstallComponent {
  // インストール手順を説明
}
```
