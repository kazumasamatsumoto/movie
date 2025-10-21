# #256 「Presentation/Container 分離」

## 概要
Presentation/Container分離は、表示ロジックとビジネスロジックを明確に区別し、コンポーネントを役割ごとに分担させる設計手法である。

## 学習目標
- Presentation/Container分離の判断基準を理解する
- ViewModelによるデータ受け渡しを実装する
- コンポーネント間の契約を型で表現する

## 技術ポイント
- ContainerはSignalとサービスを扱う
- Presentationはテンプレートとイベント通知のみ担当する
- ViewModelを介した疎結合化

## 📺 画面表示用コード（動画用）
```typescript
@Component({ selector: 'app-task-container', standalone: true, imports: [TaskListComponent], template: `<app-task-list [vm]="vm()" (toggle)="toggle($event)" />` })
export class TaskContainerComponent {
  private readonly store = inject(TaskStore);
  readonly vm = this.store.vm;
  toggle(id: string): void { this.store.toggle(id); }
}
```

```typescript
@Component({
  selector: 'app-task-list',
  standalone: true,
  template: `<ul>@for (task of vm.tasks; track task.id) {<li><label><input type="checkbox" [checked]="task.done" (change)="toggle.emit(task.id)">{{ task.title }}</label></li>}</ul>`,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class TaskListComponent {
  @Input({ required: true }) vm!: Readonly<TaskVm>;
  @Output() toggle = new EventEmitter<string>();
}
```

```typescript
export type TaskVm = {
  readonly tasks: ReadonlyArray<{ id: string; title: string; done: boolean }>;
};
```

## 💻 詳細実装例（学習用）
```typescript
@Injectable({ providedIn: 'root' })
export class TaskStore {
  private readonly tasks = signal<ReadonlyArray<Task>>([]);
  readonly vm = computed<TaskVm>(() => ({ tasks: this.tasks() }));

  load(): void {
    // API呼び出しなどでtasksを更新
  }

  toggle(id: string): void {
    this.tasks.update(list => list.map(task => task.id === id ? { ...task, done: !task.done } : task));
  }
}
```

## ベストプラクティス
- Containerはルータ・HTTP・Signal Storeを集中させ副作用を可視化する
- Presentationは`ChangeDetectionStrategy.OnPush`を設定し、副作用を持たない
- ViewModel型を共有し設計レビューでチェックする

## 注意点
- Containerが複数のPresentationを抱える場合は役割ごとに分割する
- Presentationで状態を変えない
- Outputイベントの命名をユースケース単位で揃える

## 関連技術
- Smart/Dumbパターン
- Angular Signals
- ViewModel設計
