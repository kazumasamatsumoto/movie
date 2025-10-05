# #131 「ViewChild - 子要素への参照」

## 概要
Angular v20におけるViewChildデコレータを使った子要素への参照取得方法。親コンポーネントから子コンポーネントやDOM要素に直接アクセスし、メソッドの呼び出しやプロパティの操作を実現する。

## 学習目標
- ViewChildの基本的な使い方を理解する
- 子要素への参照取得方法を学ぶ
- ngAfterViewInitでの適切なタイミングを把握する

## 技術ポイント
- @ViewChild() デコレータの使用
- ngAfterViewInit ライフサイクルでの参照取得
- 子コンポーネントへのアクセス
- DOM要素への直接アクセス

## 📺 画面表示用コード

### 基本的なViewChildの使用
```typescript
@Component({
  selector: 'app-parent',
  template: `
    <app-child #childRef></app-child>
    <button (click)="callChildMethod()">子メソッド呼び出し</button>
  `
})
export class ParentComponent implements AfterViewInit {
  @ViewChild('childRef') childComponent!: ChildComponent;
  
  ngAfterViewInit() {
    console.log('子コンポーネント:', this.childComponent);
  }
  
  callChildMethod() {
    this.childComponent.someMethod();
  }
}
```

### 子コンポーネント
```typescript
@Component({
  selector: 'app-child',
  template: `<div>子コンポーネント</div>`
})
export class ChildComponent {
  someMethod() {
    console.log('子コンポーネントのメソッドが呼ばれました');
  }
}
```

## 実践的な活用例
- フォームのリセット機能
- モーダルの表示制御
- チャートの更新制御

## ベストプラクティス
- ngAfterViewInit以降で参照を使用する
- 適切な型定義を行う
- エラーハンドリングを実装する

## 注意点
- 動的要素はngOnInitでは未初期化
- 参照が存在しない場合のチェックが必要
- ライフサイクルを理解して適切なタイミングで使用

## 関連技術
- コンポーネントライフサイクル
- 親子コンポーネント通信
- DOM操作
- TypeScript型定義
