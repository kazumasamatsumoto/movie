# #106 「EventEmitter の使い方」

## 概要
Angular v20におけるEventEmitterの詳細な使用方法を学びます。型安全性、Observableとしての機能、非同期処理との組み合わせなど、EventEmitterの高度な活用方法について解説します。

## 学習目標
- EventEmitterの基本的な使用方法を理解する
- 型安全性とObservable機能を習得する
- 非同期処理との組み合わせ方法を身につける

## 📺 画面表示用コード

```typescript
// EventEmitterの基本使用
@Component({
  selector: 'app-event-emitter',
  standalone: true,
  template: `
    <button (click)="emitString()">文字列送信</button>
    <button (click)="emitObject()">オブジェクト送信</button>
    <button (click)="emitVoid()">イベント送信</button>
  `
})
export class EventEmitterComponent {
  @Output() stringEvent = new EventEmitter<string>();
  @Output() objectEvent = new EventEmitter<{id: number, name: string}>();
  @Output() voidEvent = new EventEmitter<void>();
  
  emitString() {
    this.stringEvent.emit('Hello World');
  }
  
  emitObject() {
    this.objectEvent.emit({id: 1, name: 'テスト'});
  }
  
  emitVoid() {
    this.voidEvent.emit();
  }
}
```

```typescript
// Observableとしての使用
export class ObservableEventComponent {
  @Output() dataStream = new EventEmitter<number>();
  
  ngOnInit() {
    // EventEmitterはObservableとしても使用可能
    this.dataStream.subscribe(value => {
      console.log('受信:', value);
    });
  }
  
  startDataStream() {
    let count = 0;
    setInterval(() => {
      this.dataStream.emit(count++);
    }, 1000);
  }
}
```

## 技術ポイント

### 1. EventEmitterの基本機能
- **イベント発火**: `emit(value)`でイベントを発火
- **型安全性**: `EventEmitter<Type>`で型を指定
- **Observable**: RxJSのObservableとしても機能
- **購読管理**: 自動的な購読解除

### 2. 型指定のパターン
```typescript
// プリミティブ型
@Output() stringEvent = new EventEmitter<string>();
@Output() numberEvent = new EventEmitter<number>();
@Output() booleanEvent = new EventEmitter<boolean>();

// オブジェクト型
@Output() userEvent = new EventEmitter<User>();
@Output() configEvent = new EventEmitter<Config>();

// データなし
@Output() actionEvent = new EventEmitter<void>();
```

### 3. Observableとしての機能
```typescript
// 購読
eventEmitter.subscribe(value => {
  console.log('受信:', value);
});

// エラーハンドリング
eventEmitter.subscribe({
  next: value => console.log('受信:', value),
  error: error => console.error('エラー:', error),
  complete: () => console.log('完了')
});
```

## 実践的な活用例

### 1. 型安全なデータ送信
```typescript
// typed-data-sender.component.ts
interface UserData {
  id: number;
  name: string;
  email: string;
  createdAt: Date;
}

@Component({
  selector: 'app-typed-data-sender',
  standalone: true,
  template: `
    <div class="data-sender">
      <input [(ngModel)]="userName" placeholder="ユーザー名">
      <input [(ngModel)]="userEmail" placeholder="メールアドレス">
      <button (click)="sendUserData()">ユーザーデータ送信</button>
      <button (click)="sendError()">エラー送信</button>
    </div>
  `,
  imports: [FormsModule]
})
export class TypedDataSenderComponent {
  @Output() userDataSent = new EventEmitter<UserData>();
  @Output() errorOccurred = new EventEmitter<string>();
  
  userName = '';
  userEmail = '';
  
  sendUserData() {
    if (this.validateInput()) {
      const userData: UserData = {
        id: Math.floor(Math.random() * 1000),
        name: this.userName,
        email: this.userEmail,
        createdAt: new Date()
      };
      
      this.userDataSent.emit(userData);
      this.clearInputs();
    } else {
      this.errorOccurred.emit('入力データが無効です');
    }
  }
  
  sendError() {
    this.errorOccurred.emit('テストエラー');
  }
  
  private validateInput(): boolean {
    return this.userName.trim().length > 0 && 
           this.userEmail.trim().length > 0 &&
           this.isValidEmail(this.userEmail);
  }
  
  private isValidEmail(email: string): boolean {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }
  
  private clearInputs() {
    this.userName = '';
    this.userEmail = '';
  }
}
```

### 2. ストリーミングデータの実装
```typescript
// streaming-data.component.ts
@Component({
  selector: 'app-streaming-data',
  standalone: true,
  template: `
    <div class="streaming-data">
      <button (click)="startStream()" [disabled]="isStreaming">
        {{isStreaming ? 'ストリーミング中...' : 'ストリーム開始'}}
      </button>
      <button (click)="stopStream()" [disabled]="!isStreaming">
        ストリーム停止
      </button>
      <div class="stream-info">
        <p>送信データ数: {{sentCount}}</p>
        <p>最終データ: {{lastSentData}}</p>
      </div>
    </div>
  `
})
export class StreamingDataComponent implements OnDestroy {
  @Output() dataStream = new EventEmitter<number>();
  @Output() streamStarted = new EventEmitter<void>();
  @Output() streamStopped = new EventEmitter<void>();
  
  isStreaming = false;
  sentCount = 0;
  lastSentData: number | null = null;
  private streamInterval?: number;
  
  startStream() {
    if (this.isStreaming) return;
    
    this.isStreaming = true;
    this.sentCount = 0;
    this.streamStarted.emit();
    
    this.streamInterval = setInterval(() => {
      const data = Math.floor(Math.random() * 100);
      this.dataStream.emit(data);
      this.sentCount++;
      this.lastSentData = data;
    }, 500);
  }
  
  stopStream() {
    if (!this.isStreaming) return;
    
    this.isStreaming = false;
    
    if (this.streamInterval) {
      clearInterval(this.streamInterval);
      this.streamInterval = undefined;
    }
    
    this.streamStopped.emit();
  }
  
  ngOnDestroy() {
    this.stopStream();
  }
}
```

