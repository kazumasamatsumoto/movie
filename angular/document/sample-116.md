# #116 「兄弟 Component 間の通信」

## 概要
Angular v20における兄弟コンポーネント間の通信パターン。直接的な通信を避け、親コンポーネント経由、Service、Signal、またはState Managementライブラリを使用した効率的な通信方法を実装する。

## 学習目標
- 兄弟コンポーネント間通信の基本パターンを理解する
- 適切な通信方法の選択基準を学ぶ
- データフローの設計原則を把握する

## 技術ポイント
- 親コンポーネント経由の通信
- Service を使った状態共有
- Signal によるリアクティブな通信
- State Management ライブラリの活用

## 📺 画面表示用コード

### 親コンポーネント経由の通信
```typescript
@Component({
  template: `
    <app-sibling-a 
      [sharedData]="sharedData"
      (dataChange)="updateSharedData($event)">
    </app-sibling-a>
    <app-sibling-b [sharedData]="sharedData"></app-sibling-b>
  `
})
export class ParentComponent {
  sharedData = 'Initial Data';

  updateSharedData(newData: string) {
    this.sharedData = newData;
  }
}
```

### Signal を使った通信
```typescript
@Injectable()
export class CommunicationService {
  private _sharedData = signal('Initial Data');
  sharedData = this._sharedData.asReadonly();

  updateData(newData: string) {
    this._sharedData.set(newData);
  }
}

@Component({
  selector: 'app-sibling-a',
  template: `
    <input [(ngModel)]="inputValue">
    <button (click)="updateData()">更新</button>
  `
})
export class SiblingAComponent {
  inputValue = '';
  
  constructor(private commService: CommunicationService) {}

  updateData() {
    this.commService.updateData(this.inputValue);
  }
}
```

## 実践的な活用例
- サイドバーとメインコンテンツの連動
- フィルターとリスト表示の同期
- モーダルとフォームの状態共有

## ベストプラクティス
- 明確なデータフローを維持する
- 適切な通信方法を選択する
- 不要な依存関係を避ける
- 型安全性を保つ

## 注意点
- 直接的なコンポーネント参照を避ける
- 循環依存を防ぐ
- パフォーマンスを考慮した実装

## 関連技術
- コンポーネント通信パターン
- Signal
- State Management
- データフロー設計
