# #134 「ViewChild 子コンポーネント参照」

## 概要
Angular v20におけるViewChildを使った子コンポーネントへの参照取得とメソッド呼び出し。親コンポーネントから子コンポーネントの機能を直接制御し、より密接な連携を実現する方法を学ぶ。

## 学習目標
- 子コンポーネントの参照取得方法を理解する
- 子コンポーネントのメソッド呼び出しを学ぶ
- 親子間の密接な連携を把握する

## 技術ポイント
- @ViewChild(ComponentClass) での参照取得
- 子コンポーネントメソッドの呼び出し
- プロパティへのアクセス
- 適切なタイミングでの操作

## 📺 画面表示用コード

### 親コンポーネント
```typescript
@Component({
  selector: 'app-parent',
  template: `
    <app-counter #counterRef></app-counter>
    <div class="controls">
      <button (click)="increment()">増加</button>
      <button (click)="decrement()">減少</button>
      <button (click)="reset()">リセット</button>
      <button (click)="getValue()">値を取得</button>
    </div>
    <p>現在の値: {{ currentValue }}</p>
  `
})
export class ParentComponent implements AfterViewInit {
  @ViewChild('counterRef') counterComponent!: CounterComponent;
  currentValue = 0;
  
  ngAfterViewInit() {
    console.log('カウンターコンポーネントが準備完了');
  }
  
  increment() {
    this.counterComponent.increment();
    this.updateDisplayValue();
  }
  
  decrement() {
    this.counterComponent.decrement();
    this.updateDisplayValue();
  }
  
  reset() {
    this.counterComponent.reset();
    this.updateDisplayValue();
  }
  
  getValue() {
    this.currentValue = this.counterComponent.getValue();
  }
  
  private updateDisplayValue() {
    this.currentValue = this.counterComponent.getValue();
  }
}
```

### 子コンポーネント
```typescript
@Component({
  selector: 'app-counter',
  template: `
    <div class="counter">
      <h3>カウンター: {{ count }}</h3>
    </div>
  `
})
export class CounterComponent {
  count = 0;
  
  increment() {
    this.count++;
  }
  
  decrement() {
    this.count--;
  }
  
  reset() {
    this.count = 0;
  }
  
  getValue(): number {
    return this.count;
  }
}
```

## 実践的な活用例
- フォームコンポーネントの制御
- チャートコンポーネントの更新
- モーダルコンポーネントの表示制御

## ベストプラクティス
- 子コンポーネントのインターフェースを明確にする
- 適切なタイミングでメソッドを呼び出す
- エラーハンドリングを実装する

## 注意点
- 子コンポーネントの存在チェック
- ライフサイクルのタイミング
- 過度な結合を避ける

## 関連技術
- 親子コンポーネント通信
- メソッド呼び出し
- コンポーネント設計
- インターフェース設計
