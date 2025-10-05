# #100 「@Input() 関数の受け渡し」

## 概要
Angular v20における@Input()での関数の受け渡しを学びます。コールバック関数、イベントハンドラー、非同期関数などの受け渡し方法と、適切な関数型定義について解説します。

## 学習目標
- 関数の受け渡し方法を理解する
- 適切な関数型定義を習得する
- コールバック関数の実装方法を身につける

## 📺 画面表示用コード

```typescript
// 関数の受け渡し
@Component({
  selector: 'app-function-input',
  standalone: true,
  template: `
    <div class="function-input">
      <button (click)="callCallback()">コールバック実行</button>
      <button (click)="callHandler()">ハンドラー実行</button>
    </div>
  `
})
export class FunctionInputComponent {
  @Input() callback: (data: string) => void = () => {};
  @Input() handler: () => void = () => {};
  
  callCallback() {
    this.callback('データ');
  }
  
  callHandler() {
    this.handler();
  }
}
```

```typescript
// 型安全な関数定義
export class TypedFunctionComponent {
  @Input() onSave: (data: any) => Promise<boolean> = async () => false;
  @Input() onCancel: () => void = () => {};
  @Input() validator: (value: string) => boolean = () => true;
}
```

```typescript
// 複数の関数パラメータ
export class MultiFunctionComponent {
  @Input() onSuccess: (result: any) => void = () => {};
  @Input() onError: (error: Error) => void = () => {};
  @Input() onProgress: (progress: number) => void = () => {};
}
```

## 技術ポイント

### 1. 基本的な関数型定義
```typescript
// 同期関数
@Input() syncFunction: () => void;
@Input() syncWithReturn: () => string;

// 非同期関数
@Input() asyncFunction: () => Promise<void>;
@Input() asyncWithReturn: () => Promise<string>;

// パラメータ付き関数
@Input() functionWithParams: (param: string) => void;
@Input() functionWithMultipleParams: (a: string, b: number) => boolean;
```

### 2. 型安全な関数定義
- **パラメータの型**: 引数の型を明確に定義
- **戻り値の型**: 戻り値の型を指定
- **デフォルト値**: 安全なデフォルト関数を設定

### 3. コールバック関数のパターン
- **イベントハンドラー**: ユーザーアクションの処理
- **データ処理**: データの変換や検証
- **非同期処理**: API呼び出しやタイマー処理

## 実践的な活用例

### 1. フォームコンポーネントでの関数受け渡し
```typescript
// form-with-callbacks.component.ts
interface FormCallbacks {
  onSubmit: (data: FormData) => Promise<boolean>;
  onCancel: () => void;
  onValidate: (field: string, value: any) => boolean;
  onReset: () => void;
}

@Component({
  selector: 'app-form-with-callbacks',
  standalone: true,
  template: `
    <form (ngSubmit)="handleSubmit()">
      <div class="form-group">
        <label>名前:</label>
        <input 
          [(ngModel)]="formData.name" 
          name="name"
          (blur)="validateField('name', formData.name)">
        <div *ngIf="fieldErrors.name" class="error">{{fieldErrors.name}}</div>
      </div>
      
      <div class="form-group">
        <label>メール:</label>
        <input 
          [(ngModel)]="formData.email" 
          name="email"
          type="email"
          (blur)="validateField('email', formData.email)">
        <div *ngIf="fieldErrors.email" class="error">{{fieldErrors.email}}</div>
      </div>
      
      <div class="form-actions">
        <button type="submit" [disabled]="!isFormValid">送信</button>
        <button type="button" (click)="handleCancel()">キャンセル</button>
        <button type="button" (click)="handleReset()">リセット</button>
      </div>
    </form>
  `,
  imports: [FormsModule]
})
export class FormWithCallbacksComponent {
  @Input() callbacks: FormCallbacks = {
    onSubmit: async () => false,
    onCancel: () => {},
    onValidate: () => true,
    onReset: () => {}
  };
  
  formData = {
    name: '',
    email: ''
  };
  
  fieldErrors: { [key: string]: string } = {};
  
  get isFormValid(): boolean {
    return !Object.values(this.fieldErrors).some(error => error);
  }
  
  async handleSubmit() {
    if (this.isFormValid) {
      try {
        const success = await this.callbacks.onSubmit(this.formData);
        if (success) {
          console.log('フォーム送信成功');
        } else {
          console.log('フォーム送信失敗');
        }
      } catch (error) {
        console.error('フォーム送信エラー:', error);
      }
    }
  }
  
  handleCancel() {
    this.callbacks.onCancel();
  }
  
  handleReset() {
    this.formData = { name: '', email: '' };
    this.fieldErrors = {};
    this.callbacks.onReset();
  }
  
  validateField(field: string, value: any) {
    const isValid = this.callbacks.onValidate(field, value);
    this.fieldErrors[field] = isValid ? '' : `${field}は無効です`;
  }
}
```

