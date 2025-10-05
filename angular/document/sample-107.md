# #107 「@Output() カスタムイベント発火」

## 概要
Angular v20における@Output()でのカスタムイベント発火を学びます。独自のイベントタイプとデータ構造を定義し、柔軟で拡張性の高いイベント通信を実現する方法について解説します。

## 学習目標
- カスタムイベントの定義方法を理解する
- カスタムデータ構造の設計を習得する
- 柔軟なイベント通信の実装方法を身につける

## 📺 画面表示用コード

```typescript
// カスタムイベントの発火
interface CustomEventData {
  type: 'save' | 'delete' | 'update';
  data: any;
  timestamp: Date;
}

@Component({
  selector: 'app-custom-event',
  standalone: true,
  template: `
    <div class="custom-event">
      <button (click)="triggerSave()">保存</button>
      <button (click)="triggerDelete()">削除</button>
      <button (click)="triggerUpdate()">更新</button>
    </div>
  `
})
export class CustomEventComponent {
  @Output() customEvent = new EventEmitter<CustomEventData>();
  
  triggerSave() {
    this.emitEvent('save', { id: 1, name: 'テスト' });
  }
  
  triggerDelete() {
    this.emitEvent('delete', { id: 1 });
  }
  
  triggerUpdate() {
    this.emitEvent('update', { id: 1, changes: { name: '新しい名前' } });
  }
  
  private emitEvent(type: CustomEventData['type'], data: any) {
    const eventData: CustomEventData = {
      type,
      data,
      timestamp: new Date()
    };
    this.customEvent.emit(eventData);
  }
}
```

```html
<!-- 親コンポーネントでの使用 -->
<app-custom-event (customEvent)="handleCustomEvent($event)"></app-custom-event>
```

```typescript
// 親でのカスタムイベント処理
export class ParentComponent {
  handleCustomEvent(event: CustomEventData) {
    switch (event.type) {
      case 'save':
        this.saveData(event.data);
        break;
      case 'delete':
        this.deleteData(event.data.id);
        break;
      case 'update':
        this.updateData(event.data);
        break;
    }
  }
}
```

## 技術ポイント

### 1. カスタムイベントの設計
- **型安全性**: TypeScriptの型システムを活用
- **拡張性**: 新しいイベントタイプの追加が容易
- **一貫性**: 統一されたイベント構造

### 2. カスタムデータ構造
```typescript
// 基本的なカスタムイベント
interface CustomEvent {
  type: string;
  payload: any;
  timestamp: Date;
}

// 型安全なカスタムイベント
interface TypedCustomEvent<T> {
  type: string;
  data: T;
  metadata: {
    timestamp: Date;
    source: string;
    version: string;
  };
}
```

### 3. イベント発火パターン
- **単一イベント**: 一つのEventEmitterで複数のイベントタイプ
- **複数イベント**: 複数のEventEmitterで異なるイベントタイプ
- **階層イベント**: イベントの階層構造

## 実践的な活用例

