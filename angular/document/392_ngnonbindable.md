# #392 「ngNonBindable - バインディング無効化」

## 概要
`ngNonBindable`はAngularのバインディング評価を無効化し、`{{ }}`や`<app-component>`のようなテンプレートをそのまま表示したいときに利用する。

## 学習目標
- `ngNonBindable`の用途と挙動を理解する
- ドキュメント表示やサンプルコード埋め込みに活用する方法を学ぶ
- 部分的にバインディングを無効化する設計パターンを把握する

## 技術ポイント
- 属性として指定（例: `<div ngNonBindable>...</div>`）
- 要素配下のAngular式・ディレクティブが評価されなくなる
- SSRでも同様に評価を抑制できる

## 📺 画面表示用コード（動画用）
```html
<code ngNonBindable>{{ user.name }}</code>
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-non-bindable-demo',
  standalone: true,
  template: `
    <p>Angular式をそのまま表示</p>
    <pre ngNonBindable>
      {{ hero.name }} lives in {{ hero.city }}
    </pre>
  `
})
export class NonBindableDemoComponent {}
```

## ベストプラクティス
- ドキュメントコンポーネントやMarkdownビューアでテンプレートを表示するときに活用
- ラッパー要素を用意し、必要な範囲だけバインディングを無効化する
- ハイライトライブラリと組み合わせてサンプルコードを表示する際に便利

## 注意点
- 無効化した要素内にディレクティブを書いても機能しないため、明確な意図を持って使用
- 入力済みのユーザーコンテンツと混ざるとサニタイズが必要になる
- `ngNonBindable`は自己閉じタグには付与できないので囲い要素を確保

## 関連技術
- Markdownレンダリング
- Syntax Highlight
- Angular Universal
