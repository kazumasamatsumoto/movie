# #413 「HostBinding - プロパティバインド」

## 概要
`HostBinding`はディレクティブのプロパティとホスト要素のプロパティ・属性・クラス・スタイルをバインドする仕組みで、Renderer2を使わずに状態を同期できる。

## 学習目標
- HostBindingの基本概念を理解する
- 指定可能なプロパティ形式（class/style/attr等）を学ぶ
- ライフサイクルと連動した状態更新方法を把握する

## 技術ポイント
- `@HostBinding('class.active') isActive = false;`
- `@HostBinding('style.opacity') opacity = '1';`
- プロパティ値更新で自動的にDOMへ反映

## 📺 画面表示用コード（動画用）
```typescript
@HostBinding('class.is-open') isOpen = false;
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: '[appAccordionToggle]',
  standalone: true
})
export class AccordionToggleDirective {
  @HostBinding('class.is-open') isOpen = false;

  toggle(): void {
    this.isOpen = !this.isOpen;
  }
}
```

## ベストプラクティス
- ホスト要素の状態を表すクラスや属性はHostBindingで宣言的に記述
- 複数プロパティを管理する場合は読みやすさのためにまとめて定義
- Renderer2で直接操作するよりHostBindingを優先し、コード量を減らす

## 注意点
- HostBindingでNULLを返すとプロパティが削除されるため意図的に使用
- 高頻度更新プロパティはパフォーマンスに影響する可能性がある
- DOMに反映できないプロパティ（メソッドなど）はバインドできない

## 関連技術
- HostListener
- Renderer2
- Angular Lifecycle Hooks
