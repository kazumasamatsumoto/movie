# #119 「Input/Output のデバッグ方法」

## 概要
Angular v20におけるInput/Outputのデバッグ手法。Angular DevToolsとコンソールログを活用して、データの流れを可視化し、問題の特定と解決を迅速に行う方法を学ぶ。

## 学習目標
- Angular DevToolsの基本的な使い方を理解する
- Input/Outputの値の変更を監視する方法を学ぶ
- デバッグ手法を活用した問題解決を把握する

## 技術ポイント
- Angular DevToolsの活用
- ngOnChanges()での値の変更監視
- テンプレートでのデバッグ出力
- コンソールログによる値の確認

## 📺 画面表示用コード

### デバッグ用コンポーネント
```typescript
@Component({
  selector: 'app-debug-component',
  template: `
    <div>
      <h3>デバッグ情報</h3>
      <p>Input値: {{ inputValue }}</p>
      <p>変更回数: {{ changeCount }}</p>
      <button (click)="emitEvent()">イベント送信</button>
    </div>
  `
})
export class DebugComponent implements OnChanges {
  @Input() inputValue: string = '';
  @Output() debugEvent = new EventEmitter<string>();
  
  changeCount = 0;

  ngOnChanges(changes: SimpleChanges) {
    console.log('Input変更:', changes);
    this.changeCount++;
    
    if (changes['inputValue']) {
      console.log('新しい値:', changes['inputValue'].currentValue);
    }
  }

  emitEvent() {
    const eventData = `Event at ${new Date().toISOString()}`;
    console.log('イベント送信:', eventData);
    this.debugEvent.emit(eventData);
  }
}
```

### テンプレートでのデバッグ
```typescript
@Component({
  template: `
    <!-- デバッグ用の表示 -->
    <div style="background: #f0f0f0; padding: 10px; margin: 10px;">
      <h4>デバッグ情報</h4>
      <p>現在の値: {{ currentValue }}</p>
      <p>JSON: {{ currentValue | json }}</p>
    </div>
    
    <app-debug-component 
      [inputValue]="currentValue"
      (debugEvent)="onDebugEvent($event)">
    </app-debug-component>
  `
})
export class ParentComponent {
  currentValue = 'Initial Value';

  onDebugEvent(event: string) {
    console.log('親でイベント受信:', event);
  }
}
```

## 実践的な活用例
- フォームデータの流れの確認
- 複雑なコンポーネント階層のデバッグ
- パフォーマンス問題の特定

## ベストプラクティス
- 開発時のみデバッグコードを含める
- 本番環境ではデバッグコードを削除する
- 適切なログレベルを使用する
- Angular DevToolsを活用する

## 注意点
- デバッグコードが本番環境に含まれないよう注意する
- 大量のログ出力はパフォーマンスに影響する
- 機密情報をログに出力しない

## 関連技術
- Angular DevTools
- デバッグ手法
- ログ出力
- 開発者ツール
