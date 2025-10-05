# #105 「@Output() の基本構文」

## 概要
Angular v20における@Output()の基本構文を学びます。EventEmitterを使用したイベント発火と、親コンポーネントでのイベント受信の基本的な実装方法について解説します。

## 学習目標
- @Output()の基本構文を理解する
- EventEmitterの使用方法を習得する
- 親子間のイベント通信の実装方法を身につける

## 📺 画面表示用コード

```typescript
// @Output()の基本構文
@Component({
  selector: 'app-basic-output',
  standalone: true,
  template: `
    <button (click)="sendData()">データ送信</button>
    <button (click)="sendEvent()">イベント送信</button>
  `
})
export class BasicOutputComponent {
  @Output() dataEvent = new EventEmitter<string>();
  @Output() actionEvent = new EventEmitter<void>();
  
  sendData() {
    this.dataEvent.emit('送信データ');
  }
  
  sendEvent() {
    this.actionEvent.emit();
  }
}
```

```html
<!-- 親コンポーネントでの使用 -->
<app-basic-output
  (dataEvent)="onDataReceived($event)"
  (actionEvent)="onActionPerformed()">
</app-basic-output>
```

```typescript
// 親コンポーネントでのイベント処理
export class ParentComponent {
  receivedData = '';
  
  onDataReceived(data: string) {
    this.receivedData = data;
    console.log('受信データ:', data);
  }
  
  onActionPerformed() {
    console.log('アクションが実行されました');
  }
}
```

## 技術ポイント

### 1. @Output()の基本構文
```typescript
@Output() eventName = new EventEmitter<DataType>();
```
- `eventName`: イベント名（キャメルケース）
- `EventEmitter<DataType>`: 送信するデータの型を指定
- `DataType`: 送信するデータの型（voidの場合はデータなし）

### 2. イベントの発火
```typescript
// データ付きイベントの発火
this.eventName.emit(data);

// データなしイベントの発火
this.eventName.emit();
```

### 3. 親でのイベント受信
```html
<child-component (eventName)="handler($event)"></child-component>
```
- `(eventName)`: イベントバインディング
- `handler($event)`: イベントハンドラー関数
- `$event`: 送信されたデータ

## 実践的な活用例

### 1. 基本的なデータ送信
```typescript
// data-sender.component.ts
@Component({
  selector: 'app-data-sender',
  standalone: true,
  template: `
    <div class="data-sender">
      <input [(ngModel)]="inputData" placeholder="データを入力">
      <button (click)="sendData()">送信</button>
      <button (click)="clearData()">クリア</button>
    </div>
  `,
  imports: [FormsModule]
})
export class DataSenderComponent {
  @Output() dataSent = new EventEmitter<string>();
  @Output() dataCleared = new EventEmitter<void>();
  
  inputData = '';
  
  sendData() {
    if (this.inputData.trim()) {
      this.dataSent.emit(this.inputData);
    }
  }
  
  clearData() {
    this.inputData = '';
    this.dataCleared.emit();
  }
}
```

### 2. 複数のイベントタイプ
```typescript
// multi-event.component.ts
@Component({
  selector: 'app-multi-event',
  standalone: true,
  template: `
    <div class="multi-event">
      <button (click)="onSave()">保存</button>
      <button (click)="onCancel()">キャンセル</button>
      <button (click)="onDelete()">削除</button>
      <button (click)="onEdit()">編集</button>
    </div>
  `
})
export class MultiEventComponent {
  @Output() save = new EventEmitter<{id: number, data: any}>();
  @Output() cancel = new EventEmitter<void>();
  @Output() delete = new EventEmitter<number>();
  @Output() edit = new EventEmitter<number>();
  
  @Input() itemId: number = 0;
  @Input() itemData: any = {};
  
  onSave() {
    this.save.emit({
      id: this.itemId,
      data: this.itemData
    });
  }
  
  onCancel() {
    this.cancel.emit();
  }
  
  onDelete() {
    this.delete.emit(this.itemId);
  }
  
  onEdit() {
    this.edit.emit(this.itemId);
  }
}
```

### 3. 条件付きイベント発火
```typescript
// conditional-event.component.ts
@Component({
  selector: 'app-conditional-event',
  standalone: true,
  template: `
    <div class="conditional-event">
      <input [(ngModel)]="inputValue" placeholder="値を入力">
      <button (click)="validateAndSend()" [disabled]="!inputValue">
        検証して送信
      </button>
      <div *ngIf="errorMessage" class="error">{{errorMessage}}</div>
    </div>
  `,
  imports: [FormsModule]
})
export class ConditionalEventComponent {
  @Output() validDataSent = new EventEmitter<string>();
  @Output() validationError = new EventEmitter<string>();
  
  inputValue = '';
  errorMessage = '';
  
  validateAndSend() {
    this.errorMessage = '';
    
    if (!this.inputValue.trim()) {
      this.errorMessage = '値が入力されていません';
      this.validationError.emit(this.errorMessage);
      return;
    }
    
    if (this.inputValue.length < 3) {
      this.errorMessage = '値は3文字以上である必要があります';
      this.validationError.emit(this.errorMessage);
      return;
    }
    
    this.validDataSent.emit(this.inputValue);
  }
}
```

### 4. 非同期イベント処理
```typescript
// async-event.component.ts
@Component({
  selector: 'app-async-event',
  standalone: true,
  template: `
    <div class="async-event">
      <button (click)="startAsyncOperation()" [disabled]="isLoading">
        {{isLoading ? '処理中...' : '非同期処理開始'}}
      </button>
      <div *ngIf="result" class="result">{{result}}</div>
    </div>
  `
})
export class AsyncEventComponent {
  @Output() operationStarted = new EventEmitter<void>();
  @Output() operationCompleted = new EventEmitter<string>();
  @Output() operationFailed = new EventEmitter<string>();
  
  isLoading = false;
  result = '';
  
  async startAsyncOperation() {
    this.isLoading = true;
    this.operationStarted.emit();
    
    try {
      // 非同期処理のシミュレーション
      const result = await this.simulateAsyncOperation();
      this.result = result;
      this.operationCompleted.emit(result);
    } catch (error) {
      const errorMessage = '処理に失敗しました';
      this.operationFailed.emit(errorMessage);
    } finally {
      this.isLoading = false;
    }
  }
  
  private simulateAsyncOperation(): Promise<string> {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (Math.random() > 0.2) {
          resolve('処理が完了しました');
        } else {
          reject(new Error('ランダムエラー'));
        }
      }, 2000);
    });
  }
}
```

## ベストプラクティス

1. **明確な命名**: イベント名は動詞を含み、用途が明確になるように命名
2. **型安全性**: EventEmitterに適切な型を指定
3. **単一責任**: 各イベントは単一の責任を持つ
4. **エラーハンドリング**: 適切なエラーイベントの実装

## 注意点

- イベント名はキャメルケースで記述する
- 大量のデータを送信する場合はパフォーマンスを考慮する
- イベントの発火頻度に注意し、必要以上に頻繁に発火しないようにする

## 関連技術
- EventEmitter
- イベントバインディング
- 非同期処理
- エラーハンドリング
