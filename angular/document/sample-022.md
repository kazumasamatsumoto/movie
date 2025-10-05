# #022 「Component のホットリロード」台本

四国めたん「Component のホットリロードについて学びましょう！」
ずんだもん「ホットリロードって何？」
四国めたん「ファイルを保存すると、ページを再読み込みせずに変更が即座に反映される機能です」
ずんだもん「どんなメリットがあるの？」
四国めたん「開発効率が向上し、状態を保持したまま変更を確認できます」
ずんだもん「どうやって有効にするの？」
四国めたん「ng serveコマンドで開発サーバーを起動すると、デフォルトで有効になります」

---

## 📺 画面表示用コード

// ホットリロードのデモ用Component
```typescript
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-hot-reload-demo',
  standalone: true,
  template: `
    <div class="hot-reload-demo">
      <h2>ホットリロード デモ</h2>
      <div class="counter-section">
        <h3>カウンター: {{counter}}</h3>
        <button (click)="increment()">増加</button>
        <button (click)="decrement()">減少</button>
        <button (click)="reset()">リセット</button>
      </div>
      <div class="user-section">
        <h3>ユーザー情報</h3>
        <p>名前: {{user.name}}</p>
        <p>年齢: {{user.age}}</p>
        <p>ステータス: {{user.status}}</p>
        <button (click)="updateUser()">ユーザー更新</button>
      </div>
      <div class="message-section">
        <h3>メッセージ</h3>
        <p>{{message}}</p>
        <input [(ngModel)]="inputMessage" placeholder="メッセージを入力">
        <button (click)="updateMessage()">メッセージ更新</button>
      </div>
    </div>
  `,
  styles: [`
    .hot-reload-demo {
      padding: 20px;
      max-width: 600px;
      margin: 0 auto;
      font-family: Arial, sans-serif;
    }
    .counter-section, .user-section, .message-section {
      margin-bottom: 20px;
      padding: 15px;
      border: 1px solid #ddd;
      border-radius: 8px;
      background-color: #f8f9fa;
    }
    .counter-section h3 {
      color: #007bff;
      margin-top: 0;
    }
    .user-section h3 {
      color: #28a745;
      margin-top: 0;
    }
    .message-section h3 {
      color: #dc3545;
      margin-top: 0;
    }
    button {
      margin-right: 10px;
      padding: 8px 16px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      opacity: 0.8;
    }
    input {
      padding: 8px;
      margin-right: 10px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }
  `]
})
export class HotReloadDemoComponent implements OnInit {
  counter = 0;
  user = {
    name: '田中太郎',
    age: 30,
    status: 'active'
  };
  message = 'ホットリロードのテストメッセージ';
  inputMessage = '';
  
  ngOnInit() {
    console.log('Componentが初期化されました');
    console.log('現在のカウンター:', this.counter);
    console.log('現在のユーザー:', this.user);
  }
  
  increment() {
    this.counter++;
    console.log('カウンター増加:', this.counter);
  }
  
  decrement() {
    this.counter--;
    console.log('カウンター減少:', this.counter);
  }
  
  reset() {
    this.counter = 0;
    console.log('カウンターリセット');
  }
  
  updateUser() {
    this.user.name = '佐藤花子';
    this.user.age = 25;
    this.user.status = 'inactive';
    console.log('ユーザー情報更新:', this.user);
  }
  
  updateMessage() {
    if (this.inputMessage.trim()) {
      this.message = this.inputMessage;
      this.inputMessage = '';
      console.log('メッセージ更新:', this.message);
    }
  }
}
```

// ホットリロードの設定
```typescript
// angular.json
{
  "projects": {
    "my-app": {
      "architect": {
        "serve": {
          "builder": "@angular-devkit/build-angular:dev-server",
          "options": {
            "liveReload": true,        // ホットリロードを有効
            "watch": true,             // ファイル監視を有効
            "hmr": true,               // Hot Module Replacement
            "port": 4200,              // ポート番号
            "host": "localhost"        // ホスト
          }
        }
      }
    }
  }
}
```

// 開発サーバーの起動コマンド
```bash
# 基本的な起動
ng serve

# ホットリロードを明示的に有効化
ng serve --live-reload

# 特定のポートで起動
ng serve --port 4200

# ホストを指定
ng serve --host 0.0.0.0

# オープンで起動
ng serve --open
```

