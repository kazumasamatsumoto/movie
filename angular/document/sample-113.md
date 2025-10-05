# #113 「親子間通信のベストプラクティス」

## 概要
Angular v20における親子コンポーネント間通信の推奨パターンとベストプラクティス。明確な責任分離とデータフローの設計により、保守性の高いコンポーネント設計を実現する。

## 学習目標
- 親子間通信の責任分離パターンを理解する
- データフローの設計原則を把握する
- 保守性の高いコンポーネント設計を学ぶ

## 技術ポイント
- 一方向データフロー
- 責任分離の原則
- イミュータブルなデータ操作
- 明確なインターフェース設計

## 📺 画面表示用コード

### 推奨パターン
```typescript
@Component({
  selector: 'app-todo-item',
  template: `
    <div [class.completed]="todo.completed">
      {{ todo.title }}
      <button (click)="toggleComplete()">完了</button>
    </div>
  `
})
export class TodoItemComponent {
  @Input() todo!: Todo;
  @Output() todoChange = new EventEmitter<Todo>();

  toggleComplete() {
    const updatedTodo = { ...this.todo, completed: !this.todo.completed };
    this.todoChange.emit(updatedTodo);
  }
}
```

### 親コンポーネント
```typescript
@Component({
  template: `
    <app-todo-item 
      *ngFor="let todo of todos"
      [todo]="todo"
      (todoChange)="updateTodo($event)">
    </app-todo-item>
  `
})
export class TodoListComponent {
  todos: Todo[] = [];

  updateTodo(updatedTodo: Todo) {
    this.todos = this.todos.map(todo => 
      todo.id === updatedTodo.id ? updatedTodo : todo
    );
  }
}
```

## 実践的な活用例
- タスク管理アプリケーション
- 商品リストの編集機能
- ユーザープロフィールの更新

## ベストプラクティス
- @Input()は読み取り専用として扱う
- データの変更は親コンポーネントで行う
- イミュータブルなデータ操作を心がける
- 明確な型定義を使用する

## 注意点
- 子コンポーネントで@Input()プロパティを直接変更しない
- 大量のデータを@Input()で渡す場合はパフォーマンスを考慮する
- 循環参照を避ける

## 関連技術
- コンポーネント設計パターン
- データフロー設計
- 状態管理
- イミュータブルプログラミング