### 1. フォームアクションカスタムイベント
```typescript
// form-actions-custom.component.ts
interface FormActionEvent {
  action: 'submit' | 'cancel' | 'reset' | 'validate' | 'save_draft';
  formData: any;
  metadata: {
    timestamp: Date;
    userId?: string;
    sessionId?: string;
    validationErrors?: string[];
  };
}

@Component({
  selector: 'app-form-actions-custom',
  standalone: true,
  template: `
    <div class="form-actions">
      <h3>{{title}}</h3>
      
      <form (ngSubmit)="onSubmit()">
        <div class="form-group">
          <label>名前:</label>
          <input [(ngModel)]="formData.name" name="name" required>
        </div>
        
        <div class="form-group">
          <label>メール:</label>
          <input [(ngModel)]="formData.email" name="email" type="email" required>
        </div>
        
        <div class="form-actions">
          <button type="submit" [disabled]="!isFormValid">送信</button>
          <button type="button" (click)="onCancel()">キャンセル</button>
          <button type="button" (click)="onReset()">リセット</button>
          <button type="button" (click)="onValidate()">検証</button>
          <button type="button" (click)="onSaveDraft()">下書き保存</button>
        </div>
      </form>
    </div>
  `,
  imports: [FormsModule]
})
export class FormActionsCustomComponent {
  @Input() title: string = 'フォームアクション';
  @Input() userId?: string;
  @Input() sessionId?: string;
  
  @Output() formAction = new EventEmitter<FormActionEvent>();
  
  formData = {
    name: '',
    email: ''
  };
  
  get isFormValid(): boolean {
    return this.formData.name.trim() && this.formData.email.trim();
  }
  
  onSubmit() {
    this.emitAction('submit', this.formData);
  }
  
  onCancel() {
    this.emitAction('cancel', this.formData);
  }
  
  onReset() {
    this.emitAction('reset', this.formData);
    this.formData = { name: '', email: '' };
  }
  
  onValidate() {
    const validationErrors = this.validateForm();
    this.emitAction('validate', this.formData, { validationErrors });
  }
  
  onSaveDraft() {
    this.emitAction('save_draft', this.formData);
  }
  
  private emitAction(action: FormActionEvent['action'], formData: any, metadata?: Partial<FormActionEvent['metadata']>) {
    const event: FormActionEvent = {
      action,
      formData,
      metadata: {
        timestamp: new Date(),
        userId: this.userId,
        sessionId: this.sessionId,
        ...metadata
      }
    };
    
    this.formAction.emit(event);
  }
  
  private validateForm(): string[] {
    const errors: string[] = [];
    
    if (!this.formData.name.trim()) {
      errors.push('名前は必須です');
    }
    
    if (!this.formData.email.trim()) {
      errors.push('メールアドレスは必須です');
    } else if (!this.isValidEmail(this.formData.email)) {
      errors.push('有効なメールアドレスを入力してください');
    }
    
    return errors;
  }
  
  private isValidEmail(email: string): boolean {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }
}
```

