# #125 「SignalOutput vs @Output() 比較」

## 概要
Angular v20におけるSignalOutputと@Output()の比較分析。それぞれの特徴と使い分けを理解し、Signalベースの統一されたリアクティブプログラミングパターンを活用した効率的な通信を実現する。

## 学習目標
- SignalOutputと@Output()の特徴を理解する
- 適切な使い分けの基準を学ぶ
- Signalベースの統一パターンを把握する

## 技術ポイント
- SignalOutputのリアクティブ特性
- @Output()の従来的な動作
- Signalとの連携
- 統一されたリアクティブパターン

## 📺 画面表示用コード

### @Output() の実装
```typescript
@Component({
  selector: 'app-traditional-output',
  template: `
    <button (click)="sendData()">データ送信</button>
  `
})
export class TraditionalOutputComponent {
  @Output() dataSent = new EventEmitter<string>();
  
  sendData() {
    this.dataSent.emit('Traditional Data');
  }
}
```

### SignalOutput の実装
```typescript
@Component({
  selector: 'app-signal-output',
  template: `
    <button (click)="sendData()">データ送信</button>
  `
})
export class SignalOutputComponent {
  dataSent = output<string>();
  
  private _data = signal<string>('');
  data = this._data.asReadonly();
  
  sendData() {
    const newData = 'Signal Data';
    this._data.set(newData);
    this.dataSent.emit(newData);
  }
}
```

### 統一されたリアクティブパターン
```typescript
@Component({
  template: `
    <app-signal-output 
      (dataSent)="onDataSent($event)">
    </app-signal-output>
    
    <div>受信データ: {{ receivedData() }}</div>
  `
})
export class ParentComponent {
  private _receivedData = signal<string>('');
  receivedData = this._receivedData.asReadonly();
  
  onDataSent(data: string) {
    this._receivedData.set(data);
  }
  
  // Signal による自動計算
  displayData = computed(() => 
    `表示: ${this.receivedData()}`
  );
}
```

## 実践的な活用例
- Signalベースの統一された状態管理
- リアクティブなUI更新
- 効率的なデータフロー

## ベストプラクティス
- Signalベースの統一パターンを活用する
- 適切な使い分けを判断する
- パフォーマンスを考慮した実装
- チームでの統一ルールを決める

## 注意点
- SignalOutputは新機能のため、学習コストがある
- 既存コードとの互換性を考慮する
- 移行戦略を計画する

## 関連技術
- Signal
- リアクティブプログラミング
- 統一パターン
- 状態管理
