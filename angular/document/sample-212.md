# #212 「アコーディオン での活用例」

## 概要
Angular v20のコンテンツ投影を活用したアコーディオンコンポーネントの実装例を学習します。

## 学習目標
- アコーディオンコンポーネントでのコンテンツ投影パターンを理解する
- 構造化されたアコーディオン設計を習得する
- 実践的なアコーディオンアプリケーションを実現できるようになる

## 技術ポイント
- アコーディオンコンポーネント設計
- 構造化投影
- 展開/折りたたみ制御

## 📺 画面表示用コード

```html
<!-- 親コンポーネント -->
<app-accordion>
  <div class="accordion-header">
    <h3>セクション1</h3>
    <span class="toggle-icon">▼</span>
  </div>
  <div class="accordion-content">
    <p>セクション1のコンテンツ</p>
    <ul>
      <li>項目1</li>
      <li>項目2</li>
    </ul>
  </div>
  
  <div class="accordion-header">
    <h3>セクション2</h3>
    <span class="toggle-icon">▼</span>
  </div>
  <div class="accordion-content">
    <p>セクション2のコンテンツ</p>
    <div class="info-box">追加情報</div>
  </div>
</app-accordion>
```

```html
<!-- 子コンポーネント（app-accordion） -->
<div class="accordion">
  <div class="accordion-item" 
       *ngFor="let item of accordionItems; let i = index">
    <div class="accordion-header" 
         (click)="toggleItem(i)"
         [class.active]="item.isOpen">
      <ng-content select=".accordion-header"></ng-content>
    </div>
    <div class="accordion-content" 
         [class.open]="item.isOpen">
      <ng-content select=".accordion-content"></ng-content>
    </div>
  </div>
</div>
```

```html
<!-- 使用例 -->
<app-accordion>
  <div class="accordion-header">
    <h3>よくある質問</h3>
  </div>
  <div class="accordion-content">
    <p>質問への回答内容</p>
  </div>
</app-accordion>
```

## 実践的な活用例

```html
<!-- FAQセクション -->
<app-accordion>
  <div class="accordion-header">
    <h3>アカウントについて</h3>
  </div>
  <div class="accordion-content">
    <div class="faq-answer">
      <p>アカウント作成方法について</p>
      <ol>
        <li>メールアドレスを入力</li>
        <li>パスワードを設定</li>
        <li>確認メールを送信</li>
      </ol>
    </div>
  </div>
</app-accordion>
```

## ベストプラクティス
- アコーディオンの構造を明確に定義する
- 展開/折りたたみのアニメーションを適切に実装する
- アクセシビリティを考慮した設計を行う

## 注意点
- 複数展開の制御
- アニメーションのパフォーマンス
- キーボードナビゲーション

## 関連技術
- Accordion UI Pattern
- CSS Animations
- Accessibility (ARIA)