### 2. データテーブルカスタムイベント
```typescript
// data-table-custom.component.ts
interface TableEvent {
  eventType: 'row_select' | 'row_edit' | 'row_delete' | 'column_sort' | 'filter_change' | 'page_change';
  data: {
    rowIndex?: number;
    rowData?: any;
    columnKey?: string;
    sortDirection?: 'asc' | 'desc';
    filterValue?: string;
    pageNumber?: number;
  };
  context: {
    tableId: string;
    timestamp: Date;
    userAgent: string;
  };
}

@Component({
  selector: 'app-data-table-custom',
  standalone: true,
  template: `
    <div class="data-table">
      <h3>{{title}}</h3>
      
      <div class="table-controls">
        <input 
          [(ngModel)]="searchTerm" 
          placeholder="検索..."
          (input)="onFilterChange()">
      </div>
      
      <table>
        <thead>
          <tr>
            <th 
              *ngFor="let column of columns" 
              (click)="onColumnSort(column.key)"
              [class.sortable]="column.sortable">
              {{column.title}}
              <span *ngIf="sortColumn === column.key" class="sort-indicator">
                {{sortDirection === 'asc' ? '↑' : '↓'}}
              </span>
            </th>
            <th>アクション</th>
          </tr>
        </thead>
        <tbody>
          <tr 
            *ngFor="let row of filteredData; let i = index"
            (click)="onRowSelect(row, i)"
            [class.selected]="selectedRowIndex === i">
            <td *ngFor="let column of columns">
              {{row[column.key]}}
            </td>
            <td>
              <button (click)="onRowEdit(row, i); $event.stopPropagation()">編集</button>
              <button (click)="onRowDelete(row, i); $event.stopPropagation()">削除</button>
            </td>
          </tr>
        </tbody>
      </table>
      
      <div class="pagination">
        <button 
          *ngFor="let page of pageNumbers" 
          (click)="onPageChange(page)"
          [class.active]="currentPage === page">
          {{page}}
        </button>
      </div>
    </div>
  `,
  imports: [FormsModule]
})
export class DataTableCustomComponent {
  @Input() title: string = 'データテーブル';
  @Input() data: any[] = [];
  @Input() columns: Array<{ key: string; title: string; sortable: boolean }> = [];
  @Input() tableId: string = 'default-table';
  
  @Output() tableEvent = new EventEmitter<TableEvent>();
  
  searchTerm: string = '';
  selectedRowIndex: number = -1;
  sortColumn: string = '';
  sortDirection: 'asc' | 'desc' = 'asc';
  currentPage: number = 1;
  itemsPerPage: number = 10;
  
  get filteredData(): any[] {
    let result = this.data;
    
    if (this.searchTerm) {
      result = result.filter(row =>
        this.columns.some(column =>
          String(row[column.key]).toLowerCase().includes(this.searchTerm.toLowerCase())
        )
      );
    }
    
    if (this.sortColumn) {
      result = [...result].sort((a, b) => {
        const aVal = a[this.sortColumn];
        const bVal = b[this.sortColumn];
        
        if (aVal < bVal) return this.sortDirection === 'asc' ? -1 : 1;
        if (aVal > bVal) return this.sortDirection === 'asc' ? 1 : -1;
        return 0;
      });
    }
    
    const start = (this.currentPage - 1) * this.itemsPerPage;
    return result.slice(start, start + this.itemsPerPage);
  }
  
  get pageNumbers(): number[] {
    const totalPages = Math.ceil(this.data.length / this.itemsPerPage);
    return Array.from({ length: totalPages }, (_, i) => i + 1);
  }
  
  onRowSelect(row: any, index: number) {
    this.selectedRowIndex = index;
    this.emitEvent('row_select', {
      rowIndex: index,
      rowData: row
    });
  }
  
  onRowEdit(row: any, index: number) {
    this.emitEvent('row_edit', {
      rowIndex: index,
      rowData: row
    });
  }
  
  onRowDelete(row: any, index: number) {
    this.emitEvent('row_delete', {
      rowIndex: index,
      rowData: row
    });
  }
  
  onColumnSort(columnKey: string) {
    if (this.sortColumn === columnKey) {
      this.sortDirection = this.sortDirection === 'asc' ? 'desc' : 'asc';
    } else {
      this.sortColumn = columnKey;
      this.sortDirection = 'asc';
    }
    
    this.emitEvent('column_sort', {
      columnKey,
      sortDirection: this.sortDirection
    });
  }
  
  onFilterChange() {
    this.emitEvent('filter_change', {
      filterValue: this.searchTerm
    });
  }
  
  onPageChange(pageNumber: number) {
    this.currentPage = pageNumber;
    this.emitEvent('page_change', {
      pageNumber
    });
  }
  
  private emitEvent(eventType: TableEvent['eventType'], data: TableEvent['data']) {
    const event: TableEvent = {
      eventType,
      data,
      context: {
        tableId: this.tableId,
        timestamp: new Date(),
        userAgent: navigator.userAgent
      }
    };
    
    this.tableEvent.emit(event);
  }
}
```

