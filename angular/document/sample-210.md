# #210 「モーダル Component での活用例」

## 概要
Angular v20のコンテンツ投影を活用したモーダルコンポーネントの実装例を学習します。

## 学習目標
- モーダルコンポーネントでのコンテンツ投影パターンを理解する
- 構造化されたモーダル設計を習得する
- 実践的なモーダルアプリケーションを実現できるようになる

## 技術ポイント
- モーダルコンポーネント設計
- 構造化投影
- モーダル管理

## 📺 画面表示用コード

```html
<!-- 親コンポーネント -->
<app-modal [isOpen]="showModal" (close)="closeModal()">
  <div class="modal-header">
    <h2>確認</h2>
    <button class="close-btn" (click)="closeModal()">×</button>
  </div>
  <div class="modal-body">
    <p>この操作を実行しますか？</p>
    <div class="warning">
      <i class="icon">⚠️</i>
      <span>この操作は取り消せません</span>
    </div>
  </div>
  <div class="modal-footer">
    <button class="btn-secondary" (click)="closeModal()">キャンセル</button>
    <button class="btn-primary" (click)="confirmAction()">実行</button>
  </div>
</app-modal>
```

```html
<!-- 子コンポーネント（app-modal） -->
<div class="modal-overlay" [class.open]="isOpen" (click)="onOverlayClick($event)">
  <div class="modal-container" (click)="$event.stopPropagation()">
    <div class="modal-header">
      <ng-content select=".modal-header"></ng-content>
    </div>
    <div class="modal-body">
      <ng-content select=".modal-body"></ng-content>
    </div>
    <div class="modal-footer">
      <ng-content select=".modal-footer"></ng-content>
    </div>
  </div>
</div>
```

```html
<!-- 使用例 -->
<app-modal [isOpen]="showFormModal">
  <div class="modal-header">
    <h2>ユーザー登録</h2>
  </div>
  <div class="modal-body">
    <form>
      <input type="text" placeholder="名前">
      <input type="email" placeholder="メール">
    </form>
  </div>
  <div class="modal-footer">
    <button>登録</button>
  </div>
</app-modal>
```

## 実践的な活用例

```html
<!-- 画像プレビューモーダル -->
<app-modal [isOpen]="showImageModal">
  <div class="modal-header">
    <h2>画像プレビュー</h2>
  </div>
  <div class="modal-body">
    <img [src]="selectedImage" alt="プレビュー">
    <div class="image-info">
      <p>ファイル名: {{imageName}}</p>
      <p>サイズ: {{imageSize}}</p>
    </div>
  </div>
  <div class="modal-footer">
    <button>ダウンロード</button>
    <button>共有</button>
  </div>
</app-modal>
```

## ベストプラクティス
- モーダルの構造を明確に定義する
- 適切なアクセシビリティ機能を実装する
- キーボードナビゲーションをサポートする

## 注意点
- モーダルの表示/非表示制御
- フォーカス管理
- スクロール制御

## 関連技術
- Modal Management
- Accessibility (ARIA)
- Focus Management
