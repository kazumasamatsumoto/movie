# #114 「深い階層の Component 通信」

## 概要
Angular v20における深い階層のコンポーネント間通信の実装方法。プロパティドリリングを避け、効率的な通信パターンを使用して保守性の高いアプリケーションを構築する。

## 学習目標
- プロパティドリリングの問題点を理解する
- 深い階層での効率的な通信方法を学ぶ
- Service、State Management、EventEmitterの使い分けを把握する

## 技術ポイント
- プロパティドリリングの回避
- Service Injectionによる状態共有
- State Managementライブラリの活用
- EventEmitterの連鎖

## 📺 画面表示用コード

### Service を使った通信
```typescript
@Injectable()
export class DataService {
  private dataSubject = new BehaviorSubject<string>('');
  data$ = this.dataSubject.asObservable();

  updateData(data: string) {
    this.dataSubject.next(data);
  }
}
```

### 深い階層のコンポーネント
```typescript
@Component({
  selector: 'app-deep-child',
  template: `<p>{{ data }}</p>`
})
export class DeepChildComponent {
  data = '';

  constructor(private dataService: DataService) {
    this.dataService.data$.subscribe(data => {
      this.data = data;
    });
  }
}
```

### 祖先コンポーネント
```typescript
@Component({
  template: `
    <app-parent>
      <app-child>
        <app-deep-child></app-deep-child>
      </app-child>
    </app-parent>
  `
})
export class AncestorComponent {
  constructor(private dataService: DataService) {}

  updateData() {
    this.dataService.updateData('Updated from ancestor');
  }
}
```

## 実践的な活用例
- 設定画面の階層構造
- ナビゲーションメニューの状態管理
- モーダルダイアログの制御

## ベストプラクティス
- 適切な通信方法を選択する
- 不要なプロパティドリリングを避ける
- Serviceの責任範囲を明確にする
- パフォーマンスを考慮した実装

## 注意点
- 過度なService依存を避ける
- メモリリークを防ぐため、Subscriptionを適切に管理する
- 循環依存を避ける

## 関連技術
- Dependency Injection
- RxJS Observable
- State Management
- コンポーネント設計パターン