### 3. ワークフローカスタムイベント
```typescript
// workflow-custom.component.ts
interface WorkflowEvent {
  workflowId: string;
  stepId: string;
  action: 'start' | 'complete' | 'skip' | 'error' | 'retry';
  data: any;
  metadata: {
    timestamp: Date;
    userId: string;
    previousStep?: string;
    nextStep?: string;
    errorDetails?: {
      code: string;
      message: string;
      stack?: string;
    };
  };
}

@Component({
  selector: 'app-workflow-custom',
  standalone: true,
  template: `
    <div class="workflow">
      <h3>{{title}}</h3>
      
      <div class="workflow-progress">
        <div 
          *ngFor="let step of workflowSteps; let i = index"
          class="workflow-step"
          [class.completed]="i < currentStepIndex"
          [class.current]="i === currentStepIndex"
          [class.error]="step.error">
          <span class="step-number">{{i + 1}}</span>
          <span class="step-name">{{step.name}}</span>
          <span *ngIf="step.error" class="error-indicator">⚠️</span>
        </div>
      </div>
      
      <div class="current-step">
        <h4>{{currentStep?.name}}</h4>
        <p>{{currentStep?.description}}</p>
        
        <div class="step-actions">
          <button (click)="startStep()" [disabled]="!canStartStep">開始</button>
          <button (click)="completeStep()" [disabled]="!canCompleteStep">完了</button>
          <button (click)="skipStep()" [disabled]="!canSkipStep">スキップ</button>
          <button (click)="retryStep()" [disabled]="!canRetryStep">リトライ</button>
        </div>
      </div>
      
      <div class="workflow-actions">
        <button (click)="startWorkflow()">ワークフロー開始</button>
        <button (click)="resetWorkflow()">リセット</button>
      </div>
    </div>
  `
})
export class WorkflowCustomComponent {
  @Input() title: string = 'ワークフロー';
  @Input() workflowId: string = 'default-workflow';
  @Input() userId: string = 'anonymous';
  
  @Output() workflowEvent = new EventEmitter<WorkflowEvent>();
  
  workflowSteps = [
    { id: 'step1', name: 'データ入力', description: '必要なデータを入力してください', completed: false, error: false },
    { id: 'step2', name: '検証', description: 'データの検証を行います', completed: false, error: false },
    { id: 'step3', name: '処理実行', description: 'データを処理します', completed: false, error: false },
    { id: 'step4', name: '完了', description: '処理が完了しました', completed: false, error: false }
  ];
  
  currentStepIndex = 0;
  workflowStarted = false;
  
  get currentStep() {
    return this.workflowSteps[this.currentStepIndex];
  }
  
  get canStartStep(): boolean {
    return this.workflowStarted && !this.currentStep.completed && !this.currentStep.error;
  }
  
  get canCompleteStep(): boolean {
    return this.workflowStarted && !this.currentStep.completed && !this.currentStep.error;
  }
  
  get canSkipStep(): boolean {
    return this.workflowStarted && this.currentStepIndex < this.workflowSteps.length - 1;
  }
  
  get canRetryStep(): boolean {
    return this.workflowStarted && this.currentStep.error;
  }
  
  startWorkflow() {
    this.workflowStarted = true;
    this.currentStepIndex = 0;
    
    this.emitEvent('start', 'workflow', {
      workflowId: this.workflowId
    });
  }
  
  startStep() {
    this.emitEvent('start', this.currentStep.id, {
      stepId: this.currentStep.id
    });
  }
  
  completeStep() {
    this.currentStep.completed = true;
    this.currentStep.error = false;
    
    this.emitEvent('complete', this.currentStep.id, {
      stepId: this.currentStep.id,
      nextStep: this.workflowSteps[this.currentStepIndex + 1]?.id
    });
    
    this.moveToNextStep();
  }
  
  skipStep() {
    this.emitEvent('skip', this.currentStep.id, {
      stepId: this.currentStep.id,
      nextStep: this.workflowSteps[this.currentStepIndex + 1]?.id
    });
    
    this.moveToNextStep();
  }
  
  retryStep() {
    this.currentStep.error = false;
    
    this.emitEvent('retry', this.currentStep.id, {
      stepId: this.currentStep.id
    });
  }
  
  resetWorkflow() {
    this.workflowStarted = false;
    this.currentStepIndex = 0;
    
    this.workflowSteps.forEach(step => {
      step.completed = false;
      step.error = false;
    });
  }
  
  private moveToNextStep() {
    if (this.currentStepIndex < this.workflowSteps.length - 1) {
      this.currentStepIndex++;
    }
  }
  
  private emitEvent(action: WorkflowEvent['action'], stepId: string, data: any) {
    const event: WorkflowEvent = {
      workflowId: this.workflowId,
      stepId,
      action,
      data,
      metadata: {
        timestamp: new Date(),
        userId: this.userId,
        previousStep: this.workflowSteps[this.currentStepIndex - 1]?.id,
        nextStep: this.workflowSteps[this.currentStepIndex + 1]?.id
      }
    };
    
    this.workflowEvent.emit(event);
  }
}
```

