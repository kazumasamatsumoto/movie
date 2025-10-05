# #127 「プロパティドリリングの回避」

## 概要
Angular v20におけるプロパティドリリング問題の回避手法。深い階層での不要なプロパティ受け渡しを防ぎ、Service、Context API、Signalを活用した効率的で保守性の高い通信パターンを実装する。

## 学習目標
- プロパティドリリングの問題点を理解する
- 効果的な回避手法を学ぶ
- 適切な通信方法の選択を把握する

## 技術ポイント
- Service Injection による状態共有
- Context API の活用
- Signal を使った効率的な通信
- 適切な抽象化レベル

## 📺 画面表示用コード

### プロパティドリリングの問題例
```typescript
// ❌ プロパティドリリング
@Component({
  template: `<app-child [data]="data"></app-child>`
})
export class ParentComponent {
  data = 'Parent Data';
}

@Component({
  template: `<app-grandchild [data]="data"></app-grandchild>`
})
export class ChildComponent {
  @Input() data: string = '';
}

@Component({
  template: `<div>{{ data }}</div>`
})
export class GrandchildComponent {
  @Input() data: string = '';
}
```

### Service による解決
```typescript
@Injectable()
export class DataService {
  private _data = signal<string>('');
  data = this._data.asReadonly();
  
  updateData(newData: string) {
    this._data.set(newData);
  }
}

@Component({
  template: `<button (click)="updateData()">更新</button>`
})
export class ParentComponent {
  constructor(private dataService: DataService) {}
  
  updateData() {
    this.dataService.updateData('Updated Data');
  }
}

@Component({
  template: `<div>{{ data() }}</div>`
})
export class GrandchildComponent {
  private dataService = inject(DataService);
  data = this.dataService.data;
}
```

### Context API による解決
```typescript
export interface AppContext {
  data: string;
  updateData: (data: string) => void;
}

export const APP_CONTEXT = createContext<AppContext>({
  data: '',
  updateData: () => {}
});

@Component({
  template: `
    <app-parent>
      <app-child>
        <app-grandchild></app-grandchild>
      </app-child>
    </app-parent>
  `
})
export class AppComponent {
  data = 'App Data';
  
  updateData(newData: string) {
    this.data = newData;
  }
  
  provide() {
    return {
      data: this.data,
      updateData: (data: string) => this.updateData(data)
    };
  }
}
```

## 実践的な活用例
- 深い階層のフォーム
- 設定画面の状態管理
- ナビゲーション状態の共有

## ベストプラクティス
- 適切な抽象化レベルを選択する
- Serviceの責任範囲を明確にする
- 過度な依存関係を避ける
- パフォーマンスを考慮する

## 注意点
- 解決方法のトレードオフを理解する
- 過度な抽象化を避ける
- メモリリークを防ぐ

## 関連技術
- Dependency Injection
- Context API
- Signal
- 状態管理パターン
