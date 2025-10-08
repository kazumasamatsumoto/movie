# #151 「ViewChild vs ContentChild 使い分け」

## 概要
`@ViewChild`と`@ContentChild`の違いを整理し、どのようなシナリオで使い分けるべきかを学びます。

## 学習目標
- ViewChildとContentChildの適用範囲を理解する
- コンポーネント構造に応じた参照手法を選択できるようにする
- ライフサイクルフックとの対応関係を把握する

## 技術ポイント
- **ViewChild**: 自コンポーネントのテンプレート内要素を参照
- **ContentChild**: 親コンポーネントから投影されたコンテンツを参照
- **ライフサイクル**: ViewChild→`ngAfterViewInit`, ContentChild→`ngAfterContentInit`

## 📺 画面表示用コード（動画用）

```typescript
@ViewChild(ChildComponent)
child?: ChildComponent;
```

```typescript
@ContentChild('header')
header?: TemplateRef<unknown>;
```

```html
<ng-content></ng-content>
```

## 💻 詳細実装例（学習用）
```typescript
// host.component.ts
import { AfterContentInit, AfterViewInit, Component, ContentChild, TemplateRef, ViewChild } from '@angular/core';
import { ChildComponent } from './child.component';

@Component({
  selector: 'app-host',
  standalone: true,
  imports: [ChildComponent],
  templateUrl: './host.component.html',
})
export class HostComponent implements AfterViewInit, AfterContentInit {
  @ViewChild(ChildComponent)
  child?: ChildComponent;

  @ContentChild('header', { read: TemplateRef })
  header?: TemplateRef<unknown>;

  ngAfterViewInit(): void {
    this.child?.refresh();
  }

  ngAfterContentInit(): void {
    if (!this.header) {
      console.warn('ヘッダーが投影されていません');
    }
  }
}
```

```html
<!-- host.component.html -->
<app-child></app-child>
<section>
  <ng-container
    *ngIf="header"
    [ngTemplateOutlet]="header"
  ></ng-container>
</section>
<ng-content></ng-content>
```

```html
<!-- parent.component.html -->
<app-host>
  <ng-template #header>
    <h3>投影ヘッダー</h3>
  </ng-template>
  <p>本文コンテンツ</p>
</app-host>
```

## ベストプラクティス
- ViewChildは自分のテンプレート、ContentChildは親からの投影という役割を明確にして選ぶ
- ライフサイクルフックを適切に使い分け、参照が利用可能なタイミングで操作する
- APIドキュメントで参照方法を指定し、親コンポーネントに必要な情報を提供する

## 注意点
- ContentChildにアクセスする前にテンプレート側で`ngAfterContentInit`が呼ばれることを確認する
- ViewChildとContentChildを混在させると複雑になるため、責務を分割する
- 参照が未提供の場合に備え、フォールバックやnullチェックを徹底する

## 関連技術
- `@ViewChildren` / `@ContentChildren`
- コンテンツプロジェクション（`ng-content`）
- Angularライフサイクルフック
