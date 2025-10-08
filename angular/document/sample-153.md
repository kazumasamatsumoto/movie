# #153 「テンプレート参照変数のスコープ」

## 概要
テンプレート参照変数の有効範囲（スコープ）と構造ディレクティブによる影響を理解し、意図しない参照エラーを防ぐ方法を学びます。

## 学習目標
- テンプレート参照変数のスコープルールを理解する
- *ngIfやng-templateを使う場合の注意点を把握する
- 参照を別のコンポーネントに渡すパターンを習得する

## 技術ポイント
- **基本スコープ**: 同一テンプレートおよび子テンプレートで有効
- **構造ディレクティブ**: *ngIf/*ngForで生成されるテンプレートは別スコープ
- **ng-template**: `<ng-template #tmpl>`の参照は`ngTemplateOutlet`等で受け渡し可能

## 📺 画面表示用コード（動画用）

```html
<ng-template #dialog>...</ng-template>
```

```html
<ng-container *ngIf="visible; else dialog"></ng-container>
```

```html
<button #btn (click)="handle(btn)">クリック</button>
```

## 💻 詳細実装例（学習用）
```typescript
// scope-demo.component.ts
import { Component, TemplateRef, ViewChild } from '@angular/core';

@Component({
  selector: 'app-scope-demo',
  standalone: true,
  templateUrl: './scope-demo.component.html',
})
export class ScopeDemoComponent {
  visible = true;

  @ViewChild('dialogTemplate')
  dialogTemplate?: TemplateRef<unknown>;

  toggle(): void {
    this.visible = !this.visible;
  }
}
```

```html
<!-- scope-demo.component.html -->
<button type="button" (click)="toggle()">表示切替</button>

<section *ngIf="visible; else hiddenBlock">
  <p>visibleがtrueのときだけ表示されます</p>
</section>

<ng-template #hiddenBlock>
  <p>visibleがfalseのときに表示されます</p>
</ng-template>

<ng-template #dialogTemplate>
  <p>ダイアログ用テンプレート</p>
</ng-template>
```

## ベストプラクティス
- 参照を他のコンポーネントへ渡す場合は`@Input()`経由でTemplateRefを渡すとスコープ問題を避けられる
- 構造ディレクティブ内で参照したい場合は`let`変数や`as`構文を活用する
- 参照名は一意に保ち、同じテンプレート内で衝突しないようにする

## 注意点
- *ngIfで切り替わる要素に対しViewChildを使うと参照がnullになるタイミングがある
- ng-template内部で宣言した参照はそのテンプレート内でのみ有効
- DOMに存在しない状態で参照を使わないようライフサイクルを意識する

## 関連技術
- `ngTemplateOutlet`によるテンプレートの再利用
- ViewContainerRefでのテンプレート挿入
- Angular構造ディレクティブのスコープ規則
