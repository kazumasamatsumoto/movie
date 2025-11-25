# #426 「global styles.scss vs Standalone Component styles あなたはどっち派？」

## 概要
global stylesはテーマとベースルールに最適。Component stylesは局所スタイルを安全に適用できる。両者の境界を決める。

## 学習目標
- global styles.scssの構成と得意なシナリオを整理する
- コンポーネントstylesの採用メリットを理解する
- プロジェクト条件に応じた使い分け基準を決める

## 技術ポイント
- global styles.scssを成り立たせる主要API/構成要素
- コンポーネントstylesで押さえる設定やコード記述
- 両者を共存・移行させるためのブリッジ手法

## 📺 画面表示用コード（動画用）
**global派：`styles.scss`で宣言**
```typescript
:root {
  --primary: #22c55e;
}
body {
  font-family: 'Inter', sans-serif;
}
```

**component派：`styleUrls`へ閉じ込め**
```typescript
@Component({
  selector: 'app-card',
  standalone: true,
  styleUrls: ['./card.component.scss'],
})
export class CardComponent {}
```

## 💻 詳細実装例（学習用）
```typescript
@Component({
  selector: 'app-card',
  standalone: true,
  styles: [
    `
      :host {
        display: block;
        border: 1px solid var(--border, #e5e7eb);
      }
    `,
  ],
})
export class CardComponent {}
```

## ベストプラクティス
- テーマトークンやリセットはglobal、UIパーツ固有スタイルはcomponent内に配置する
- CSS変数やSASS mixinを通じてglobalとcomponentを接続し、直接依存を減らす
- globalファイルの肥大化を防ぐためセクションごとにコメントや分割importを行う

## 注意点
- component stylesでも`:host ::ng-deep`を乱用するとglobalと同じ状態になるので避ける
- globalスタイルに依存していることをREADME等に明記し、削除時の影響を把握する
- CSSの`@use`や`@forward`で循環参照を作らない

## 関連技術
- Angular CLI styles
- Scoped styles
- CSS設計
