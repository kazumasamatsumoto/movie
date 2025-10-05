# #110 「@Output() 複数イベントの管理」

## 概要
Angular v20における複数の@Output()イベントの管理方法を学びます。複数のEventEmitterを効率的に管理し、整理されたイベント通信を実現する方法について解説します。

## 学習目標
- 複数の@Output()イベントの定義方法を理解する
- イベントの分類と整理方法を習得する
- 効率的な複数イベント管理パターンを身につける

## 📺 画面表示用コード

```typescript
// 複数の@Output()イベント
@Component({
  selector: 'app-multiple-events',
  standalone: true,
  template: `
    <button (click)="onSave()">保存</button>
    <button (click)="onCancel()">キャンセル</button>
    <button (click)="onDelete()">削除</button>
  `
})
export class MultipleEventsComponent {
  @Output() save = new EventEmitter<any>();
  @Output() cancel = new EventEmitter<void>();
  @Output() delete = new EventEmitter<number>();
  
  onSave() {
    this.save.emit({ data: '保存データ' });
  }
  
  onCancel() {
    this.cancel.emit();
  }
  
  onDelete() {
    this.delete.emit(123);
  }
}
```

```html
<!-- 親コンポーネントでの複数イベント処理 -->
<app-multiple-events
  (save)="onSave($event)"
  (cancel)="onCancel()"
  (delete)="onDelete($event)">
</app-multiple-events>
```

## 技術ポイント

### 1. 複数イベントの定義パターン
```typescript
// パターン1: 個別のEventEmitter
@Output() event1 = new EventEmitter<Type1>();
@Output() event2 = new EventEmitter<Type2>();
@Output() event3 = new EventEmitter<Type3>();

// パターン2: グループ化されたイベント
@Output() userEvents = new EventEmitter<UserEvent>();
@Output() dataEvents = new EventEmitter<DataEvent>();
```

### 2. イベントの分類方法
- **機能別分類**: 保存、削除、更新など
- **データ別分類**: ユーザー関連、データ関連など
- **優先度別分類**: 重要、通常、軽量など

### 3. イベント管理のベストプラクティス
- **明確な命名**: イベント名で用途が分かるようにする
- **型安全性**: 各イベントに適切な型を指定
- **ドキュメント**: イベントの用途を明確に文書化

## 実践的な活用例

### 1. フォームコンポーネントの複数イベント
```typescript
// form-actions.component.ts
interface FormAction {
  type: 'save' | 'cancel' | 'reset' | 'validate';
  data?: any;
}

@Component({
  selector: 'app-form-actions',
  standalone: true,
  template: `
    <div class="form-actions">
      <button (click)="onSave()" [disabled]="!isValid">保存</button>
      <button (click)="onCancel()">キャンセル</button>
      <button (click)="onReset()">リセット</button>
      <button (click)="onValidate()">検証</button>
    </div>
  `
})
export class FormActionsComponent {
  @Input() isValid: boolean = false;
  @Input() formData: any = {};
  
  @Output() save = new EventEmitter<any>();
  @Output() cancel = new EventEmitter<void>();
  @Output() reset = new EventEmitter<void>();
  @Output() validate = new EventEmitter<any>();
  
  onSave() {
    if (this.isValid) {
      this.save.emit(this.formData);
    }
  }
  
  onCancel() {
    this.cancel.emit();
  }
  
  onReset() {
    this.reset.emit();
  }
  
  onValidate() {
    this.validate.emit(this.formData);
  }
}
```

