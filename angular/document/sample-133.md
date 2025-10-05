# #133 「ViewChild テンプレート参照変数」

## 概要
Angular v20におけるテンプレート参照変数を使ったViewChildの実装方法。#refNameで定義したテンプレート参照変数をViewChildで参照し、DOM要素に直接アクセスする手法を学ぶ。

## 学習目標
- テンプレート参照変数の定義方法を理解する
- ViewChildでのテンプレート参照変数の使用方法を学ぶ
- DOM要素への直接アクセス方法を把握する

## 技術ポイント
- テンプレート参照変数の定義（#refName）
- @ViewChild('refName') での参照取得
- ElementRef を使ったDOMアクセス
- 型安全性の確保

## 📺 画面表示用コード

### 基本的なテンプレート参照変数
```typescript
@Component({
  selector: 'app-template-ref',
  template: `
    <input #inputRef type="text" placeholder="入力してください">
    <button (click)="focusInput()">フォーカス</button>
    <button (click)="clearInput()">クリア</button>
  `
})
export class TemplateRefComponent implements AfterViewInit {
  @ViewChild('inputRef') inputRef!: ElementRef<HTMLInputElement>;
  
  ngAfterViewInit() {
    console.log('入力要素:', this.inputRef.nativeElement);
  }
  
  focusInput() {
    this.inputRef.nativeElement.focus();
  }
  
  clearInput() {
    this.inputRef.nativeElement.value = '';
  }
}
```

### 複数のテンプレート参照変数
```typescript
@Component({
  selector: 'app-multiple-refs',
  template: `
    <div #headerRef>ヘッダー</div>
    <div #contentRef>コンテンツ</div>
    <div #footerRef>フッター</div>
    <button (click)="highlightSection('header')">ヘッダー強調</button>
    <button (click)="highlightSection('content')">コンテンツ強調</button>
  `
})
export class MultipleRefsComponent implements AfterViewInit {
  @ViewChild('headerRef') headerRef!: ElementRef;
  @ViewChild('contentRef') contentRef!: ElementRef;
  @ViewChild('footerRef') footerRef!: ElementRef;
  
  ngAfterViewInit() {
    // 参照の初期化確認
    console.log('すべての参照が準備完了');
  }
  
  highlightSection(section: string) {
    const refs = {
      header: this.headerRef,
      content: this.contentRef,
      footer: this.footerRef
    };
    
    const element = refs[section as keyof typeof refs];
    if (element) {
      element.nativeElement.style.backgroundColor = 'yellow';
    }
  }
}
```

## 実践的な活用例
- フォーム要素の制御
- アニメーション要素の操作
- カスタム要素の状態管理

## ベストプラクティス
- 明確で意味のある参照名を使用する
- 適切な型定義を行う
- エラーハンドリングを実装する

## 注意点
- 参照名の重複を避ける
- ngAfterViewInit以降で使用する
- DOM操作は最小限に留める

## 関連技術
- テンプレート参照変数
- ElementRef
- DOM操作
- イベントハンドリング