### 2. データ処理コンポーネント
```typescript
// data-processor.component.ts
interface DataProcessorCallbacks {
  onDataProcessed: (result: any) => void;
  onError: (error: Error) => void;
  onProgress: (progress: number) => void;
}

@Component({
  selector: 'app-data-processor',
  standalone: true,
  template: `
    <div class="data-processor">
      <h3>{{title}}</h3>
      
      <div class="input-section">
        <textarea 
          [(ngModel)]="inputData" 
          placeholder="処理するデータを入力">
        </textarea>
        <button (click)="processData()" [disabled]="isProcessing">
          {{isProcessing ? '処理中...' : 'データ処理'}}
        </button>
      </div>
      
      <div class="progress-section" *ngIf="isProcessing">
        <div class="progress-bar">
          <div class="progress-fill" [style.width.%]="progress"></div>
        </div>
        <p>進行状況: {{progress}}%</p>
      </div>
      
      <div class="result-section" *ngIf="result">
        <h4>処理結果:</h4>
        <pre>{{result | json}}</pre>
      </div>
      
      <div class="error-section" *ngIf="error">
        <h4>エラー:</h4>
        <p>{{error.message}}</p>
      </div>
    </div>
  `,
  imports: [FormsModule]
})
export class DataProcessorComponent {
  @Input() title: string = 'データ処理';
  @Input() callbacks: DataProcessorCallbacks = {
    onDataProcessed: () => {},
    onError: () => {},
    onProgress: () => {}
  };
  
  inputData: string = '';
  result: any = null;
  error: Error | null = null;
  isProcessing = false;
  progress = 0;
  
  async processData() {
    if (!this.inputData.trim()) {
      this.error = new Error('データが入力されていません');
      return;
    }
    
    this.isProcessing = true;
    this.progress = 0;
    this.error = null;
    this.result = null;
    
    try {
      // データ処理のシミュレーション
      await this.simulateDataProcessing();
      
      // 結果をコールバックで通知
      this.callbacks.onDataProcessed(this.result);
    } catch (error) {
      this.error = error instanceof Error ? error : new Error('不明なエラー');
      this.callbacks.onError(this.error);
    } finally {
      this.isProcessing = false;
    }
  }
  
  private async simulateDataProcessing() {
    const steps = 10;
    
    for (let i = 0; i < steps; i++) {
      // 進捗をコールバックで通知
      this.progress = (i + 1) * 10;
      this.callbacks.onProgress(this.progress);
      
      // 処理時間のシミュレーション
      await new Promise(resolve => setTimeout(resolve, 200));
    }
    
    // 処理結果の生成
    this.result = {
      originalData: this.inputData,
      processedAt: new Date(),
      wordCount: this.inputData.split(/\s+/).length,
      characterCount: this.inputData.length,
      processedData: this.inputData.toUpperCase()
    };
  }
}
```

### 3. カスタムフックコンポーネント
```typescript
// custom-hooks.component.ts
interface CustomHooks {
  onInit?: () => void;
  onDestroy?: () => void;
  onDataChange?: (newData: any, oldData: any) => void;
  onUserAction?: (action: string, data: any) => void;
}

@Component({
  selector: 'app-custom-hooks',
  standalone: true,
  template: `
    <div class="custom-hooks">
      <h3>{{title}}</h3>
      
      <div class="data-display">
        <p>現在のデータ: {{currentData}}</p>
        <button (click)="updateData()">データ更新</button>
      </div>
      
      <div class="actions">
        <button (click)="triggerAction('save')">保存</button>
        <button (click)="triggerAction('delete')">削除</button>
        <button (click)="triggerAction('edit')">編集</button>
      </div>
      
      <div class="logs">
        <h4>ログ:</h4>
        <div *ngFor="let log of logs" class="log-entry">{{log}}</div>
      </div>
    </div>
  `
})
export class CustomHooksComponent implements OnInit, OnDestroy {
  @Input() title: string = 'カスタムフック';
  @Input() hooks: CustomHooks = {};
  @Input() initialData: any = null;
  
  currentData: any = null;
  logs: string[] = [];
  
  ngOnInit() {
    this.currentData = this.initialData;
    this.addLog('コンポーネント初期化');
    
    if (this.hooks.onInit) {
      this.hooks.onInit();
    }
  }
  
  ngOnDestroy() {
    this.addLog('コンポーネント破棄');
    
    if (this.hooks.onDestroy) {
      this.hooks.onDestroy();
    }
  }
  
  updateData() {
    const oldData = this.currentData;
    this.currentData = { 
      value: Math.random(), 
      timestamp: new Date() 
    };
    
    this.addLog(`データ更新: ${oldData?.value} → ${this.currentData.value}`);
    
    if (this.hooks.onDataChange) {
      this.hooks.onDataChange(this.currentData, oldData);
    }
  }
  
  triggerAction(action: string) {
    this.addLog(`アクション実行: ${action}`);
    
    if (this.hooks.onUserAction) {
      this.hooks.onUserAction(action, this.currentData);
    }
  }
  
  private addLog(message: string) {
    const timestamp = new Date().toLocaleTimeString();
    this.logs.push(`[${timestamp}] ${message}`);
    
    // ログの最大数を制限
    if (this.logs.length > 10) {
      this.logs.shift();
    }
  }
}
```

