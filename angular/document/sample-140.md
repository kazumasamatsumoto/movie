# #140 「ViewChild でメソッド呼び出し」

## 概要
Angular v20におけるViewChildを使った子コンポーネントのメソッド呼び出し。親コンポーネントから子コンポーネントの機能を直接制御し、密接な連携を実現する方法を学ぶ。

## 学習目標
- 子コンポーネントメソッドの呼び出し方法を理解する
- 適切なタイミングでの呼び出しを学ぶ
- エラーハンドリングを把握する

## 技術ポイント
- 子コンポーネント参照の取得
- メソッドの直接呼び出し
- パラメータの渡し方
- 戻り値の取得

## 📺 画面表示用コード

### 基本的なメソッド呼び出し
```typescript
@Component({
  selector: 'app-parent',
  template: `
    <app-child #childRef></app-child>
    <div class="controls">
      <button (click)="callChildMethods()">子メソッド呼び出し</button>
      <button (click)="getChildData()">データ取得</button>
    </div>
    <p>子からの値: {{ childValue }}</p>
  `
})
export class ParentComponent implements AfterViewInit {
  @ViewChild('childRef') childComponent!: ChildComponent;
  childValue = '';
  
  ngAfterViewInit() {
    console.log('子コンポーネント準備完了');
  }
  
  callChildMethods() {
    // パラメータなしメソッド
    this.childComponent.reset();
    
    // パラメータ付きメソッド
    this.childComponent.updateValue('親から更新');
    
    // 戻り値ありメソッド
    this.childValue = this.childComponent.getValue();
  }
  
  getChildData() {
    this.childValue = this.childComponent.getValue();
  }
}
```

### 子コンポーネント
```typescript
@Component({
  selector: 'app-child',
  template: `
    <div>値: {{ value }}</div>
    <div>カウント: {{ count }}</div>
  `
})
export class ChildComponent {
  value = '初期値';
  count = 0;
  
  updateValue(newValue: string) {
    this.value = newValue;
    this.count++;
  }
  
  reset() {
    this.value = 'リセット';
    this.count = 0;
  }
  
  getValue(): string {
    return this.value;
  }
  
  getCount(): number {
    return this.count;
  }
}
```

## 実践的な活用例
- フォームのリセット
- チャートの更新
- モーダルの制御

## ベストプラクティス
- 適切なタイミングで呼び出し
- エラーハンドリングの実装
- 明確なインターフェース設計

## 注意点
- 子コンポーネントの存在チェック
- ライフサイクルの考慮
- 過度な結合を避ける

## 関連技術
- 親子コンポーネント通信
- メソッド呼び出し
- インターフェース設計
