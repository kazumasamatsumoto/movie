# #104 「@Output() - 子から親へイベント通知」

## 概要
Angular v20における@Output()デコレータの基本概念を学びます。子コンポーネントから親コンポーネントへのイベント通知の仕組みと、EventEmitterを使用した安全なイベント通信について解説します。

## 学習目標
- @Output()デコレータの基本的な使用方法を理解する
- 子から親へのイベント通知の仕組みを把握する
- EventEmitterを使用した安全なイベント通信を習得する

## 📺 画面表示用コード

```typescript
// 子コンポーネント
@Component({
  selector: 'app-child',
  standalone: true,
  template: `
    <button (click)="sendMessage()">メッセージ送信</button>
  `
})
export class ChildComponent {
  @Output() messageEvent = new EventEmitter<string>();
  
  sendMessage() {
    this.messageEvent.emit('子コンポーネントからのメッセージ');
  }
}
```

```html
<!-- 親コンポーネント -->
<app-child (messageEvent)="onMessage($event)"></app-child>
```

```typescript
// 親コンポーネント
@Component({
  selector: 'app-parent',
  standalone: true,
  imports: [ChildComponent],
  template: `
    <h2>親コンポーネント</h2>
    <p>受信メッセージ: {{receivedMessage}}</p>
    <app-child (messageEvent)="onMessage($event)"></app-child>
  `
})
export class ParentComponent {
  receivedMessage = '';
  
  onMessage(message: string) {
    this.receivedMessage = message;
  }
}
```

## 技術ポイント

### 1. @Output()デコレータの基本
@Output()デコレータは、子コンポーネントから親コンポーネントにイベントを送信するためのAngularの機能です。EventEmitterと組み合わせて使用します。

### 2. 基本的な構文
```typescript
@Output() eventName = new EventEmitter<DataType>();
```
- `eventName`: イベント名
- `DataType`: 送信するデータの型
- `EventEmitter`: イベント発火のためのクラス

### 3. イベントの発火と受信
```typescript
// 子コンポーネントで発火
this.eventName.emit(data);

// 親コンポーネントで受信
(eventName)="onEvent($event)"
```

## 実践的な活用例

### 1. 基本的なイベント通知
```typescript
// counter.component.ts
@Component({
  selector: 'app-counter',
  standalone: true,
  template: `
    <div class="counter">
      <button (click)="decrement()">-</button>
      <span>{{count}}</span>
      <button (click)="increment()">+</button>
    </div>
  `
})
export class CounterComponent {
  @Input() count: number = 0;
  @Output() countChange = new EventEmitter<number>();
  
  increment() {
    this.count++;
    this.countChange.emit(this.count);
  }
  
  decrement() {
    this.count--;
    this.countChange.emit(this.count);
  }
}
```

```typescript
// parent.component.ts
@Component({
  selector: 'app-parent',
  standalone: true,
  imports: [CounterComponent],
  template: `
    <h2>カウンター: {{currentCount}}</h2>
    <app-counter 
      [count]="currentCount"
      (countChange)="onCountChange($event)">
    </app-counter>
  `
})
export class ParentComponent {
  currentCount = 0;
  
  onCountChange(newCount: number) {
    this.currentCount = newCount;
    console.log('カウントが変更されました:', newCount);
  }
}
```

### 2. データ付きイベント通知
```typescript
// user-form.component.ts
interface UserFormData {
  name: string;
  email: string;
  age: number;
}

@Component({
  selector: 'app-user-form',
  standalone: true,
  imports: [FormsModule],
  template: `
    <form (ngSubmit)="onSubmit()">
      <input [(ngModel)]="formData.name" name="name" placeholder="名前" required>
      <input [(ngModel)]="formData.email" name="email" placeholder="メール" required>
      <input [(ngModel)]="formData.age" name="age" placeholder="年齢" type="number" required>
      <button type="submit">送信</button>
      <button type="button" (click)="onCancel()">キャンセル</button>
    </form>
  `
})
export class UserFormComponent {
  @Output() formSubmit = new EventEmitter<UserFormData>();
  @Output() formCancel = new EventEmitter<void>();
  
  formData: UserFormData = {
    name: '',
    email: '',
    age: 0
  };
  
  onSubmit() {
    if (this.isValid()) {
      this.formSubmit.emit(this.formData);
    }
  }
  
  onCancel() {
    this.formCancel.emit();
  }
  
  private isValid(): boolean {
    return this.formData.name && this.formData.email && this.formData.age > 0;
  }
}
```

### 3. 複数イベントの管理
```typescript
// todo-item.component.ts
interface TodoItem {
  id: number;
  text: string;
  completed: boolean;
}

@Component({
  selector: 'app-todo-item',
  standalone: true,
  template: `
    <div class="todo-item" [class.completed]="todo.completed">
      <input 
        type="checkbox" 
        [checked]="todo.completed"
        (change)="onToggle()">
      <span>{{todo.text}}</span>
      <button (click)="onEdit()">編集</button>
      <button (click)="onDelete()">削除</button>
    </div>
  `
})
export class TodoItemComponent {
  @Input() todo!: TodoItem;
  @Output() toggle = new EventEmitter<TodoItem>();
  @Output() edit = new EventEmitter<TodoItem>();
  @Output() delete = new EventEmitter<TodoItem>();
  
  onToggle() {
    const updatedTodo = { ...this.todo, completed: !this.todo.completed };
    this.toggle.emit(updatedTodo);
  }
  
  onEdit() {
    this.edit.emit(this.todo);
  }
  
  onDelete() {
    this.delete.emit(this.todo);
  }
}
```

### 4. カスタムイベントの実装
```typescript
// custom-event.component.ts
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
  @Input() itemData: any = {};
  
  triggerSave() {
    this.emitEvent('save', this.itemData);
  }
  
  triggerDelete() {
    this.emitEvent('delete', this.itemData);
  }
  
  triggerUpdate() {
    this.emitEvent('update', this.itemData);
  }
  
  private emitEvent(type: 'save' | 'delete' | 'update', data: any) {
    const eventData: CustomEventData = {
      type,
      data,
      timestamp: new Date()
    };
    this.customEvent.emit(eventData);
  }
}
```

## ベストプラクティス

1. **型安全性**: EventEmitterに適切な型を指定
2. **明確な命名**: イベント名を明確で意味のあるものにする
3. **単一責任**: 各イベントは単一の責任を持つ
4. **ドキュメント**: イベントの用途とデータ形式を文書化

## 注意点

- イベント名はキャメルケースで記述し、動詞を含める
- 大量のデータを送信する場合は、パフォーマンスを考慮する
- イベントの発火頻度に注意し、必要以上に頻繁に発火しないようにする

## 関連技術
- EventEmitter
- イベントバインディング
- コンポーネント通信
- カスタムイベント
