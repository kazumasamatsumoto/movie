# #393 「ngPlural - 複数形制御」

## 概要
`ngPlural`は数値に応じてテンプレートを切り替えるディレクティブで、多言語対応における複数形の差異を表現しやすい。

## 学習目標
- `ngPlural`と`ngPluralCase`の関係を理解する
- カテゴリ（=0, =1, otherなど）を定義する方法を学ぶ
- 国際化で複数形を扱う際のベストプラクティスを把握する

## 技術ポイント
- `[ngPlural]="count"`で対象数値を指定
- `<ng-template ngPluralCase="=0">`などでケースを定義
- `other`ケースは必ず用意する

## 📺 画面表示用コード（動画用）
```html
<p [ngPlural]="items.length">
  <ng-template ngPluralCase="=0">アイテムなし</ng-template>
  <ng-template ngPluralCase="=1">1件のアイテム</ng-template>
  <ng-template ngPluralCase="other">{{ items.length }}件のアイテム</ng-template>
</p>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-ngplural-demo',
  standalone: true,
  imports: [CommonModule],
  template: `
    <p [ngPlural]="count">
      <ng-template ngPluralCase="=0">通知はありません</ng-template>
      <ng-template ngPluralCase="=1">1件の通知があります</ng-template>
      <ng-template ngPluralCase="other">{{ count }}件の通知があります</ng-template>
    </p>
  `
})
export class NgPluralDemoComponent {
  protected count = 3;
}
```

## ベストプラクティス
- i18nと組み合わせる場合は翻訳ファイルで複数形メッセージを管理
- `Intl.PluralRules`を確認し、言語ごとのケース数を把握する
- 数値のフォーマットも`DecimalPipe`などで合わせて調整する

## 注意点
- ケース指定を忘れると`other`にフォールバックするため、必要なケースを漏れなく定義
- 言語によっては`dual`, `few`, `many`など追加カテゴリが必要
- countが非数値の場合はエラーになるため型を厳密に

## 関連技術
- Angular i18n
- Intl.PluralRules
- Transloco/ngx-translate
