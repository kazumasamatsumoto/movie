# #124 「SignalOutput - signal() ベース出力」

## 概要
Angular v20の新機能であるSignalOutputの実装方法。signal()ベースの出力プロパティにより、Signalの変更を親コンポーネントに通知し、リアクティブな通信を実現する効率的な出力システムを学ぶ。

## 学習目標
- SignalOutputの基本的な使い方を理解する
- 従来の@Output()との違いを把握する
- Signalとの連携による効率的な実装を学ぶ

## 技術ポイント
- output() 関数によるSignalOutputの実装
- Signalの変更通知
- リアクティブな通信パターン
- 型安全性の向上

## 📺 画面表示用コード

### SignalOutput の実装
```typescript
@Component({
  selector: 'app-signal-output',
  template: `
    <div>
      <input [(ngModel)]="inputValue">
      <button (click)="updateData()">更新</button>
      <button (click)="resetData()">リセット</button>
    </div>
  `
})
export class SignalOutputComponent {
  inputValue = '';
  
  // SignalOutput の定義
  dataChanged = output<string>();
  dataReset = output<void>();
  
  private _data = signal<string>('');
  data = this._data.asReadonly();
  
  updateData() {
    this._data.set(this.inputValue);
    this.dataChanged.emit(this.inputValue);
  }
  
  resetData() {
    this.inputValue = '';
    this._data.set('');
    this.dataReset.emit();
  }
}
```

### 使用例
```typescript
@Component({
  template: `
    <app-signal-output 
      (dataChanged)="onDataChanged($event)"
      (dataReset)="onDataReset()">
    </app-signal-output>
    
    <div *ngIf="receivedData()">
      受信データ: {{ receivedData() }}
    </div>
  `
})
export class ParentComponent {
  private _receivedData = signal<string>('');
  receivedData = this._receivedData.asReadonly();
  
  onDataChanged(data: string) {
    this._receivedData.set(data);
  }
  
  onDataReset() {
    this._receivedData.set('');
  }
}
```

## 実践的な活用例
- リアルタイムデータ更新
- フォーム状態の管理
- 動的なUI制御

## ベストプラクティス
- Signalとの連携を活用する
- 適切なイベント名を使用する
- 型安全性を保つ
- 不要な通知を避ける

## 注意点
- SignalOutputはAngular v20の新機能
- 従来の@Output()との互換性を考慮する
- パフォーマンスを考慮した実装

## 関連技術
- Signal
- output()
- リアクティブプログラミング
- イベント処理
