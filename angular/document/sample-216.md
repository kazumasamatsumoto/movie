# #216 「コンテンツ投影のデバッグ」

## 概要
コンテンツ投影が期待通りに表示されない場合のデバッグ手法を整理し、セレクタミスや契約違反を素早く特定できるようにします。

## 学習目標
- DevToolsで投影結果を確認する手順を理解する
- `select`セレクタや`ContentChild`の値を検証する方法を習得する
- デバッグメッセージやフォールバック表示を活用して原因を追跡する

## 技術ポイント
- **DOM確認**: ブラウザDevToolsで`<ng-content>`の展開結果を確認し、セレクタがマッチしているか検証
- **ログ**: `ContentChild`が`undefined`になっていないかライフサイクルでログを出す
- **フォールバック表示**: 投影がない場合にデフォルトコンテンツを表示し、状態を可視化

## 📺 画面表示用コード（動画用）

```typescript
ngAfterContentInit() {
  console.log('header exists:', !!this.header);
}
```

```html
<p *ngIf="!hasHeader" class="debug">headerが投影されていません</p>
```

```html
<!-- DevToolsで<ng-content>展開を確認 -->
```

## 💻 詳細実装例（学習用）
```typescript
// debug-panel.component.ts
import { AfterContentInit, Component, ContentChild, ElementRef } from '@angular/core';

@Component({
  selector: 'app-debug-panel',
  standalone: true,
  templateUrl: './debug-panel.component.html',
  styleUrls: ['./debug-panel.component.scss'],
})
export class DebugPanelComponent implements AfterContentInit {
  @ContentChild('[panel-header]', { read: ElementRef })
  header?: ElementRef;

  hasHeader = false;

  ngAfterContentInit(): void {
    this.hasHeader = !!this.header;
    console.debug('panel-header exists:', this.hasHeader);
  }
}
```

```html
<!-- debug-panel.component.html -->
<article class="panel">
  <header class="panel__header">
    <ng-container *ngIf="hasHeader; else warn">
      <ng-content select="[panel-header]"></ng-content>
    </ng-container>
    <ng-template #warn>
      <p class="panel__debug">panel-header が投影されていません</p>
    </ng-template>
  </header>
  <section class="panel__body">
    <ng-content></ng-content>
  </section>
</article>
```

## ベストプラクティス
- セレクタ（クラス/属性）が正しく付与されているかコンポーネント利用者にガイドを提供する
- デバッグ時はログやフォールバック表示を有効にし、原因を視覚的に把握する
- Storybookやユニットテストで投影パターンを検証し、リグレッションを防ぐ

## 注意点
- `console.log`などのデバッグコードは開発時のみ有効にし、本番では外す
- ブラウザDevToolsで展開結果を確認する際、`ng-content`は変換済みDOMに置き換わる点を理解する
- セレクタに複雑なCSSを使うとミスマッチに気づきにくいので、シンプルな命名を心がける

## 関連技術
- コンテンツ投影のテスト（#217）
- `ContentChild` / `ContentChildren`
- Angular DevToolsでコンポーネント構造を確認