### 3. 非同期処理との組み合わせ
```typescript
// async-event.component.ts
interface AsyncResult {
  success: boolean;
  data?: any;
  error?: string;
  duration: number;
}

@Component({
  selector: 'app-async-event',
  standalone: true,
  template: `
    <div class="async-event">
      <button (click)="performAsyncOperation()" [disabled]="isLoading">
        {{isLoading ? '処理中...' : '非同期処理実行'}}
      </button>
      <div *ngIf="lastResult" class="result">
        <p>成功: {{lastResult.success}}</p>
        <p>処理時間: {{lastResult.duration}}ms</p>
        <p *ngIf="lastResult.error">エラー: {{lastResult.error}}</p>
      </div>
    </div>
  `
})
export class AsyncEventComponent {
  @Output() operationStarted = new EventEmitter<void>();
  @Output() operationCompleted = new EventEmitter<AsyncResult>();
  @Output() operationFailed = new EventEmitter<AsyncResult>();
  
  isLoading = false;
  lastResult: AsyncResult | null = null;
  
  async performAsyncOperation() {
    this.isLoading = true;
    this.operationStarted.emit();
    
    const startTime = Date.now();
    
    try {
      const result = await this.simulateAsyncWork();
      const duration = Date.now() - startTime;
      
      const asyncResult: AsyncResult = {
        success: true,
        data: result,
        duration
      };
      
      this.lastResult = asyncResult;
      this.operationCompleted.emit(asyncResult);
    } catch (error) {
      const duration = Date.now() - startTime;
      
      const asyncResult: AsyncResult = {
        success: false,
        error: error instanceof Error ? error.message : '不明なエラー',
        duration
      };
      
      this.lastResult = asyncResult;
      this.operationFailed.emit(asyncResult);
    } finally {
      this.isLoading = false;
    }
  }
  
  private simulateAsyncWork(): Promise<any> {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (Math.random() > 0.3) {
          resolve({ message: '処理が完了しました', timestamp: new Date() });
        } else {
          reject(new Error('ランダムエラーが発生しました'));
        }
      }, 2000);
    });
  }
}
```

### 4. イベントの購読と管理
```typescript
// event-subscription.component.ts
@Component({
  selector: 'app-event-subscription',
  standalone: true,
  template: `
    <div class="event-subscription">
      <button (click)="startListening()">イベント監視開始</button>
      <button (click)="stopListening()">イベント監視停止</button>
      <div class="event-log">
        <h4>イベントログ:</h4>
        <div *ngFor="let log of eventLogs" class="log-entry">
          {{log.timestamp | date:'HH:mm:ss'}} - {{log.message}}
        </div>
      </div>
    </div>
  `
})
export class EventSubscriptionComponent implements OnInit, OnDestroy {
  @Output() eventEmitted = new EventEmitter<{type: string, data: any}>();
  
  eventLogs: Array<{timestamp: Date, message: string}> = [];
  private subscription?: any;
  
  ngOnInit() {
    // EventEmitterをObservableとして購読
    this.subscription = this.eventEmitted.subscribe(event => {
      this.addLog(`イベント受信: ${event.type}`, event.data);
    });
  }
  
  ngOnDestroy() {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }
  
  startListening() {
    this.addLog('イベント監視を開始しました');
    
    // 定期的にイベントを発火
    setInterval(() => {
      this.eventEmitted.emit({
        type: 'periodic_event',
        data: { timestamp: new Date(), value: Math.random() }
      });
    }, 3000);
  }
  
  stopListening() {
    this.addLog('イベント監視を停止しました');
  }
  
  private addLog(message: string, data?: any) {
    this.eventLogs.push({
      timestamp: new Date(),
      message: data ? `${message} - ${JSON.stringify(data)}` : message
    });
    
    // ログの最大数を制限
    if (this.eventLogs.length > 10) {
      this.eventLogs.shift();
    }
  }
}
```

## ベストプラクティス

1. **型安全性**: EventEmitterに適切な型を指定
2. **購読管理**: 適切な購読の解除
3. **エラーハンドリング**: エラーイベントの適切な処理
4. **パフォーマンス**: 不要なイベント発火を避ける

## 注意点

- EventEmitterはObservableとしても機能するが、主な用途は親子間の通信
- 大量のデータを送信する場合はパフォーマンスを考慮
- 購読の解除を忘れずに行う

## 関連技術
- RxJS Observable
- 非同期処理
- イベント管理
- 型安全性