// ホットリロードの動作確認
```typescript
@Component({
  selector: 'app-hot-reload-test',
  standalone: true,
  template: `
    <div class="test-container">
      <h2>ホットリロード テスト</h2>
      <div class="test-item">
        <h3>スタイル変更テスト</h3>
        <p class="test-text">このテキストの色を変更してみてください</p>
      </div>
      <div class="test-item">
        <h3>テンプレート変更テスト</h3>
        <p>このテキストを変更してみてください</p>
        <button (click)="showAlert()">アラート表示</button>
      </div>
      <div class="test-item">
        <h3>ロジック変更テスト</h3>
        <p>計算結果: {{calculate()}}</p>
        <button (click)="updateCalculation()">計算更新</button>
      </div>
    </div>
  `,
  styles: [`
    .test-container {
      padding: 20px;
      max-width: 800px;
      margin: 0 auto;
    }
    .test-item {
      margin-bottom: 20px;
      padding: 15px;
      border: 1px solid #ccc;
      border-radius: 8px;
      background-color: #f8f9fa;
    }
    .test-text {
      color: #007bff;  /* この色を変更してテスト */
      font-weight: bold;
    }
    button {
      padding: 8px 16px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background-color: #0056b3;
    }
  `]
})
export class HotReloadTestComponent {
  calculationValue = 10;
  
  calculate(): number {
    // この計算ロジックを変更してテスト
    return this.calculationValue * 2;
  }
  
  updateCalculation() {
    this.calculationValue = Math.floor(Math.random() * 100);
    console.log('計算値更新:', this.calculationValue);
  }
  
  showAlert() {
    // このメッセージを変更してテスト
    alert('ホットリロードのテストです！');
  }
}
```

// ホットリロードの制限事項
```typescript
@Component({
  selector: 'app-hot-reload-limitations',
  standalone: true,
  template: `
    <div class="limitations">
      <h2>ホットリロードの制限事項</h2>
      <div class="limitation-item">
        <h3>1. コンストラクタの変更</h3>
        <p>コンストラクタの変更は完全なリロードが必要</p>
        <button (click)="constructorTest()">コンストラクタテスト</button>
      </div>
      <div class="limitation-item">
        <h3>2. インポートの変更</h3>
        <p>新しいモジュールのインポートは完全なリロードが必要</p>
      </div>
      <div class="limitation-item">
        <h3>3. デコレータの変更</h3>
        <p>@Componentデコレータの変更は完全なリロードが必要</p>
      </div>
      <div class="limitation-item">
        <h3>4. グローバル変数の変更</h3>
        <p>グローバル変数の変更は完全なリロードが必要</p>
      </div>
    </div>
  `,
  styles: [`
    .limitations {
      padding: 20px;
      max-width: 600px;
      margin: 0 auto;
    }
    .limitation-item {
      margin-bottom: 15px;
      padding: 15px;
      border: 1px solid #ffc107;
      border-radius: 8px;
      background-color: #fff3cd;
    }
    .limitation-item h3 {
      color: #856404;
      margin-top: 0;
    }
    button {
      padding: 8px 16px;
      background-color: #ffc107;
      color: #212529;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
  `]
})
export class HotReloadLimitationsComponent {
  constructor() {
    // このコンストラクタを変更すると完全なリロードが必要
    console.log('コンストラクタが実行されました');
  }
  
  constructorTest() {
    console.log('コンストラクタテストが実行されました');
  }
}
```

// ホットリロードのベストプラクティス
```typescript
@Component({
  selector: 'app-hot-reload-best-practices',
  standalone: true,
  template: `
    <div class="best-practices">
      <h2>ホットリロードのベストプラクティス</h2>
      <div class="practice-item">
        <h3>1. 小さな変更を頻繁に</h3>
        <p>大きな変更よりも小さな変更を頻繁に行う</p>
      </div>
      <div class="practice-item">
        <h3>2. 状態の保持</h3>
        <p>重要な状態はローカルストレージに保存</p>
      </div>
      <div class="practice-item">
        <h3>3. エラーハンドリング</h3>
        <p>エラーが発生した場合は手動でリロード</p>
      </div>
      <div class="practice-item">
        <h3>4. パフォーマンス監視</h3>
        <p>ホットリロードのパフォーマンスを監視</p>
      </div>
    </div>
  `,
  styles: [`
    .best-practices {
      padding: 20px;
      max-width: 600px;
      margin: 0 auto;
    }
    .practice-item {
      margin-bottom: 15px;
      padding: 15px;
      border: 1px solid #28a745;
      border-radius: 8px;
      background-color: #d4edda;
    }
    .practice-item h3 {
      color: #155724;
      margin-top: 0;
    }
  `]
})
export class HotReloadBestPracticesComponent {
  // ホットリロードを効果的に活用するためのベストプラクティス
}
```
