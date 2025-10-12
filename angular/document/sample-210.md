# #210 「モーダル Component での活用例」

## 概要
コンテンツ投影を利用して、ヘッダー・本文・アクションを柔軟に差し替えられるモーダルコンポーネントを構築する例を紹介します。

## 学習目標
- モーダル構造に合わせた複数スロット設計を理解する
- 親コンポーネントで任意の内容を差し込み、再利用できるモーダルを実装する
- 閉じるボタンやアクションのデフォルト化を行う方法を把握する

## 技術ポイント
- **スロット構成**: `[modal-header]`, `[modal-body]`, `[modal-actions]` の3スロットなど
- **Overlay**: Angular CDK Overlay等と組み合わせて表示制御が可能
- **フォールバック**: アクションがない場合のデフォルトボタンなど

## 📺 画面表示用コード（動画用）

```html
<div class="modal">
  <header class="modal__header">
    <ng-content select="[modal-header]"></ng-content>
  </header>
  <section class="modal__body">
    <ng-content select="[modal-body]"></ng-content>
  </section>
  <footer class="modal__actions">
    <ng-content select="[modal-actions]"></ng-content>
  </footer>
</div>
```

```html
<app-modal>
  <h3 modal-header>タイトル</h3>
  <p modal-body>本文</p>
  <button modal-actions>閉じる</button>
</app-modal>
```

```scss
.modal { max-width: 480px; }
```

## 💻 詳細実装例（学習用）
```typescript
// modal.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-modal',
  standalone: true,
  templateUrl: './modal.component.html',
  styleUrls: ['./modal.component.scss'],
})
export class ModalComponent {}
```

```html
<!-- modal.component.html -->
<div class="modal">
  <header class="modal__header">
    <ng-content select="[modal-header]"></ng-content>
  </header>
  <section class="modal__body">
    <ng-content select="[modal-body]"></ng-content>
  </section>
  <footer class="modal__actions">
    <ng-content select="[modal-actions]"></ng-content>
  </footer>
</div>
```

```scss
/* modal.component.scss */
.modal {
  width: min(480px, 90vw);
  padding: 24px;
  border-radius: 16px;
  background: #fff;
  display: grid;
  gap: 16px;
}
.modal__actions {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
}
```

```html
<!-- parent.component.html -->
<app-modal>
  <h3 modal-header>モーダルタイトル</h3>
  <p modal-body>モーダル本文が入ります。</p>
  <div modal-actions>
    <button class="btn-secondary">キャンセル</button>
    <button class="btn-primary">OK</button>
  </div>
</app-modal>
```

## ベストプラクティス
- アクションが省略された場合のため、`modal-actions`スロットにデフォルトボタンを用意する
- スロット名は明確にし、アクセシビリティ（`aria-labelledby`, `aria-describedby`）と連動させる
- モーダルの開閉はサービスまたは親コンポーネントが制御し、投影部分は内容に専念する

## 注意点
- 投影コンテンツが多い場合、スクロールや高さ制限を設けてレイアウト崩れを防ぐ
- モーダル外クリックやESCキー閉じなどの動作はコンテンツ投影とは別に設計する
- 多言語対応やボタンラベルなど、親が投影する箇所をドキュメントで明確にする

## 関連技術
- Angular CDK Overlay / Dialog
- `ContentChild`でアクション存在チェック
- モーダルのアクセシビリティ（フォーカストラップ等）