### 2. データテーブルの複数イベント
```typescript
// data-table.component.ts
interface TableEvent {
  type: 'select' | 'edit' | 'delete' | 'sort' | 'filter';
  data: any;
  index?: number;
}

@Component({
  selector: 'app-data-table',
  standalone: true,
  template: `
    <table>
      <thead>
        <tr>
          <th *ngFor="let column of columns" (click)="onSort(column)">
            {{column.title}}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr *ngFor="let row of data; let i = index" 
            (click)="onSelect(row, i)"
            [class.selected]="selectedIndex === i">
          <td *ngFor="let column of columns">
            {{row[column.key]}}
          </td>
          <td>
            <button (click)="onEdit(row, i)">編集</button>
            <button (click)="onDelete(row, i)">削除</button>
          </td>
        </tr>
      </tbody>
    </table>
  `
})
export class DataTableComponent {
  @Input() data: any[] = [];
  @Input() columns: any[] = [];
  @Input() selectedIndex: number = -1;
  
  @Output() select = new EventEmitter<{row: any, index: number}>();
  @Output() edit = new EventEmitter<{row: any, index: number}>();
  @Output() delete = new EventEmitter<{row: any, index: number}>();
  @Output() sort = new EventEmitter<{column: any, direction: 'asc' | 'desc'}>();
  @Output() filter = new EventEmitter<{key: string, value: any}>();
  
  onSelect(row: any, index: number) {
    this.select.emit({ row, index });
  }
  
  onEdit(row: any, index: number) {
    this.edit.emit({ row, index });
  }
  
  onDelete(row: any, index: number) {
    this.delete.emit({ row, index });
  }
  
  onSort(column: any) {
    const direction = 'asc'; // 実際の実装では現在の方向を管理
    this.sort.emit({ column, direction });
  }
}
```

### 3. モーダルコンポーネントの複数イベント
```typescript
// modal.component.ts
interface ModalEvent {
  type: 'open' | 'close' | 'confirm' | 'cancel';
  data?: any;
}

@Component({
  selector: 'app-modal',
  standalone: true,
  template: `
    <div *ngIf="isOpen" class="modal-overlay" (click)="onClose()">
      <div class="modal-content" (click)="$event.stopPropagation()">
        <div class="modal-header">
          <h3>{{title}}</h3>
          <button (click)="onClose()">×</button>
        </div>
        <div class="modal-body">
          <ng-content></ng-content>
        </div>
        <div class="modal-footer">
          <button (click)="onConfirm()">確認</button>
          <button (click)="onCancel()">キャンセル</button>
        </div>
      </div>
    </div>
  `
})
export class ModalComponent {
  @Input() isOpen: boolean = false;
  @Input() title: string = 'モーダル';
  @Input() modalData: any = {};
  
  @Output() open = new EventEmitter<void>();
  @Output() close = new EventEmitter<void>();
  @Output() confirm = new EventEmitter<any>();
  @Output() cancel = new EventEmitter<void>();
  
  onOpen() {
    this.open.emit();
  }
  
  onClose() {
    this.close.emit();
  }
  
  onConfirm() {
    this.confirm.emit(this.modalData);
  }
  
  onCancel() {
    this.cancel.emit();
  }
}
```

### 4. イベントグループ化の実装
```typescript
// event-group.component.ts
interface UserEvent {
  type: 'login' | 'logout' | 'profile_update';
  user: any;
  timestamp: Date;
}

interface DataEvent {
  type: 'create' | 'update' | 'delete';
  data: any;
  id: string;
}

@Component({
  selector: 'app-event-group',
  standalone: true,
  template: `
    <div class="event-group">
      <button (click)="triggerUserEvent('login')">ログイン</button>
      <button (click)="triggerUserEvent('logout')">ログアウト</button>
      <button (click)="triggerDataEvent('create')">データ作成</button>
      <button (click)="triggerDataEvent('update')">データ更新</button>
    </div>
  `
})
export class EventGroupComponent {
  @Input() currentUser: any = {};
  @Input() currentData: any = {};
  
  @Output() userEvents = new EventEmitter<UserEvent>();
  @Output() dataEvents = new EventEmitter<DataEvent>();
  
  triggerUserEvent(type: 'login' | 'logout' | 'profile_update') {
    const event: UserEvent = {
      type,
      user: this.currentUser,
      timestamp: new Date()
    };
    this.userEvents.emit(event);
  }
  
  triggerDataEvent(type: 'create' | 'update' | 'delete') {
    const event: DataEvent = {
      type,
      data: this.currentData,
      id: this.currentData.id || 'unknown'
    };
    this.dataEvents.emit(event);
  }
}
```

## ベストプラクティス

1. **論理的なグループ化**: 関連するイベントをグループ化
2. **一貫した命名**: イベント名の一貫性を保つ
3. **型安全性**: 各イベントに適切な型を指定
4. **ドキュメント**: イベントの用途とデータ形式を明確に文書化

## 注意点

- イベントの数が多くなりすぎないよう注意
- 関連性のないイベントを無理にグループ化しない
- 親コンポーネントでのイベントハンドリングの複雑さを考慮

## 関連技術
- EventEmitter
- イベント設計
- コンポーネント通信
- 型安全性
