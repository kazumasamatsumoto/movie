# #207 「ContentChild での投影取得」

## 概要
`@ContentChild`デコレータを用いて投影された要素やテンプレートを取得し、子コンポーネント内で利用する方法を学びます。

## 学習目標
- `@ContentChild`/`@ContentChildren`の使い分けを理解する
- TemplateRefやディレクティブインスタンスを取得して後処理する方法を習得する
- 投影コンテンツの存在チェックによるフォールバック実装を把握する

## 技術ポイント
- **単一取得**: `@ContentChild`で最初にマッチした要素/テンプレート/ディレクティブを取得
- **readオプション**: `read: TemplateRef`などで取得する型を指定
- **ライフサイクル**: `ngAfterContentInit`で参照が利用可能になる

## 📺 画面表示用コード（動画用）

```typescript
@ContentChild('header', { read: TemplateRef })
headerTpl?: TemplateRef<unknown>;
```

```typescript
ngAfterContentInit() {
  if (!this.headerTpl) { ... }
}
```

```typescript
@ContentChild(MyDirective) directive?: MyDirective;
```

## 💻 詳細実装例（学習用）
```typescript
// content-reader.component.ts
import { AfterContentInit, Component, ContentChild, TemplateRef } from '@angular/core';

@Component({
  selector: 'app-content-reader',
  standalone: true,
  templateUrl: './content-reader.component.html',
})
export class ContentReaderComponent implements AfterContentInit {
  @ContentChild('customHeader', { read: TemplateRef })
  headerTemplate?: TemplateRef<unknown>;

  hasHeader = false;

  ngAfterContentInit(): void {
    this.hasHeader = !!this.headerTemplate;
  }
}
```

```html
<!-- content-reader.component.html -->
<section class="content-reader">
  <ng-container *ngIf="hasHeader; else defaultHeader" [ngTemplateOutlet]="headerTemplate"></ng-container>
  <ng-template #defaultHeader>
    <h3>デフォルトヘッダー</h3>
  </ng-template>
  <ng-content></ng-content>
</section>
```

```html
<!-- parent.component.html -->
<app-content-reader>
  <ng-template #customHeader>
    <h2>投影されたテンプレート</h2>
  </ng-template>
  <p>本文コンテンツ</p>
</app-content-reader>
```

## ベストプラクティス
- `read`オプションを明示し、取得したい型（TemplateRef、ElementRef、ディレクティブなど）を指定する
- `ContentChild`で取得した参照を公開する場合は`@Input()`やgetterでラップし、安全に扱う
- フォールバック表示を用意し、投影がない場合にもコンポーネントが機能するようにする

## 注意点
- `@ContentChild`は単一の要素しか取得しない。複数ある場合は`@ContentChildren`でQueryListとして扱う
- `ngOnInit`では参照がundefinedのままなので、必ず`ngAfterContentInit`以降でアクセスする
- 投影コンテンツが変更される可能性がある場合は`ngAfterContentChecked`や`QueryList.changes`で更新を監視する

## 関連技術
- `ContentChildren`による複数投影の取得
- `TemplateRef`と`ViewContainerRef`
- `ngTemplateOutlet`によるテンプレート描画

