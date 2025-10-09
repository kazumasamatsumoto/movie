# #069 「ngAfterContentChecked - コンテンツチェック後」

## 概要
投影コンテンツが変更検知されたあとに呼ばれる`ngAfterContentChecked`を利用して、内容の変化に応じた処理を実装する方法を学びます。

## 学習目標
- `ngAfterContentChecked`の呼び出しタイミングと頻度を理解する
- コンテンツの変更を検知して軽量な更新処理を行う
- パフォーマンスへの影響を考慮した条件分岐を設計する

## 技術ポイント
- **定期的な呼び出し**: 変更検知サイクルごとに実行される
- **差分検出**: `QueryList.changes`や比較ロジックで更新を判断
- **軽量化**: 処理は最小限にし、重いロジックは避ける

## 📺 画面表示用コード（動画用）
**表示ルール**: 最大3個、各10行以内、動画で見せる部分のみ

```typescript
@ContentChildren(ItemDirective) items!: QueryList<ItemDirective>;
```

```typescript
ngAfterContentChecked(): void {
  this.count = this.items.length;
}
```

```html
<ng-content></ng-content>
```

## 💻 詳細実装例（学習用）
```typescript
import { AfterContentChecked, AfterContentInit, Component, ContentChildren, Directive, QueryList } from '@angular/core';

@Directive({
  selector: '[appTab]',
  standalone: true,
})
export class TabDirective {
  constructor(public readonly el: ElementRef<HTMLElement>) {}
}

@Component({
  selector: 'app-tab-group',
  standalone: true,
  templateUrl: './tab-group.component.html',
})
export class TabGroupComponent implements AfterContentInit, AfterContentChecked {
  @ContentChildren(TabDirective) tabs!: QueryList<TabDirective>;
  tabCount = 0;

  ngAfterContentInit(): void {
    this.updateCount();
  }

  ngAfterContentChecked(): void {
    this.updateCount();
  }

  private updateCount(): void {
    const next = this.tabs?.length ?? 0;
    if (next !== this.tabCount) {
      this.tabCount = next;
    }
  }
}
```

```html
<div class="tab-group">
  <ng-content select="[appTab]"></ng-content>
</div>
<p>タブ数: {{ tabCount }}</p>
```

## ベストプラクティス
- 初回処理は`ngAfterContentInit`で行い、`ngAfterContentChecked`では差分がある場合のみ更新する
- `QueryList.changes`Observableを購読すると必要なタイミングだけ処理できる
- 重い処理はサービスに委譲し、フックでは状態の更新だけ行う

## 注意点
- タブ数のような単純な統計でも毎回計算すると負荷が高くなるので、差分比較を導入する
- コンテンツの変更をトリガーにDOM操作をすると、さらに変更検知が走る点に注意
- `ngAfterContentChecked`内でSignal更新を行うと無限ループになり得るため条件を厳しくする

## 関連技術
- `QueryList`と`changes`ストリーム
- `ngAfterContentInit`との組み合わせ
- ChangeDetectionStrategy.OnPushとの相互作用
