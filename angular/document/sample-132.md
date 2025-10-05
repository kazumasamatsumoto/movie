# #132 「ViewChild の基本構文」

## 概要
Angular v20におけるViewChildの基本構文とセレクタの指定方法。コンポーネントクラス、ディレクティブ、テンプレート参照変数など、様々なセレクタを使用した柔軟な要素参照の実装方法を学ぶ。

## 学習目標
- ViewChildの基本構文を理解する
- セレクタの種類と使い分けを学ぶ
- 適切なセレクタの選択方法を把握する

## 技術ポイント
- @ViewChild() の基本構文
- セレクタの種類（クラス、文字列、型）
- 適切なセレクタの選択
- 型安全性の確保

## 📺 画面表示用コード

### コンポーネントクラスでの参照
```typescript
@Component({
  selector: 'app-parent',
  template: `<app-child></app-child>`
})
export class ParentComponent implements AfterViewInit {
  @ViewChild(ChildComponent) child!: ChildComponent;
  
  ngAfterViewInit() {
    this.child.someMethod();
  }
}
```

### テンプレート参照変数での参照
```typescript
@Component({
  selector: 'app-parent',
  template: `
    <div #myDiv>テンプレート参照</div>
    <button (click)="accessElement()">要素アクセス</button>
  `
})
export class ParentComponent implements AfterViewInit {
  @ViewChild('myDiv') myDiv!: ElementRef;
  
  ngAfterViewInit() {
    console.log('要素:', this.myDiv.nativeElement);
  }
  
  accessElement() {
    this.myDiv.nativeElement.style.color = 'red';
  }
}
```

### ディレクティブでの参照
```typescript
@Component({
  selector: 'app-parent',
  template: `<div myDirective></div>`
})
export class ParentComponent implements AfterViewInit {
  @ViewChild(MyDirective) directive!: MyDirective;
  
  ngAfterViewInit() {
    this.directive.someDirectiveMethod();
  }
}
```

## 実践的な活用例
- カスタムコンポーネントの制御
- フォーム要素へのアクセス
- ディレクティブの状態管理

## ベストプラクティス
- 適切なセレクタタイプを選択する
- 型安全性を保つ
- 明確な命名規則を使用する

## 注意点
- セレクタの一意性を確保する
- 動的要素の存在チェック
- ライフサイクルのタイミング

## 関連技術
- セレクタ指定
- 型安全性
- テンプレート参照変数
- ディレクティブ
