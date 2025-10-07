# #020 「Component のデバッグ方法」

## 概要
Componentの問題を効率的にデバッグする方法を学びます。Angular DevTools、console.log、ブレークポイントなど様々な手法を理解します。

## 学習目標
- Angular DevToolsの使い方を習得する
- 効果的なログ出力方法を学ぶ
- デバッグツールを使いこなす

## 技術ポイント
- **Angular DevTools**: Component階層・状態の可視化
- **console.log**: 値の確認
- **ブレークポイント**: 実行の一時停止

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
// console.logでデバッグ
ngOnInit() {
  console.log('Component initialized');
  console.log('User:', this.user);
}

onClick() {
  console.log('Button clicked');
}
```

```typescript
// ライフサイクルフックで確認
ngOnChanges(changes: SimpleChanges) {
  console.log('Changes:', changes);
}

ngAfterViewInit() {
  console.log('View initialized');
}
```

```typescript
// エラーハンドリング
try {
  this.processData();
} catch (error) {
  console.error('Error:', error);
}
```

## 💻 詳細実装例（学習用）

### 1. Angular DevToolsの使用
```typescript
// Chrome拡張機能をインストール
// 1. Chrome Web Storeで "Angular DevTools" を検索
// 2. インストール
// 3. 開発者ツールで "Angular" タブを開く

// Component階層の確認
@Component({
  selector: 'app-user-list',
  template: `
    <div *ngFor="let user of users">
      <app-user-card [user]="user"></app-user-card>
    </div>
  `
})
export class UserListComponent {
  users = [/* データ */];

  // DevToolsで users の値を確認できる
}
```

### 2. console.logを使ったデバッグ
```typescript
@Component({
  selector: 'app-data-display',
  template: `...`
})
export class DataDisplayComponent implements OnInit, OnChanges {
  @Input() data: any;

  ngOnInit() {
    console.log('ngOnInit called');
    console.log('Initial data:', this.data);
  }

  ngOnChanges(changes: SimpleChanges) {
    console.log('ngOnChanges called');
    console.log('Changes:', changes);
    console.log('Previous value:', changes['data'].previousValue);
    console.log('Current value:', changes['data'].currentValue);
  }

  processData() {
    console.log('Processing data...');
    console.log('Before:', this.data);

    this.data = this.transform(this.data);

    console.log('After:', this.data);
  }
}
```

### 3. ブレークポイントの使用
```typescript
@Component({
  selector: 'app-debugger-example',
  template: `<button (click)="calculate()">Calculate</button>`
})
export class DebuggerExampleComponent {
  calculate() {
    const a = 10;
    const b = 20;

    debugger;  // ここで実行が一時停止

    const result = a + b;
    console.log('Result:', result);
  }
}
```

### 4. エラーハンドリング
```typescript
@Component({
  selector: 'app-error-handler',
  template: `...`
})
export class ErrorHandlerComponent {
  async loadData() {
    try {
      const data = await this.fetchData();
      console.log('Data loaded:', data);
    } catch (error) {
      console.error('Error loading data:', error);
      // エラーの詳細情報を出力
      if (error instanceof Error) {
        console.error('Error message:', error.message);
        console.error('Stack trace:', error.stack);
      }
    }
  }

  private async fetchData() {
    throw new Error('API call failed');
  }
}
```

### 5. Performance監視
```typescript
@Component({
  selector: 'app-performance',
  template: `...`
})
export class PerformanceComponent {
  processLargeData() {
    console.time('データ処理');

    // 処理
    const result = this.heavyComputation();

    console.timeEnd('データ処理');
    console.log('Result:', result);
  }

  heavyComputation() {
    // 重い処理
    return Array(10000).fill(0).map((_, i) => i * 2);
  }
}
```

## デバッグチェックリスト

1. ✅ Angular DevToolsでComponent階層確認
2. ✅ console.logでプロパティ値確認
3. ✅ ライフサイクルフックで実行順確認
4. ✅ ブレークポイントで詳細調査
5. ✅ エラーログで問題特定

## 便利なデバッグテクニック

- `console.table()`: 配列を表形式で表示
- `console.trace()`: スタックトレース表示
- `console.group()`: ログをグループ化
- Chrome DevTools の Network タブで通信確認

## 注意点

- 本番環境ではconsole.logを削除
- 過度なログは避ける
- エラーは適切にハンドリング
- DevToolsを常に開いて開発

## 関連技術
- Angular DevTools
- Chrome DevTools
- Error Handling
- Performance Profiling