### 4. リアルタイム通知カスタムイベント
```typescript
// notification-custom.component.ts
interface NotificationEvent {
  notificationId: string;
  type: 'info' | 'success' | 'warning' | 'error';
  title: string;
  message: string;
  actions: Array<{
    label: string;
    action: string;
    data?: any;
  }>;
  metadata: {
    timestamp: Date;
    priority: 'low' | 'medium' | 'high';
    category: string;
    autoClose?: boolean;
    duration?: number;
  };
}

@Component({
  selector: 'app-notification-custom',
  standalone: true,
  template: `
    <div class="notification-system">
      <h3>{{title}}</h3>
      
      <div class="notification-controls">
        <button (click)="showInfoNotification()">情報通知</button>
        <button (click)="showSuccessNotification()">成功通知</button>
        <button (click)="showWarningNotification()">警告通知</button>
        <button (click)="showErrorNotification()">エラー通知</button>
      </div>
      
      <div class="notification-history">
        <h4>通知履歴</h4>
        <div *ngFor="let notification of notifications" class="notification-item" [class]="notification.type">
          <h5>{{notification.title}}</h5>
          <p>{{notification.message}}</p>
          <div class="notification-actions">
            <button 
              *ngFor="let action of notification.actions"
              (click)="handleNotificationAction(notification, action)">
              {{action.label}}
            </button>
          </div>
          <small>{{notification.metadata.timestamp | date:'short'}}</small>
        </div>
      </div>
    </div>
  `
})
export class NotificationCustomComponent {
  @Input() title: string = '通知システム';
  
  @Output() notificationEvent = new EventEmitter<NotificationEvent>();
  
  notifications: NotificationEvent[] = [];
  
  showInfoNotification() {
    this.emitNotification('info', '情報', 'これは情報通知です', [
      { label: '詳細', action: 'show_details' },
      { label: '閉じる', action: 'close' }
    ]);
  }
  
  showSuccessNotification() {
    this.emitNotification('success', '成功', '操作が正常に完了しました', [
      { label: 'OK', action: 'acknowledge' }
    ]);
  }
  
  showWarningNotification() {
    this.emitNotification('warning', '警告', '注意が必要な状況です', [
      { label: '確認', action: 'confirm' },
      { label: '無視', action: 'ignore' }
    ]);
  }
  
  showErrorNotification() {
    this.emitNotification('error', 'エラー', 'エラーが発生しました', [
      { label: '再試行', action: 'retry', data: { attempt: 1 } },
      { label: 'キャンセル', action: 'cancel' }
    ]);
  }
  
  handleNotificationAction(notification: NotificationEvent, action: NotificationEvent['actions'][0]) {
    // 通知アクションの処理
    console.log('通知アクション:', action);
    
    if (action.action === 'close' || action.action === 'acknowledge') {
      this.removeNotification(notification.notificationId);
    }
  }
  
  private emitNotification(
    type: NotificationEvent['type'],
    title: string,
    message: string,
    actions: NotificationEvent['actions']
  ) {
    const notification: NotificationEvent = {
      notificationId: this.generateNotificationId(),
      type,
      title,
      message,
      actions,
      metadata: {
        timestamp: new Date(),
        priority: this.getPriorityByType(type),
        category: 'user-notification',
        autoClose: type === 'success',
        duration: type === 'success' ? 3000 : undefined
      }
    };
    
    this.notifications.unshift(notification);
    
    // 履歴の最大数を制限
    if (this.notifications.length > 10) {
      this.notifications.pop();
    }
    
    this.notificationEvent.emit(notification);
  }
  
  private removeNotification(notificationId: string) {
    this.notifications = this.notifications.filter(n => n.notificationId !== notificationId);
  }
  
  private generateNotificationId(): string {
    return `notification_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }
  
  private getPriorityByType(type: NotificationEvent['type']): NotificationEvent['metadata']['priority'] {
    switch (type) {
      case 'error': return 'high';
      case 'warning': return 'medium';
      case 'success':
      case 'info': return 'low';
      default: return 'low';
    }
  }
}
```

## ベストプラクティス

1. **型安全性**: TypeScriptの型システムを活用したカスタムイベント定義
2. **一貫性**: 統一されたイベント構造と命名規則
3. **拡張性**: 新しいイベントタイプの追加が容易な設計
4. **ドキュメント**: カスタムイベントの用途とデータ形式の明確な文書化

## 注意点

- カスタムイベントの構造は慎重に設計する
- イベントの種類が多くなりすぎないよう注意
- 親コンポーネントでのイベント処理の複雑さを考慮

## 関連技術
- EventEmitter
- カスタムイベント
- TypeScript型定義
- イベント設計
