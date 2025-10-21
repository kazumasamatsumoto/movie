# #496 「インデックスの提供」

## 概要
構造ディレクティブでインデックスを提供するにはコンテキストオブジェクトに`index`プロパティを設定し、テンプレートで`let i = index`として利用する。

## 学習目標
- コンテキストを通じたインデックス提供方法を理解する
- テンプレートで`let`構文を使う手順を学ぶ
- 追加で`first`/`last`などのフラグを渡す方法を把握する

## 技術ポイント
- `{ $implicit: value, index: i }`を`createEmbeddedView`第2引数に渡す
- `context.index`など任意のキーを設定
- テンプレート側で`let`を利用して取り出す

## 📺 画面表示用コード（動画用）
```typescript
this.viewContainer.createEmbeddedView(this.template, { $implicit: item, index: i });
```

## 💻 詳細実装例（学習用）
```typescript
interface RepeatContext<T> {
  $implicit: T;
  index: number;
  even: boolean;
}

@Directive({
  selector: '[appRepeatOf]',
  standalone: true
})
export class RepeatOfDirective<T> implements OnChanges {
  @Input('appRepeatOf') items: T[] = [];

  constructor(
    private readonly template: TemplateRef<RepeatContext<T>>,
    private readonly viewContainer: ViewContainerRef
  ) {}

  ngOnChanges(): void {
    this.viewContainer.clear();
    this.items.forEach((item, i) => {
      this.viewContainer.createEmbeddedView(this.template, {
        $implicit: item,
        index: i,
        even: i % 2 === 0
      });
    });
  }
}
```

## ベストプラクティス
- Context型を定義してテンプレート側で型安全に扱う
- `even`, `odd`, `first`, `last`など必要なメタデータを提供
- `let item; let i = index`のように明示的に使うことをドキュメント化

## 注意点
- `$implicit`は暗黙メイン値なので他プロパティとの混同を避ける
- 大量データでは重複生成に注意し、差分更新を検討
- Structural Directiveは1要素に1つだけ適用可能

## 関連技術
- Contextオブジェクト
- TemplateRef
- `*ngFor`のコンテキスト
