# #207 「ContentChild での投影取得」

## 概要
Angular v20の@ContentChildデコレーターを使用して投影されたコンテンツにアクセスする方法を学習します。

## 学習目標
- @ContentChildデコレーターの使用方法を理解する
- 投影コンテンツへのアクセス方法を習得する
- 投影コンテンツとの双方向通信を実現できるようになる

## 技術ポイント
- @ContentChildデコレーター
- 投影コンテンツアクセス
- 双方向通信

## 📺 画面表示用コード

```html
<!-- 親コンポーネント -->
<app-content-accessor>
  <div #projectedContent class="custom-content">
    <h3>投影されたコンテンツ</h3>
    <p>ContentChildでアクセス可能</p>
  </div>
</app-content-accessor>
```

```html
<!-- 子コンポーネント（app-content-accessor） -->
<div class="accessor-container">
  <ng-content></ng-content>
  <button (click)="toggleContent()">コンテンツ切り替え</button>
</div>
```

```typescript
// 子コンポーネントクラス
export class ContentAccessorComponent implements AfterContentInit {
  @ContentChild('projectedContent') projectedContent!: ElementRef;
  
  ngAfterContentInit() {
    console.log('投影コンテンツ:', this.projectedContent);
  }
  
  toggleContent() {
    const element = this.projectedContent.nativeElement;
    element.style.display = element.style.display === 'none' ? 'block' : 'none';
  }
}
```

## 実践的な活用例

```html
<!-- フォームバリデーター -->
<app-form-validator>
  <input #emailInput type="email" placeholder="メールアドレス">
  <div #errorMessage class="error-message"></div>
</app-form-validator>
```

## ベストプラクティス
- 投影コンテンツの存在を確認してから操作する
- 適切なライフサイクルフックでアクセスする
- 投影コンテンツの変更を適切に検知する

## 注意点
- 投影コンテンツの初期化タイミング
- DOM操作の安全性
- メモリリークの防止

## 関連技術
- ContentChild Decorator
- ElementRef
- Template References