### 4. 非同期処理コンポーネント
```typescript
// async-operations.component.ts
interface AsyncCallbacks {
  onStart: () => void;
  onComplete: (result: any) => void;
  onError: (error: Error) => void;
  onRetry: (attempt: number) => void;
}

@Component({
  selector: 'app-async-operations',
  standalone: true,
  template: `
    <div class="async-operations">
      <h3>{{title}}</h3>
      
      <div class="operation-controls">
        <button (click)="startOperation()" [disabled]="isRunning">
          {{isRunning ? '実行中...' : '操作開始'}}
        </button>
        <button (click)="retryOperation()" [disabled]="!hasError">リトライ</button>
        <button (click)="cancelOperation()" [disabled]="!isRunning">キャンセル</button>
      </div>
      
      <div class="operation-status">
        <p>ステータス: {{status}}</p>
        <p *ngIf="attemptCount > 0">試行回数: {{attemptCount}}</p>
        <p *ngIf="lastResult">最終結果: {{lastResult | json}}</p>
        <p *ngIf="lastError">エラー: {{lastError.message}}</p>
      </div>
    </div>
  `
})
export class AsyncOperationsComponent {
  @Input() title: string = '非同期操作';
  @Input() callbacks: AsyncCallbacks = {
    onStart: () => {},
    onComplete: () => {},
    onError: () => {},
    onRetry: () => {}
  };
  
  isRunning = false;
  status = '待機中';
  attemptCount = 0;
  lastResult: any = null;
  lastError: Error | null = null;
  private operationAborted = false;
  
  get hasError(): boolean {
    return this.lastError !== null;
  }
  
  async startOperation() {
    this.operationAborted = false;
    this.isRunning = true;
    this.status = '実行中';
    this.lastError = null;
    this.attemptCount++;
    
    this.callbacks.onStart();
    
    try {
      const result = await this.performAsyncOperation();
      
      if (!this.operationAborted) {
        this.lastResult = result;
        this.status = '完了';
        this.callbacks.onComplete(result);
      }
    } catch (error) {
      if (!this.operationAborted) {
        this.lastError = error instanceof Error ? error : new Error('不明なエラー');
        this.status = 'エラー';
        this.callbacks.onError(this.lastError);
      }
    } finally {
      if (!this.operationAborted) {
        this.isRunning = false;
      }
    }
  }
  
  retryOperation() {
    this.lastError = null;
    this.callbacks.onRetry(this.attemptCount);
    this.startOperation();
  }
  
  cancelOperation() {
    this.operationAborted = true;
    this.isRunning = false;
    this.status = 'キャンセル';
  }
  
  private async performAsyncOperation(): Promise<any> {
    // 非同期操作のシミュレーション
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    if (Math.random() > 0.7) {
      throw new Error('ランダムエラーが発生しました');
    }
    
    return {
      success: true,
      data: { value: Math.random(), timestamp: new Date() }
    };
  }
}
```

## ベストプラクティス

1. **型安全性**: 明確な関数型定義
2. **デフォルト値**: 安全なデフォルト関数の設定
3. **エラーハンドリング**: 適切なエラー処理
4. **非同期処理**: Promise/async-awaitの適切な使用

## 注意点

- 関数の参照渡しにより、親で関数を変更すると子にも影響する
- 非同期関数の場合は適切なエラーハンドリングが必要
- メモリリークを防ぐため、不要な関数参照を適切に管理

## 関連技術
- 関数型プログラミング
- コールバック関数
- Promise/async-await
- 型安全性
