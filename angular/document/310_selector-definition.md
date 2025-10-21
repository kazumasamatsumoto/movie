# #310 「selector の指定方法」

## 概要
Directiveのselectorは適用対象を決める識別子で、要素・属性・クラスなど複数の形式を組み合わせて指定できる。命名規約を整えることで衝突を防げる。

## 学習目標
- selectorの基本形式（要素・属性・クラス）を理解する
- 複数セレクタを組み合わせる記法を学ぶ
- プロジェクトの命名規約に沿ったselector設計を実践する

## 技術ポイント
- `selector: '[appX]'`で属性、`selector: '.appX'`でクラス、`selector: 'app-x'`で要素指定
- カンマ区切りで複数のselectorを定義可能
- Standaloneでも従来のNgModuleでも宣言方法は同じ

## 📺 画面表示用コード（動画用）
```typescript
@Directive({
  selector: 'button[appCta], a[appCta], [appPrimary]',
  standalone: true
})
export class CtaDirective {}
```

## 💻 詳細実装例（学習用）
```typescript
@Directive({
  selector: 'button[appCta], a[appCta], [appPrimary]',
  standalone: true
})
export class CtaDirective {
  @Input() appPrimary = true;
  @HostBinding('class.is-primary') get isPrimary(): boolean {
    return this.appPrimary;
  }
}

@Component({
  selector: 'app-selector-demo',
  standalone: true,
  imports: [CommonModule, CtaDirective],
  template: `
    <button appCta>CTAボタン</button>
    <a appCta href="#">CTAリンク</a>
    <span appPrimary="false">スタイル適用</span>
  `
})
export class SelectorDemoComponent {}
```

## ベストプラクティス
- プロジェクト固有のプレフィックス（例: `app`, `lib`）を統一し衝突を避ける
- 複数のselectorを与える場合は役割ごとに分かる命名にする
- 属性とクラスを混在させる場合はAPIドキュメントで利用方法を明示する

## 注意点
- 要素セレクタを使うとHTMLバリデータで未知タグ扱いされる場合がある
- 同一要素に複数selectorが当たると責務が混ざるため、優先度を整理する
- 大文字小文字の扱いはHTML仕様に従い小文字に統一する

## 関連技術
- Angular Style Guide
- HostDirectives
- Schematics命名規約
